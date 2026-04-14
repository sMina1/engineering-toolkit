def convert_temperature(value, from_unit, to_unit):
    
    converted_val = None
    
    # to celsius first
    if from_unit.lower() == "c":
        celsius = value
    elif from_unit.lower() == "f":
        celsius = (value - 32) * 5/9
    elif from_unit.lower() == "k":
        celsius = value - 273.15
    else:
      raise ValueError(f"Invalid from_unit: {from_unit}")

    # from celsius to target
    if to_unit.lower() == "c":
        converted_val = celsius
    elif to_unit.lower() == "f":
        converted_val = celsius * 9/5 + 32
    elif to_unit.lower() == "k":
        converted_val = celsius + 273.15
            
    if converted_val is None:
        raise ValueError(f"Invalid units: {from_unit} to {to_unit}")
        
    return converted_val