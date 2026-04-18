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
        "n.m": 1,
        "knm": 1_000,
        "lb.ft": 1.35582,
        "lb.in": 0.11299
    }
    conversion_list = []

    if ( (from_unit in to_newtons) and (to_unit in to_newtons) ):
        newtons = value * to_newtons[from_unit]
        conversion_list.append((from_unit, "n", newtons))
        conversion_list.append(("n", to_unit, newtons / to_newtons[to_unit]))
    elif ( (from_unit in to_newton_metre) and (to_unit in to_newton_metre) ):
        newton_meter = value * to_newton_metre[from_unit]
        conversion_list.append((from_unit, "n.m", newton_meter))
        conversion_list.append(("n.m", to_unit, newton_meter / to_newton_metre[to_unit]))
    else:
        raise ValueError(f"Invalid from_unit: {from_unit} & to_unit: {to_unit} combination")
    
    return(conversion_list)

