"""Main entry point for the sine generator application."""

import sys
from typing import Sequence

from sine_generator.cli import parse_args
from sine_generator.generator import generate_sine_data, plot_sine_wave
from sine_generator.utils import generate_timestamped_filename


def main(args: Sequence[str] | None = None) -> int:
    """Execute main program logic.

    Args:
        args: Sequence of CLI command line arguments.

    Returns:
        Exit code (0 for success).
    """
    parsed = parse_args(args)

    print(
        f"Generating sine wave -> Frequency: {parsed.frequency} Hz, "
        f"Amplitude: {parsed.amplitude}, Color: {parsed.color}"
    )

    time, wave = generate_sine_data(
        frequency=parsed.frequency, amplitude=parsed.amplitude
    )

    output_file = None
    if parsed.export:
        output_file = generate_timestamped_filename()
        print(f"Exporting plot to PNG file: {output_file}")

    plot_sine_wave(time, wave, color=parsed.color, output_path=output_file)

    if output_file:
        print("Export completed successfully.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
