"""Research regression for the exact ACI counterexample (standard library)."""
from fractions import Fraction
from pathlib import Path
import runpy

def test_aci_temporal_order_counterexample():
    module = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "reproduce_aci_counterexample.py"))
    scenario = module["scenario"]
    assert scenario(1, 2)[:2] == (2, Fraction(9, 2))
    assert scenario(0, 2)[:2] == (2, Fraction(6))
    assert scenario(1, 1)[:2] == (3, Fraction(21, 4))
    assert scenario(0, 2)[2] == (Fraction(-31, 4), Fraction(1, 4))
    assert scenario(1, 1)[2] == (Fraction(-1, 4), Fraction(7, 4))
