from itertools import product

import numpy as np
import pytest

from econplan import BoxInputOutputSystem, InputOutputSystem


LOW = np.array([[.1, .1], [.05, .2]])
HIGH = np.array([[.25, .3], [.2, .35]])
DLOW = np.array([1., 2.])
DHIGH = np.array([2., 3.])


def test_all_64_vertices_attain_bounds():
    box = BoxInputOutputSystem(LOW, HIGH)
    low, high = box.gross_output_bounds(DLOW, DHIGH)
    outputs = []
    for bits in product([False, True], repeat=6):
        a = np.where(np.array(bits[:4]).reshape(2, 2), HIGH, LOW)
        d = np.where(bits[4:], DHIGH, DLOW)
        outputs.append(InputOutputSystem(a).gross_output(d))
    np.testing.assert_allclose(np.min(outputs, axis=0), low)
    np.testing.assert_allclose(np.max(outputs, axis=0), high)


def test_nominal_feasible_can_fail_robust_test():
    nominal = InputOutputSystem((LOW + HIGH) / 2)
    cap = nominal.gross_output((DLOW + DHIGH) / 2) + .1
    assert InputOutputSystem(nominal.coefficients, cap).is_capacity_feasible(
        (DLOW + DHIGH) / 2
    )
    assert not BoxInputOutputSystem(LOW, HIGH, cap).is_robustly_capacity_feasible(
        DLOW, DHIGH
    )
    _, high = BoxInputOutputSystem(LOW, HIGH).gross_output_bounds(DLOW, DHIGH)
    assert BoxInputOutputSystem(LOW, HIGH, high).is_robustly_capacity_feasible(
        DLOW, DHIGH
    )


def test_productive_despite_large_row_sum():
    high = np.array([[.1, 2.], [.1, .1]])
    assert np.linalg.norm(high, np.inf) > 1
    box = BoxInputOutputSystem(np.zeros((2, 2)), high)
    lo, hi = box.gross_output_bounds([1, 1], [1, 1])
    np.testing.assert_allclose(hi - high @ hi, [1, 1])
    assert np.all(hi >= lo)


def test_exact_perturbation_identity():
    x = InputOutputSystem(LOW).gross_output(DLOW)
    _, high = BoxInputOutputSystem(LOW, HIGH).gross_output_bounds(DLOW, DHIGH)
    delta = np.linalg.solve(np.eye(2) - HIGH, (HIGH - LOW) @ x + DHIGH - DLOW)
    np.testing.assert_allclose(high - x, delta)


def test_seeded_interior_points():
    rng = np.random.default_rng(20261115)
    for n in [1, 2, 5, 10]:
        upper = rng.uniform(0, 1, (n, n))
        upper *= .8 / max(abs(np.linalg.eigvals(upper)))
        lower = upper * rng.uniform(0, 1, (n, n))
        dl = rng.uniform(0, 1, n)
        du = dl + rng.uniform(0, 1, n)
        lo, hi = BoxInputOutputSystem(lower, upper).gross_output_bounds(dl, du)
        for _ in range(25):
            a = lower + rng.uniform(size=(n, n)) * (upper - lower)
            d = dl + rng.uniform(size=n) * (du - dl)
            x = InputOutputSystem(a).gross_output(d)
            assert np.all(x >= lo - 1e-10)
            assert np.all(x <= hi + 1e-10)


@pytest.mark.parametrize("lo,hi", [([[.2]], [[.1]]), ([[0]], [[1]]),
                                     ([[0]], [[-1]]), ([[0]], [[np.nan]]),
                                     ([[0]], [[0, 0], [0, 0]])])
def test_bad_matrix_intervals(lo, hi):
    with pytest.raises(ValueError):
        BoxInputOutputSystem(lo, hi)


@pytest.mark.parametrize("lo,hi", [([2], [1]), ([-1], [1]), ([0], [np.inf]),
                                     ([0, 0], [1]), ([0], [np.nan])])
def test_bad_demand_intervals(lo, hi):
    with pytest.raises(ValueError):
        BoxInputOutputSystem([[0]], [[.2]]).gross_output_bounds(lo, hi)


@pytest.mark.parametrize("tol", [-1, np.inf, np.nan])
def test_bad_tolerance(tol):
    with pytest.raises(ValueError):
        BoxInputOutputSystem([[0]], [[.2]], [2]).is_robustly_capacity_feasible(
            [0], [1], tol
        )


def test_missing_capacity():
    with pytest.raises(ValueError):
        BoxInputOutputSystem([[0]], [[.2]]).worst_case_capacity_slack([0], [1])


def test_degenerate_zero_demand_and_input_copies():
    a = np.array([[.2]])
    cap = np.array([2.])
    model = BoxInputOutputSystem(a, a, cap)
    a[:] = 3
    cap[:] = 0
    lo, hi = model.gross_output_bounds([0], [0])
    np.testing.assert_array_equal(lo, [0])
    np.testing.assert_array_equal(hi, [0])
    assert model.capacity[0] == 2
    assert not model.lower_coefficients.flags.writeable
    assert not model.upper_coefficients.flags.writeable


def test_numeric_strings_use_numeric_order():
    box = BoxInputOutputSystem([[0]], [[0]])
    with pytest.raises(ValueError):
        box.gross_output_bounds(["10"], ["2"])
    lo, hi = box.gross_output_bounds(["2"], ["10"])
    np.testing.assert_array_equal(lo, [2])
    np.testing.assert_array_equal(hi, [10])


def test_demand_expansion_limit_is_attained_and_larger_fails():
    model = BoxInputOutputSystem(LOW, HIGH, [10, 12])
    base, direction = np.array([1., 1.]), np.array([2., .5])
    limit = model.demand_expansion_limit(base, direction)
    assert limit > 0
    slack = model.worst_case_capacity_slack(base, base + limit * direction)
    assert np.min(slack) == pytest.approx(0, abs=1e-12)
    assert model.is_robustly_capacity_feasible(base, base + limit * direction)
    assert not model.is_robustly_capacity_feasible(
        base, base + (limit + 1e-5) * direction
    )


def test_expansion_accounts_for_indirect_input_bottleneck():
    model = BoxInputOutputSystem([[0, 0], [0, 0]], [[0, .5], [0, 0]], [1, 10])
    # Sector 2 final demand consumes sector 1 capacity, so its limit is 2, not 10.
    assert model.demand_expansion_limit([0, 0], [0, 1]) == pytest.approx(2)


def test_expansion_zero_growth_and_zero_headroom():
    model = BoxInputOutputSystem([[0]], [[.5]], [2])
    assert np.isinf(model.demand_expansion_limit([1], [0]))
    assert model.demand_expansion_limit([1], [1]) == 0
    with pytest.raises(ValueError, match="baseline"):
        model.demand_expansion_limit([2], [0])


@pytest.mark.parametrize("base,growth", [([-1], [1]), ([0], [-1]),
                                        ([0], [np.nan]), ([0], [1, 2])])
def test_expansion_rejects_invalid_inputs(base, growth):
    with pytest.raises(ValueError):
        BoxInputOutputSystem([[0]], [[.5]], [2]).demand_expansion_limit(base, growth)


def test_expansion_requires_capacity():
    with pytest.raises(ValueError, match="capacity"):
        BoxInputOutputSystem([[0]], [[.5]]).demand_expansion_limit([0], [1])
