"""Sine wave calculation and matplotlib rendering engine."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Force non-interactive Agg backend to support headless container execution
matplotlib.use("Agg")


def generate_sine_data(
    frequency: float, amplitude: float, num_points: int = 1000, duration: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """Calculate time vector and corresponding sine wave values.

    Args:
        frequency: Sine wave frequency in Hz (cycles per unit time).
        amplitude: Peak amplitude of the sine wave.
        num_points: Total number of sampling data points.
        duration: Total time duration in seconds.

    Returns:
        A tuple containing (time_vector, sine_wave_values).
    """
    time = np.linspace(0.0, duration, num_points)
    wave = amplitude * np.sin(2 * np.pi * frequency * time)
    return time, wave


def plot_sine_wave(
    time: np.ndarray,
    wave: np.ndarray,
    color: str = "blue",
    output_path: str | Path | None = None,
) -> plt.Figure:
    """Render a sine wave plot using Matplotlib with customizable color.

    Args:
        time: Array of time sampling points.
        wave: Array of calculated sine wave values.
        color: Matplotlib color string (e.g., "red", "#FF0000", "blue").
        output_path: Optional file path to save the generated PNG plot.

    Returns:
        The matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time, wave, color=color, linewidth=2, label="Sine Wave")
    ax.set_title("Sine Wave Plot", fontsize=14)
    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_ylabel("Amplitude", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend(loc="upper right")

    if output_path is not None:
        fig.savefig(output_path, dpi=300, bbox_inches="tight")

    return fig
