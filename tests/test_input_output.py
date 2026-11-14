import numpy as np
import pytest

from econplan import InputOutputSystem


def test_leontief_balance_and_nonnegative_output():
    a = np.array([[0.2, 0.1], [0.3, 0.2]])
    demand = np.array([100.0, 80.0])
    model = InputOutputSystem(a)
    x = model.gross_output(demand)
    np.testing.assert_allclose(x - a @ x, demand, atol=1e-10)
    assert np.all(x >= 0)


def test_capacity_feasibility():
    a = np.array([[0.2, 0.1], [0.3, 0.2]])
    demand = np.array([100.0, 80.0])
    x = InputOutputSystem(a).gross_output(demand)
    assert InputOutputSystem(a, capacity=x + 1).is_capacity_feasible(demand)
    assert not InputOutputSystem(a, capacity=x - 1).is_capacity_feasible(demand)


@pytest.mark.parametrize("matrix", [
    [[1.0, 0.0], [0.0, 0.5]],
    [[0.1, -0.1], [0.0, 0.2]],
    [[float("nan")]],
    [[0.0, 0.1]],
])
def test_invalid_technical_coefficients(matrix):
    with pytest.raises(ValueError):
        InputOutputSystem(matrix)


def test_invalid_demand():
    model = InputOutputSystem([[0.2]])
    with pytest.raises(ValueError):
        model.gross_output([-5])


def test_requires_capacity_for_slack():
    model = InputOutputSystem([[0.2]])
    with pytest.raises(ValueError):
        model.capacity_slack([2])


def test_inputs_are_copied():
    a = np.array([[0.2]])
    cap = np.array([5.0])
    model = InputOutputSystem(a, cap)
    a[0, 0] = 2.0
    cap[0] = 0.0
    assert model.coefficients[0, 0] == 0.2
    assert model.capacity[0] == 5.0
