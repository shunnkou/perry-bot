"""Set up console."""

from rich.console import Console
from rich.theme import Theme

theme = Theme(
    {"default": "light_steel_blue on default", "cancel": "dark_red on default"}
)


def main_console() -> Console:
    """Console."""
    return Console(theme=theme)
