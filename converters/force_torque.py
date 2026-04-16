def convert_force_torque(value, from_unit, to_unit):
    # Conversion factors TO newtons
    to_newtons = {
        "n": 1,
        "kn": 1_000,
        "lbf": 4.44822,
        "kgf": 9.80665
    }
    
    # Conversion factors TO newton-meters
    to_newton_metre = {
        "N.m": 1,
        "knm": 1_000,
        "lb.ft": 1.35582,
        "lb.in": 0.11299
    }
    if ( (from_unit in to_newtons) and (to_unit in to_newtons) ):
        newtons = value * to_newtons[from_unit]
        return newtons / to_newtons[to_unit]
    elif ( (from_unit in to_newton_metre) and (to_unit in to_newton_metre) ):
        newtons = value * to_newton_metre[from_unit]
        return newtons / to_newton_metre[to_unit]
    else:
        raise ValueError(f"Invalid from_unit: {from_unit} & to_unit: {to_unit} combination")

