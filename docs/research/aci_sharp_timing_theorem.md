# A sharp timing reversal theorem for advance capacity information

Research proof draft, 2026-11-15. This extends the isolated `p=1/2,b/h=5`
example to every nondegenerate Bernoulli demand frequency, characterizes
the exact cost thresholds, and attains both directions of the universal
timing-spread bound. External peer review and an exhaustive priority audit
remain outstanding. The 2011 journal full text has not been obtained.

## 1. Model and main result

There are three periods, zero lead time, nonnegative real orders bounded
by the current capacity, unlimited backlogging, no ordering cost, no
terminal salvage, and no discount. The post-demand period cost is
`h x_+ + b (-x)_+`, with `h,b>0`. Demand is iid:

\[
 D_t=2\eta B_t,\qquad \Pr(B_t=1)=p\in(0,1),\quad \eta>0.
\]

All future capacities are known when choosing the first target. Compare
the baseline `q=(eta,2 eta)` in periods 2 and 3 with

\[
 q^E=(0,2\eta),\qquad q^L=(\eta,\eta),
\]

obtained by an equal early or late loss of `eta`. Let `S_E,S_L` be the
sets of global minimizers of the first-period post-order Bellman cost.
Write `r=b/h` and

\[
 r_0=\frac{1-p}{p},\quad
 L(p)=\frac{3-p-p^2}{2p^2},\quad
 E(p)=\frac{3-2p+p^2-p^3}{p^2(1+p)},\quad
 U(p)=\frac{3-p+p^2-p^3}{p^3}.                         \tag{1}
\]

**Theorem 1 (exact timing phase diagram).** For every `0<p<1`,

\[
 r_0<L(p)<E(p)<U(p).
\]

In the entire regime `r>r0`, the minimizer sets are exactly as follows:

| Cost ratio | S_E / eta | S_L / eta |
| --- | --- | --- |
| r0 < r < L(p) | {2} | {2} |
| r = L(p) | {2} | [2,3] |
| L(p) < r < E(p) | {2} | {3} |
| r = E(p) | [2,4] | {3} |
| E(p) < r < U(p) | {4} | {3} |
| r = U(p) | {4} | [3,4] |
| r > U(p) | {4} | {4} |

Thus a later equal capacity loss raises the current target more on an
explicit nonempty open interval for **every** nondegenerate demand
probability. The opposite strict ordering occurs on the next nonempty
open interval. Demand frequency alone cannot restore a universal timing
order in this family. The cost ratio changes the sign of that order.
No assertion about `r<=r0` is needed or included in the phase diagram.

**Theorem 2 (sharp universal spread).** In the finite-horizon convex
inventory model, if a coordinate loss of `eta` increases the smallest
target by an amount between zero and `eta`, then any two scenarios
obtained from the same baseline by an `eta` loss in different coordinates
satisfy

\[
 |s_E-s_L|\le\eta.                                    \tag{2}
\]

Theorem 1 attains equality with either sign, for every `p in (0,1)`.
Consequently (2) cannot be improved uniformly even with iid two-point
demands, three periods, equal loss sizes, and unique targets. The
one-coordinate bound is already in prior literature; the sharp
parameter family is the contribution proposed here.

## 2. Proof of Theorem 1

Rescale inventory by `eta` and costs by `h eta`, so `eta=h=1`. Define

\[
 G(y)=\mathbb E[\ell(y-D)],\quad a=1-p-pr,\quad
 J_t(y)=G(y)+\mathbb E[V_{t+1}(y-D)],\quad
 V_t(x)=\min_{0\le z\le q_t}J_t(x+z),\quad V_4=0.
\]

All these functions are finite convex piecewise linear. If `r>r0`,
then `a<0`, and `G` has unique minimizer 2, with slopes
`-r,a,1` on `(-infinity,0),(0,2),(2,infinity)`.
For a convex function `J` with unique minimizer `s`, capacity clipping
has slope `J'(x+q)` below `s-q`, zero between `s-q` and `s`, and
`J'(x)` above `s`. The same rule with the full minimizer interval handles
the equality cases.

