# Sharp ACI timing theorem audit, 2026-11-15

## Supplied final-journal continuation

The user supplied the 15-page typeset 2011 article. Direct source comparison
and a separate internal model-agent review verified the model, smallest-target
definition, final Conjectures 1–2 (p.360) and Appendix A (p.368). Both exact
counterexamples refute final Conjecture 1; the low-cost example also refutes
the adjacent h>b assertion. Final Theorem 4 is not the temporal comparison.
The WP's false equality proof is absent from the final temporal discussion.
The independent reviewer also read the integrated changes and found no
blocking source/model/priority-scope issue.

The anonymous manuscript, version audit, claim register, roadmap, older
research notes, reading ledger and cover letter are updated. External
human peer review and exhaustive priority clearance are not claimed.

Checks repeated after the source update:

* `env PYTHONPATH=src python -m pytest -q`: 13 passed, Python 3.14.10.
* `python scripts/aci_piecewise.py`: 1,168 complete-phase whole-real-line
  certificates at 73 distinct probabilities passed (plus the earlier
  504-certificate high-cost subset and exact example checks).
* `python scripts/audit_aci_full_phase.py`: 1,168 independent exact
  knot-Bellman certificates passed, including all six boundaries and
  recourse switches. The source reviewer separately reran this audit.
* `bash scripts/build_manuscript.sh`: seven-page PDF compiled; no
  overfull/underfull boxes or undefined references in the final log.
  All seven pages were rendered and visually inspected.
* The source archive passed checksum verification and isolated compilation.
  Its only PDF is our manuscript; the supplied journal PDF and its rendered
  pages are excluded. The compiled text cites final Conjecture 1 on p.360.
* No mathematical code changed. The 102 scenario-tree LP comparisons below
  are the earlier recorded run, not a new local LP run in this continuation.

## Manuscript continuation

The full paper `manuscript/main.tex` now classifies every positive cost ratio.
Independent model-agent and integration reviews confirmed the proof and
identified scope fixes now incorporated: smallest-target selection, the
separate correlated loss-location experiment, and location independent of
demands. Each of the whole-real-line and independent knot solvers passed
1,168 all-phase certificates at 73 distinct probabilities; the scenario-tree
LP passed 102 comparisons; all 13 tests passed. All 7 final PDF pages were
rendered and inspected and the final LaTeX log has no overflow or undefined
reference warning. At this earlier stage the final journal copy was
unavailable and a user-authorized author-copy request had been sent.
The supplied-copy continuation above supersedes that access limitation.
Version/priority coverage and historical access failures are recorded in
the literature audit. Author identity is omitted at the user's request.
The earlier snapshot below is historical.

## Initial proof-note snapshot

Scope: [the all-probability phase theorem](aci_sharp_timing_theorem.md),
including continuous-order boundary intervals and matched loss-location
information. This is not an external proof review.

* Derived Bellman slopes analytically in both recourse regimes, with the
  internal switch `R=2/p^2-1`; checked that the formulas agree at `R`.
* Proved the threshold order `r0<L<E<U` and all boundary minimizer sets.
  In particular, early-loss indifference is the real interval `[2,4]`,
  not two isolated integer decisions.
* `python scripts/aci_piecewise.py`: 504 exact rational whole-real-line
  parameter certificates passed, including every phase boundary for the
  tested rational probabilities; fractional scale/capacity checks passed.
  Counts include repeated rational probabilities arising from different
  numerator/denominator pairs and are not 504 distinct demand laws.
* `python scripts/check_aci_scenario_lp.py`: 54 separate scenario-tree LP
  comparisons passed. Orders are indexed by observed histories, with a
  common first decision for the no-location-information benchmark.
  This implementation uses floating point; it does not provide an exact
  LP certificate. The test includes equal and unequal priors and minimax
  regret, with independently LP-computed full-information baselines.
* `python -m pytest -q`: all 13 tests passed.
* `git diff --check`: passed.
* Environment used for LP/tests: Python 3.13.11, NumPy 2.5.4,
  SciPy 1.18.1, pytest 9.2.0, installed in a temporary research venv.
* `bash scripts/build_proof_pdf.sh`: proof PDF compiled and rendered for
  visual checking. Generated files are ignored; source and build command
  are versioned.

Rechecked the 2016 thesis's Conjectures 2.1–2.2 and the 2011 publisher
page. The tested final-journal PDF/epdf routes did not supply the full
text, and the dlib stream route returned HTML. The new result is scoped
to the precisely reproduced model and the working-paper/thesis assertions.
No correction of the final 2011 journal theorem is claimed. External
review and a complete forward-citation/erratum audit remain outstanding.
