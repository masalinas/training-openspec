"""Unit tests for command-line interface parsing and execution."""

import pytest

from sine_generator.cli import parse_args
from sine_generator.main import main


def test_cli_default_arguments() -> None:
    """Test default values when no CLI arguments are supplied."""
    parsed = parse_args([])
    assert parsed.frequency == 1.0
    assert parsed.amplitude == 1.0
    assert parsed.color == "blue"
    assert parsed.export is False


def test_cli_custom_arguments() -> None:
    """Test custom CLI arguments for frequency, amplitude, color, and export flag."""
    parsed = parse_args(
        ["--frequency", "5.5", "--amplitude", "3.2", "--color", "red", "--export"]
    )
    assert parsed.frequency == 5.5
    assert parsed.amplitude == 3.2
    assert parsed.color == "red"
    assert parsed.export is True


def test_cli_short_flags() -> None:
    """Test short CLI flag aliases (-f, -a, -c, -e)."""
    parsed = parse_args(["-f", "2.0", "-a", "1.5", "-c", "green", "-e"])
    assert parsed.frequency == 2.0
    assert parsed.amplitude == 1.5
    assert parsed.color == "green"
    assert parsed.export is True


def test_cli_help_output(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that --help displays usage information in English and exits cleanly."""
    with pytest.raises(SystemExit) as exc_info:
        parse_args(["--help"])
    assert exc_info.value.code == 0

    captured = capsys.readouterr()
    assert "sine-generator" in captured.out
    assert "Frequency of the sine wave" in captured.out
    assert "Peak amplitude" in captured.out
    assert "Line color" in captured.out
    assert "Export the generated plot" in captured.out


def test_main_execution(
    tmp_path: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test main() entry point execution with export flag."""
    monkeypatch.chdir(tmp_path)
    exit_code = main(["--frequency", "2.0", "--export"])
    assert exit_code == 0

    # Verify PNG file was generated in working directory
    generated_pngs = list(tmp_path.glob("senoide_*.png"))
    assert len(generated_pngs) == 1
