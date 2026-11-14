# Research agenda

## Long-term objective

Construct an empirically anchored, dynamically updated economy-wide model of production, trade, labor, logistics, household demand, capital accumulation, public services, and institutional interactions. Use it to test economic allocation and coordination rules under uncertainty.

## Track A — Mathematical foundations (first priority)

**Model class:** nonnegative production networks with input-output matrix `A`, final demand `d`, gross output `x`, and capacity vector `k`.

Initial feasibility conditions: `x = A x + d`, `0 <= x <= k`, with nonnegative inputs and spectral radius `rho(A) < 1`.

Research questions:
- Quantify feasible-demand regions and identify critical capacity bottlenecks.
- Bound changes in `x` when `A`, `d`, and `k` are uncertain or perturbed together.
- Compare nominally optimal, robust, and recovery-oriented allocations.
- Extend static results to intertemporal inventories, delays, and capital accumulation.
- Explore guaranteed feasible decisions under delayed or strategically reported information.

Each proposed theorem must be checked against existing literature before being claimed as new. Provide explicit assumptions, proofs, tightness examples, and numerical counterexample searches.

## Track B — Dynamic optimization

A general time-indexed balance equation takes the form:

`S[t+1] = S[t] + Q[t] + imports[t] + arrivals[t] - intermediate_inputs[t] - final_use[t] - exports[t] - losses[t]`.

Introduce sector and region indices, production yields, workforce and technology constraints, transport capacity and delays, inventory buffers, and capital dynamics.

Candidate methods: linear/convex programming, mixed-integer optimization where needed, robust and stochastic programming, model predictive control, distributed decomposition, and online learning.

## Track C — Empirical calibration

1. Start with a small, published input-output table with documented units and sector definitions.
2. Reconstruct basic accounting identities before adding optimization.
3. Separate observation, calibration, and evaluation periods.
4. Track parameter uncertainty and sensitivity to sector aggregation.
5. Compare against simple baselines to determine whether more elaborate models add predictive value.

Candidate datasets: OECD ICIO, Eurostat FIGARO, and public multi-regional input-output tables.

## Track D — Coordination benchmarks

Compare mechanisms in a common simulation environment with matched initial endowments, information access, reporting latency, external shocks, and objective metrics:

- Centralized allocation through an optimization solver.
- Decentralized decisions with price-mediated coordination.
- Hybrid / polycentric allocation with regional control and cross-region negotiation.

Evaluate unmet essential demand, nonessential consumption, production losses, capital growth, shock recovery, regional distribution, solver costs, and sensitivity to strategic behavior. Do not infer empirical institutional superiority from synthetic settings alone.

## Deliverable ladder

- **M0:** Tested static input-output reference model (this repository's initial code).
- **M1:** Capacity bottlenecks, parameter perturbation experiments, and an annotated literature review.
- **M2:** Multi-region resource and transportation constraints with reproducible benchmarks.
- **M3:** Dynamic inventory/capital model and rolling-horizon planners.
- **M4:** Real-data calibration, holdout validation, and alternative coordination benchmarks.
- **M5:** Heterogeneous-agent economic world model coupled to calibrated aggregate accounts.

## Experiment checklist

Every numerical result should record: source data and license, parameter definition and units, random seed, algorithm and version, solver settings, hardware where relevant, baseline comparison, uncertainty intervals/sensitivity, and test command.
