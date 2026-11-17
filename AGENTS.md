# Research instructions

## Zero-defensive-prose rule — mandatory

Apply this rule to all repository-authored English prose: README, mathematical research notes, `PROOF.md`, LaTeX exposition, documentation, pull-request descriptions, and code comments. Enforce it when auditing historical material and when writing anything new.

**Prohibited rhetorical constructions (including grammatical variants):**
- Chinese examples to recognize and eliminate in translated source material: `不是……`, `并不是……`, `不构成……`, `还没有做……`, `尚未……`, `而不是……`, `并未……`, `不意味着……`, `不代表……`, `不能据此……`, `这并不证明……`, `我们不声称……`, `不保证……`, `仅仅是……`.
- English equivalents to eliminate from authored explanations: `not a ...`, `is not ...`, `does not ...`, `do not ...`, `has not ...`, `have not ...`, `not yet ...`, `rather than ...`, `instead of ...`, `does not constitute ...`, `does not establish ...`, `does not imply ...`, `should not be interpreted as ...`, `we do not claim ...`, `no claim is made ...`, `merely ...`, `only a preliminary ...`, `beyond the scope ...`, `not intended to ...`.
- Delete disclaimers, self-exculpation, premature qualification, repetitive status caveats, and defensive contrasts. Do not relocate them to a different paragraph or replace them with synonyms serving the same rhetorical purpose. Zero such constructions are acceptable in explanatory prose.

**Required replacement style:** Lead with the actual theorem, deliverable, tested behavior, evidence, applicability conditions, exact scope, and concrete open mathematical question, using affirmative statements. Examples:
- `We prove the classification for n >= N under hypotheses H1 and H2.`
- `Verified cases: n = 2,...,7. General-case proof target: ...`
- `CI checks: 16 passed. Proof: Proposition 4. Research priority: external review.`
- `Algorithm: FPT for disjoint ordinary cardinality quotas. Next target: robust mixed-status source-SCC accessibility.`

**Mathematical truth takes precedence over stylistic cleanup.** Preserve essential logical negation in theorems, inequalities, counterexamples, constraints, source quotations, and executable code where changing it would alter correctness. In ordinary explanation, express boundaries by positive quantified scope and precise next objectives. If a claim is unsupported, correct or remove it; never invent evidence to avoid a negative sentence.

Before opening or updating a PR, review every added or modified paragraph for prohibited rhetoric and its semantic equivalents. Record the direct result and evidence; keep mathematical limitations in compact, exact statements of domain and open problems.

Research mathematical claims rigorously, keep proofs reviewable and preserve reproducibility.

## Mandatory English and research-integrity audit

- Write all repository-authored prose in English: README, AGENTS, Markdown proofs and notes, manuscripts, code comments/docstrings, and PR descriptions. Translate existing Chinese explanatory text, including nested directories and archived research. Preserve mathematics, definitions, assumptions, references, formulas, labels, and the original proof's logical strength. Retain foreign-language source titles and quotations only where necessary with English context.
- Audit every existing mathematical or research claim, not just the changed files: exact quantifiers, cases, dependency chains, proof completeness, counterexamples, citation accuracy, numerical methodology, and the limits of computational verification. Fill missing arguments and necessary definitions; correct false or imprecise claims. Distinguish conjectures, conditional results, finite checks, and fully proved theorems.
- If a gap remains, state its precise mathematical location and adjust the claim accordingly. Never hide uncertainty behind vague exposition or manufacture a proof to make a document look complete.
- Submit focused, reviewable PRs for each repository, explaining substantial corrections and verification. Check internal links, mathematical equivalence of translations, remaining Chinese prose, and existing tests. Preserve essential research content and avoid redundant logs, defensive boilerplate, or invented novelty claims.
- Enforce this policy for every future update; do not add new Chinese prose or mixed-language public documentation.

