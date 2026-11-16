# Computational Economic Planning

A **theorem-first, reproducible research program** on production-network feasibility, dynamic inventory/capacity decisions, and the information requirements of coordination. The codebase retains its classical static Leontief reference implementation, while the active research program tests **published mathematical claims** with explicit counterexamples and proofs.

**Active research tracker:** [Issue #3 — capacity-information theory](https://github.com/dongxuelian2/computational-economic-planning/issues/3). Detailed documentation changes are in [draft PR #2](https://github.com/dongxuelian2/computational-economic-planning/pull/2).

**New theorem draft (2026-11-15):** [sharp ACI timing phase diagram](docs/research/aci_sharp_timing_theorem.md).
For every Bernoulli demand probability `0<p<1`, explicit cost thresholds give
both strict timing orderings and every boundary minimizer interval. Both signs
attain the universal target spread `eta`. Exact rational real-line Bellman
certificates and an independent scenario-tree LP accompany the proof. External
peer review and broader priority clearance remain outstanding.

**Manuscript-stage update:** [complete paper](manuscript/main.tex) covers
every positive cost ratio, with six exact thresholds and all boundary intervals.
Independent model-agent review added a low-backlog reversal (`h=1,b=1/2`)
and corrected the loss-location benchmark's capacity-dependence scope.
See the [review](docs/research/independent-aci-review-2026-11-15.md) and
[version/priority audit](docs/literature/aci-version-priority-audit-2026-11-15.md).
The supplied final 2011 journal article has now been
[independently checked](docs/research/final-journal-independent-review-2026-11-15.md):
the examples disprove its Conjecture 1 and adjacent h>b assertion on p.360.
Its Theorem 4 is a different coordinate-monotonicity result and remains unaffected.
Build the paper with `bash scripts/build_manuscript.sh`.

With Pandoc and XeLaTeX installed, `bash scripts/build_proof_pdf.sh` renders
the complete theorem note to `output/pdf/`.

## Two levels of work

**Reference baseline (classical):** For nonnegative input coefficients \(A\) and final demand \(d\), solve \((I-A)x=d\) subject to production viability and capacities. [Draft PR #1](https://github.com/dongxuelian2/computational-economic-planning/pull/1) adds matrix-box uncertainty bounds and demand-headroom calculations. This is a documented reference, **not** a new Leontief theorem.

**Active mathematical research:** finite-horizon advance capacity information (ACI). A concrete three-period i.i.d.-demand model contradicts the published conjecture on temporal ordering of optimal base-stock responses to equal capacity losses, while an independent convex-operator argument establishes a valid \(0\le\Delta y^*\le\eta\) sensitivity bound. Further audits of hidden-demand common beliefs and noncommuting production-network paths are separate, precisely scoped leads. Broader publication priority requires additional review.

## Research navigation

| File | Role |
| --- | --- |
| [Research roadmap](docs/research/ROADMAP.md) | Main theorem target, conditional second tracks, milestones and stop criteria |
| [Claim register](docs/research/CLAIM_REGISTER.md) | Separates validated calculations, working arguments, source defects and open problems |
| [ACI counterexample and proof](docs/research/advance_capacity_audit.md) | Three-period exact counterexample, continuous-demand extension, independent sensitivity proof |
| [Sharp timing theorem](docs/research/aci_sharp_timing_theorem.md) | All-`p` phase diagram, sharp spread, matched-information value and minimax regret |
| [Common-belief factorization audit](docs/research/information_state_audit.md) | Conditional dependence induced by unobserved shared history |
| [Production-path mathematical audit](docs/research/production_paths_audit.md) | Noncommuting power-order and series-convergence scope issues |
| [Literature reading ledger](docs/literature/reading-ledger-2026-11-15.md) | 205 deduplicated references, with actual inspection levels and per-source notes |
| [Existing overall research agenda](docs/research-agenda.md) | Long-term economic-world-model vision, calibration and coordination comparisons |
| [Initial literature](docs/literature.md) | Selected founding sources and public input-output datasets |

## Run the reference model

~~~sh
python -m pip install -e '.[dev]'
python -m econplan.demo
python -m pytest -q
~~~

To reproduce the **separate ACI research example** using only the Python standard library:

~~~sh
python scripts/reproduce_aci_counterexample.py
python scripts/aci_piecewise.py
~~~

For the independent continuous scenario-tree LP audit:

~~~sh
python -m pip install -e '.[dev,research]'
python scripts/check_aci_scenario_lp.py
python scripts/audit_aci_full_phase.py
~~~

The initial code and tests live under src/econplan/ and tests/. New research notes are under docs/research/, while paper-by-paper references live under docs/literature/. This keeps classical implementation claims separate from theoretical discoveries and unreviewed proposals.

**Evidence standards:** Reproducible computations do not prove general theorems; a mathematically correct counterexample is distinct from priority over later literature; a local error in a paper does not invalidate its main conclusions. Comparisons of institutions require matched information, resources, timing and objectives, followed by real-data calibration where appropriate.
