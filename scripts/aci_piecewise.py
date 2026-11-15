#!/usr/bin/env python3
"""Exact convex piecewise-linear Bellman recursion on the real line.

All arithmetic is Fraction; no inventory/action grid and no truncated domain.
Functions are stored by their value at zero, breakpoints and right slopes.
"""
from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class PWL:
    knots: tuple
    slopes: tuple
    zero: Q

    def __post_init__(self):
        assert len(self.slopes) == len(self.knots)+1
        assert tuple(sorted(set(self.knots))) == self.knots
        assert all(a <= b for a, b in zip(self.slopes, self.slopes[1:]))

    def value(self, x):
        x = Q(x)
        return self.zero+self.slopes[0]*x+sum(
            (b-a)*(max(x-k, Q(0))-max(-k, Q(0)))
            for k, a, b in zip(self.knots, self.slopes, self.slopes[1:])
        )

    def derivative(self, x):
        return self.slopes[bisect_right(self.knots, Q(x))]

    def argmin(self):
        if not self.slopes[0] < 0 < self.slopes[-1]:
            raise ValueError("argmin requires a coercive convex function")
        left = next(k for k, slope in zip(self.knots, self.slopes[1:]) if slope >= 0)
        right = next(k for k, slope in zip(self.knots, self.slopes[1:]) if slope > 0)
        return left, right

    def shift(self, d):
        """Return x -> self(x-d)."""
        d = Q(d)
        return PWL(tuple(k+d for k in self.knots), self.slopes, self.value(-d))

    def clip(self, capacity):
        """Return x -> min_{0<=z<=capacity} self(x+z), exactly."""
        capacity = Q(capacity)
        if capacity < 0:
            raise ValueError("negative capacity")
        knots = sorted(set(self.knots) | {k-capacity for k in self.knots})
        slopes = [max(self.slopes[0], Q(0))+min(self.slopes[0], Q(0))]
        slopes.extend(max(self.derivative(k), Q(0))+
                      min(self.derivative(k+capacity), Q(0)) for k in knots)
        candidates = [Q(0), capacity]+[k for k in self.knots if 0 <= k <= capacity]
        zero = min(self.value(x) for x in candidates)
        return simplified(knots, slopes, zero)


def simplified(knots, slopes, zero):
    kept_knots, kept_slopes = [], [Q(slopes[0])]
    for k, slope in zip(knots, slopes[1:]):
        if slope != kept_slopes[-1]:
            kept_knots.append(Q(k))
            kept_slopes.append(Q(slope))
    return PWL(tuple(kept_knots), tuple(kept_slopes), Q(zero))


def add(*weighted_functions):
    """Sum (weight,function) terms by merging their exact breakpoints."""
    knots = sorted({k for _, f in weighted_functions for k in f.knots})
    slopes = [sum(w*f.slopes[0] for w, f in weighted_functions)]
    slopes.extend(sum(w*f.derivative(k) for w, f in weighted_functions) for k in knots)
    return simplified(knots, slopes, sum(w*f.zero for w, f in weighted_functions))


def objective(capacities, p=Q(1, 2), r=Q(5), eta=Q(1), h=Q(1)):
    """First post-order objective; capacities start in period 2."""
    p, r, eta, h = map(Q, (p, r, eta, h))
    if not 0 < p < 1 or min(r, eta, h) <= 0:
        raise ValueError("require 0<p<1 and positive r,eta,h")
    loss = PWL((Q(0),), (-h*r, h), Q(0))
    demands = [(Q(0), 1-p), (2*eta, p)]
    immediate = add(*[(prob, loss.shift(d)) for d, prob in demands])
    future = PWL((), (Q(0),), Q(0))
    for capacity in reversed(capacities):
        continuation = add(*[(prob, future.shift(d)) for d, prob in demands])
        future = add((Q(1), immediate), (Q(1), continuation)).clip(capacity)
    return add((Q(1), immediate),
               *[(prob, future.shift(d)) for d, prob in demands])


