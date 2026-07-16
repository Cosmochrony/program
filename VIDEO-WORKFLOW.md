# Cosmochrony Video Workflow

This document is the source of truth for planning, producing, validating, cataloguing, publishing, and embedding
Cosmochrony scientific videos.
It applies to every video associated with a paper, result, sub-programme, or the programme as a whole.

## 1. Sources of truth

- This workflow defines the production and publication procedure.
- The most specific owning paper repository contains the editable video sources, normally under `video/`.
- `program/videos.json` is the canonical programme-wide video inventory.
- `cosmochrony.github.io/data/videos.json` is an exact published copy of that inventory.
- The paper and website remain authoritative for scientific claims; a video must not strengthen their epistemic status.

## 2. Determine ownership before production

Before creating files, inventory all plausible owners:

- the paper establishing the result;
- neighbouring or downstream papers;
- the presentation note for the relevant sub-programme;
- the programme root when the subject is genuinely programme-wide.

Choose one canonical owner: the most specific repository that establishes the result explained by the video.
Record all secondary associations separately.
Do not assign a foundational topic to the first superficially plausible repository.

## 3. Define the production brief

Record the following decisions before writing the scene:

- working title;
- canonical owner and associated papers or sub-programmes;
- scientific result and its status: proved, structural, conditional, interpretive, or open;
- intended audience and target duration;
- required formats and aspect ratios;
- narration language and voice;
- intended publication platforms and website scope.

All public video text, narration, metadata, code comments, and production documentation must be in English.
Conversation with the author remains in French.

## 4. Standard source layout

Use the following layout unless the production has a documented reason to differ:

```text
video/
├── README.md
├── <scene_name>.py
├── narration.py
├── edge_tts_service.py        # when Edge TTS is used
├── manim.cfg
├── render.sh
├── assets/                    # only when required
├── media/                     # generated, ignored
└── out/                       # generated deliverables, ignored
```

The README must identify the owning paper, explain the video, document the pinned toolchain and render commands,
and list every official publication URL once published.
Keep narration separate from scene logic so it can be reviewed and edited without searching animation code.

## 5. Toolchain and reproducibility

- Use Manim Community unless another framework is explicitly justified.
- Pin Python, Manim, voice-over, text-to-speech, and compatibility package versions in `render.sh`.
- Use `uv run --no-project --with` and the shared user-level `uv` package cache.
- Do not create a `.venv` inside each paper's `video/` directory.
- Do not use `uv tool run` on the author's Mac: `~/.local` is root-owned and the persistent tool installation fails.
- Use paths relative to the video directory so an independently cloned paper remains reproducible.
- Provide at least `draft` and `final` render modes.

The current free narration default is Edge TTS with the British male voice `en-GB-RyanNeural`.
Treat the voice as a production choice, not a permanent scientific convention; document any change in the README.

## 6. Scientific script and narration

- Start from the exact result established by the owning paper.
- State load-bearing hypotheses whenever the conclusion depends on them.
- Distinguish theorem, interpretation, motivation, and open extension.
- Prefer one conceptual claim per scene.
- Keep on-screen text concise and complementary to the narration.
- Avoid claims that are stronger, broader, or more experimentally suggestive than the paper.
- Use consistent notation with the owning paper.
- Pronounce symbols through readable English in narration while retaining mathematical notation on screen.

Review the narration as prose before rendering.
Check grammar, pacing, pronunciation risks, and consistency with the current paper version.

## 7. Rendering

The rendering script must:

- fail on command errors;
- resolve its own directory before running;
- pin all dependencies;
- render from the video directory;
- write final deliverables to ignored `out/`;
- copy generated subtitles beside the MP4 when available;
- print the final output paths and sizes.

The default deliverables are:

- draft: 480p15 for rapid review;
- final: 1920x1080 at 60 fps with H.264 video and AAC audio;
- subtitles: SRT suitable for platform upload.

When a platform needs a different format, such as a vertical Reel, produce a deliberate platform-specific variant.
Do not crop a scientific diagram automatically without checking labels and safe areas.

## 8. Mandatory quality assurance

Do not treat a successful Manim exit code as sufficient validation.

### Scientific review

