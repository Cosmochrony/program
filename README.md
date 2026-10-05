# The Cosmochrony Research Programme — Roadmap and Paper Inventory

This repository contains the source of the **programme synthesis paper**
*The Cosmochrony Research Programme: A Structural Roadmap and Paper
Inventory*.

It is the **central registry** of the whole Cosmochrony corpus: it inventories every paper,
documents the dependency graph between them, and tracks their status. It is the reference to
consult first to understand how the pieces fit together.

Version 2.28 synchronises the PRS 3.0 / A4-Note 3.0 source contract and its consumers: Q14 3.1, EBJ 2.1, PYO 2.1,
PYL 3.0.1, AAR 1.3, Q11OF 1.1, CHO 1.1, AOG-Note 1.8, KUD 1.5, TPC 1.2 and FM-Note 3.1. Statuses are typed
per result. PRS: under a contraction hypothesis the compression remainder of the projected Dirac square is
the Schur complement $-N^\dagger N \preceq 0$ (zero-order only under a symbol condition), equal to the projective endomorphism of Q14 only when
$\Pi_S D^2 \Pi_S^* = \mathrm{Lich}$; under the generation-reading hypothesis [H-Gen] a $J_\Pi$-commuting locking
operator gives $u = 0$; the Schur-null and Schur-transverse loci form a dichotomy proved under explicit hypotheses,
which locus holds being open (the exact $\mathfrak{sl}_2$ opening, produced by $[E,F]=H$, reaches the locking operator
only under the transport hypothesis [H-Tr]); no mechanism for a non-zero split is derived. A4-Note: the radicand
quartic coefficient is chart-dependent and selects no lock, the first contact is chart-independent when it exists, the
Lorentzian genus is not determined, and the Front D factorisation is formal. EBJ: its finite witness has $J^2 = +1$ and
lies outside [H-Gen](i). Q14 3.1 states $E_\Pi \preceq 0$ as an explicit hypothesis. The commutation
$[\gamma_5, R_b] = 0$ is the hypothesis [H-WS] of Q11OF, part (i) (a scalar on the chiral carrier; the value $-1$, part (ii), is used only by AOG-Note), carried by CHO and AOG-Note;
the $J_3$ signal comes from the $\mathfrak{sl}_2$ commutator $[E,F]=H$, not from the Heisenberg bracket (AAR 1.3).
The registry entries, table rows, dependency figure, bibliography entries and interactive-graph nodes carry these
statements; PRS and the A4-Note are typed conditional, the edges PRS to A4-Note and A4-Note to EBJ are typed
conditional, and the node suffix "Written against Q14 2.0" is removed from PRS and the A4-Note and reworded for CHO,
AOG-Note and Q11OF. The versions listed above are planned versions of their papers and programme 2.28 is a candidate;
none of them is deposited yet, and the Zenodo record numbers of the new versions are added at deposit.

