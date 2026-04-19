import pandas as pd
from converters.length import convert_length
from converters.pressure import convert_pressure

def load_sensor_data(filepath):
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    df = load_sensor_data("data/sensor_data.csv")

    #convert length_mm to length_m
    df["length_mm"] = df["length_mm"].apply(lambda x: convert_length(x, "mm", "m")[-1][2])
    df = df.rename(columns={"length_mm": "length_m"})
    
    #convert pressure_psi to pressure_pa
    df["pressure_psi"] = df["pressure_psi"].apply(lambda x: convert_pressure(x, "psi", "pa")[-1][2])
    df = df.rename(columns={"pressure_psi": "pressure_pa"})
    
    df = df.round(4)
    df.to_csv("data/sensor_data_si.csv", index=False)
