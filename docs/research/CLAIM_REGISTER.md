# Claim register (2026-11-15)

| Statement | Current status | Evidence / needed validation |
| --- | --- | --- |
| All-`p`, all-`r>0` six-threshold classification | **complete manuscript, independent model-agent review passed** | [Paper](../../manuscript/main.tex), [review](independent-aci-review-2026-11-15.md); 1,168 certificates from each of two exact solvers, 102 LP checks |
| Low-backlog reversal despite `h>b` | **proved source-specific counterexample** | `p=1/2,h=1,b=1/2`: targets 0 and 1, contradicting final journal p.360 and thesis p.31 prose; explicit continuous-density extension |
| Loss-location benchmark scope | **separate correlated-capacity experiment** | Location independent of demands; not the source's independent-capacity stochastic law. Low-cost fair-prior EVPI/minimax `1/32`. |
| \(x=(I-A)^{-1}d\) and matrix-box endpoints for nonnegative productive \(A\) | **classical** M-matrix/Leontief theory, implemented on [draft PR #1](https://github.com/dongxuelian2/computational-economic-planning/pull/1) | Reproduced on synthetic examples; never label this a new economic theorem |
| Temporal monotonicity of base-stock response to equal early vs late capacity reductions | **final Conjecture 1 disproved** | [Final-journal source review](final-journal-independent-review-2026-11-15.md), p.360; same model and target selector; no claim against final Theorem 4 or of exhaustive priority clearance |
| Universal timing spread `abs(s_E-s_L)<=eta`, equality with both signs for every `0<p<1` | **elementary upper bound plus sharp new parameter family** | Same theorem; bound derives from the prior-known coordinate sensitivity, whose priority is not claimed |
| Exact EVPI and minimax regret for loss-location information in this family | **proved model calculation** | Same note; matched timing/recourse, sample value `1/8`; generic decision-theory identity is classical |
| One-coordinate sensitivity \(0\le\Delta y^*\le\eta\) | **independent proof, internal review passed** | [Paper](../../manuscript/main.tex); statement is final Conjecture 2 and prior-known. Final Appendix A relies on Conjecture 1; our derivative sandwich does not. No first-discovery claim. |
| Same failure for continuous-demand densities | **proved explicit perturbation bounds, internal review passed** | [Paper](../../manuscript/main.tex); uniform objective bounds and disjoint minimizer neighborhoods for epsilon=0.001 in both exact examples |
| Full joint retailer-inventory belief factors given only current hidden state | **false in a scoped 2025 preprint model** | [Belief audit](information_state_audit.md); conditional dependence through shared past; does not refute other conclusions |
| \(W^k A^k\) as a general heterogeneous weighted-path expansion | **local discrepancy** | [Path audit](production_paths_audit.md); \((WA)^k\) required, and paper's appendix already displays it |
| Neumann-series convergence whenever a certain inverse exists | **missing domain condition** | [Path audit](production_paths_audit.md); negative-response example; does not invalidate the inverse |
| Timing ordering under arbitrary demand/capacity paths | **open** under restricted conditions | New note exactly classifies one iid family and proves both signs occur; no general ordering follows |
| Rigorous value of \(B\) bits of forecast/communication and robust inventory | **future problem** | Need explicit timing, decision/info assumptions and matched upper/lower bounds |
| Real-economy or institutional effects of these model results | **unverified** | Calibration and matched empirical comparisons required |

**Important:** validity, bibliographic priority, software reproducibility, and causal economic applicability are separate gates. The supplied final typesetting has now been checked directly; the journal-specific conclusions concern Conjecture 1, its adjacent h>b assertion, and a proof of the prior-known sensitivity bound independent of that conjecture. These are internal model-agent reviews, not external human peer review.
