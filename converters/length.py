def convert_length(value, from_unit, to_unit):
    # Conversion factors TO metres
    to_metres = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "miles": 1609.344,
    }

    # Validate units
    if from_unit not in to_metres:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit not in to_metres:
        raise ValueError(f"Invalid to_unit: {to_unit}")

    # Convert: from_unit -> metres -> to_unit
    conversion_list = []
    
    metres = value * to_metres[from_unit]
    conversion_list.append((from_unit, "m", metres))
    conversion_list.append(("m", to_unit, metres / to_metres[to_unit]))

    return(conversion_list)