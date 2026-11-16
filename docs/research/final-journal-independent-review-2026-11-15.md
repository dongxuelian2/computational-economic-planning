# Independent audit of the supplied final 2011 journal version

Reviewed on 2026-11-15 by a separately instructed model agent. This is
independent internal source/proof review, not external human peer review.
Only this report was written; existing manuscript and audit files were not
edited. No email or external mutation was performed.

## File identification and visual checks

The user supplied the actual 15-page typeset article, *Inventory management
with advance capacity information*, Naval Research Logistics 58 (2011),
355–369, DOI 10.1002/nav.20450. The metadata, page headers, title/authors,
DOI and printed pagination agree. The input SHA256 is
`5149f716675f09ca4ebf208b8163ad905e09c6325129ee55fcdd402755335481`.

The critical printed pages 360 and 368 were rendered and visually inspected
at readable resolution. They are PDF pages 6 and 14 (one-based), respectively.
Working images and extracted text remain under `/tmp/final-journal-review/`;
the copyrighted source PDF was not copied into the public repository.
Downloaded-copy provenance/watermark details are not needed for the audit.

## Main conclusion

The final journal article **does contain** the two assertions targeted by
the counterexamples, but the temporal assertion is explicitly **Conjecture
1**, not a theorem. The final paper must not be described as having a false
Theorem 4 about temporal ranking. Its actual Theorem 4 is the different,
coordinatewise capacity-monotonicity result, which these examples do not
contradict.

The current manuscript's deliberate restriction of criticism to WP/thesis
versions can now be updated to include the final article's **Conjecture 1**
and its immediately preceding h>b prose. The previous “final journal text
not obtained” qualification is obsolete. This source identification does
not establish exhaustive subsequent priority or erratum clearance.

## Exact source locations and version mapping

| Item | Final journal location | Consequence |
| --- | --- | --- |
| Model timing, exogenous capacity, lost unused capacity, independent period distributions, full backlogging, zero fixed costs | Section 2, printed pp.357–358 | Matches the comparison's physical setting. No blanket b>h assumption is imposed. |
| Bellman recursion and zero terminal value | Eq.(4), printed p.358 | Taking T=3, ACI horizon n=2, alpha=1 gives exactly the recursion used in the new paper. |
| Post-order objective J and target definition | Eq.(5), p.358, Theorem 2 pp.358–359 | The target is the **smallest** minimizer of the unconstrained post-order objective. Current capacity does not enter that target. |
| Coordinate capacity monotonicity | Theorem 4, p.359 | Not the temporal ordering and not refuted by our comparison. |
| Temporal equal-loss comparison | Conjecture 1, p.360 | Same proposed ordering as thesis Conjecture 2.1; it was WP Theorem 4(1). The final article labels it conjectural and motivates it by numerical/qualitative reasoning. |
| Equal targets when holding cost exceeds backlog cost | Prose immediately before Conjecture 1, p.360 | The low-backlog example directly contradicts this separate final-version assertion as well. |
| One-coordinate sensitivity | Conjecture 2, p.360 | Same surviving bound as thesis Conjecture 2.2; earlier WP Theorem 4(2). |
| First-future-coordinate sensitivity lemma | Appendix A, Lemma 4 and Eq.(A9), p.368 | Uses a derivative inequality, not the earlier erroneous stock-translation equality. |
| General sensitivity proof | Appendix A, proof of Conjecture 2, p.368 | Explicitly assumes Conjecture 1 to extend the first-coordinate bound to later coordinates. A separate valid sandwich proof is therefore relevant; the statement itself is prior-known. |

The final appendix does **not** reproduce the WP's false equality proof of
the temporal comparison. The reported WP equality discrepancy at y=5/2
must remain explicitly WP-only. In the final paper the temporal comparison
is not given that proof; the sensitivity argument's dependence on it is
instead stated openly.

## Applicability of the exact counterexamples

Normalize eta=1 and h=1, take independent iid D_t in {0,2} with equal probability,
T=3, n=2, alpha=1, and terminal continuation f4=0. The baseline future
capacity vector is (1,2); the early and late one-unit loss vectors are
(0,2) and (1,1). The final Eq.(4) then reduces directly to our Bellman
recursion. Both reductions are admissible nonnegative capacities.

The known capacity vectors can be states of one independent capacity
process: for instance independently give Q2 support {0,1} and Q3 support
{1,2}, with positive probabilities at both values, independent of demands.
Every compared vector is then an admissible fully revealed ACI state.
There is no requirement to put a correlated two-vector prior on the
original capacity process to compare these conditional targets.

The exact whole-real-line solver was rerun after reading the final model:

| b/h | Future capacities | Unique target | Optimal J1 value |
| ---: | --- | ---: | ---: |
| 5 | (1,2) baseline | 2 | 9/2 |
| 5 | (0,2) early loss | 2 | 6 |
| 5 | (1,1) late loss | 3 | 21/4 |
| 1/2 | (1,2) baseline | 0 | 15/8 |
| 1/2 | (0,2) early loss | 0 | 9/4 |
| 1/2 | (1,1) late loss | 1 | 33/16 |

Thus both examples contradict final Conjecture 1, and the second also
contradicts the final p.360 h>b equality assertion. Choosing initial
inventory zero and sufficiently large q1 makes the nominal target decisions
feasible; these are target comparisons, not total-cost reversals.

The final paper uses density notation but says the model is general, and
its Section 4.1 (p.360) immediately uses discrete uniform numerical demand.
In any event the explicit continuous-density smoothing argument in our
manuscript supplies reversals with small uniform perturbations, eliminating
dependence on a permissive reading of discrete-demand notation.

The separate loss-location EVPI/minimax experiment still needs its present
scope caveat: a prior supported only on (0,2) and (1,1) creates correlated
capacities. The supplied final article confirms the original periodwise
independence assumption, so that experiment must remain separately defined
and its location independent of demand. No new problem was found in the
current manuscript's corrected formulation.

## Checks and recommended integration

* Independent exact knot audit rerun: 1,168 certificates at 73 distinct
  demand probabilities passed, including six thresholds and recourse ties.
* Whole-real-line solver independently reproduced both tables above.
* Relevant journal pages were inspected in rendered form, not solely via
  potentially scrambled two-column text extraction.
* Update the introduction and source-scope section to cite final Conjecture
  1 and printed p.360; identify Conjecture 2 and Appendix A p.368 accurately.
* Remove unavailable-final-version language from current-status records,
  retaining prior access failures only as historical provenance.
* Do not rename the result a refutation of final Theorem 4, a failure of
  base-stock optimality, or a refutation of the final article as a whole.
* Do not infer that every later citing paper preserved the conjecture;
  subsequent priority/erratum checks retain their bounded-search status.

## Read-only integration follow-up

After the parent integrated these findings, the same separate reviewer
read the manuscript and documentation diff without editing it. No blocking
source-attribution, model-mapping or priority-scope problem was found.
In particular, the Appendix A dependency is stated correctly, final
Conjecture 1 is distinguished from Theorem 4 throughout, and the WP
equality defect remains limited to that earlier version. The independent
capacity embedding and the separately defined correlated-capacity
information experiment remain consistent with the final model.
