from rich.console import Console
from rich.theme import Theme

theme = Theme(
    {"default": "light_steel_blue on default", "cancel": "dark_red on default"}
)


def console():
    """Console."""
    return Console(theme=theme)
