def convert_pressure(value, from_unit, to_unit):
    # Conversion factors TO pascals
    to_pascals = {
        "pa": 1,
        "kpa": 1000,
        "mpa": 1_000_000,
        "bar": 100_000,
        "atm": 101_325,
        "psi": 6894.757,
    }

    if from_unit not in to_pascals:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit not in to_pascals:
        raise ValueError(f"Invalid to_unit: {to_unit}")

    conversion_list = []

    pascals = value * to_pascals[from_unit]
    conversion_list.append((from_unit, "pa", pascals))
    conversion_list.append(("pa", to_unit, pascals / to_pascals[to_unit]))
    
    return(conversion_list)