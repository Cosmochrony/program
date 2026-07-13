# The Cosmochrony Research Programme — Roadmap and Paper Inventory

This repository contains the source of the **programme synthesis paper**
*The Cosmochrony Research Programme: A Structural Roadmap and Paper
Inventory*.

It is the **central registry** of the whole Cosmochrony corpus: it inventories every paper,
documents the dependency graph between them, and tracks their status. It is the reference to
consult first to understand how the pieces fit together.

## What This Paper Is

The Cosmochrony programme develops a pre-geometric framework in which physical structure —
spacetime, quantum mechanics, gauge symmetry, and Standard Model observables — arises from a
single primitive: the local structure of admissible non-injective transitions between observable
states. The corpus comprises **109 papers** across three theory branches:

- **Branch I — Foundation track**: four axioms suffice to derive the Heisenberg group
  $\mathrm{Heis}_3(\mathbb{Z}/q)$ and its Weil representation as theorems, with no background
  substrate or relaxation mechanism.
- **Branch II — O-series** (spectral admissibility): derives and numerically validates the
  transfer chain $c_{\mathrm{BI}} \to \delta_{\mathrm{pair}} \to \beta^* \approx 0.126$ connecting
  the Born–Infeld saturation constant to the charged-lepton mass hierarchy.
- **Branch III — Q-series and companion papers**: derives quantum mechanics, spacetime geometry,
  gauge structure, and further observables from the Branch I axioms and Branch II spectral data.

## Role in the Repository

- **Paper inventory**: the authoritative list of all papers and their status.
- **Dependency graph**: maintained here and exported as an interactive HTML visualisation, which
  is copied to the website for publication at https://cosmochrony.org.
- **Coherence**: updated whenever a new result is obtained or a new paper is created, so the
  programme stays traceable.

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
