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
    metres = value * to_metres[from_unit]
    result = metres / to_metres[to_unit]

    return result
  
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


def main():
    # test your function here
    
    while True:
        user_conversion = input(
            "Which conversion would you like to make?\n"
            "T for Temperature, L for Length. Q to quit.\n").lower()
        
        if user_conversion == "q":
            break
        
        if user_conversion not in ("l", "t"):
            print("No valid selection")
            continue
        
        user_input = input("Enter value, from_unit, to_unit.\n")
        parts = user_input.split()
        
        try:
            value, from_unit, to_unit = parts
            value = float(value)
            from_unit = from_unit.lower()
            to_unit = to_unit.lower()
            
            if user_conversion == "l":
                result = convert_length(value, from_unit, to_unit)
            else:
                result = convert_temperature(value, from_unit, to_unit)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()