# Output uncertainty and robust capacity in a Leontief system

## Question and scope

A nominal allocation may fit sector capacities while a modest increase in
technical coefficients or final demand makes it infeasible. This baseline
computes the exact componentwise range of required gross output under a
rectangular uncertainty set. It supplies a reproducible reference for the first
research milestone, not a new theorem or a dynamic planning algorithm.

Use the repository convention: A[i,j] is input i required per unit output j.
Suppose

\[
0\le A_-\le A\le A_+,\qquad 0\le d_-\le d\le d_+,
\qquad \rho(A_+)<1.
\]

All comparisons are entrywise. Every matrix/demand combination in the rectangle
is allowed; capacity c is fixed and nonnegative.

## Sharp ranges and a capacity decision

The gross output range has simultaneously attained endpoints

\[
x_-=(I-A_-)^{-1}d_-,\qquad x_+=(I-A_+)^{-1}d_+.
\]

To see this, monotonicity of the spectral radius for nonnegative matrices gives
rho(A) <= rho(A_+) < 1. The Neumann expansion

\[
(I-A)^{-1}d=\sum_{k=0}^{\infty}A^k d
\]

has nonnegative terms, each increasing entrywise in A and d. Comparing every
term and taking limits bounds every output between x_- and x_+. Both corners
belong to the rectangle, so the bounds are attained, not merely conservative
norm estimates. This describes componentwise extrema, not a claim that every
vector between them is attainable.

Consequently, all realizations satisfy x <= c exactly when x_+ <= c. The vector
c - x_+ identifies deficits and their sectors. If the true uncertainty is
correlated and excludes the upper corner, this test is sufficient but need not
be necessary. If capacity has its own independent interval, its lower endpoint
can be supplied as c; otherwise the joint dependence needs separate treatment.

## An exact perturbation identity

For nominal (A,d) and perturbed (A+E,d+e), assume both systems are productive.
Subtracting their balance equations gives

\[
x'-x=(I-A-E)^{-1}(Ex+e).
\]

In particular, take E=A_+-A_- and e=d_+-d_- to obtain the exact endpoint
spread. This avoids the often much stricter sufficient condition ||A_+||<1.
For example [[0.1,2],[0.1,0.1]] has infinity norm 2.1, yet spectral radius
0.1+sqrt(0.2) < 1 and finite nonnegative outputs. The tests include this case.

## Reproduce the example

```sh
python -m pip install -e '.[dev]'
python -m econplan.uncertainty_demo
python -m pytest -q
```

The deterministic synthetic example is saved in `results/box-example.json`.
Coefficients and demand are illustrative, dimensionless inputs; no economic
dataset is used. Nominal output is approximately (2.7699,3.9258), and capacity
is set 0.1 above it. Worst-case output is (5.1462,6.1988), so worst-case slack
is (-2.2763,-2.1730): nominal feasibility is not robust feasibility.

Testing enumerates all 64 coefficient/demand vertices of a two-sector box,
checks exact endpoint attainment and the perturbation identity, and tests 100
seeded interior points over dimensions 1,2,5,10 (seed 20261115). It also covers
invalid/reversed endpoints, zero demand, degenerate boxes, copy isolation,
missing capacity and absolute feasibility tolerances. These tests complement
the proof; random samples alone do not prove robustness.

## Numerical limits

The implementation uses NumPy linear solves, not explicit inverses. It inherits
the baseline's conservative productivity check rho(A) < 1 - 1e-12 and uses an
absolute output-unit tolerance (default 1e-9) for capacity decisions. It is not
outward-rounded interval arithmetic or a formal floating-point certificate.
Near-singular systems may amplify data and rounding error; the small spectral
margin does not control condition number. Sparse large networks, residual/error
certificates and empirical interval calibration remain future work.

## Context and sources

The inverse positivity used here is classical nonsingular M-matrix theory, not
a new identification result: see [Higham, What Is an M-Matrix? (2021)](
https://nhigham.com/2021/03/16/what-is-an-m-matrix/), including the Neumann
representation and the standard Berman–Plemmons reference it cites.

The repository's [Fernández Salguero (2026)](https://arxiv.org/abs/2606.19214)
uses synthetic coordination comparisons and explicitly qualifies institutional
interpretations. The present result does not rank coordination mechanisms.
[Han et al. (2026)](https://arxiv.org/abs/2608.06020) provides a broader economic
world-model roadmap; this module addresses only a small static feasibility
building block, not that full architecture. Those two papers were screened
at abstract level for scope, not independently reproduced.

## Planning application: demand headroom and indirect bottlenecks

For a nonnegative demand-growth direction g and an already feasible baseline b,
let demand's upper bound be b + lambda g. With R=(I-A_+)^{-1}, set x_b=Rb and
y=Rg. The robust expansion limit is

\[
\lambda_* = \min_{i:y_i>0} \frac{c_i-(x_b)_i}{y_i}.
\]

Indeed, monotonicity reduces the box problem to its upper corner and linearity
gives x(lambda)=x_b+lambda y. Each positive y_i imposes exactly the displayed
upper bound; zero y_i imposes none, provided baseline feasibility holds. Zero
growth yields infinity. An infeasible baseline is rejected, not labeled a
zero-growth solution. This is a classical linear bottleneck calculation, not
an optimal allocation across freely chosen demand directions.

`demand_expansion_limit(upper_base_demand, upper_growth)` implements the formula.
It accounts for upstream intermediate-input requirements: with A[0,1]=0.5,
other entries zero, capacity (1,10), zero baseline and growth (0,1), sector 1
limits expansion to 2 although sector 2 alone would permit 10. Tests verify
attainment, violation above the limit, zero growth and infeasible baselines.
Correlated uncertainty and near-singular numerical limitations remain as above.
