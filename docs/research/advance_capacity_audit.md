# Advance capacity information: exact counterexample and independent sensitivity proof

**Continuation:** [sharp timing theorem](aci_sharp_timing_theorem.md) extends
the example to every `0<p<1`, gives exact cost thresholds and all boundary
minimizer intervals, and attains the sharp timing-spread bound with either
sign. An exact continuous-domain solver and independent scenario-tree LP
are now included in this repository; see that note for their roles and limits.

Research audit: 2026-11-15. Source version and mathematical scope matter. The counterexample and sensitivity argument were checked in the preceding research audit, but external peer review and a complete subsequent-priority check have not occurred.

## Source and precise question

Marko Jakšič, *Inventory models with uncertain supply* (PhD thesis, TU Eindhoven, 2016), Chapter 2, pp. 25–32 and Appendix A, pp. 50–56: [thesis PDF](https://pure.tue.nl/ws/files/41303873/20161031_Jaksic.pdf). Conjecture 2.1 says that, when equal capacity losses occur in consecutive future periods, the earlier loss should induce at least as high a current base-stock target. Conjecture 2.2 states an \(\eta\)-unit loss in one future capacity increases the base-stock target by at most \(\eta\).

Earlier: Jakšič, Fransoo, Tan, de Kok & Rusjan (2008), BETA Working Paper 249, *Inventory management with advance capacity information*, [working paper](https://pure.tue.nl/ws/portalfiles/portal/3296948/691623823560851.pdf), Theorem 4 and Appendix. A later 2011 journal article, [DOI 10.1002/nav.20450](https://doi.org/10.1002/nav.20450), is identified bibliographically, but the full final text was **not** checked. Do not claim to have refuted the journal version.

## Three-period model and exact counterexample

Horizon \(T=3\), zero lead time, unlimited backlogging, current inventory holding cost \(h=1\), backlog cost \(b=5\), no discount (\(\alpha=1\)). Demands are independent and identically distributed:

\[
\mathbb P(D_t=0)=\mathbb P(D_t=2)=1/2.
\]

A post-order inventory level \(y\) incurs \(\ell(y-D_t)=(y-D_t)_++5(D_t-y)_+\); for \(V_4=0\), use the source's Bellman recursion

\[
J_t(y)=\mathbb E[\ell(y-D_t)+V_{t+1}(y-D_t)],\qquad
V_t(x)=\min_{0\le z\le q_t}J_t(x+z).
\]

Compare the baseline \((q_2,q_3)=(1,2)\), an **earlier** one-unit loss \((0,2)\), and a **later** one-unit loss \((1,1)\). Exact rational values:

| \(y\) | Baseline \(J_1(y)\) | Earlier loss \(J_1(y)\) | Later loss \(J_1(y)\) |
| ---: | ---: | ---: | ---: |
| 0 | \(63/4\) | \(43/2\) | \(18\) |
| 1 | \(8\) | \(55/4\) | \(41/4\) |
| 2 | \(9/2\) | \(6\) | \(11/2\) |
| 3 | \(19/4\) | \(25/4\) | \(21/4\) |
| 4 | \(13/2\) | \(13/2\) | \(7\) |

All relevant Bellman costs are convex piecewise linear, with integer breakpoints (the terminal loss has these, and integer-demand expectation and minimization over integer-capacity intervals preserve them). This establishes the *continuous-order* minima as well as the integer-grid check. At \(y=2\) the earlier-loss cost has adjacent slopes \(-31/4,1/4\), so its unique minimizer is 2. At \(y=3\) the later-loss cost has slopes \(-1/4,7/4\), so its unique minimizer is 3. Baseline minimizes uniquely at 2. Thus

\[
\boxed{\hat y_1(0,2)=2<3=\hat y_1(1,1).}
\]

The proposed temporal monotonicity fails even with iid demands and the same total future capacity in the two loss scenarios. With initial inventory 0 and current capacity \(q_1\ge3\), both decisions can be implemented. Total optimized costs do **not** reverse in the same direction (6 for earlier loss and 21/4 for later loss). This is a counterexample to a *policy threshold ordering*, not to the general ordering of total welfare losses.

The reversed ordering persists over the **open** holding/backorder ratio region \(9/2<b/h<17/3\), holding the demand/capacity assumptions fixed. For earlier loss, slopes on (1,2) and (2,3) are \(h-7b/4<0\) and \((17h-3b)/8>0\). For later loss, slopes on (2,3) and (3,4) are \((9h-2b)/4<0\) and \(7h/4>0\).

## Continuous demand extension

To exclude an artefact of discrete demand, couple \(D_t^\varepsilon=2B_t+U_t\) to \(D_t=2B_t\), where \(B_t\) are iid fair Bernoulli and \(U_t\) iid Uniform[0,\(\varepsilon\)]. The current loss is 5-Lipschitz and the future-horizon continuation value has Lipschitz constants at most 5 per remaining period. Backward induction yields

\[
\sup_y|J_1^\varepsilon(y)-J_1^0(y)|\le30\varepsilon.
\]

For the earlier and later loss objectives, global growth away from the unique minimizers is at least \(|y-y^*|/4\). Consequently every minimizer under smoothed demand is within \(240\varepsilon\) of the discrete minimizer. With \(\varepsilon=10^{-3}\), the earlier minimizer lies in [1.76,2.24], the later one in [2.76,3.24], so the ordering reversal remains strict with a continuous density.

## Independent proof of the surviving sensitivity bound

**Proposition (under the original finite-horizon convex inventory assumptions).** If future capacity in coordinate \(i\) decreases by \(0\le\eta\le q_i\), and \(\hat y_H\), \(\hat y_L\) denote the smallest pre- and post-change minimizers, then

\[
0\le \hat y_L-\hat y_H\le\eta.
\]

For a finite convex function \(J\), write \(g=J'_+\) (nondecreasing) and define the capacity-clipping operator \((T_qJ)(x)=\min_{0\le z\le q}J(x+z)\). Its right derivative is

\[
(T_qJ)'_+(x)=\Phi_qg(x)
=\max\{g(x),0\}+\min\{g(x+q),0\}.
\]

Geometrically, if \([x,x+q]\) lies below the minimizer, optimize at the right endpoint; if it meets the minimizer, value is constant; if it lies above, optimize at the left endpoint. Monotonicity of \(g\) gives

\[
\Phi_qg(x-\eta)\le \Phi_{q-\eta}g(x)\le \Phi_qg(x).
\]

The derivative operator preserves pointwise order and commutes with translations. At the time of the altered capacity, both scenarios have the same post-order cost \(J\), so this sandwich holds for the future values. Moving backward, expectation and addition of convex holding/backorder cost preserve the derivative sandwich; the unchanged preceding capacity operators also preserve it. Bounded finite-horizon linear-cost slopes justify passing right derivatives through expectation. At the initial period,

\[
(J_t^H)'_+(y-\eta)\le (J_t^L)'_+(y)\le(J_t^H)'_+(y).
\]

For a convex function with smallest minimizer \(s\), \(s=\inf\{y:J'_+(y)\ge0\}\), so the sandwich gives \(\hat y_H\le\hat y_L\le\hat y_H+\eta\). Changing multiple capacities one coordinate at a time yields \(|\hat y(q)-\hat y(r)|\le\|q-r\|_1\).

This is an **independent correct proof of a claim already present in the 2008 source**, not a first-publication claim. It must not rely on the false earlier/later comparison.

## Local defect in the older proof

The 2008 working paper's Appendix for Theorem 4 replaces a capacity loss with a stock-position translation in a derivative **as an equality**. These are different resources. In our model at \(y=5/2\), the actual derivative for future capacities (0,2) is \(1/4\), whereas the alleged translated expression evaluates to \(-1/2\). A valid one-sided derivative sandwich replaces that equality, but does not prove the temporal ranking. The 2016 thesis uses a valid comparison for a related first-coordinate lemma.

## Reproduce and audit priorities

~~~sh
python scripts/reproduce_aci_counterexample.py
python -m pytest -q
~~~

The original standard-library script checks rational Bellman values and adjacent slopes; convexity supplies real-order global optimality. The continuation adds `scripts/aci_piecewise.py`, a rational Bellman solver over the whole real line, and `scripts/check_aci_scenario_lp.py`, a separate continuous scenario-tree LP implementation. The latter uses floating point and checks rather than proves the new theorem. Before claims about the final journal version, obtain the **2011 final journal text** and complete the forward-citation/erratum audit.
