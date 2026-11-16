# Anonymous manuscript package

Title: **Capacity-loss timing and optimal inventory targets: a complete three-period classification**.

`manuscript/main.tex` is a complete paper: abstract, related models,
six-threshold theorem for every `0<p<1` and every `r>0`, proofs of every
boundary, sharp sensitivity, discrete and continuous-density counterexamples,
and a separately specified information experiment. The author block is
intentionally empty at the user's request. No submission has been made.

Build with `bash scripts/build_manuscript.sh`; output is
`output/manuscript/aci-timing-manuscript.pdf`. A standard pdfLaTeX
installation with AMS packages, Latin Modern, microtype and hyperref is
sufficient. The bibliography is embedded; no external network or figures
are required.

Reproduce with:

```sh
python -m pip install -e '.[dev,research]'
python scripts/aci_piecewise.py
python scripts/audit_aci_full_phase.py
python scripts/check_aci_scenario_lp.py
python -m pytest -q
```

The whole-real-line and independently implemented knot solvers each pass
1,168 complete-phase certificates at 73 distinct rational probabilities.
The scenario-tree LP passes 102 floating-point cross-checks. These
computations do not replace the symbolic proofs.

The [version and priority audit](../docs/literature/aci-version-priority-audit-2026-11-15.md)
distinguishes actual full-text/section inspection from metadata screening.
The user supplied the final 2011 journal typesetting, and a separate
[source review](../docs/research/final-journal-independent-review-2026-11-15.md)
checked its model, target definition, Conjectures 1–2 and Appendix A.
The reversals disprove Conjecture 1 and the adjacent h>b assertion on
printed p.360. Its coordinate-monotonicity Theorem 4 is not contradicted.
The older working-paper proof defect is not attributed to the final article.
The source PDF and its rendered pages are excluded from this package;
the package contains our own manuscript and audit reports.

The independent reviewer was a separate model agent. Its report is not
external human peer review or a journal decision. The loss-location
experiment induces correlated capacities and is explicitly separate from
the original independent-capacity model.

The paper uses journal-neutral formatting. Operations Research Letters is
a possible short-paper venue; the [publisher's current journal description](https://shop.elsevier.com/journals/operations-research-letters/0167-6377)
limits articles to eight journal pages and allows an online appendix.
The present seven-page manuscript is not a measurement of the eventual
typeset journal-page count. No venue or author identity is selected here.
