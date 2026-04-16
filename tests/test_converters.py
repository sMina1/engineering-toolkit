import pytest
from converters.length import convert_length
from converters.temperature import convert_temperature
from converters.pressure import convert_pressure
from converters.force_torque import convert_force_torque


# --- Length tests ---

def test_meters_to_km():
    assert convert_length(1000, "m", "km") == 1.0
    
def test_ft_to_meters():
    assert convert_length(1, "ft", "m") == pytest.approx(0.3048)

def test_same_unit_returns_original():
    assert convert_length(5, "cm", "cm") == 5.0
    
def test_invalid_unit_raises():
    with pytest.raises(ValueError):
        convert_length(1, "m", "furlongs")

# --- Temperature tests ---

def test_celsius_to_fahrenheit():
    assert convert_temperature(100, "c", "f") == pytest.approx(212.0)

def test_freezing_point():
    assert convert_temperature(0, "c", "k") == pytest.approx(273.15)

def test_invalid_from_unit_raises():
    with pytest.raises(ValueError):
        convert_temperature(100, "x", "c")
        
        
# --- Pressure tests ---

def test_bar_to_atm():
    assert convert_pressure(100, "bar", "atm") == pytest.approx(98.6923)

def test_mpa_to_psi():
    assert convert_pressure(3_000_000, "mpa", "psi") == pytest.approx(435113213)

def test_invalid_from_unit_raises_p():
    with pytest.raises(ValueError):
        convert_pressure(100, "x", "c")
        
        
# --- Force Torque tests ---

def test_kgf_to_lbf():
    assert convert_force_torque(3.8, "kgf", "lbf") == pytest.approx(8.378, abs=.01)

def test_lbft_to_knm():
    assert convert_force_torque(2_200, "lb.ft", "knm") == pytest.approx(2.98, abs = .01)

def test_same_unit_returns_original_f():
    assert convert_force_torque(5, "n", "n") == 5.0

def test_invalid_from_unit_raises_ftq():
    with pytest.raises(ValueError):
        convert_force_torque(100, "n", "c")
        
def test_mixed_unit_types_raises_ftq():
    with pytest.raises(ValueError):
        convert_force_torque(100, "n", "nm")
        
        
  
