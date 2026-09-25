"""Utility functions for filename formatting and timestamping."""

from datetime import datetime


def generate_timestamped_filename(
    prefix: str = "senoide", timestamp: datetime | None = None
) -> str:
    """Generate a timestamped filename.

    Pattern: `<prefix>_YYYYMMDDHHmmSS.png`.

    Args:
        prefix: The prefix string for the filename (defaults to "senoide").
        timestamp: An optional explicit datetime object. Defaults to datetime.now().

    Returns:
        The formatted filename string (e.g., `senoide_20260924120000.png`).
    """
    if timestamp is None:
        timestamp = datetime.now()
    formatted_time = timestamp.strftime("%Y%m%d%H%M%S")
    return f"{prefix}_{formatted_time}.png"
