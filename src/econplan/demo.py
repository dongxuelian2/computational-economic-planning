"""Small reproducible two-sector input-output example."""

import numpy as np

from econplan import InputOutputSystem


def main() -> None:
    a = np.array([[0.2, 0.1], [0.3, 0.2]])
    demand = np.array([100.0, 80.0])
    model = InputOutputSystem(a, capacity=np.array([180.0, 170.0]))
    output = model.gross_output(demand)
    print("Input coefficients (rows = inputs, columns = producing sectors):")
    print(a)
    print("Final demand:", demand)
    print("Required gross output:", np.round(output, 4))
    print("Capacity slack:", np.round(model.capacity_slack(demand), 4))
    print("Capacity feasible:", model.is_capacity_feasible(demand))


if __name__ == "__main__":
    main()
