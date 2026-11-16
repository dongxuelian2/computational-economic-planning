# ACI version and priority audit

Audit date: 2026-11-15. This is a bounded source/version investigation,
not an assertion that every relevant work has been read or that priority
can be guaranteed. The current paper's mathematical criticism targets
the specific 2008 working-paper and 2016 thesis assertions below. It does
not infer the content of the final 2011 journal theorem.

## Version identification

| Version / route | Evidence actually inspected | Finding |
| --- | --- | --- |
| [BETA WP 249, 2008](https://pure.tue.nl/ws/portalfiles/portal/3296948/691623823560851.pdf) | Actual title/authors, printed pp.5–8 model, p.11 Theorem 4, appendix derivative argument | Correct ACI paper; 29-page working-paper body, not the journal's 355–369 typesetting. Repository cover labels an accepted manuscript, but cites the 2008 report. The cover alone does not identify the final journal theorem. |
| [TU/e file 638020](https://pure.tue.nl/ws/files/3296946/638020.pdf) | Cover and actual first body pages | **Wrong attached body:** the ACI metadata cover is followed by *Single item inventory control under periodic review and a minimum order quantity*, by Kiesmüller, de Kok and Dabia. Excluded as evidence for ACI. |
| [Jakšič 2016 thesis](https://pure.tue.nl/ws/files/41303873/20161031_Jaksic.pdf) | Chapter 2 model, printed pp.31–32, appendices; p.31 rendered visually | Exact target Conjecture 2.1 and separate prose assertion that when h>b the two targets coincide; low-cost counterexample refutes the latter too. Conjecture 2.2 is the surviving coordinate bound. |
| [2011 NRL journal](https://doi.org/10.1002/nav.20450) | Publisher metadata/abstract, Crossref, TU/e and Tilburg journal records; ordinary browser full-text entry | DOI and pp.355–369 confirmed. Browser explicitly showed institutional/personal access requirements. Final text **not obtained**. No theorem wording inferred from abstract or prior versions. |
| [Ljubljana repository record 16946](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=16946) | Actual HTTP response and page content | OpenAlex/Semantic Scholar label it green/publishedVersion, but current endpoint returned HTTP 410 and “record does not exist.” Excluded as accessible full text. |
| Crossref TDM / publisher PDF and ePDF links | Endpoint responses and ordinary publisher UI | No final journal PDF supplied through the tested public routes. |

The exact thesis claim and the working-paper model were also checked by
an independently instructed reviewer agent; see
[the report](../research/independent-aci-review-2026-11-15.md). The two
independent mathematical implementations confirm the counterexamples,
but cannot establish what an unread journal version says.

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

Crossref's work record supplied no correction/update relation, and no
matching erratum was returned by the tested title/DOI searches. Absence
of an index relation is not proof that no correction or prior treatment
exists. The priority statement supported here is limited: the identified
primary sources contain the assertions challenged, and the searched and
inspected material did not reveal this classification.

## Actions and publication consequence

With the user's explicit authorization, a short request for the final
2011 journal copy was successfully sent to the corresponding author on
2026-11-15. The response is pending. Mailbox identifiers and the user's
account information are not stored in this public repository.

The manuscript is written as a standalone exact classification, with a
carefully versioned counterexample to the thesis/working paper. Its title,
abstract and proofs do not advertise a correction to an unread journal
theorem. On receipt of the final copy, compare the model, assertion status,
proof and appendix against the exact printed versions before adding any
journal-specific statement. No actual journal submission has been made.
