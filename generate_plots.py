"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Seed for the random number generator to ensure reproducibility.

    Returns
    -------
    sensor_a : ndarray of shape (200,)
        Temperature readings for Sensor A (mean 25°C, std 3°C).
    sensor_b : ndarray of shape (200,)
        Temperature readings for Sensor B (mean 27°C, std 4.5°C).
    timestamps : ndarray of shape (200,)
        Timestamps uniformly distributed from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed=seed)
    
    # Generate 200 timestamps uniformly distributed from 0 to 10 seconds
    timestamps = rng.uniform(0, 10, 200)
    
    # Generate temperature readings for Sensor A: normal distribution, mean 25°C, std 3°C
    sensor_a = rng.normal(25, 3, 200)
    
    # Generate temperature readings for Sensor B: normal distribution, mean 27°C, std 4.5°C
    sensor_b = rng.normal(27, 4.5, 200)
    
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor readings vs timestamps.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A.
    sensor_b : array_like
        Temperature readings for Sensor B.
    timestamps : array_like
        Timestamps corresponding to the readings.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the provided Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B')
    ax.set_xlabel('Timestamp (seconds)')
    ax.set_ylabel('Sensor Reading (°C)')
    ax.set_title('Sensor Readings vs Time')
    ax.legend()


def plot_histogram(sensor_a, sensor_b, ax):
    """Create an overlaid histogram of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A.
    sensor_b : array_like
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the provided Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='--', label='Sensor A Mean')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='--', label='Sensor B Mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distributions of Sensors A and B')
    ax.legend()


def plot_boxplot(sensor_a, sensor_b, ax):
    """Create a side-by-side box plot comparing two sensor distributions.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings for Sensor A.
    sensor_b : array_like
        Temperature readings for Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the provided Axes object in place.
    """
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    ax.axhline(overall_mean, color='red', linestyle='--', label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Box Plot Comparison of Sensor A and B Temperatures')
    ax.legend()


def main():
    """Generate synthetic sensor data, build plots, and save the figure.

    This function creates the full figure for the sensor analysis by:
    - generating reproducible sensor data,
    - drawing a scatter plot, histogram, and box plot on a 1x3 subplot grid,
    - adjusting the layout, and
    - saving the result to sensor_analysis.png.

    Returns
    -------
    None
        Saves the figure to disk and does not return any value.
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=2682)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
    axes_flat = axes.flatten()

    plot_scatter(sensor_a, sensor_b, timestamps, axes_flat[0])
    plot_histogram(sensor_a, sensor_b, axes_flat[1])
    plot_boxplot(sensor_a, sensor_b, axes_flat[2])

    stats_ax = axes_flat[3]
    stats_ax.axis('off')
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    overall_median = np.median(np.concatenate([sensor_a, sensor_b]))
    summary_text = (
        f"Sensor A mean: {sensor_a.mean():.2f} °C\n"
        f"Sensor B mean: {sensor_b.mean():.2f} °C\n"
        f"Overall mean: {overall_mean:.2f} °C\n"
        f"Overall median: {overall_median:.2f} °C\n"
        f"Total readings: {sensor_a.size + sensor_b.size}\n"
    )
    stats_ax.text(0.05, 0.95, summary_text, va='top', ha='left', fontsize=12, family='monospace')
    stats_ax.set_title('Summary Statistics')

    fig.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')


if __name__ == '__main__':
    main()