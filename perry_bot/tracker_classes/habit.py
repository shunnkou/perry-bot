"""Habit dataclass."""

import attr

# from rich.markup import escape
# from rich.prompt import IntPrompt, Prompt
# from perry_bot.class_helpers import EditExistingEntry
from rich.table import Table
from perry_bot.console import Console, main_console

# from perry_bot.db_models import HabitDB, db

console: Console = main_console()


@attr.s(kw_only=True)
class Habit:
    """Habit dataclass."""

    id = attr.ib()
    habit_name = attr.ib()
    completion = attr.ib()
    start_date = attr.ib()
    completed_on = attr.ib()
    frequency = attr.ib()
    next_due = attr.ib()

    @classmethod
    def make_table(cls, **kwargs):
        """Create a table to view habits."""
        table = Table(title="My Habits")
        table.add_column("Habit")
        table.add_column("Complete?")
        table.add_column("Next due on")
        table.add_column("Start Date")
        table.add_column("Frequency")
        ...
