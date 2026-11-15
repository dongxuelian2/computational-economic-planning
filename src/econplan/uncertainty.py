"""Sharp output ranges for independent entrywise nonnegative uncertainty.

These are deterministic box bounds, not statistical confidence intervals.
See docs/box-uncertainty.md for assumptions and the monotonicity proof.
"""
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray

from .input_output import InputOutputSystem


@dataclass(frozen=True)
class BoxInputOutputSystem:
    """Leontief systems A_lower <= A <= A_upper, with fixed capacity.

    The upper matrix must be productive. A box containing a nonproductive
    upper corner is rejected rather than assigned a finite output bound.
    """

    lower_coefficients: ArrayLike
    upper_coefficients: ArrayLike
    capacity: ArrayLike | None = None
    _lower: InputOutputSystem = field(init=False, repr=False, compare=False)
    _upper: InputOutputSystem = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        lower = InputOutputSystem(self.lower_coefficients, self.capacity)
        upper = InputOutputSystem(self.upper_coefficients, self.capacity)
        if lower.coefficients.shape != upper.coefficients.shape:
            raise ValueError("coefficient endpoints must have the same shape")
        if np.any(lower.coefficients > upper.coefficients):
            raise ValueError("lower coefficients must not exceed upper coefficients")
        object.__setattr__(self, "lower_coefficients", lower.coefficients)
        object.__setattr__(self, "upper_coefficients", upper.coefficients)
        object.__setattr__(self, "capacity", lower.capacity)
        object.__setattr__(self, "_lower", lower)
        object.__setattr__(self, "_upper", upper)

    def gross_output_bounds(
        self, lower_demand: ArrayLike, upper_demand: ArrayLike
    ) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
        """Return attained componentwise extrema over the full rectangle.

        For correlated uncertainty these remain outer bounds, but their
        attaining corners may not be admissible. No inverse is formed.
        """
        lower_demand = np.asarray(lower_demand, dtype=float)
        upper_demand = np.asarray(upper_demand, dtype=float)
        low = self._lower.gross_output(lower_demand)
        high = self._upper.gross_output(upper_demand)
        if np.any(lower_demand > upper_demand):
            raise ValueError("lower demand must not exceed upper demand")
        return low, high

    def worst_case_capacity_slack(
        self, lower_demand: ArrayLike, upper_demand: ArrayLike
    ) -> NDArray[np.float64]:
        """Return capacity minus the worst-case output in each sector."""
        if self.capacity is None:
            raise ValueError("capacity must be provided")
        _, high = self.gross_output_bounds(lower_demand, upper_demand)
        return self.capacity - high

    def is_robustly_capacity_feasible(
        self, lower_demand: ArrayLike, upper_demand: ArrayLike,
        tolerance: float = 1e-9,
    ) -> bool:
        """Check every box realization, up to an absolute output tolerance."""
        if tolerance < 0 or not np.isfinite(tolerance):
            raise ValueError("tolerance must be finite and nonnegative")
        return bool(np.all(
            self.worst_case_capacity_slack(lower_demand, upper_demand) >= -tolerance
        ))
