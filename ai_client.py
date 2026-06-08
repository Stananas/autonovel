#!/usr/bin/env python3
"""
Unified AI client for Autonovel.

Supports both Anthropic Messages API and OpenAI-compatible APIs (opencode.ai/go, etc.).
Auto-detects which format to use based on the API base URL.
"""
import os
import json
import httpx
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

# --- Configuration ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
API_BASE_URL = os.environ.get("AUTONOVEL_API_BASE_URL", "https://api.anthropic.com").rstrip("/")

WRITER_MODEL = os.environ.get("AUTONOVEL_WRITER_MODEL", "claude-sonnet-4-6")
JUDGE_MODEL = os.environ.get("AUTONOVEL_JUDGE_MODEL", "claude-opus-4-6")
REVIEW_MODEL = os.environ.get("AUTONOVEL_REVIEW_MODEL", "claude-opus-4-6")

ANTHROPIC_BETA = "context-1m-2025-08-07"

# --- Detection ---
def _is_anthropic():
    """Detect if the API base URL is Anthropic's native API."""
    return "anthropic.com" in API_BASE_URL.lower()

def _get_api_key():
    """Return the appropriate API key based on detected API type."""
    if _is_anthropic():
        key = os.environ.get("ANTHROPIC_API_KEY", "")
    else:
        key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        key = _read_opencode_key_from_hermes()
        if key:
            if _is_anthropic():
                os.environ["ANTHROPIC_API_KEY"] = key
            else:
                os.environ["OPENAI_API_KEY"] = key
    return key

def _auth_header():
    """Build the auth header for the detected API type."""
    key = _get_api_key()
    if _is_anthropic():
        return {"x-api-key": key}
    return {"Authorization": f"Bearer {key}"}

def _build_url(endpoint="messages"):
    """Build the full API URL. Anthropic uses /v1/messages, OpenAI uses /v1/chat/completions."""
    if _is_anthropic():
        return f"{API_BASE_URL}/v1/{endpoint}"
    return f"{API_BASE_URL}/chat/completions"

def _build_headers():
    """Build request headers for the detected API type."""
    headers = {
        "content-type": "application/json",
    }
    if _is_anthropic():
        headers.update(_auth_header())
        headers["anthropic-version"] = "2023-06-01"
        headers["anthropic-beta"] = ANTHROPIC_BETA
    else:
        headers.update(_auth_header())
    return headers

def _build_payload(model, system, messages, max_tokens, temperature):
    """Build the request payload for the detected API type."""
    if _is_anthropic():
        payload = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages,
        }
        if system:
            payload["system"] = system
        return payload
    else:
        # OpenAI-compatible format
        oai_messages = []
        if system:
            oai_messages.append({"role": "system", "content": system})
        oai_messages.extend(messages)
        return {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": oai_messages,
        }

def _extract_response(resp_json):
    """Extract text from the response based on API type."""
    if _is_anthropic():
        return resp_json["content"][0]["text"]
    else:
        return resp_json["choices"][0]["message"]["content"]

def _call_api(model, system, prompt, max_tokens, temperature, timeout):
    """Core API call function."""
    key = _get_api_key()
    if not key:
        raise ValueError(
            f"No API key found. Set {'ANTHROPIC_API_KEY' if _is_anthropic() else 'OPENAI_API_KEY'} in .env"
        )

    headers = _build_headers()
    messages = [{"role": "user", "content": prompt}]
    payload = _build_payload(model, system, messages, max_tokens, temperature)
    url = _build_url()

    resp = httpx.post(url, headers=headers, json=payload, timeout=timeout)
    resp.raise_for_status()
    return _extract_response(resp.json())


def _read_opencode_key_from_hermes():
    """Fallback: read the opencode API key from Hermes .env."""
    import subprocess
    try:
        result = subprocess.run(
            ["grep", "^OPENCODE_GO_API_KEY", os.path.expanduser("~/.hermes/.env")],
            capture_output=True, text=True, timeout=5
        )
        for line in result.stdout.strip().split("\n"):
            line = line.strip()
            if "=" in line:
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key and key != "***":
                    return key
    except Exception:
        pass
    return None


# --- Public API ---

def call_writer(prompt, max_tokens=16000, temperature=0.7, timeout=300, system=None):
    """Call the writer model (for drafting, world-building, character gen, etc.)."""
    if system is None:
        system = (
            "You are a literary fiction writer with deep knowledge of the craft. "
            "You write specific, sensory prose. You show, don't tell. "
            "You vary sentence length. You trust the reader. "
            "You never use AI slop words (delve, tapestry, myriad, etc)."
        )
    return _call_api(WRITER_MODEL, system, prompt, max_tokens, temperature, timeout)


def call_judge(prompt, max_tokens=2000, temperature=0.3, timeout=180, system=None):
    """Call the judge model (for evaluation, comparison, adversarial editing)."""
    if system is None:
        system = (
            "You are a literary critic and novel editor. "
            "You evaluate fiction with precision. Always respond with valid JSON. "
            "No markdown fences, no preamble -- just the JSON object."
        )
    return _call_api(JUDGE_MODEL, system, prompt, max_tokens, temperature, timeout)


def call_review(prompt, max_tokens=8000, temperature=0.3, timeout=600, system=None):
    """Call the review model (for deep prose-level Opus-style analysis)."""
    if system is None:
        system = (
            "You are a literary critic and professor of fiction. "
            "You read novels with deep attention to craft, structure, character, and theme. "
            "Give specific, actionable feedback. Be fair but honest."
        )
    return _call_api(REVIEW_MODEL, system, prompt, max_tokens, temperature, timeout)
