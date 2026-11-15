# Independent review and full-cost extension of the ACI timing theorem

Date: 2026-11-15. Reviewer: a separately tasked agent, working from the
mathematical model and primary sources. This is an independent internal
review, not external peer review, an editorial decision, or exhaustive
priority clearance. Existing theorem notes and solver files were not edited.

## 1. Review conclusion

The high-backlog phase diagram in `aci_sharp_timing_theorem.md` is correct
under its stated assumptions. I re-derived the Bellman slopes, including
the period-2 switch `R=2/p^2-1`, the real minimizer intervals at equality,
the coordinate-sensitivity sandwich and the location-information formula.
I found no counterexample or invalid algebra in that stated theorem.

Two changes materially strengthen or clarify a submission:

1. The diagram can be completed for **every positive cost ratio**, not only
   `r>(1-p)/p`. The low-cost range has another strict reversal region and
   another opposite-order region, and all six cost thresholds interlace.
2. The two-scenario loss-location information benchmark induces dependence
   between future capacities. It is a valid separately defined benchmark,
   but should not be described as the original source's independent-capacity
   stochastic model. The deterministic-vector comparison and counterexample
   remain an admissible conditional-state comparison in the original model.

The new low-cost result also contradicts a distinct prose assertion on
printed p.31 of Jakšič's 2016 thesis: it says the two scenarios have the
same optimal target when `h>b`. This is not just a high-backlog objection
to Conjecture 2.1. The page was checked in a rendered PDF, as was the
2008 working paper's Theorem 4 on printed p.11.

## 2. Complete phase statement

Normalize `eta=h=1` and write `u=1-p`, `c=3-3p+p^2`, `r0=u/p`. Define

\[
 A=\frac{uc}{p(5-3p+p^2)},\qquad
 B=\frac{uc}{p(4-2p+p^2)},\qquad
 C=\frac{u(3-p)}{3p}.
\]

Retain the high-cost thresholds from the reviewed theorem:

\[
 L=\frac{3-p-p^2}{2p^2},\quad
 E=\frac{3-2p+p^2-p^3}{p^2(1+p)},\quad
 U=\frac{3-p+p^2-p^3}{p^3}.
\]

For every `0<p<1`,

\[
 0<A<B<C<r_0<L<E<U.
\]

The **early-loss** minimizer set is

\[
 S_E=\begin{cases}
 \{0\},&0<r<B,\\
 [0,2],&r=B,\\
 \{2\},&B<r<E,\\
 [2,4],&r=E,\\
 \{4\},&r>E.
 \end{cases}
\]

The **late-loss** minimizer set is

\[
 S_L=\begin{cases}
 \{0\},&0<r<A,\\
 [0,1],&r=A,\\
 \{1\},&A<r<C,\\
 [1,2],&r=C,\\
 \{2\},&C<r<L,\\
 [2,3],&r=L,\\
 \{3\},&L<r<U,\\
 [3,4],&r=U,\\
 \{4\},&r>U.
 \end{cases}
\]

Multiply every inventory value and interval by `eta` to restore scale.
Thus two open cost intervals, `(A,B)` and `(L,E)`, have the reversed
ordering `s_L-s_E=eta`; `(B,C)` and `(E,U)` attain the opposite extreme.
The intermediate threshold `r0` is a recourse change, **not** an extra
first-period phase boundary: both targets equal 2 throughout `(C,L)`.

## 3. Independent derivation for 0<r<r0

Let `a=u-pr>0`. The terminal expected loss `G` has slopes `-r,a,1` on
the intervals separated by 0 and 2, hence has unique minimizer 0.
For a convex function with minimizer interval `[s_-,s_+]`, clipping over
`[x,x+q]` has minimizer interval `[s_--q,s_+]`; its derivative is the
right-endpoint derivative below that interval, zero within it, and the
left-endpoint derivative above it. This observation handles all recourse
ties without choosing one minimizer arbitrarily.

### Early loss: capacities (0,2)

The slopes of `V3` on intervals separated by `-2,0,2` are `-r,0,a,1`.
Consequently the period-2 post-order objective `J2` has slopes

\[
 -(1+p)r\quad(-2<y<0),\quad
 a(2-p)\quad(0<y<2),\quad
 2-p+pa\quad(2<y<4).
\]

Its unique target is 0, but `q2=0` means `V2=J2`. The current objective
has slopes

\[
 J'_{1,E}(y)=uc-pr(4-2p+p^2)
           =p(4-2p+p^2)(B-r),\qquad 0<y<2,
\]

\[
 J'_{1,E}(y)=c+pa(3-2p)>0,\qquad 2<y<4.
\]

It is strictly decreasing below zero, because the current loss has slope
`-r` there and the continuation derivative cannot be positive. Thus the
early-loss classification at `B` follows globally from convexity.

### Late loss: capacities (1,1)

The slopes of `V3` on intervals separated by `-1,0,2` are `-r,0,a,1`.
Set