def thresholds(p):
    p = Q(p)
    return ((1-p)/p, (3-p-p*p)/(2*p*p),
            (3-2*p+p*p-p**3)/(p*p*(1+p)),
            (3-p+p*p-p**3)/p**3)


def predicted_intervals(p, r):
    r0, lo, early, hi = thresholds(p)
    if r <= r0:
        raise ValueError("phase theorem assumes r>r0")
    e = (Q(2), Q(2)) if r < early else (Q(4), Q(4)) if r > early else (Q(2), Q(4))
    if r < lo:
        late = (Q(2), Q(2))
    elif r == lo:
        late = (Q(2), Q(3))
    elif r < hi:
        late = (Q(3), Q(3))
    elif r == hi:
        late = (Q(3), Q(4))
    else:
        late = (Q(4), Q(4))
    return e, late


def reversal_slopes(p, r):
    p, r = Q(p), Q(r)
    _, lo, early, _ = thresholds(p)
    assert lo < r < early
    e = p*p*(1+p)*(early-r)
    stage_switch = 2/(p*p)-1
    beta = 2*p*p*(r-lo) if r <= stage_switch else p*p*(1+p)*r-1-p+p**3
    return e, beta


def audit():
    checked = 0
    for denominator in range(2, 10):
        for numerator in range(1, denominator):
            p = Q(numerator, denominator)
            r0, lo, early, hi = thresholds(p)
            assert r0 < lo < early < hi
            stage_switch = 2/(p*p)-1
            # Every phase boundary, every phase interior and the recourse switch.
            probes = [lo, early, hi, stage_switch, (r0+lo)/2,
                      (lo+early)/2, (early+hi)/2, hi+1]
            probes += [lo+(early-lo)*Q(j, 7) for j in range(1, 7)]
            for r in probes:
                e = objective((0, 2), p, r)
                late = objective((1, 1), p, r)
                assert (e.argmin(), late.argmin()) == predicted_intervals(p, r), (p, r)
                a = 1-p-p*r
                assert e.derivative(Q(3)) == p*p*(1+p)*(early-r)
                assert e.derivative(Q(1)) == a*(2+p-2*p*p)-p*(1+p)*r
                if r <= stage_switch:
                    assert late.derivative(Q(5, 2)) == 2*p*p*(lo-r)
                    assert late.derivative(Q(7, 2)) == 3-3*p+p*p
                else:
                    assert late.derivative(Q(5, 2)) == 1+p-p**3-p*p*(1+p)*r
                    assert late.derivative(Q(7, 2)) == p**3*(hi-r)
                if lo < r < early:
                    es, beta = reversal_slopes(p, r)
                    assert e.value(3)-e.value(2) == es
                    assert late.value(2)-late.value(3) == beta
                    common = add((Q(1, 2), e), (Q(1, 2), late))
                    perfect = (e.value(2)+late.value(3))/2
                    assert common.value(common.argmin()[0])-perfect == min(es, beta)/2
                checked += 1
    # Homogeneity and genuinely nonintegral orders/capacities.
    eta, h = Q(7, 5), Q(3, 2)
    for capacities in [(0, 2*eta), (eta, eta)]:
        f = objective(capacities, eta=eta, h=h)
        target = 2*eta if capacities[0] == 0 else 3*eta
        assert f.argmin() == (target, target)
    print(f"PASS: {checked} exact real-line parameter certificates, including all phase boundaries")
    p, r = Q(1, 2), Q(5)
    for capacities in [(1, 2), (0, 2), (1, 1)]:
        f = objective(capacities, p, r)
        interval = f.argmin()
        print(f"capacities={capacities}: argmin={interval}, minimum={f.value(interval[0])}")
    es, beta = reversal_slopes(p, r)
    assert es*beta/(es+beta) == Q(1, 8)
    print("PASS: equal-prior EVPI = minimax location regret = 1/8")


if __name__ == "__main__":
    audit()
