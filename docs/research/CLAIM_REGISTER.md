# Claim register (2026-11-15)

| Statement | Current status | Evidence / needed validation |
| --- | --- | --- |
| \(x=(I-A)^{-1}d\) and matrix-box endpoints for nonnegative productive \(A\) | **classical** M-matrix/Leontief theory, implemented on [draft PR #1](https://github.com/dongxuelian2/computational-economic-planning/pull/1) | Reproduced on synthetic examples; never label this a new economic theorem |
| Temporal monotonicity of base-stock response to equal early vs late capacity reductions | **counterexample in source's stated model** | [ACI audit](advance_capacity_audit.md), exact 3-period iid demand; novel priority and final 2011 journal version unchecked |
| Exact all-`p` three-period timing phase diagram | **new complete theorem proof draft, external review outstanding** | [Sharp timing theorem](aci_sharp_timing_theorem.md); explicit thresholds and boundary intervals; 504 rational real-line certificates and 54 independent floating-point LP checks |
| Universal timing spread `abs(s_E-s_L)<=eta`, equality with both signs for every `0<p<1` | **elementary upper bound plus sharp new parameter family** | Same theorem; bound derives from the prior-known coordinate sensitivity, whose priority is not claimed |
| Exact EVPI and minimax regret for loss-location information in this family | **proved model calculation** | Same note; matched timing/recourse, sample value `1/8`; generic decision-theory identity is classical |
| One-coordinate sensitivity \(0\le\Delta y^*\le\eta\) | **independently argued proof** | [Convex derivative-sandwich proof](advance_capacity_audit.md); statement already appears in early prior work, no claim of first discovery |
| Same failure for continuous-demand densities | **working extension with uniform approximation bound** | [ACI audit](advance_capacity_audit.md); check quantifier and coupling detail on review |
| Full joint retailer-inventory belief factors given only current hidden state | **false in a scoped 2025 preprint model** | [Belief audit](information_state_audit.md); conditional dependence through shared past; does not refute other conclusions |
| \(W^k A^k\) as a general heterogeneous weighted-path expansion | **local discrepancy** | [Path audit](production_paths_audit.md); \((WA)^k\) required, and paper's appendix already displays it |
| Neumann-series convergence whenever a certain inverse exists | **missing domain condition** | [Path audit](production_paths_audit.md); negative-response example; does not invalidate the inverse |
| Timing ordering under arbitrary demand/capacity paths | **open** under restricted conditions | New note exactly classifies one iid family and proves both signs occur; no general ordering follows |
| Rigorous value of \(B\) bits of forecast/communication and robust inventory | **future problem** | Need explicit timing, decision/info assumptions and matched upper/lower bounds |
| Real-economy or institutional effects of these model results | **unverified** | Calibration and matched empirical comparisons required |

**Important:** validity, bibliographic priority, software reproducibility, and causal economic applicability are separate gates. A numerical check alone is not a mathematical proof; a working-paper error alone is not a correction of its later journal version.
