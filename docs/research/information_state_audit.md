# Conditional-independence audit: inventory remembers a shared hidden past

Source under review: Sudhakara and Zhang, *Coordinated Communication and Inventory Optimization in Multi-Retailer Supply Chains*, [arXiv:2507.09223v1](https://arxiv.org/html/2507.09223v1), especially §§3.1–3.5 and §4.1. Check later versions before publishing a criticism.

**Claim being checked, not the entire paper:** whether retailer inventories, conditional on the **current** shared hidden Markov state and common observation history, factor as a product of per-retailer inventory distributions. Conditional independence of demand shocks given the state at the time of their realization does not imply conditional independence of inventories accumulated over unobserved earlier states.

## Exact two-retailer counterexample

Two retailers start with inventories (1,1), use zero communication and zero orders, both publicly known policies. The previous common state \(X_0\) is a fair binary variable. Given \(X_0=0\), each demand independently equals 0 with probability 3/4; given \(X_0=1\), each independently equals 0 with probability 1/4. Set \(X_1\) independent of \(X_0\) and fair, a valid finite-state Markov transition. The public history \(C_1\) is deterministic under the announced policy, and each ending inventory is 1 exactly when its demand was 0.

For either current \(X_1=x\),

\[
\Pr(I_1^i=1\mid X_1=x,C_1)=\tfrac12,\qquad
\Pr(I_1^1=I_1^2=1\mid X_1=x,C_1)=\tfrac5{16}\ne\tfrac14.
\]

The conditional covariance is \(1/16>0\). This is not caused by disallowed cross-retailer demand noise: **conditional on the historical regime \(X_0\)**, demands are independent. Inventory records memory of that shared past. A persistent \(X_1\)-transition also leaves strictly positive dependence.

## Correct scope and future theorem target

The example refutes the exact product factorization under these assumptions; it does not independently reproduce or invalidate the paper's simulations, approximations or other policy results. An exact belief state must in general retain the **joint** conditional distribution of current hidden state and inventory vector, or another sufficient statistic whose factorization is proven. For a useful theory, characterize when factorization is exact, develop explicit approximation error bounds for practical compressed common beliefs, and translate these into decision-value guarantees under fixed communication budgets. Generic POMDP belief updates alone are established theory and not a novelty claim.