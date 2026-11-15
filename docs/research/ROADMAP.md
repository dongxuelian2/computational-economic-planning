# Research roadmap — 2026-11-15

**Current manuscript:** [main.tex](../../manuscript/main.tex) proves the
six-threshold classification for all positive costs and incorporates independent
model-agent review. The [version/priority audit](../literature/aci-version-priority-audit-2026-11-15.md)
records actual coverage and unavailable final-journal routes. An authorized
request for the final copy has been sent to the author; its response is pending.
The paper's criticism targets only the precisely identified thesis/WP assertions.

## Objective

Use mathematics to identify rigorous, economically meaningful structure in constrained production and coordination. Begin with published questions whose assumptions, conclusions and proof status can be checked. Static nonnegative Leontief theory is a **baseline**; it should not be advertised as novel economics. The long-horizon economic world model in [research-agenda.md](../research-agenda.md) remains a destination only after sharply formulated theory and validation.

## Primary track A — advance capacity information and inventory policy

**Continuation result:** [sharp timing theorem](aci_sharp_timing_theorem.md)
now gives a full cost-ratio phase diagram for every `0<p<1` in a three-period
iid family, the sharp universal timing spread with equality in both directions,
and exact value/regret for learning the loss location. The continuous-domain
Bellman and independent scenario-tree LP implementations are included.
External review and the final-2011-version audit remain open gates; the
computations do not close them.

**Source:** Jakšič et al., BETA Working Paper 249 (2008), and Marko Jakšič, *Inventory models with uncertain supply* (2016), Chapter 2, Conjectures 2.1–2.2. The 2011 Naval Research Logistics journal version has not been checked in full; never claim a refutation of its final theorem without reading it.

1. **Source-version audit.** Obtain the 2011 final journal version (DOI 10.1002/nav.20450), identify exact published assertion, inspect subsequent errata/citations and changes from the 2008 working paper to the 2016 thesis.
2. **Formalize the counterexample.** Three periods, i.i.d. demands 0 or 2 with probability 1/2, h=1, b=5, \(\alpha=1\). A one-unit loss in future period 2 changes \((q_2,q_3)=(1,2)\) to (0,2) without changing the optimal first-period post-order stock (2). A loss in period 3 yields (1,1) and raises the unique target to 3. Include exact Bellman values, real-order convexity and an independent scenario-tree LP check. See [audit](advance_capacity_audit.md) and [script](../../scripts/reproduce_aci_counterexample.py).
3. **Prove the surviving bound independently.** With future capacity \(q_i\) reduced by \(\eta\ge0\), derive \(0\le\hat y(q-\eta e_i)-\hat y(q)\le\eta\) through a derivative sandwich for convex capacity-clipping operators, not from the false temporal ordering. Obtain vector \(L^1\) sensitivity.
4. **Identify the sharp positive theorem.** Map exact parameter regions; test whether a two-period horizon, deterministic demand, constrained cost ratio, fixed bottleneck location or extra information order restores temporal monotonicity. Favor a structural necessary-and-sufficient condition or sharp restricted-family theorem over more sample rows.
5. **Information value extension.** Quantize capacity forecasts and prove decision-error and regret bounds under matched lead-time, inventory and reporting assumptions. Stronger result should have a lower bound or tight example, and a clear difference from established inventory and communication theory.

**Acceptance:** a statement precise enough to falsify, complete proof or exact counterexample, independent validation, source-version and novelty check, physical interpretation, and reproducible commands.

## Second track B — common hidden history and compressed beliefs

[Audited preprint](information_state_audit.md): Sudhakara & Zhang (arXiv:2507.09223v1), §4.1. Two retailers can retain conditionally dependent inventories even given the current hidden Markov state: past unobserved shared regimes remain a common latent cause. The exact product-form belief needs additional conditions. The counterexample is **local to that assertion**, not to the whole paper or simulation. Target a low-dimensional sufficient statistic or a computable approximation error for common-information inventory control. First construct and verify an exact finite-state joint-belief baseline.

## Third track C — weighted production paths

[Scoped path audit](production_paths_audit.md): Nikolakoudis, *Incomplete Information in Production Networks* (2025). When path weights are heterogeneous, \((WA)^k\) generally differs from \(W^k A^k\); a later appendix already has the correct expression. An inverse matrix can exist while the relevant Neumann series diverges for negative response. Treat these as **local formula/domain clarifications**, not as a refutation of the model. Future work: rigorous signed-response conditions and error-controlled truncated path representations, if nontrivial and not already covered by M-matrix theory.

## Evidence and calibrated extension

- The [205-item reading ledger](../literature/reading-ledger-2026-11-15.md) includes 142 actually inspected abstracts/sections/proofs, 63 bibliography-only items; the entire corpus has **not** been fully read. Use exact version identifiers and check forward citations.
- Keep core model assumptions, decision timing, observable information, guarantees and economic interpretation in separate sections. Synthetic numerical models are **not** evidence about which institution is superior.
- Only add multiregion calibration, empirical data and coordination benchmarks after the theoretical question and comparable baseline are fixed.
- Stop or narrow a line that yields only known general inventory-control statements, large unverified simulations or mathematical artifacts with no economic interpretation.

## Milestones

**M1** literature/priority audit and exact ACI counterexample → **M2** independently reviewed convex sensitivity proof → **M3** restricted structural timing theorem or sharp impossibility → **M4** information quantization/belief bounds with matching benchmark → **M5** calibrated supply-network comparisons. [Existing draft PR #1](https://github.com/dongxuelian2/computational-economic-planning/pull/1) remains a separate classical reference.
