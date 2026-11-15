#!/usr/bin/env python3
"""Independent continuous scenario-tree LP audit (requires scipy).

Builds order variables indexed only by observed demand histories, and
holding/backlog epigraphs on every demand node. No Bellman recursion.
LP arithmetic is floating point, and is not advertised as an exact proof.
"""
from fractions import Fraction as Q
from itertools import product

from scipy.optimize import linprog

from aci_piecewise import add, objective, reversal_slopes, thresholds


def solve(scenarios, p, r, minimax=False):
    """scenarios: (prior, (q2,q3)); common y, scenario known before order 2."""
    costs, bounds, rows, rhs = [0.0], [(None, None)], [], []
    scenario_costs = []

    def variable(lower=0, upper=None):
        i = len(costs)
        costs.append(0.0)
        bounds.append((lower, upper))
        return i

    for prior, capacities in scenarios:
        order = {}
        for depth, capacity in enumerate(capacities, start=1):
            for history in product((0, 1), repeat=depth):
                order[history] = variable(0, float(capacity))
        c = {}
        for depth in range(1, 4):
            for history in product((0, 1), repeat=depth):
                prob = float(p**sum(history)*(1-p)**(depth-sum(history)))
                hold, backlog = variable(), variable()
                c[hold], c[backlog] = prob, prob*float(r)
                inventory = {0: 1.0}
                for d in range(1, depth):
                    inventory[order[history[:d]]] = 1.0
                a = dict(inventory)
                a[hold] = -1.0
                rows.append(a)
                rhs.append(2.0*sum(history))
                a = {i: -value for i, value in inventory.items()}
                a[backlog] = -1.0
                rows.append(a)
                rhs.append(-2.0*sum(history))
        scenario_costs.append(c)
        for i, coef in c.items():
            costs[i] = float(prior)*coef

    if minimax:
        costs[:] = [0.0]*len(costs)
        regret = variable(0)
        costs[regret] = 1.0
        for (_, capacities), c in zip(scenarios, scenario_costs):
            # This baseline is independently computed by a single-scenario LP.
            optimum, _ = solve([(Q(1), capacities)], p, r)
            rows.append({**c, regret: -1.0})
            rhs.append(optimum)
    matrix = [[row.get(i, 0.0) for i in range(len(costs))] for row in rows]
    result = linprog(costs, A_ub=matrix, b_ub=rhs, bounds=bounds, method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    return result.fun, result.x[0]


def audit():
    checked = 0
    for p in [Q(1, 5), Q(1, 2), Q(4, 5)]:
        r0, lo, early, hi = thresholds(p)
        for r in [(r0+lo)/2, lo, (lo+early)/2, early, (early+hi)/2, hi, hi+1]:
            for capacities in [(0, 2), (1, 1)]:
                f = objective(capacities, p, r)
                left, right = f.argmin()
                want = f.value(left)
                value, target = solve([(Q(1), capacities)], p, r)
                assert abs(value-float(want)) < 1e-7, (p, r, capacities, value, want)
                assert float(left)-1e-7 <= target <= float(right)+1e-7
                checked += 1
        r = (lo+early)/2
        e, beta = reversal_slopes(p, r)
        for prior in [Q(1, 4), Q(1, 2), Q(3, 4)]:
            scenarios = [(prior, (0, 2)), (1-prior, (1, 1))]
            value, _ = solve(scenarios, p, r)
            f, g = objective((0, 2), p, r), objective((1, 1), p, r)
            perfect = prior*f.value(2)+(1-prior)*g.value(3)
            want = min(prior*e, (1-prior)*beta)
            assert abs(value-float(perfect)-float(want)) < 1e-7
            checked += 1
        value, target = solve([(Q(1, 2), (0, 2)), (Q(1, 2), (1, 1))], p, r, minimax=True)
        assert abs(value-float(e*beta/(e+beta))) < 1e-7
        assert abs(target-float(2+beta/(e+beta))) < 1e-7
        checked += 1
    print(f"PASS: {checked} independent scenario-tree LP comparisons (floating point)")


if __name__ == "__main__":
    audit()
