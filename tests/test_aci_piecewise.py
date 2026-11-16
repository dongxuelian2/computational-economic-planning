"""Continuous-domain regression, including flat optimum intervals."""
from fractions import Fraction as Q
from pathlib import Path
import runpy


api = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "aci_piecewise.py"))


def test_complete_phase_certificates():
    api["audit"]()
    assert api["audit_full"]() == 1168


def test_clip_flat_minimum_and_fractional_capacity():
    f = api["PWL"]((Q(0), Q(2)), (Q(-2), Q(0), Q(3)), Q(0))
    clipped = f.clip(Q(1, 2))
    assert clipped.argmin() == (Q(-1, 2), Q(2))
    assert clipped.value(Q(-1)) == 1
    assert clipped.value(Q(5, 2)) == Q(3, 2)


def test_real_boundary_is_interval_not_discrete_points():
    f = api["objective"]((0, 2), Q(1, 2), Q(17, 3))
    assert f.argmin() == (Q(2), Q(4))
    assert f.value(Q(13, 5)) == f.value(2) == f.value(4)
