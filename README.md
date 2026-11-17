# Computational Economic Planning

Research on production networks and the information needed for economic
coordination, with a reproducible Leontief reference model and a study of
advance capacity information in inventory decisions.

## Capacity-loss timing

In a three-period inventory model, an early loss of production capacity can
raise the current base-stock target either more or less than an equally
large later loss. For independent two-point demands and positive holding and
backlog costs, six thresholds classify the target sets for every nondegenerate
demand probability and every cost ratio. The examples attain both directions
of the one-loss target-spread bound, and the reversals persist under the
continuous-density perturbations specified in the paper.

The model has backlogging, zero lead time, real orders and known future
capacity. The two compared future capacity vectors remove the same amount
from a common baseline. The examples contradict Conjecture 1 and the adjacent
equal-target assertion in the final journal version of the cited ACI paper;
its Theorem 4 concerns coordinatewise capacity monotonicity. The manuscript
also studies a separately specified loss-location information experiment.
External peer review and broader priority review remain open.

- [Manuscript](manuscript/main.tex) and [PDF](manuscript/main.pdf): model,
  classification, proofs, and references.
- [Sharp timing theorem](docs/research/aci_sharp_timing_theorem.md): detailed
  phase diagram and exact calculations.
- [Source review](docs/research/final-journal-independent-review-2026-11-15.md):
  comparison with the journal version and its numbered claims.
- [Claim register](docs/research/CLAIM_REGISTER.md): evidence and open
  questions for the research program.

## Production-network baseline

The reference implementation solves `(I - A)x = d` for a nonnegative input
coefficient matrix `A` and final demand `d`, with viability and capacity
checks. This is a classical Leontief model. The research agenda also considers
information constraints, production paths, and comparisons of coordination
mechanisms; empirical institutional conclusions require calibrated data and
matched information, resources, timing, and objectives.

The [research roadmap](docs/research/ROADMAP.md) describes the mathematical
questions. The [research agenda](docs/research-agenda.md) sets out the broader
modeling program. The [literature ledger](docs/literature/reading-ledger-2026-11-15.md)
records sources and their inspection levels.

## Reproduce

Install the reference model and run its tests:

```sh
python -m pip install -e '.[dev]'
python -m econplan.demo
python -m pytest -q
```

Reproduce the exact ACI calculations with the Python standard library:

```sh
python scripts/reproduce_aci_counterexample.py
python scripts/aci_piecewise.py
```

For the scenario-tree linear-programming checks, install the research
dependencies and run:

```sh
python -m pip install -e '.[dev,research]'
python scripts/check_aci_scenario_lp.py
python scripts/audit_aci_full_phase.py
```

Build the manuscript with `bash scripts/build_manuscript.sh` and a LaTeX
installation. The proof note can be rendered with
`bash scripts/build_proof_pdf.sh`, Pandoc, and XeLaTeX.

## Repository map

`manuscript/` contains the ACI paper; `docs/research/` contains research
notes and the claim register; `docs/literature/` contains source reviews;
`src/econplan/` contains the reference model; `scripts/` contains the research
calculations and build commands; and `tests/` contains executable checks.
