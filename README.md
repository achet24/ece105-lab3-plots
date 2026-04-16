# Sensor Plot Generation

A small Python script that generates synthetic sensor temperature data and saves a combined analysis figure with scatter, histogram, and box plot visualizations.

## Installation

1. Activate the `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required dependencies using either `conda` or `mamba`:

```bash
conda install numpy matplotlib
```

or

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the repository directory:

```bash
python generate_plots.py
```

This will generate the sensor data and save the output figure in the current working directory.

## Example output

The script produces a single PNG file named `sensor_analysis.png` containing three side-by-side plots:

- A scatter plot of Sensor A and Sensor B temperature readings versus timestamp.
- An overlaid histogram showing the temperature distributions for both sensors, with mean markers.
- A box plot comparing Sensor A and Sensor B distributions, including an overall mean line.

## AI tools used and disclosure

[Add a brief disclosure here about any AI tools used during the project creation or editing process.]
