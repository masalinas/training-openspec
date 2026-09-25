"""Unit tests for utility functions."""

from datetime import datetime

from sine_generator.utils import generate_timestamped_filename


def test_generate_timestamped_filename_default_prefix() -> None:
    """Test filename generation with explicit datetime and default prefix."""
    fixed_time = datetime(2026, 9, 24, 15, 30, 45)
    filename = generate_timestamped_filename(timestamp=fixed_time)
    assert filename == "senoide_20260924153045.png"


def test_generate_timestamped_filename_custom_prefix() -> None:
    """Test timestamped filename generation with custom prefix."""
    fixed_time = datetime(2026, 9, 24, 15, 30, 45)
    filename = generate_timestamped_filename(prefix="custom", timestamp=fixed_time)
    assert filename == "custom_20260924153045.png"


def test_generate_timestamped_filename_current_time() -> None:
    """Test timestamped filename generation using default current time."""
    filename = generate_timestamped_filename()
    assert filename.startswith("senoide_")
    assert filename.endswith(".png")
    assert len(filename) == 26