### Early-loss scenario

With `q3=2`, the slopes of `V3` on the intervals with endpoints `-2,0,2`
are `-r,a,0,1`. Therefore `J2` has slopes

\[
 (1-p)a-(1+p)r\quad(-2<y<0),\qquad
 a(1+p)\quad(0<y<2),\qquad
 2-p\quad(2<y<4).
\]

The first two are negative and the third is positive, so `J2` minimizes
uniquely at 2. Since `q2=0`, `V2=J2`. The first-period slopes are

\[
 J_{1,E}'(y)=
 \begin{cases}
 a(2+p-2p^2)-p(1+p)r<0,&0<y<2,\\
 3-2p+p^2-p^3-p^2(1+p)r,&2<y<4,\\
 3-p>0,&4<y<6.
 \end{cases}                                         \tag{3}
\]

The middle slope is `p^2(1+p)(E(p)-r)`. Convexity proves the asserted
minimizer set, including the entire interval `[2,4]` at equality; it is
not just the discrete pair `{2,4}`.

### Late-loss scenario

With `q3=1`, `V3` has slopes `-r,a,0,1` with endpoints `-1,1,2`.
The slopes of `J2` on `(0,1),(1,2),(2,3),(3,4)` are respectively

\[
 (1-p)(2-p)-pr(3-p),\quad a(1+p),\quad
 B=2-p^2(1+r),\quad 2-p.                             \tag{4}
\]

Thus its target is 2 if `r<R=2/p^2-1`, is 3 if `r>R`, and is `[2,3]`
at equality. Applying the `q2=1` clipping rule to (4) gives

\[
 J_{1,L}'(y)=
 \begin{cases}
 2p^2(L(p)-r),&2<y<3,\ r\le R,\\
 1+p-p^3-p^2(1+p)r,&2<y<3,\ r\ge R,\\
 3-3p+p^2>0,&3<y<4,\ r\le R,\\
 p^3(U(p)-r),&3<y<4,\ r\ge R.
 \end{cases}                                         \tag{5}
\]

At `r=R` the formulas on each interval agree. On `(1,2)` the derivative
is negative: for `r<=R` it is
`a+p((1-p)(2-p)-pr(3-p))<0`; for `r>=R` there is the additional
nonpositive term `(1-p)B`. On `(4,5)` it is positive in both regimes
(respectively at least 1, or `3-2p`). These signs and convexity
exclude minimizers outside `[2,4]`.

The auxiliary threshold obeys `L(p)<R<U(p)`. At `r=R` the first two
lines of (5) equal `p^2-p-1<0`. Consequently the `(2,3)` slope changes
sign only at `L(p)`, while the `(3,4)` slope changes sign only at `U(p)`.
This proves the late-loss minimizer sets.

Finally,

\[
 L-r_0=\frac{3-3p+p^2}{2p^2}>0,\qquad
 E-L=\frac{(1-p)(p^2-3p+3)}{2p^2(1+p)}>0,
\]
\[
 U-E=\frac{3-p+2p^2-p^3}{p^3(1+p)}>0.
\]

Also `R-L=(1+p-p^2)/(2p^2)>0` and
`U-R=(3-3p+p^2)/p^3>0`. This completes all threshold comparisons and
the proof. \(\square\)

## 3. Proof of the universal bound and equality

For completeness, the one-coordinate sensitivity statement follows
without temporal ranking. If `g=J'_+`, the derivative of the convex
capacity-clipping operator is

\[
 \Phi_qg(x)=\max(g(x),0)+\min(g(x+q),0).
\]

Monotonicity of `g` gives
`Phi_q g(x-eta) <= Phi_(q-eta) g(x) <= Phi_q g(x)`.
Both pointwise order and translations are preserved by `Phi_q`.
Backward expectations preserve the derivative sandwich; adding the same
convex immediate cost preserves it because its derivative is increasing.
Therefore the smallest minimizers obey
`s(q)<=s(q-eta e_i)<=s(q)+eta`. Coercivity, positive costs and finite first
demand moments ensure the relevant minimizers exist; bounded linear-cost
slopes justify the derivative/expectation interchange. The same argument
allows a discount factor in `[0,1]` when the objectives are coercive.