- Compare every narrated conclusion with the owning paper.
- Confirm that assumptions and epistemic qualifications remain visible or audible.
- Check notation, spelling, labels, and mathematical symbols.

### Video review

- Confirm duration, codec, resolution, frame rate, and audio stream metadata.
- Decode the complete video without errors.
- Inspect representative frames from the opening, each conceptual transition, and the conclusion.
- Check that no text is clipped, malformed, too small, or hidden by platform safe areas.
- Confirm animation timing follows the actual narration duration.

### Audio and subtitle review

- Listen to the complete narration for pronunciation, artefacts, silence, clipping, and pacing.
- If the executing agent cannot listen to audio, state this limitation and obtain an explicit human listening check
  before publication.
- Read the complete SRT file and verify ordering, timing boundaries, text, and final duration.
- Confirm that platform captions use the reviewed SRT rather than an unchecked automatic transcription.

## 9. Publication package

Prepare the following English metadata:

- final title with deliberate capitalization;
- concise description of the result and its assumptions;
- owning paper page;
- Zenodo concept DOI when available, never a version-record DOI;
- Cosmochrony programme URL;
- author and production credits;
- restrained keywords or hashtags;
- reviewed subtitle file;
- thumbnail or cover when the platform requires one.

The canonical long-form channel is the Cosmochrony YouTube channel.
Instagram and future platforms are additional distributions of the same video, not separate catalogue entries.

Uploading to an external platform requires an explicit user request or an already completed author upload.
Once a public URL is supplied, continue automatically with catalogue and website updates.

## 10. Catalogue the video

Create or update one entry in `program/videos.json` containing, as applicable:

- stable internal identifier and title;
- language, duration, status, and publication date;
- canonical owner repository, source path, and paper URL;
- associated results, papers, and sub-programmes;
- platform identifiers, URLs, account names, and account URLs;
- every website page that references or embeds the video.

Reuse the same entry when another platform publishes the same production.
Do not create one catalogue record per platform.
After every change, copy the file byte-for-byte to `cosmochrony.github.io/data/videos.json` and verify equality.

## 11. Integrate the website

After publication, add the video according to scope:

- always: the owning paper page;
- when relevant: the associated sub-programme page;
- only for programme-wide material: the programme root page.

Use the privacy-enhanced YouTube embed domain `www.youtube-nocookie.com` for the primary player.
Link additional distributions such as Instagram without duplicating the embedded player unless there is a clear need.
Update every translation present beside each modified base page, preserving structural parity.
Add responsive embed styling to the shared stylesheet rather than page-local styles.

After any website change:

1. commit and push the website repository;
2. run the production Netlify deployment;
3. fetch every affected public URL;
4. verify the platform identifier in the deployed HTML;
5. verify the public inventory JSON.

If sandboxed tools encounter root-owned user caches, redirect only the temporary tool cache to an allowed temporary
directory.
Do not use `sudo`, change ownership, or modify the author's personal configuration to complete a deployment.

## 12. Git and completion

Commit and push each affected repository separately:

- owning paper: source, scripts, narration, and publication links;
- programme: canonical inventory;
- website: public inventory, embeds, links, translations, and shared styling.

Never commit generated `media/`, `out/`, MP4, WAV, MP3, or SRT files unless the author explicitly changes the policy.
Preserve unrelated dirty worktree changes.
Verify each pushed commit against `origin/main`.

A video task is complete only when every in-scope item is satisfied:

- canonical owner selected;
- English script and narration reviewed;
- reproducible render succeeds;
- scientific, visual, audio, and subtitle QA completed;
- publication URLs recorded;
- one canonical inventory entry updated and copied to the website;
- relevant translations updated;
- repositories committed and pushed;
- website deployed and production URLs verified.

## 13. Common failure modes

- Assigning the video to a broad synthesis before checking the result paper.
- Creating one virtual environment per video.
- Using `uv tool run` and failing under the root-owned `~/.local` directory.
- Treating render success as visual or audio QA.
- Publishing an unqualified theorem statement when the paper is conditional.
- Linking a Zenodo version DOI instead of the concept DOI.
- Creating duplicate inventory entries for YouTube and Instagram.
- Updating the English website without its translations.
- Pushing the website without deploying Netlify.
- Reporting completion without checking the public pages and inventory.
