"""Command Line Interface parsing using standard library argparse."""

import argparse
from typing import Sequence


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the sine generator CLI.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="sine-generator",
        description=(
            "Generate and plot a mathematical sine wave with custom parameters."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--frequency",
        type=float,
        default=1.0,
        help="Frequency of the sine wave in Hz (cycles per unit time)",
    )

    parser.add_argument(
        "-a",
        "--amplitude",
        type=float,
        default=1.0,
        help="Peak amplitude of the sine wave",
    )

    parser.add_argument(
        "-c",
        "--color",
        type=str,
        default="blue",
        help="Line color for the plot (e.g. 'blue', 'red', 'green', '#FF0000')",
    )

    parser.add_argument(
        "-e",
        "--export",
        action="store_true",
        help=(
            "Export the generated plot to a timestamped PNG file "
            "(senoide_YYYYMMDDHHmmSS.png)"
        ),
    )

    return parser


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        args: Sequence of argument strings, or None to read from sys.argv.

    Returns:
        Parsed arguments namespace.
    """
    parser = create_parser()
    return parser.parse_args(args)