Both `s_E,s_L` lie in `[s(q),s(q)+eta]`, which proves (2), sharper than
applying the two-vector L1 bound directly. In the reversal region of
Theorem 1 they equal `2 eta,3 eta`; in the opposite-order region they
equal `4 eta,3 eta`. These also force the baseline target to equal
`2 eta` and `3 eta`, respectively. \(\square\)

## 4. Exact value of learning the loss location

Fix `L(p)<r<E(p)`. Suppose the two capacity scenarios have the same
physical probabilities and feasible recourse in both information systems.
Only their **location** is withheld until immediately after period 1;
it is revealed before the period-2 order. Let the prior probability of
the early-loss scenario be `theta`. Starting inventory zero and current
capacity at least `4 eta` make all targets below feasible.

On `[2 eta,3 eta]`, scenario regret is linear with slopes

\[
 e=h p^2(1+p)(E-r)>0,\qquad
 \beta=\begin{cases}
 2h p^2(r-L),&r\le R,\\
 h[p^2(1+p)r-1-p+p^3],&r\ge R,
 \end{cases}                                         \tag{6}
\]

where `beta>0`. Convexity and the two unique targets imply that any
common first decision outside this interval can be moved inside without
increasing either scenario cost. Thus the exact expected cost reduction
from revealing the loss location before period 1 is

\[
 \mathrm{EVPI}(\theta)=\eta\min\{\theta e,(1-\theta)\beta\}. \tag{7}
\]

Without a specified prior, the minimum worst-case regret is

\[
 \eta\frac{e\beta}{e+\beta},\qquad
 y=\eta\left(2+\frac{\beta}{e+\beta}\right).             \tag{8}
\]

For `p=1/2,h=1,b=5,eta=1`, `e=beta=1/4`. Equal prior EVPI and minimax
regret both equal `1/8`. The generic two-action information calculation
is elementary decision theory; its application to the sharp timing
family, with matched information and recourse, is the point here.
This does not claim that a distant loss has greater total welfare cost.

## 5. Reproducibility and scope

`scripts/aci_piecewise.py` performs exact rational Bellman recursion on
convex piecewise-linear functions over the **whole real line**. It uses
neither an integer action grid nor a truncated inventory range. It checks
all boundary minimizer intervals, the formulas (3)–(5), and a grid of
rational parameters inside every phase. `scripts/check_aci_scenario_lp.py`
uses a separate continuous scenario-tree LP to check selected values and
the location-information calculation. Its floating-point output is an
independent numerical audit, not an exact proof.

The family strictly extends the previously recorded counterexample:
at `p=1/2` it yields `L=9/2,E=17/3,U=21`, and the opposite strict ordering
holds on the additional interval `17/3<r<21`. At the endpoints it records
the correct real minimizer intervals, including `[2,4]`.

Each strict interior point is robust to sufficiently small cost and
probability perturbations. Small continuous-demand perturbations preserve
the strict ordering by the same uniform Lipschitz/coercive-growth argument
as [the original audit](advance_capacity_audit.md); this note does not
claim that the displayed exact thresholds remain unchanged after smoothing.

The target assertion is Conjecture 2.1 in Jakšič's
[2016 thesis, Chapter 2](https://pure.tue.nl/ws/files/41303873/20161031_Jaksic.pdf),
and Theorem 4(1) of the
[2008 BETA working paper](https://pure.tue.nl/ws/portalfiles/portal/3296948/691623823560851.pdf).
The surviving one-coordinate bound already appears in these sources.
The [2011 journal page](https://onlinelibrary.wiley.com/doi/10.1002/nav.20450)
was rechecked on 2026-11-15, but its full text/PDF was unavailable through
the tested routes. No assertion is made about the final journal theorem.
Bounded searches for the title, timing conjecture and counterexamples did
not find this sharp parameter family; this is not exhaustive priority
clearance. No external reviewer or independent agent has reviewed it.
