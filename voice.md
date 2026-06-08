# Voice Profile

This file has two parts:
1. **Guardrails** -- universal rules to avoid AI-generated slop. These
   apply to ALL voices and are non-negotiable.
2. **Voice Identity** -- the specific voice for THIS novel. Generated
   during the foundation phase. Could be anything: dense and mythic,
   spare and brutal, warm and whimsical. The voice emerges from the
   story's needs.

---

## Part 1: Guardrails (permanent, all novels)

These are the cliff edges. Stay away from them regardless of voice.

### Tier 1: Banned words -- kill on sight

These are statistically overrepresented in LLM output vs. human writing.
If one appears, rewrite the sentence. No exceptions.

| Kill this         | Use instead                                    |
|-------------------|------------------------------------------------|
| delve             | dig into, examine, look at                     |
| utilize           | use                                            |
| leverage (verb)   | use, take advantage of                         |
| facilitate        | help, enable, make possible                    |
| elucidate         | explain, clarify                               |
| embark            | start, begin                                   |
| endeavor          | effort, try                                    |
| encompass         | include, cover                                 |
| multifaceted      | complex, varied                                |
| tapestry          | (describe the actual thing)                    |
| testament to      | shows, proves, demonstrates                    |
| paradigm          | model, approach, framework                     |
| synergy           | (delete the sentence and start over)           |
| holistic          | whole, complete, full-picture                  |
| catalyze          | trigger, cause, spark                          |
| juxtapose         | compare, contrast, set against                 |
| nuanced (filler)  | (cut it -- if it's nuanced, show how)          |
| realm             | area, field, domain                            |
| landscape (metaphorical) | field, space, situation                 |
| myriad            | many, lots of                                  |
| plethora          | many, a lot                                    |

### Tier 2: Suspicious in clusters

Fine alone. Three in one paragraph = rewrite that paragraph.

robust, comprehensive, seamless, cutting-edge, innovative, streamline,
empower, foster, enhance, elevate, optimize, pivotal, intricate,
profound, resonate, underscore, harness, navigate (metaphorical),
cultivate, bolster, galvanize, cornerstone, game-changer, scalable

### Tier 3: Filler phrases -- delete on sight

These add zero information. The sentence is always better without them.

- "It's worth noting that..." -> just state it
- "It's important to note that..." -> just state it
- "Importantly, ..." / "Notably, ..." / "Interestingly, ..." -> just state it
- "Let's dive into..." / "Let's explore..." -> start with the content
- "As we can see..." -> they can see
- "Furthermore, ..." / "Moreover, ..." / "Additionally, ..." -> and, also, or just start
- "In today's [fast-paced/digital/modern] world..." -> delete the clause
- "At the end of the day..." -> delete
- "It goes without saying..." -> then don't say it
- "When it comes to..." -> just talk about the thing
- "One might argue that..." -> argue it or don't
- "Not just X, but Y" -> restructure (the #1 LLM rhetorical crutch)

### Structural slop patterns

These are the shapes that betray machine origin. Avoid them in any voice.

**Paragraph template machine**: Don't repeat the same paragraph
structure (topic sentence -> elaboration -> example -> wrap-up).
Vary it. Sometimes the point comes last. Sometimes a paragraph is
one sentence. Sometimes three long ones in a row.

**Sentence length uniformity**: If every sentence is 15-25 words,
it reads as synthetic. Mix in fragments. And long, winding,
clause-heavy sentences that carry the reader through a thought
the way a river carries a leaf. Then a short one.

**Transition word addiction**: If consecutive paragraphs start with
"However," "Furthermore," "Additionally," "Moreover," "Nevertheless"
-- rewrite. Start with the subject. Start with action. Start with
dialogue. Start with a sense detail.

**Symmetry addiction**: Don't balance everything. Three pros, three
cons, five steps -- that's a tell. Real writing is lumpy. Some
sections are long because they need to be. Some are two lines.

**Hedge parade**: "may," "might," "could potentially," "it's possible
that" -- pick one per page, max. State things or don't.

**Em dash overload**: One or two per page is fine. Five per paragraph
is a dead giveaway. Use commas, parentheses, or two sentences instead.

**List abuse**: Prose, not bullets. If the scene calls for a list
(a merchant's inventory, a spell's components), earn it. Don't
default to bullet points because it's easy.

### The smell test

After writing any passage, ask:
- Read it aloud. Does it sound like a person talking?
- Is there a single surprising sentence? Human writing surprises.
- Does it say something specific? Could you swap the topic and the
  words would still work? Specificity kills slop.
- Would a reader think "AI wrote this"? If yes, rewrite.

---

## Part 2: Voice Identity (generated per novel)

Everything below is discovered during the foundation phase.
The agent proposes a voice that serves THIS story, writes exemplar
passages, and calibrates against them throughout drafting.

### Tone
Réaliste, tendu, intime. La tension monte comme la pression dans une cuve — invisible d'abord, puis inévitable. Les moments calmes sont lourds de ce qui va venir. Les moments de crise sont précis, sensoriels, désorientants. Le quotidien et l'apocalypse cohabitent dans la même soirée. Le langage est celui d'un roman français contemporain — pas de lyrisme fantastique, pas de détours poétiques. La peur s'écrit dans les gestes : une main qui tremble, le bruit du verre qui éclate, le noir après le flash.

### Sentence Rhythm
Alternance de phrases longues, techniques, presque cliniques (quand Thomas analyse les données SCADA) et de phrases courtes, hachées, vitales (quand l'explosion frappe). Les moments de Camille privilégient le flux de conscience, les pensées qui se bousculent, les phrases qui s'interrompent. Les descriptions sont précises, documentaires — on sait ce qu'on voit, on le voit comme un technicien ou comme une fille de seize ans, jamais comme un poème.

### Vocabulary Register
Français contemporain oral et technique. Le registre d'ingénieur : SCADA, barres de contrôle, pressuriseur, débit de refroidissement. Le registre adolescent : « sérieux », « trop », les phrases qui tombent comme des textos. Le registre parental : la voix qui se veut calme et qui craque sous la pression. La narration passe de l'un à l'autre selon le point de vue, sans prévenir, comme on change de chaise dans une pièce.

### POV and Tense
Présent. Focalisation externe-interne alterne entre les personnages selon les chapitres : principalement Thomas (le technicien, celui qui sait) et Camille (la survivante, celle qui apprend). Parfois Hélène, parfois Nolan. Jamais omniscient — on est dans une tête à la fois, on ne sait que ce qu'elle sait.

### Dialogue Conventions
Tirets cadratins (—) pour ouvrir les dialogues. Pas d'incises autour des tirets. Quand un personnage parle puis agit, rupture de ligne, retour à la ligne avec un nouveau tiret s'il reprend la parole. Les personnages s'interrompent, se coupent la parole. Personne ne termine ses phrases comme dans un script — ils parlent vrai, avec des faux départs, des lapsus, des silences qui veulent dire plus que les mots. Les émotions passent par ce qui n'est pas dit.

### Exemplar Passages
<!-- À écrire après la phase fondation : 3-5 paragraphes qui sont LA voix. -->

### Anti-Exemplars
<!-- 3-5 paragraphes montrant ce que cette voix n'est PAS. -->
