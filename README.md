# Computational Economic Planning

**An open research program in economy-wide modeling, dynamic resource allocation, and computational coordination.**

The long-term objective is to build an empirically calibrated economic planning and simulation framework that connects production networks, regional trade, labor, investment, logistics, public services, household demand, uncertainty, and institutional behavior. The research emphasizes mathematical structure, falsifiable experiments, and reproducible comparisons between centralized, decentralized, and hybrid coordination methods.

## Research questions

1. **Feasibility:** Which production and consumption allocations satisfy interdependent resource, capacity, labor, and logistics constraints?
2. **Robustness:** How far can a feasible allocation deviate from forecasts before critical constraints fail?
3. **Information:** What is the cost of partial observability, delayed reporting, and misreported local information?
4. **Dynamics:** How should investments, inventories, and production schedules adapt to shocks and technological change?
5. **Coordination:** How do centralized, price-mediated, and hybrid mechanisms compare under matched information, costs, and objectives?
6. **Empirical fidelity:** Which added model features measurably improve out-of-sample predictions or decisions?

## Research structure

| Track | Scope | Intended output |
| --- | --- | --- |
| Mathematical foundations | Input-output systems, feasible allocation sets, perturbation bounds, network bottlenecks | Theorems, counterexamples, reproducible experiments |
| Robust dynamic planning | Partial observability, uncertain demand/capacity, rolling-horizon optimization | Algorithms with feasibility and performance guarantees |
| Empirical economic networks | Multi-region input-output data, calibration, scenario construction | Versioned datasets, validation reports |
| Coordination benchmarks | Planner, decentralized, and hybrid models under common evaluation | Reproducible and adversarial comparisons |
| Economic world models | Heterogeneous agents, endogenous demand, institutional evolution | Calibrated simulation and policy experiments |

## Initial implementation

The first executable module is deliberately small: a **static Leontief input-output baseline**. It solves

\[
(I-A)x=d
\]

for gross output `x`, with a nonnegative input coefficient matrix `A` and nonnegative final demand `d`. It checks basic viability and capacity feasibility. This is a reference model, **not** an economy-wide dynamic optimizer.

```bash
python -m pip install -e '.[dev]'
python -m econplan.demo
python -m pytest -q
```

### Rectangular uncertainty

`BoxInputOutputSystem` computes sharp output endpoints and worst-case capacity
slack for independent nonnegative coefficient/demand intervals whose upper
matrix is productive. Its `demand_expansion_limit` also identifies how far a
nonnegative demand direction can grow before an upstream capacity binds. Run `python -m econplan.uncertainty_demo`; see
[assumptions, proof and numerical limits](docs/box-uncertainty.md).

### Repository layout

```text
src/econplan/        Core reference models
tests/              Numerical and validation tests
docs/research-agenda.md   Research stages and evaluation protocol
docs/literature.md        Initial reading list
data/README.md            Data sources and provenance policy
.github/workflows/ci.yml Linux continuous integration
```

## First milestones

- [x] Establish a numerical input-output reference baseline with tests.
- [ ] Derive and test perturbation bounds for uncertain technical coefficients and demand.
- [ ] Implement capacity-constrained and multi-region extensions.
- [ ] Add rolling-horizon inventory, investment, and transportation dynamics.
- [ ] Create a fair comparison benchmark for alternative coordination mechanisms.
- [ ] Calibrate and validate against public multi-regional input-output data.

See [research agenda](docs/research-agenda.md) and [literature](docs/literature.md) for the detailed plan.

## Contributing

Research contributions, reproducible counterexamples, numerical experiments, and literature-based improvements are welcome through pull requests. Include assumptions, equations, numerical tolerances, and evidence supporting any mathematical or empirical claim.

## License

MIT. See [LICENSE](LICENSE).
