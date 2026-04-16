"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np


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
