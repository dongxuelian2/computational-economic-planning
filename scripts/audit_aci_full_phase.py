#!/usr/bin/env python3
"""Independent exact audit of the complete r>0 ACI timing phase diagram.

This implementation does not import the existing PWL solver or its threshold
functions. It evaluates the integer knots by direct finite Bellman minimization.
Integer demands/capacities and convexity preserve integer breakpoints, so the
resulting knot slopes certify continuous-order minimizer intervals as explained
in the independent review report. Finite probes are not the symbolic proof.
"""
from fractions import Fraction as Q
from functools import lru_cache


def knot_objective(capacities, p, r):
    def loss(x):
        return Q(x) if x >= 0 else -r*x

    @lru_cache(None)
    def value(t, x):
        if t == 4:
            return Q(0)
        capacity = capacities[t-2]
        return min(
            (1-p)*(loss(x+z)+value(t+1, x+z))
            + p*(loss(x+z-2)+value(t+1, x+z-2))
            for z in range(capacity+1)
        )

    def objective(y):
        return ((1-p)*(loss(y)+value(2, y))
                + p*(loss(y-2)+value(2, y-2)))

    return objective


def full_thresholds(p):
    u, c = 1-p, 3-3*p+p*p
    return (
        u*c/(p*(5-3*p+p*p)),
        u*c/(p*(4-2*p+p*p)),
        u*(3-p)/(3*p),
        (3-p-p*p)/(2*p*p),
        (3-2*p+p*p-p**3)/(p*p*(1+p)),
        (3-p+p*p-p**3)/p**3,
    )


def predicted(p, r):
    low, early_low, late_low, late_high, early_high, high = full_thresholds(p)
    early = ((0, 0) if r < early_low else
             (0, 2) if r == early_low else
             (2, 2) if r < early_high else
             (2, 4) if r == early_high else (4, 4))
    late = ((0, 0) if r < low else
            (0, 1) if r == low else
            (1, 1) if r < late_low else
            (1, 2) if r == late_low else
            (2, 2) if r < late_high else
            (2, 3) if r == late_high else
            (3, 3) if r < high else
            (3, 4) if r == high else (4, 4))
    return early, late


def audit():
    probabilities = sorted({Q(i, d) for d in range(2, 16) for i in range(1, d)}
                           | {Q(1, 1000), Q(999, 1000)})
    total = 0
    for p in probabilities:
        ts = full_thresholds(p)
        r0, recourse_low, recourse_high = (1-p)/p, (1-p)*(2-p)/(p*(3-p)), 2/(p*p)-1
        assert 0 < ts[0] < ts[1] < ts[2] < r0 < ts[3] < ts[4] < ts[5]
        probes = set(ts) | {r0, recourse_low, recourse_high}
        probes |= {(a+b)/2 for a, b in zip((Q(0),)+ts, ts+(ts[-1]+2,))}
        for r in sorted(probes):
            found = []
            for capacities in [(0, 2), (1, 1)]:
                j = knot_objective(capacities, p, r)
                values = {y: j(y) for y in range(-2, 9)}
                # Every objective is strictly decreasing below 0 and strictly
                # increasing above 6; these guards also catch a truncated scan.
                assert values[-2] > values[-1] > values[0]
                assert values[6] < values[7] < values[8]
                assert all(values[y+1]-values[y] <= values[y+2]-values[y+1]
                           for y in range(-2, 7))
                minimum = min(values.values())
                minimizers = [y for y, cost in values.items() if cost == minimum]
                found.append((min(minimizers), max(minimizers)))
                if r <= r0:
                    a, u, c = 1-p-p*r, 1-p, 3-3*p+p*p
                    if capacities == (0, 2):
                        assert values[1]-values[0] == u*c-p*r*(4-2*p+p*p)
                        assert values[3]-values[2] == c+p*a*(3-2*p)
                    else:
                        b0 = u*(2-p)-p*r*(3-p)
                        assert values[1]-values[0] == a+u*max(b0, Q(0))-p*(1+p)*r
                        assert values[2]-values[1] == a*c+p*min(b0, Q(0))
            assert tuple(found) == predicted(p, r), (p, r, found, predicted(p, r))
            total += 1
    p, r = Q(1, 2), Q(1, 2)
    early, late = knot_objective((0, 2), p, r), knot_objective((1, 1), p, r)
    assert (early(0), early(1), early(2)) == (Q(9, 4), Q(37, 16), Q(19, 8))
    assert (late(0), late(1), late(2)) == (Q(17, 8), Q(33, 16), Q(5, 2))
    print(f"PASS: {total} independent exact knot-Bellman parameter certificates")
    print(f"Distinct demand probabilities: {len(probabilities)}; all six phase boundaries tested")
    print("PASS: r=r0, both period-2 recourse switches, and low-cost counterexample")


if __name__ == "__main__":
    audit()
