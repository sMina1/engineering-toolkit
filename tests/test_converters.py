import pytest
from converters.length import convert_length
from converters.temperature import convert_temperature

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