"""Unit tests for sine wave data generation and plotting."""

from pathlib import Path

import numpy as np

from sine_generator.generator import generate_sine_data, plot_sine_wave


def test_generate_sine_data_shape_and_values() -> None:
    """Test sine wave data calculation values and array dimensions."""
    freq = 2.0
    amp = 3.0
    num_pts = 500
    duration = 2.0

    t, y = generate_sine_data(
        frequency=freq, amplitude=amp, num_points=num_pts, duration=duration
    )

    assert len(t) == num_pts
    assert len(y) == num_pts
    assert t[0] == 0.0
    assert np.isclose(t[-1], duration)
    assert np.isclose(np.max(y), amp)
    assert np.isclose(np.min(y), -amp)


def test_plot_sine_wave_without_export() -> None:
    """Test matplotlib figure rendering without saving file to disk."""
    t, y = generate_sine_data(frequency=1.0, amplitude=1.0, num_points=100)
    fig = plot_sine_wave(t, y, color="red")
    assert fig is not None


def test_plot_sine_wave_with_export(tmp_path: Path) -> None:
    """Test saving plot to disk as PNG image."""
    t, y = generate_sine_data(frequency=1.0, amplitude=1.0, num_points=100)
    output_file = tmp_path / "test_sine.png"

    plot_sine_wave(t, y, color="green", output_path=output_file)

    assert output_file.exists()
    assert output_file.stat().st_size > 0
