---
name: produce-cosmochrony-video
description: >-
  Produce, revise, render, validate, catalogue, publish, or embed a Cosmochrony scientific video. Use for video ideas
  tied to papers or results, Manim scenes, English narration and voice-over, render scripts, MP4/SRT quality assurance,
  YouTube or Instagram publication, the central video inventory, and video integration into paper, sub-programme, or
  programme website pages. Do not use for static manuscript figures or unrelated external videos.
---

# Produce Cosmochrony Video

Follow the complete programme workflow in `../../../VIDEO-WORKFLOW.md`.
Read that file in full before taking any production, publication, catalogue, or website action.
If this skill is accessed through a workspace-level link, resolve the workflow from the canonical `program/` repository.

## Procedure

1. Identify the current phase: brief, ownership, scripting, rendering, QA, publication, catalogue, or website.
2. Inspect all plausible owning papers before creating sources.
3. Apply every workflow section relevant to the current phase and preserve the completion state of earlier phases.
4. Keep conversation in French and every production artifact in English.
5. Treat external upload as requiring explicit user authorization; a supplied public URL authorizes catalogue and
   website follow-through, not unrelated external changes.
6. Preserve unrelated dirty worktrees and commit and push each affected repository separately.
7. Do not report completion until the workflow's in-scope validation and public verification checks pass.

## Required records

- Editable sources belong to the most specific owning paper under `video/`.
- The canonical catalogue is `program/videos.json`.
- The public catalogue copy is `cosmochrony.github.io/data/videos.json` and must remain byte-identical.
- Publication links must be recorded in the owning video's README and on every website page required by scope.

## Non-negotiable checks

- Do not skip scientific claim review, complete decode, representative-frame inspection, audio listening, or SRT review.
- Do not create per-video virtual environments or use `uv tool run` on the author's Mac.
- Do not duplicate a catalogue entry when the same video appears on another platform.
- Do not modify a website base page without updating all adjacent translations.
- Do not stop after a website push; deploy Netlify and verify production.