\[
 b_0=u(2-p)-pr(3-p),\qquad R_0=\frac{u(2-p)}{p(3-p)}.
\]

The period-2 post-order slopes on `(0,1),(1,2),(2,3),(3,4)` are
respectively

\[
 b_0,\quad a(2-p),\quad 2-p+pa,\quad 2-p+pa.
\]

Thus `J2` has target 0 for `r<R0`, target 1 for `r>R0`, and minimizer
interval `[0,1]` at `R0`. Clipping with `q2=1` gives the following two
current slopes, valid also at `r=R0`:

\[
 d_0:=J'_{1,L}|_{(0,1)}
   =a+u\max(b_0,0)-p(1+p)r,
\]
\[
 d_1:=J'_{1,L}|_{(1,2)}
   =ac+p\min(b_0,0).
\]

For `r<=R0` these simplify to

\[
 d_0=uc-pr(5-3p+p^2)=p(5-3p+p^2)(A-r),\qquad d_1=ac>0.
\]

For `r>=R0` they simplify to

\[
 d_0=u-pr(2+p),\qquad d_1=u(3-p)-3pr=3p(C-r).
\]

The recourse threshold lies strictly between `A` and `C`. Indeed,

\[
 R_0-A=\frac{u(1+p-p^2)}{p(3-p)(5-3p+p^2)}>0,
\]
\[
 C-R_0=\frac{uc}{3p(3-p)}>0.
\]

At `R0` both formulas for `d0` agree and are negative, because

\[
 R_0-\frac{u}{p(2+p)}
 =\frac{u(1+p-p^2)}{p(3-p)(2+p)}>0.
\]

Both formulas for `d1` also agree at `R0` and are positive. Therefore
`d0` changes sign exactly at `A` and `d1` changes sign exactly at `C`.
The current objective is strictly decreasing below 0; its slope on `(2,3)`
is positive, since `G'=1`, the positive-argument continuation derivative
is positive, and the other continuation derivative is nonnegative.
Convexity proves the late-loss minimizer sets and the complete intervals
at the two equality thresholds.

### Threshold order and r=r0

The explicit differences are

\[
 B-A=\frac{u^2c}{p(5-3p+p^2)(4-2p+p^2)}>0,
\]
\[
 C-B=\frac{u(3-p+2p^2-p^3)}{3p(4-2p+p^2)}>0,
 \qquad r_0-C=u/3>0.
\]

The source's high-cost inequalities prove `r0<L<E<U` independently.
At `r=r0`, the terminal minimizer interval becomes `[0,2]`; the early
period-2 interval is `[0,2]`, and the late period-2 interval is `[1,2]`.
Nevertheless the first-period early slopes immediately below and above
2 are `-(1+p)u<0` and `c>0`; the corresponding late slopes are
`-pu<0` and `c>0`. Both current targets are uniquely 2. Thus no phase
or indifference interval is omitted at `r0`.

## 4. Concrete low-backlog counterexample and robustness

For `p=1/2`, the new thresholds are

\[
 A=7/15,\qquad B=7/13,\qquad C=5/6.
\]

Set `h=1,b=1/2,eta=1`. Exact current costs at three consecutive knots are

| y | Early loss (0,2) | Late loss (1,1) |
| ---: | ---: | ---: |
| 0 | 9/4 | 17/8 |
| 1 | 37/16 | 33/16 |
| 2 | 19/8 | 5/2 |

The early target is uniquely 0; the late target is uniquely 1. The
baseline `(1,2)` target is uniquely 0, with cost `15/8`. Thus the
late loss raises the current target even though `h>b`, and the early
loss does not. Current inventory 0 and capacity at least 1 implement
both decisions. This directly contradicts the thesis's p.31 prose
assertion as well as its general proposed ordering.

The adjacent growth constants for both objectives are at least `1/16`.
Coupling demands to `2B+Uniform[0,epsilon]` gives a uniform objective
perturbation of at most `6 epsilon` because `max(h,b)=1` and there are
three stages. Every new minimizer is therefore within `192 epsilon`
of the corresponding discrete target. For `epsilon=10^-3` the two
minimizer neighborhoods are disjoint. This supplies an explicit
continuous-density version of the low-backlog reversal as well.

For a separately defined loss-location information benchmark in the
low-cost reversal interval, the scenario regret slopes on `[0,eta]` are

\[
 e=h p(4-2p+p^2)(B-r)>0,
\]
\[
 \beta=\begin{cases}
 h p(5-3p+p^2)(r-A),&r\le R_0,\\
 h[pr(2+p)-u],&r\ge R_0.
 \end{cases}
\]

The same elementary two-scenario calculation gives
`EVPI(theta)=eta min(theta e,(1-theta) beta)` and minimax regret
`eta e beta/(e+beta)`. For the preceding example both slopes are
`1/16`; the fair-prior EVPI and minimax regret are `1/32`.

## 5. Source-model mapping and publication scope

