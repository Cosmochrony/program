# Referee-style review — version 2.2

Date: 2026-07-30

## Registry correction

- The inventory contains 113 papers, including HeisenbergCarrierObstruction.
- Found and HeisStr are no longer classified as proved.
- The finite countermodel is scoped to the carrier-selection edge; downstream mathematics
  internal to a supplied Heisenberg/Weil carrier is not declared false.
- The abstract and conclusion distinguish the programme's interpretive reading from proved
  results.

## Edge discipline

- Node and edge statuses are declared independent.
- Audited claim-bearing edges support proved, conditional, postulated, interpretive, and
  withdrawn statuses.
- Synthesis links are rendered separately.
- Untyped substantive links default to dependency and explicitly carry no derivational
  status.
- The Found-to-Heis carrier-selection edge is postulated.
- The audited low-ell capacity consumer edges are conditional, postulated, or interpretive
  as appropriate.

## Build and presentation

- Full `pdflatex -> bibtex -> pdflatex -> pdflatex` cycle succeeds.
- No undefined citations, undefined references, LaTeX errors, or overfull boxes remain.
- Visual inspection of the abstract, corrected Branch I discussion, static dependency graph,
  and first inventory page found no clipping or overlap.
- The interactive script passes `node --check`.
- Local browser loading is blocked by the browser URL policy; visual and functional browser
  acceptance must therefore be run against the deployed public URL.

## Verdict

Suitable for release after the public interactive-graph acceptance test.
