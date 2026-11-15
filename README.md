# Computational Economic Planning

A **theorem-first, reproducible research program** on production-network feasibility, dynamic inventory/capacity decisions, and the information requirements of coordination. The codebase retains its classical static Leontief reference implementation, while the active research program tests **published mathematical claims** with explicit counterexamples and proofs.

**Active research tracker:** [Issue #3 — capacity-information theory](https://github.com/dongxuelian2/computational-economic-planning/issues/3). Detailed documentation changes are in [draft PR #2](https://github.com/dongxuelian2/computational-economic-planning/pull/2).

## Two levels of work

**Reference baseline (classical):** For nonnegative input coefficients \(A\) and final demand \(d\), solve \((I-A)x=d\) subject to production viability and capacities. [Draft PR #1](https://github.com/dongxuelian2/computational-economic-planning/pull/1) adds matrix-box uncertainty bounds and demand-headroom calculations. This is a documented reference, **not** a new Leontief theorem.

**Active mathematical research:** finite-horizon advance capacity information (ACI). A concrete three-period i.i.d.-demand model contradicts the proposed temporal ordering of optimal base-stock responses to equal capacity losses, while an independent convex-operator argument establishes a valid \(0\le\Delta y^*\le\eta\) sensitivity bound. Further audits of hidden-demand common beliefs and noncommuting production-network paths are separate, precisely scoped leads. Publication priority and later versions require additional review.

## Research navigation

| File | Role |
| --- | --- |
| [Research roadmap](docs/research/ROADMAP.md) | Main theorem target, conditional second tracks, milestones and stop criteria |
| [Claim register](docs/research/CLAIM_REGISTER.md) | Separates validated calculations, working arguments, source defects and open problems |
| [ACI counterexample and proof](docs/research/advance_capacity_audit.md) | Three-period exact counterexample, continuous-demand extension, independent sensitivity proof |
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
~~~

The initial code and tests live under src/econplan/ and tests/. New research notes are under docs/research/, while paper-by-paper references live under docs/literature/. This keeps classical implementation claims separate from theoretical discoveries and unreviewed proposals.

**Evidence standards:** Reproducible computations do not prove general theorems; a mathematically correct counterexample is distinct from priority over later literature; a local error in a paper does not invalidate its main conclusions. Comparisons of institutions require matched information, resources, timing and objectives, followed by real-data calibration where appropriate.