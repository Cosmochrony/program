# The Cosmochrony Research Programme — Roadmap and Paper Inventory

This repository contains the source of the **programme synthesis paper**
*The Cosmochrony Research Programme: A Structural Roadmap and Paper
Inventory*.

It is the **central registry** of the whole Cosmochrony corpus: it inventories every paper,
documents the dependency graph between them, and tracks their status. It is the reference to
consult first to understand how the pieces fit together.

Version 2.16 synchronises HeisenbergStructure 2.1 (15 August) and the 28--31 August release wave: O25 1.5,
O27 2.0, Q5a 3.2, Q5b 2.1, Q12 1.4, Q13 1.4, Q14 2.0, and
the Gauge Structure, Gauge--Gravity Stratification, and Fermionic Matter presentation notes.
It consolidates the retired standalone HCO record into HeisenbergStructure 2.1, preserves the
separation between supplied-data theorems and emergent-base readings, and records the exact
[H-F] $\Rightarrow$ [H-lift] scope of Q9. O29's finite-precision diagnostics are numerical rather
than exact carrier-identification theorems, and O30 is a conditional $3\times3$ model distinct from
O28's measured covariance. It also distinguishes the Heisenberg/Schrödinger representation
identified by Stone--von Neumann from the separate associated Weil action. The registry and
website graph remain a single
116-node artefact. It also synchronises the September releases: O29 2.0, O30 2.0, O26 2.0, O28 2.0, the Spectral
Admissibility presentation note 2.0, PYL 2.0, EBJ 2.0, PRS 2.1, A4-Note 2.1, FM-Note 2.1 and PYO 1.10.1,
and aligns the bibliography titles of thirteen entries with their deposited records. Version labels of
Foundation, Q9, NIF-Note, ENT-Note, the white paper and SpectralAdmissibility are aligned with the deposits, the
Branch III description is restated on the open bridges, and the dependency graph gains numerical and conditional
statuses and the edges O25 to O26/O27, O28/O29 to O30, O31 to O32 and SGN/CC-Note to the Spectral Admissibility
note; it records the Q11OF central Weil lift resolution, the AOG proved status and the O14, O31, O32 and SGN
row corrections, reverses the AAR/PRS edge, removes the unsupported AAR to Q11OF, Gravity to A4-Note, SRN to Q14 and O31 to TPC edges, types
the O28 to O30 edge as interpretive, retypes O26 Level II as a conjecture, corrects the O32 bibliography note, and
reduces the CHO node to CHO's own results.

Version 2.2 records the finite \(S_3\) countermodel to the published Heisenberg carrier-selection
argument. The algebraic properties extracted from A1--A3 do not force a central commutator,
class-two nilpotence, a finite Heisenberg group, or a Weil carrier. Found and HeisStr are therefore
reclassified, while results internal to a supplied Heisenberg/Weil carrier retain their status.

Version 2.7 updates the SRN inventory row for spin-rotation-note v1.4: an independent downstream
representation audit shows the Dirac-conjugated fermionic bilinear carries exact Higgs-typed
electroweak quantum numbers in every tree-level Yukawa sector, permitting but not deriving a
composite Higgs condensate; the pre-existing soldering audit is untouched. No new paper, node, or
edge is registered; the corpus count remains 116.

## What This Paper Is

The Cosmochrony programme develops a pre-geometric framework in which physical structure —
spacetime, quantum mechanics, gauge symmetry, and Standard Model observables — arises from a
single primitive: the local structure of admissible non-injective transitions between observable
states. The corpus comprises **116 papers** across three theory branches:

- **Branch I — Foundation track**: four axioms organise the admissibility framework. Their published
  carrier-selection argument is refuted by a finite \(S_3\) countermodel; the Heisenberg/Weil carrier
  remains a supplied realisation.
- **Branch II — O-series** (spectral admissibility): derives the canonical pair-capacity
  observable and its fibre/representation structure. The proposed
  $\delta_{\mathrm{pair}}\to\beta^*$ continuation is now recorded as a refuted native
  Heisenberg transfer and retained only as a cross-substrate phenomenological prescription.
- **Branch III — Q-series and companion papers**: develops conditional mathematical models toward
  quantum mechanics, spacetime geometry, gauge structure, and further observables. It contains
  proved internal results, but the physical chains retain supplied carriers and open bridges such
  as the Born rule, [H-L], and the colour factor.

## Role in the Repository

- **Paper inventory**: the authoritative list of all papers and their status.
- **Dependency graph**: covers all 116 inventory entries, is maintained here, and is exported as
  an interactive HTML visualisation copied to the website for publication at
  https://cosmochrony.org.
- **Coherence**: updated whenever a new result is obtained or a new paper is created, so the
  programme stays traceable.
- **Video workflow**: [`VIDEO-WORKFLOW.md`](VIDEO-WORKFLOW.md) is the source of truth for scientific
  video production and publication; [`videos.json`](videos.json) is the canonical video inventory.

## Compilation

```bash
pdflatex -output-directory=out tex/program.tex
cd out && bibtex program && cd ..
pdflatex -output-directory=out tex/program.tex
pdflatex -output-directory=out tex/program.tex
```

## Links

- 🔗 DOI: [10.5281/zenodo.19759956](https://doi.org/10.5281/zenodo.19759956)
- 🌐 Interactive dependency graph: https://cosmochrony.org/science/cosmochrony_graph

## Citation

> J. Beau, *The Cosmochrony Research Programme: A Structural Roadmap and Paper Inventory*,
> Zenodo, 2026. DOI: 10.5281/zenodo.19759956.

## Acknowledgements

Portions of the editorial refinement benefited from iterative interactions with large language
models, used as analytical assistants. All claims and final formulations remain the sole
responsibility of the author.