Version 2.27 synchronises FM-Note 3.0, PYL 3.0 and PYO 2.0, which type the fermionic and mass sectors on the Q14 3.0
hypotheses. [H-Spin] (a spin solder) and [H-Weak] (a distinct $U(2)$ weak factor $E_{\mathrm{weak}}$) are separate
hypotheses supplied by no source; the $\mathfrak{sl}_2(\mathbb{C})$ tensor algebra is proved on supplied model data
only; the hypercharge line $L_Y = \wedge^2(E_{\mathrm{weak}})$ rests on [H-Weak], the exterior square of the soldered
spinor doublet being trivial under [H-Spin]; Lorentz chirality (left-admissibility, an input branch) is distinct from
weak $V{-}A$; and $R_b = W(-I)$ commutes with $\gamma_5$ only under the hypothesis [H-WS] of Q11OF, no group-level Weil-to-spin map being available at the primes of the corpus (superseded in 2.28). PYL
records a conditional weak determinant line and the ordering of the three levels of the model operator
$\mathrm{diag}(1, \tfrac12 + u, \tfrac12 - u)$, read as $E_\Pi^2|_{\mathbb{C}^3_{\mathrm{gen}}}$ only under the named
hypothesis [H-Res]; the level-to-generation map is not established and no mass value is claimed.
PYO states that $E_\Pi^2$ fixes the squared Yukawa levels, not the
morphism, under [H-Res], [H-Sq], [H-Fac] and [H-Grad]; the projection of the $\mathfrak{sl}_2$ lift onto its
$J_\Pi$-odd anti-Hermitian part vanishes, by representation theory, for the projection as defined
and is not the polar generator, so the physical polar
class is open and the choice of the $J_\Pi$-odd part is a modelling choice that no source justifies. The registry
entries, table rows, dependency figure, bibliography entries and interactive-graph nodes carry these statements; the
edges into PYL and PYO are typed conditional and the PYO-to-NPI edge interpretive, NPI's reference to a trivial polar
class being an open consumer correction. FM-Note 3.0 is [Zenodo record 23111382](https://zenodo.org/record/23111382)
(concept DOI 10.5281/zenodo.20562665), PYL 3.0 [Zenodo record 23111395](https://zenodo.org/record/23111395) (concept
DOI 10.5281/zenodo.20767265) and PYO 2.0 [Zenodo record 23102550](https://zenodo.org/record/23102550) (concept DOI
10.5281/zenodo.20767498).
Programme 2.27 was deposited as [Zenodo record 23118577](https://zenodo.org/record/23118577).

Version 2.26 synchronises Q14 3.0. Q14 now states what the fermionic sector rests on: the finite carrier acts
through $\mathrm{SL}(2,\mathbb{Z}/q\mathbb{Z})$, so a real metaplectic model and a doublet carrying
$\mathfrak{sl}_2(\mathbb{C})$ are supplied model data, on which the tensor algebra is proved; the Lorentz reading
rests on a spin solder [H-Spin] and the electroweak reading on a distinct $U(2)$ weak factor [H-Weak], neither
supplied. The Q14 entry, table row, figure node, bibliography entry and interactive-graph node carry these results.
The Q11-to-Q14 edge is typed conditional: Q11 Corollary 6.1 supplies a Lorentzian signature under its stated
hypotheses, which is all Q14 uses; spin soldering remains an input. PRS, the A4-Note, CHO, AOG-Note and
Q11OF were written against Q14 2.0 and are flagged as open consumer corrections in the registry text and
the graph. Q14 3.0 was deposited as [Zenodo record 23071163](https://zenodo.org/record/23071163) (concept DOI
10.5281/zenodo.20218409). Programme 2.26 was deposited as [Zenodo record 23071204](https://zenodo.org/record/23071204).

Version 2.25 synchronises Q11 2.0 and Q5b 2.2.1. Q11 proves that invariance under a spatial $\mathrm{SU}(2)$ action
leaves the temporal coefficient free: with the action trivial on the ordering line and spin one on the spatial sector,
every invariant form is $\alpha\,k_\tau^2 + \beta\,Q_{\mathrm{sp}}$ with independent scalars and no mixed term, and
no linear $\mathrm{SU}(2)$ action on four real dimensions fixes a Lorentzian form up to an overall factor. The
identification of $\tau$ with BFS depth is a modelling input with a free step, and fixing $A_\tau/A_H$ needs a datum
coupling the temporal and spatial normalisations that no source supplies. Q11 closes a derivation route, not the
possibility $A_\tau = 2$. Q5b 2.2.1 describes Q11 2.0 and Q10 2.0.1 as they stand. The Q11 entry, table row, figure,
bibliography and dependency graph carry these results; the W1-to-Q11 and U1-to-Q11 edges are removed, a Q7-to-Q11
edge in the interactive graph records the supplied spatial action, and the edges from Q11 to the consumers of the
former values are marked pending revision. Q11 2.0 was deposited as [Zenodo record 23024499](https://zenodo.org/record/23024499) (concept DOI
10.5281/zenodo.20098387) and Q5b 2.2.1 as [Zenodo record 23024508](https://zenodo.org/record/23024508). Programme
2.25 was deposited as [Zenodo record 23024512](https://zenodo.org/record/23024512).

Version 2.24 synchronises Q8 2.0 and Q10 2.0, deposited as
[Zenodo record 23002451](https://zenodo.org/record/23002451) (concept DOI 10.5281/zenodo.19879909) and
[Zenodo record 23002454](https://zenodo.org/record/23002454) (concept DOI 10.5281/zenodo.19880900), together
with Q5b 2.2 ([Zenodo record 23023118](https://zenodo.org/record/23023118), concept DOI 10.5281/zenodo.19686700)
and Q10 2.0.1 ([Zenodo record 23023127](https://zenodo.org/record/23023127)), which aligns Q10's description of Q5b
with Q5b 2.2. Q8 proves that the Heisenberg commutator supplies no central coefficient, that a
positive constant central coefficient needs a term of homogeneous degree four and a length scale, and that for a
supplied fully invariant rank-three target $A_H = A_Z = 2\lambda$ with $\lambda$ free. Q10 proves a sharp ratio
lemma and a conditional isotropy theorem under named inputs, with the absolute value only from an independent
scale; no coefficient value is derived. Q5b records [H-lift], the full-rank extension Q5b-O2 and the coefficient
values Q5b-O3 as open. The synthesis, inventory, figure, bibliography and dependency graph carry these results;
the circular Q8-to-Q10 edge is removed. Q6b, Q11, the emergent-geometry note and the other consumers of the former
values remain marked pending revision. Programme 2.24 was deposited as
[Zenodo record 23023148](https://zenodo.org/record/23023148).

Version 2.23 synchronises W1 2.0.1, deposited as
[Zenodo record 22926106](https://zenodo.org/record/22926106) under concept DOI
10.5281/zenodo.19886319. W1 withdraws its claimed proof of [H-w]. Its exact
summation inequality concerns a separately defined finite-window proxy under a
relative profile estimate that U1 never proved. Under the specified five-block
calibration, the proxy's target is a sum through depth 22, not the infinite
series formerly claimed. The bridge to Q5a's response-average weights, their
separate directional limits [H-w′], and a common positive limit [H-w] remain
open. The synthesis, inventory, bibliography and dependency graph now carry
that distinction. Q10 and the other downstream papers remain pending their
own audits. Programme 2.23 was deposited as
[Zenodo record 22945485](https://zenodo.org/record/22945485).

Version 2.22 synchronises U1 2.0. U1 proves an unconditional equidistance obstruction for
finite Heisenberg multiplication generators; a separate adjacent-character example excludes
the claimed uniform modulus for their sum. Its former proof of [U], its $O(q^{-1/2})$ rate and
the claimed Q10/Q7 closure are withdrawn, while [U] remains open. The inventory, bibliography
and both graph surfaces now record that result. W1's quantitative step imports the withdrawn
U1 rate and awaits its own audit; Q10 and the other downstream papers remain pending.
U1 2.0 is deposited as [Zenodo record 22905732](https://zenodo.org/record/22905732),
under concept DOI 10.5281/zenodo.19881146. Programme 2.22 was deposited as
[Zenodo record 22913308](https://zenodo.org/record/22913308).

Version 2.21 synchronises Q9 2.0. The Q9 entry now records a kinetic Mosco limit conditional on [K]
and [R], with the energy scale retained in its modulation bound. Its free kinetic form selects no
nonzero central character, and the relative moment estimate applies to individual vectors in a
cone rather than defining a closed coercive form. Q9 no longer discharges [H-lift] or establishes
bridge non-obstruction or a geometric coefficient $A_H$. The programme synthesis, Q5b/Q6b rows,
Q9 inventory entry, bibliography and both graph surfaces carry that distinction; the Q9-to-Q10
edge remains a citation edge, without theorem supply. The downstream paper audit continues in the
agreed Q9–U1–W1–Q10–Q8–Q11–Q5b order.

Version 2.20 retypes the Q7 entry for Q7 version 2.0, whose central result changes. Q7 now states the
requirements an equivariant bridge would have to meet and proves those that follow from representation theory on
the supplied carrier. Q7 distinguishes the measured-space identification [ID], target action [ACT], real rotation
compatibility [INV] and adapted unitary transport [ADAPT]. Abstract intertwiners exist once the
isomorphic modules are supplied. The rank-two spatial principal symbol of Q5b cannot equal a
positive rank-three Casimir form. A new positive spatial target remains to be constructed.
The Casimir reading of the central coefficient, the isotropy fit, the
transfer of a discrete compression to the continuum symbol, and the values imported from Q8, Q10, U1 and Q11 are
withdrawn. Status changes: the Q7 row becomes proved for the requirements on the supplied carrier with the
identification recorded as open, and the Q7 node is redrawn accordingly in both figures, with the interactive
graph's status letter moving from structural to proved and its description naming the open geometric hypotheses; the
arrow leaving Q7 loses the proved colour and the Q7-to-Q9 edge is no longer drawn on the spine; the terminal edge
into the co-metric result box is likewise demoted and the box marked pending revision; the physical-path prose no
longer lists O29 among the suppliers of the dimensional bridge, the dependency edge being kept since Q7 cites O29
for the audit of the measured rank; and the Q5a-to-Q5b-O3 chain is no longer recorded as closed, with a second gap
at the Q7 step and a circular junction beyond it. The three edges this release is about -- O29 to Q7, Q7 to Q8 and
Q7 to Q9 -- now carry the graph's own edge typing, which states what each does and does not supply. The Q8, Q10,
U1, W1 and Q11 entries are marked pending revision on the surfaces that assert their results, each pending its own
step in this cascade. The Q5b and Q6b entries are marked too: each asserts the co-metric on the strength of those
values, Q6b's own remarks calling it fully explicit and fully determined. The Lorentz-capacity entries, which
consume the values rather than deriving them, carry the marker on the value, and on their own conclusions only
where those conclusions restate it.

This registry version describes Q7 version 2.0, deposited on 19 September 2026 as version record
10.5281/zenodo.22838313 of concept 10.5281/zenodo.19802123; the bibliography cites the concept DOI.

Version 2.19 synchronises O26 2.1 in the synthesis, inventory row, bibliography and interactive graph.
Under O26 Hypothesis 4.4(a), the embedded products lie in the symmetric square, with rank at most three for
dimension two: the rank-four target is excluded under that contract alone. Tests 1–2 are implementation checks.
The O28–O29 ranks measured in End(H_eff) do not measure End(V_rho), and occupy no row of the embedded-covariance
decision table. The admissible embedding remains open. No primary status or dependency edge is changed.

Version 2.18 synchronises the NIF-Note 1.5 release in the Branch I synthesis, inventory row, bibliography note and
interactive graph. It separates ENI's one-way implication from the conditional representation route, records
temporal order under [H-acyc] and irreducibility under the representation dictionary, carries the dimension and
generating-pair premises for non-commutation, and attributes the finite obstruction to HeisenbergStructure 2.1. The
Heisenberg group, non-trivial central character and associated Weil action remain supplied. The Born rule and Q5b
spatial limit [H-L] remain open. No new result or status reclassification is introduced.

Version 2.17 types the status of every paper on one vocabulary of seven labels (proved, structural, numerical,
conditional, heuristic, open, synthesis), with a primary label per paper carried identically by the inventory row,
the synthesis paragraphs where they state a status, the dependency figures and the interactive graph. Numerical
and conditional are defined in the conventions; synthesis becomes a graph status. Primary labels re-audited
against the papers' own status statements: EBJ proved with open items; O25, O28 and O32 numerical;
HeisenbergStructure, O18, O27, Q5a, AOG and SRN proved with open items; O21, O23 and Q9 conditional; Q6a open;
the presentation notes and the Lorentz-capacity synthesis typed synthesis; figure styles corrected for the white
paper, Born-Infeld, Q1, Q3, O18, O22, O24, O27, O29, O30, O31, Gravity and E2, and the dependency-figure
styles are brought into line with the rows throughout.

The re-audit of every primary against the papers' own status statements also retypes O10, O11, O13, PTO
and LowLCapacity numerical; O16, O20, O24, Q5b, Q10, Q13, U1, W1, LCII, LorCap, TempProj, SpectralRelaxation,
FibreErasure, Thermodynamics, Q3, ENT-E2 and Gravity conditional on the hypothesis each names; O4, O19 and TPC
open; Q12, KUD and Lorentz (a proved negative result about a posited truncation) proved; Cosmology heuristic; O22
structural; O6 keeps its proved primary with the confinement corollary now recorded conditional, O8
structural on an empirical premise, CHO
conditional on the inherited central-phase lift, TopInv and O31 with their secondary labels; the O4 and O6 rows
and paragraphs state the current negative results.

The pass also removes the last bare-word status cells (O29 numerical, O30 conditional), defines heuristic and the
principal-contribution rule in the conventions, reorders the graph legend on that vocabulary, and restates the
contribution cells of H2, TopInv and ENT-E1 and the short titles of Q9, U1 and W1, so that each names the hypothesis
or the open
extension its result carries. The graph node descriptions are swept against the rows over the whole surface,
correcting those that stated a
retracted derivation (O4), an unestablished observable (O19) or an identification the paper does not prove (Q7),
and Q6b is retyped conditional on the Q5a Mosco hypotheses and [H-L] on all four surfaces.

The status conventions state the secondary-label rule as mandatory for an open or conditional item of the paper's
own principal result, and it is applied by predicate over all rows. Two claims the registry itself refutes are
withdrawn: the free-fraction identification of the capacity radius with the metric radius (LCII), and the
gravitomagnetic reading of the Lorentz vector sector, which its paper lists as open.

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
row corrections, reverses the AAR/PRS edge, removes the unsupported AAR to Q11OF, Gravity to A4-Note, SRN to Q14 and
O31 to TPC edges, types
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
