# Scoped audit of weighted production-network path claims

Source: George Nikolakoudis, *Incomplete Information in Production Networks* (2025 working paper), [author PDF](https://www.nikolakoudis.com/JMP.pdf), §3.4 and Appendix A.7/A.15. These are two **local** mathematical clarifications, not a general refutation of the paper's matrix-inverse model.

## Path-order issue

Let \(D=\operatorname{diag}(b)\), \(H=(I-D)^{-1}\), \(W=\omega H\) and input matrix \(A\). Whenever \(\rho(WA)<1\), factoring the inverse yields

\[
\gamma'(I-\omega A-D)^{-1}
=\gamma'\sum_{k\ge0}(WA)^k H.
\]

The main-text weighted-path display instead uses \(W^k A^k\). In general these are different because diagonal \(W\) need not commute with \(A\); a scalar common response \(\omega\) does **not** make \(W\) scalar unless the \(b_i\) also agree. A two-sector positive-response example in the Nov 15 audit yields a second response component \(15/14\) under the correct expression versus \(37/35\) using the displayed \(W^k A^k\), a difference of \(1/70\). The paper's Appendix already displays \((WA)^k\), so this should be treated as a correctable main-text representation issue.

## Inverse existence does not imply series convergence

With one-sector roundabout input share \(a=1/2\), admissible response \(\omega=-4\), and induced \(b=5/4\), the scalar inverse expression is defined and equals \(4/7\). Yet \(H=(1-b)^{-1}=-4\), \(W=\omega H=16\) and the proposed geometric expansion has ratio \(Wa=8\), hence diverges. The correct Neumann condition is \(\rho(WA)<1\); with negative weights, a norm/spectral convergence statement must be justified separately from invertibility. The paper's positive-response appendix already has tighter hypotheses.

## Follow-up

Check the revised and cited versions. A useful new result would give sharp, economically interpretable signed-response convergence domains or certified truncation-error bounds and compare them to standard matrix-series theory. The exact inverse theorem and the paper's major economic claims are **not** invalidated by these local observations.