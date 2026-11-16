# ACI version and priority audit

Audit date: 2026-11-15. This is a bounded source/version investigation,
not an assertion that every relevant work has been read or that priority
can be guaranteed. The final 2011 journal typesetting was supplied by the
user and checked directly. The counterexamples target its **Conjecture 1**
and adjacent h>b assertion on printed p.360, with the earlier working-paper
and later thesis assertions distinguished below. Final Theorem 4 concerns
coordinate monotonicity and is not refuted.

## Version identification

| Version / route | Evidence actually inspected | Finding |
| --- | --- | --- |
| [BETA WP 249, 2008](https://pure.tue.nl/ws/portalfiles/portal/3296948/691623823560851.pdf) | Actual title/authors, printed pp.5–8 model, p.11 Theorem 4, appendix derivative argument | Correct ACI paper; 29-page working-paper body, not the journal's 355–369 typesetting. Repository cover labels an accepted manuscript, but cites the 2008 report. The cover alone does not identify the final journal theorem. |
| [TU/e file 638020](https://pure.tue.nl/ws/files/3296946/638020.pdf) | Cover and actual first body pages | **Wrong attached body:** the ACI metadata cover is followed by *Single item inventory control under periodic review and a minimum order quantity*, by Kiesmüller, de Kok and Dabia. Excluded as evidence for ACI. |
| [Jakšič 2016 thesis](https://pure.tue.nl/ws/files/41303873/20161031_Jaksic.pdf) | Chapter 2 model, printed pp.31–32, appendices; p.31 rendered visually | Exact target Conjecture 2.1 and separate prose assertion that when h>b the two targets coincide; low-cost counterexample refutes the latter too. Conjecture 2.2 is the surviving coordinate bound. |
| [2011 NRL journal](https://doi.org/10.1002/nav.20450) | User-supplied 15-page typeset PDF; model pp.357–358, target definition and Theorem 4 pp.358–359, Conjectures 1–2 and h>b prose p.360, Appendix A p.368; critical pages rendered visually | Final Conjecture 1 is the temporal comparison, contradicted by both exact examples. The h>b prose is contradicted by the low-cost example. Theorem 4 is coordinate monotonicity. Appendix A proves Conjecture 2 conditionally on Conjecture 1; it does not reproduce the WP's false temporal-proof equality. |
| [Ljubljana repository record 16946](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=16946) | Actual HTTP response and page content | OpenAlex/Semantic Scholar label it green/publishedVersion, but current endpoint returned HTTP 410 and “record does not exist.” Excluded as accessible full text. |
| Crossref TDM / publisher PDF and ePDF links | Endpoint responses and ordinary publisher UI, before the user supplied the copy | Historical access failures through these routes; they no longer leave the journal comparison blocked. |

The exact thesis claim and the working-paper model were also checked by
an independently instructed reviewer agent; see
[the report](../research/independent-aci-review-2026-11-15.md). The two
independent mathematical implementations confirm the counterexamples.
The supplied final version was separately checked in the
[final-journal review](../research/final-journal-independent-review-2026-11-15.md),
which also reran 1,168 exact certificates and reproduced both numerical
examples. Both reviewer reports are internal model-agent reviews, not
external human peer review.

## Final-version correspondence

The supplied copy has the title/authors, DOI, volume 58, and printed
pp.355–369 matching the publisher record. Its file SHA256 is
`5149f716675f09ca4ebf208b8163ad905e09c6325129ee55fcdd402755335481`;
this identifies the reviewed copy, not a universal publisher-file checksum.
Neither the source PDF nor its rendered pages are redistributed.

| Our object / conclusion | Final article correspondence |
| --- | --- |
| Three-period Bellman recursion, zero terminal value | Eq.(4), p.358, with T=3, n=2, alpha=1 and f4=0 |
| Unconstrained target, smallest-minimizer selector | Eq.(5) and Theorem 2, pp.358–359 |
| Baseline (eta,2eta), early loss (0,2eta), late loss (eta,eta) | Fully revealed ACI states of one independent process: Q2 support {0,eta}, Q3 support {eta,2eta}, all probabilities positive and independent of demands |
| Temporal comparison disproved | Conjecture 1, p.360; WP Theorem 4(1); thesis Conjecture 2.1 |
| h>b equal-target assertion disproved | Prose immediately before final Conjecture 1, p.360; thesis p.31 |
| Coordinate capacity monotonicity retained | Final Theorem 4, p.359 |
| Coordinate sensitivity statement retained, independent proof supplied | Final Conjecture 2, p.360; its Appendix A proof on p.368 explicitly invokes Conjecture 1 and Lemma 4 |

For p=1/2,h=1,eta=1, b=5 gives unique early/late targets 2 and 3;
b=1/2 gives 0 and 1. The original independent-capacity model and the
separate correlated-capacity loss-location information experiment must
remain distinguished. The final article uses density notation and also
uses discrete uniform demand in Section 4.1; the manuscript's explicit
continuous-density perturbations supply reversals under either reading.

## Forward-citation search and inspected near neighbors

Crossref reported 14 citing references; OpenAlex and Semantic Scholar each
returned 20 citing records. Their coverage differs: they mix journal
articles, preprints, proceedings and theses. These counts are index
snapshots, not numbers of full papers read. The OpenAlex record list and
source URLs are preserved in `aci-forward-citations-2026-11-15.json`.

| Work | Primary inspection level | Relevance to the present result |
| --- | --- | --- |
| [Altuğ–Muharremoğlu 2011, DOI 10.1016/j.ijpe.2010.11.005](https://www.sciencedirect.com/science/article/pii/S0925527310004342) | Publisher introduction/model/conclusion snippets; Columbia author record abstract | Evolving capacity forecasts via MMFE and optimal state-dependent targets. No exact six-threshold family was found in the inspected material; full-text priority exclusion is not claimed. |
| [Jakšič–Rusjan 2009 heuristic, DOI 10.2478/v10051-009-0010-5](https://reference-global.com/download/article/10.2478/v10051-009-0010-5.pdf) | Full primary PDF; model, heuristic and numerical discussion | Builds an anticipatory-stock heuristic on WP 249. Discusses heterogeneous effects of uncertainty; does not present the present exact temporal-comparison phase diagram in the inspected body. |
| [Atasoy–Güllü–Tan, BETA WP 342](https://pure.tue.nl/ws/portalfiles/portal/3407748/710869.pdf), journal DOI 10.1016/j.dss.2012.01.005 | Primary working-paper model/results and journal model/conclusion snippets | Deterministic nonstationary demand, all-or-nothing supply, optional fixed order costs. A distinct model; its order-up-to characterizations are not the iid two-point finite-capacity comparison here. |
| [Çınar–Güllü 2012, DOI 10.1016/j.dss.2012.01.008](https://www.sciencedirect.com/science/article/abs/pii/S0167923612000346) | Publisher abstract/introduction snippets | Capacity flexibility/outsourcing changes the feasible recourse. Full body not audited; no claim to have excluded every related comparison. |
| [Boulaksil–Fransoo–Tan 2017, DOI 10.1007/s00291-016-0471-x](https://pure.tue.nl/ws/files/48403237/OR_Spectrum_Youssef_Jan_Tarkan_2015_final_accepted_version.pdf) | Accepted manuscript, model and ACI literature passage | Capacity reservation/utilization; cites ACI for information and ACI–ADI equivalence under restrictive assumptions, not the sharp family established here. |
| [Jakšič–Fransoo 2018, DOI 10.1016/j.ejor.2017.11.030](https://pure.tue.nl/ws/files/85751954/Jaksic_Fransoo_Dual_sourcing_in_the_age_of_near_shoring.pdf) | Accepted manuscript, model, structural/literature passages | Dual sourcing with differing lead times and uncertain capacity, not this three-period known-vector comparison. |
| [Viet–Behdani–Bloemhof 2018 review, DOI 10.1016/j.cie.2018.04.034](https://edepot.wur.nl/449530) | Accepted manuscript; framework, inventory tables, timing discussion and ACI citation context | Review of information value, not a source of the exact target-order classification. Its scope helps distinguish information timeliness from temporal capacity-loss comparisons. |
| [Jakšič–Marinč 2016 ASI, DOI 10.15458/85451.28](https://doi.org/10.15458/85451.28) | Journal metadata; related thesis Chapter 3 model | Information on replenishment of orders already in a pipeline. Journal full PDF route unavailable; no full-text exclusion is claimed. |
| [Senga–Chua–Chen, online 2026, DOI 10.1016/j.ejor.2026.04.004](https://www.sciencedirect.com/science/article/pii/S037722172600319X) | Publisher abstract, introduction, model and conclusion snippets | Regeneration/carry-over and lost sales differ from the present expiring-capacity backlogged model. Crossref assigns volume 336(1), pp.152–166, January 2027, although online publication is April 2026. No proof-level full-text audit is claimed. |

Remaining records in the saved snapshot were screened by title and
bibliographic/model information only. Topics include freight-load
forecasts, safety-stock variance, network lost sales, supply-chain
contracts, perishables, warranty supply and empirical information
asymmetry. They have **not** all been full-text audited. Search queries
also combined the ACI title/DOI with “counterexample”, “conjecture”,
“temporal”, “monotonicity” and the h>b assertion. No matching prior
six-threshold classification or specific correction was located in this
bounded investigation.

After reading the final copy, the title with “correction”, the DOI with
“erratum”, and “advance capacity information” with “Conjecture 1” and
“counterexample” were searched again. The returned publisher/university
records did not identify a matching correction. RePEc's generic
“Corrections” link concerns bibliographic-record edits and was not counted
as an erratum. This adds a targeted search, not exhaustive clearance.

Crossref's work record supplied no correction/update relation, and no
matching erratum was returned by the tested title/DOI searches. Absence
of an index relation is not proof that no correction or prior treatment
exists. The priority statement supported here is limited: the identified
primary sources contain the assertions challenged, and the searched and
inspected material did not reveal this classification.

## Actions and publication consequence

With the user's explicit authorization, a short request for the final
2011 journal copy was successfully sent to the corresponding author on
2026-11-15. The user subsequently supplied the final journal copy directly,
so the version audit no longer depends on an author response. Mailbox
identifiers and the user's account information are not stored here.

The manuscript is written as a standalone exact classification, with a
carefully versioned refutation of final Conjecture 1 and its adjacent h>b
assertion. The model, assertion status, target selector and appendix have
now been compared against the supplied typeset article, and the anonymous
manuscript, cover letter and source package are updated accordingly.
The final-version comparison is complete within this stated scope;
broader priority and external specialist review remain separate gates.
No actual journal submission has been made.
