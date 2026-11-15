"""Reproduce the deterministic example in docs/box-uncertainty.md."""
import json
import numpy as np
from .input_output import InputOutputSystem
from .uncertainty import BoxInputOutputSystem


def main():
    low = np.array([[.1, .1], [.05, .2]])
    high = np.array([[.25, .3], [.2, .35]])
    dl, du = np.array([1., 2.]), np.array([2., 3.])
    a, d = (low + high) / 2, (dl + du) / 2
    nominal = InputOutputSystem(a).gross_output(d)
    capacity = nominal + .1
    model = BoxInputOutputSystem(low, high, capacity)
    lower, upper = model.gross_output_bounds(dl, du)
    print(json.dumps({
        "source": "synthetic, deterministic; dimensionless illustrative units",
        "nominal_output": nominal.tolist(), "capacity": capacity.tolist(),
        "output_lower": lower.tolist(), "output_upper": upper.tolist(),
        "worst_case_slack": model.worst_case_capacity_slack(dl, du).tolist(),
        "nominal_feasible": InputOutputSystem(a, capacity).is_capacity_feasible(d),
        "robust_feasible": model.is_robustly_capacity_feasible(dl, du),
    }, indent=2))


if __name__ == "__main__":
    main()
