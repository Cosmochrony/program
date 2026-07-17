# What Is Cosmochrony Trying to Explain?

This directory contains the editable Manim sources and English narration for video 1.2 of the
*Start Here: The Cosmochrony Programme* playlist.

## Production brief

- **Working title:** *What Is Cosmochrony Trying to Explain?*
- **Canonical owner:** *The Cosmochrony Research Programme — Roadmap and Paper Inventory*
- **Associated branches:** non-injective foundations, spectral admissibility, quantum structure, emergent geometry,
  gauge structure, spectral gravity, fermionic matter, and cosmology
- **Scientific role:** interpretive programme overview; it introduces the research question without presenting every
  downstream physical identification as established
- **Audience:** scientifically curious viewers with no prior knowledge of Cosmochrony
- **Target duration:** 2 minutes to 2 minutes 20 seconds
- **Primary format:** 16:9 landscape; a separately composed 9:16 version may be produced for Instagram
- **Narration:** English, British male voice `en-GB-RyanNeural`
- **Intended platforms:** Cosmochrony YouTube channel and Instagram account
- **Website scope after publication:** programme root and science overview pages

The rendering script uses `uv run --no-project` with the shared global `uv` package cache and pins Python 3.13,
Manim 0.20.1, Manim Voiceover 0.3.7, Edge TTS 7.2.8, and the compatibility version of `setuptools` required by the
voice-over plugin.
It does not create a virtual environment inside this directory or install a persistent tool under `~/.local`.
The free online Edge TTS service generates the narration automatically from `narration.py` with the British male
voice `en-GB-RyanNeural`.

Render the final narrated 1080p60 video with:

```bash
./render.sh
```

For a faster 480p15 draft render, use:

```bash
./render.sh draft
```

The generated MP4 and SRT subtitle file are written to `out/`.

The episode deliberately avoids introducing either $\Omega$ or $\chi$.
At programme-overview level, the phrase *underlying description* is sufficient and avoids suggesting an identification
between the framework-independent fine-grained space used by the emergence theorem and the preliminary substrate
vocabulary of the white paper.

## Storyboard

### Scene 1 — Successful theories, separated domains

**Narration:** `opening`

Show four clean visual domains labelled *Quantum theory*, *Spacetime*, *Gauge interactions*, and *Matter*.
They work independently but remain visually separated.

**On-screen text:**

```text
Powerful theories
Separate foundations
```

### Scene 2 — The programme question

**Narration:** `question`

Pull the four domains outward and reveal a single unresolved relational structure behind them.
The animation must pose a question rather than depict a completed reduction.

**On-screen text:**

```text
Could these structures emerge
from a common deeper description?
```

### Scene 3 — Non-injective observation

**Narration:** `projection`

Animate several fine distinctions converging onto fewer observable states.
The projection should visibly erase distinctions without destroying the underlying source diagram.

**On-screen text:**

```text
Non-injective projection
Several distinctions → one observable state
```

### Scene 4 — Level one: structural foundations

**Narration:** `foundations`

Build a compact chain from admissible transitions to unresolved fibres, non-commuting generators, and finite
Heisenberg structure.
Mark the continuum bridge as a separate outgoing arrow rather than part of the proved finite chain.

**On-screen text:**

```text
Level 1 — Structural foundations
Non-injectivity · admissibility · finite fibre structure
```

### Scene 5 — Level two: spectral selection

**Narration:** `spectra`

Transform a relational graph into a spectrum, then highlight the modes and histories that remain distinguishable.
Use the word *selection*, not *dynamics*.

**On-screen text:**

```text
Level 2 — Spectral admissibility
Which structures remain distinguishable?
```

### Scene 6 — Level three: effective physics

**Narration:** `physics`

Branch the selected spectral structure into restrained icons for quantum states, geometry, gauge fields, gravity,
matter, and cosmology.
Use dotted or conditional connectors wherever the programme still requires continuum or physical-identification
hypotheses.

**On-screen text:**

```text
Level 3 — Effective physics
Quantum · geometry · gauge · gravity · matter · cosmology
```

### Scene 7 — Epistemic map

**Narration:** `status`

Replace the branch diagram with three clearly separated columns.
Do not use a linear progress bar, which would falsely imply that all open bridges differ only by completion time.

**On-screen text:**

```text
Proved in stated settings
Conditional bridges
Open physical identifications
```

### Scene 8 — Closing question

**Narration:** `closing`

Recombine the scientific domains around the projection motif, while keeping them distinct.
Finish on the programme question and the Cosmochrony wordmark.

**On-screen text:**

```text
Which features of observable physics
become unavoidable under non-injective projection?
```

## Scientific guardrails

- Do not describe Cosmochrony as a completed theory of everything.
- Do not claim that the programme has experimentally validated a common origin of all physical sectors.
- Do not present continuum geometry or downstream physical identifications as consequences of non-injectivity alone.
- Distinguish results proved in their stated finite or analytical settings from structural interpretations and open
  bridges.
- Describe spectral admissibility as a selection principle, not as motion of a substrate.
- Do not infer thermodynamic temperature, energy, or fundamental information creation from distinguishable-history
  counts.
- Do not claim a predicted value of Newton's constant or a quartic graviton dispersion relation.
