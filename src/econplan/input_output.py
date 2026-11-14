"""Static Leontief input-output system and capacity feasibility checks.

Convention: A[i, j] is the input of sector i required per unit of output
of sector j. Therefore gross output satisfies x = A @ x + d.
"""

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class InputOutputSystem:
    coefficients: ArrayLike
    capacity: ArrayLike | None = None

    def __post_init__(self) -> None:
        a = np.asarray(self.coefficients, dtype=float).copy()
        if a.ndim != 2 or a.shape[0] != a.shape[1] or a.shape[0] == 0:
            raise ValueError("coefficients must be a nonempty square matrix")
        if not np.isfinite(a).all() or np.any(a < 0):
            raise ValueError("coefficients must be finite and nonnegative")
        if max(abs(np.linalg.eigvals(a))) >= 1.0 - 1e-12:
            raise ValueError("productive input-output system requires spectral radius < 1")
        a.setflags(write=False)
        object.__setattr__(self, "coefficients", a)

        if self.capacity is not None:
            c = np.asarray(self.capacity, dtype=float).copy()
            if c.shape != (a.shape[0],) or np.any(c < 0) or not np.isfinite(c).all():
                raise ValueError("capacity must be a finite nonnegative vector")
            c.setflags(write=False)
            object.__setattr__(self, "capacity", c)

    def gross_output(self, final_demand: ArrayLike) -> NDArray[np.float64]:
        """Solve (I-A)x=d; does not enforce a capacity constraint."""
        d = np.asarray(final_demand, dtype=float)
        n = self.coefficients.shape[0]
        if d.shape != (n,) or not np.isfinite(d).all() or np.any(d < 0):
            raise ValueError("final_demand must be a finite nonnegative sector vector")
        return np.linalg.solve(np.eye(n) - self.coefficients, d)

    def capacity_slack(self, final_demand: ArrayLike) -> NDArray[np.float64]:
        """Capacity minus required gross output; negative entries are deficits."""
        if self.capacity is None:
            raise ValueError("capacity must be provided")
        return self.capacity - self.gross_output(final_demand)

    def is_capacity_feasible(self, final_demand: ArrayLike, tolerance: float = 1e-9) -> bool:
        if tolerance < 0 or not np.isfinite(tolerance):
            raise ValueError("tolerance must be finite and nonnegative")
        return bool(np.all(self.capacity_slack(final_demand) >= -tolerance))
