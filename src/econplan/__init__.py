"""Numerical reference models for computational economic planning."""

from .input_output import InputOutputSystem

__all__ = ["InputOutputSystem"]

from .uncertainty import BoxInputOutputSystem

__all__.append("BoxInputOutputSystem")
