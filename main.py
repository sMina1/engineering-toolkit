from converters.length import convert_length
from converters.temperature import convert_temperature

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