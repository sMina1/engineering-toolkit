import pandas as pd
import matplotlib.pylab as plt

def plot_sensor_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8), sharex=True)
    
    axes[0].plot(df["timestamp"], df["temperature_c"], label="Temperature (°C)")
    axes[1].plot(df["timestamp"], df["pressure_pa"], label="Pressure (Pa)", color="orange")
    axes[2].plot(df["timestamp"], df["force_n"], label="Force (N)", color="green")

    for ax in axes:
        ax.legend()
        ax.grid(True)

    axes[0].set_title("Sensor Data Over Time")
    axes[2].set_xlabel("Timestamp")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_sensor_data("data/sensor_data_si.csv")