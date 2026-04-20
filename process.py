import pandas as pd
import argparse
from converters.length import convert_length
from converters.pressure import convert_pressure

def load_sensor_data(filepath):
    df = pd.read_csv(filepath)
    return df

def parse_args():
    parser = argparse.ArgumentParser(description="Process sensor data CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_args()
    df = load_sensor_data(args.input)
    
    df_si = df
    #convert length_mm to length_m
    df_si["length_mm"] = df_si["length_mm"].apply(lambda x: convert_length(x, "mm", "m")[-1][2])
    df_si = df_si.rename(columns={"length_mm": "length_m"})
    
    #convert pressure_psi to pressure_pa
    df_si["pressure_psi"] = df_si["pressure_psi"].apply(lambda x: convert_pressure(x, "psi", "pa")[-1][2])
    df_si = df_si.rename(columns={"pressure_psi": "pressure_pa"})
    
    df_si = df_si.round(4)
    df_si.to_csv(args.output, index=False)

    #summry stats
    #iterative/long way
    # df_summary = pd.DataFrame()
    # df_summary["mean"] = df.mean()
    # df_summary["std"] = df.std()
    # df_summary["max"] = df.max()

    #short way
    df_summary = pd.DataFrame({
    "mean": df_si.mean(numeric_only=True),
    "std": df_si.std(numeric_only=True),
    "max": df_si.max(numeric_only=True)
    }).round(4)
    
    df_summary.index.name = "label"
    df_summary.to_csv("data/sensor_data_summary_stats.csv")
