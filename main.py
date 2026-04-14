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

      # Convert: from_unit -> metres -> to_unit
      metres = value * to_metres[from_unit]
      result = metres / to_metres[to_unit]

      return result

def main():
    # test your function here
    
    while True:
        user_input = input("Enter value, from_unit, to_unit. Q to exit.\n")
        if user_input.lower() == "q":
            break
        parts = user_input.split()  # splits on whitespace
        
        try:
            value, from_unit, to_unit = parts 
            value = float(value)
            result = convert_length(value, from_unit, to_unit)
            print(result)
        except KeyError:
            print("Unknown unit. Supported: m, km, cm, mm, in, ft, yd, miles")
        except ValueError:
            print("Expected format: 5 km miles")

if __name__ == "__main__":
    main()