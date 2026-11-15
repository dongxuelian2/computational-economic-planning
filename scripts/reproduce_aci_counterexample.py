#!/usr/bin/env python3
"""Exact three-period ACI counterexample: rational Bellman recursion.

Integer demand/capacity and convex piecewise-linear costs imply integer
breakpoints. Checking all adjacent integer slopes at the optimum, together
with convexity, certifies the continuous-order optimum as well.
No third-party dependencies. See docs/research/advance_capacity_audit.md.
"""
from fractions import Fraction
from functools import lru_cache

DEMAND = ((0, Fraction(1, 2)), (2, Fraction(1, 2)))


def loss(s):
    return s if s >= 0 else -5*s


def scenario(q2, q3):
    @lru_cache(None)
    def v3(x):
        return min(sum(p*loss(x+z-d) for d,p in DEMAND) for z in range(q3+1))

    @lru_cache(None)
    def v2(x):
        return min(sum(p*(loss(x+z-d)+v3(x+z-d)) for d,p in DEMAND) for z in range(q2+1))

    def j1(y):
        return sum(p*(loss(y-d)+v2(y-d)) for d,p in DEMAND)

    costs = {y: j1(y) for y in range(-6, 11)}
    optimum = min(costs.values())
    minimizers = [y for y,c in costs.items() if c == optimum]
    assert len(minimizers)==1, minimizers
    y = minimizers[0]
    slopes = (costs[y]-costs[y-1], costs[y+1]-costs[y])
    assert slopes[0] < 0 < slopes[1]
    return y, costs[y], slopes, costs


def main():
    expected = {
        "baseline": ((1,2), 2, Fraction(9,2)),
        "earlier_loss": ((0,2), 2, Fraction(6)),
        "later_loss": ((1,1), 3, Fraction(21,4)),
    }
    for label,(q,want_y,want_cost) in expected.items():
        y,c,slopes,_ = scenario(*q)
        assert (y,c) == (want_y,want_cost), (label,y,c)
        print(f"{label}: capacities={q}, y*={y}, J(y*)={c}, adjacent_slopes={slopes}")
    assert scenario(0,2)[0] < scenario(1,1)[0]
    print("PASS: a later capacity loss raises the optimal base-stock target more")


if __name__ == "__main__":
    main()
