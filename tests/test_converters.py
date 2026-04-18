import pytest
from converters.length import convert_length
from converters.temperature import convert_temperature
from converters.pressure import convert_pressure
from converters.force_torque import convert_force_torque

# --- Length tests ---

def test_meters_to_km():
    steps = convert_length(1000, "m", "km")
    assert steps[-1][2] == pytest.approx(1.0)

def test_ft_to_meters():
    steps = convert_length(1, "ft", "m")
    assert steps[-1][2] == pytest.approx(0.3048)

def test_same_unit_returns_original():
    steps = convert_length(5, "cm", "cm")
    assert steps[-1][2] == pytest.approx(5.0)

def test_invalid_unit_raises():
    with pytest.raises(ValueError):
        convert_length(1, "m", "furlongs")


# --- Temperature tests ---

def test_celsius_to_fahrenheit():
    steps = convert_temperature(100, "c", "f")
    assert steps[-1][2] == pytest.approx(212.0)

def test_freezing_point():
    steps = convert_temperature(0, "c", "k")
    assert steps[-1][2] == pytest.approx(273.15)

def test_invalid_from_unit_raises():
    with pytest.raises(ValueError):
        convert_temperature(100, "x", "c")
        
# --- Pressure tests ---

def test_bar_to_atm():
    steps = convert_pressure(100, "bar", "atm")
    assert steps[-1][2] == pytest.approx(98.6923)

def test_mpa_to_psi():
    steps = convert_pressure(3_000_000, "mpa", "psi")
    assert steps[-1][2] == pytest.approx(435113213)

def test_invalid_from_unit_raises_p():
    with pytest.raises(ValueError):
        convert_pressure(100, "x", "c")


# --- Force Torque tests ---

def test_kgf_to_lbf():
    steps = convert_force_torque(3.8, "kgf", "lbf")
    assert steps[-1][2] == pytest.approx(8.378, abs=.01)

def test_lbft_to_knm():
    steps = convert_force_torque(2_200, "lb.ft", "knm")
    assert steps[-1][2] == pytest.approx(2.98, abs=.01)

def test_same_unit_returns_original_f():
    steps = convert_force_torque(5, "n", "n")
    assert steps[-1][2] == pytest.approx(5.0)

def test_invalid_from_unit_raises_ftq():
    with pytest.raises(ValueError):
        convert_force_torque(100, "n", "c")

def test_mixed_unit_types_raises_ftq():
    with pytest.raises(ValueError):
        convert_force_torque(100, "n", "nm")