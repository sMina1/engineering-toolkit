import pandas as pd
import matplotlib.pylab as plt
import numpy as np

def moving_average(series, window=3):
    return series.rolling(window=window, center=True).mean()

def linear_regression(x, y):
    x_numeric = (x - x.iloc[0]).dt.total_seconds()
    coeffs = np.polyfit(x_numeric, y, deg=3)
    trend = np.polyval(coeffs, x_numeric)
    return trend, coeffs

def plot_sensor_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8), sharex=True)
    
    axes[0].plot(df["timestamp"], df["temperature_c"], label="Temperature (°C)", alpha=0.4)
    axes[1].plot(df["timestamp"], df["pressure_pa"], label="Pressure (Pa)", color="orange")
    axes[2].plot(df["timestamp"], df["force_n"], label="Force (N)", color="green")

    # moving average plot
    axes[0].plot(df["timestamp"], moving_average(df["temperature_c"]), label="Moving Avg (°C)", color="red")
    # linear regression plot
    trend, coeffs = linear_regression(df["timestamp"], df["temperature_c"])
    axes[0].plot(df["timestamp"], trend, label=f"Trend (slope={coeffs[0]:.4f} °C/s)", color="black", linestyle="--")
    print(df["timestamp"])
    print(trend)
    for ax in axes:
        ax.legend()
        ax.grid(True)

    axes[0].set_title("Sensor Data Over Time")
    axes[2].set_xlabel("Timestamp")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_sensor_data("data/sensor_data_si.csv")