Sources independently retrieved and inspected:

* [2008 BETA WP 249](https://pure.tue.nl/ws/portalfiles/portal/3296948/691623823560851.pdf),
  printed pp.5–8: model, timing, Bellman equations and terminal condition;
  printed p.11: Theorem 4. A publisher-provided repository cover is present,
  so PDF page indices differ from printed page numbers.
* [Jakšič's 2016 thesis](https://pure.tue.nl/ws/files/41303873/20161031_Jaksic.pdf),
  printed pp.25–28: model/Bellman formulation; pp.31–32: the `h>b` prose
  assertion and Conjectures 2.1–2.2. Rendered printed p.31 was checked.

The model permits independent nonstationary demand and capacities, zero
lead time, lost unused capacity, full backlogging, finite horizon and
holding/backlog costs with zero terminal continuation. Its Bellman cost
matches the tested recursion at `T=3`, ACI horizon 2 and discount 1.
The iid demand law is a special case. Although density notation occurs,
the source says the nature of the demand law is unrestricted and also
uses discrete-demand numerical examples. The continuous-density
robustness argument removes any remaining concern about that notation.

Conditional capacity vectors can be compared within independent capacity
laws that assign positive probability to all relevant coordinate values.
In contrast, a prior supported only on `(0,2 eta)` and `(eta,eta)` induces
negative dependence. A paper must explicitly label that loss-location
experiment as a separate information benchmark rather than silently
asserting the source's independent-capacity assumption there.

The final 2011 journal version and its subsequent citations are the parent
agent's separate audit. This report does not infer the final text from the
working paper or thesis and does not claim a journal correction without
reading that version. No author's contact was initiated.

## 6. Computational review and limits

`scripts/audit_aci_full_phase.py` is a new independent exact implementation.
It imports neither the prior PWL solver nor its threshold functions. It
evaluates integer knots by direct finite Bellman minimization. Convexity,
integer demand and integer capacity preserve integer breakpoints, so a
minimum at a noninteger order can only fill a flat interval between
consecutive minimizing integer knots. Below 0 the objective decreases;
above 6 it increases. These facts justify the finite knot range used.

The script passed **1,168 parameter certificates at 73 distinct rational
demand probabilities**, including all six phase boundaries, both recourse
switches, `r=r0` and the low-cost example. It checks the new low-regime
slope formulas independently of the published draft's derivation.

As an additional cross-check, 1,539 low-regime probes using the earlier
whole-real-line PWL implementation agreed with the new classification.
These are finite checks, not proofs of all parameter values. The symbolic
slope and threshold proof above supplies the universal conclusion.

The coordinate-sensitivity proof was reviewed directly: the clipping
derivative formula, its order preservation and translation property are
correct. The proof needs coercivity/existence of smallest minimizers and
bounded slopes for passing right derivatives through expectations; the
linear-cost finite-horizon model supplies these hypotheses. It must not
be stated for arbitrary convex costs without the appropriate integrability
and existence assumptions. The universal spread statement concerns a
consistent smallest-minimizer selector, not unconstrained choices of
different points on flat optimum intervals.

The existing scenario-tree LP uses correct history-indexed orders and
common period-1 decisions; no anticipativity error was found. Its
absolute tolerance and floating-point arithmetic make it a numerical
cross-check, especially when `p` is very close to zero or one, rather
than a universal certificate. The new exact knot audit covers such
edge probabilities without floating-point underflow.

## 7. Review of the integrated manuscript

I independently read `manuscript/main.tex` after the parent integrated the
all-cost result. The six-threshold statement, the low- and high-cost
slopes, both recourse switches, all flat optimum intervals, and the
`r=r0` comparison agree with the derivation above. I found no fatal
mathematical issue in the integrated classification.

The manuscript now correctly specifies a consistent smallest-minimizer
selector, positive linear costs, finite demand first moments, fixed known
capacities, and a separate correlated-capacity location experiment. Its
source criticism is limited to the exact working-paper and thesis
assertions; the 2011 final journal theorem is not inferred from them.

The continuous-density argument is valid: terminal objective perturbation
is at most `M epsilon`, the period-2 bound is `3M epsilon`, and the current
bound is `6M epsilon`. This gives minimizer displacement at most
`12M epsilon/mu`, hence the stated radii 192 and 240 times epsilon. All
perturbed objectives are coercive, so perturbed minimizers exist. The
numerical examples use `eta=1`; the displayed epsilon is in those units.

One precise model assumption should be added to the information section:
**the loss location is independent of the demand process**. The formula
`theta J_E+(1-theta)J_L` requires the same conditional demand law in both
scenarios. Merely having iid marginal demands is not enough if the loss
location can be correlated with their realization. With this independence
stated, revelation after period 1 and before the period-2 order produces
exactly the common-first-decision calculation in the manuscript.

The bibliographic DOI checks and final-version/priority audit are outside
this integration review and remain separately documented by the parent.
