import os
from pathlib import Path

import attr
from peewee import BooleanField, IntegerField, Model, SqliteDatabase, TextField
from rich.table import Table

from perry_bot.console import console

console = console()

db_path = os.path.join(Path(__file__).parent, 'files', 'perry-bot.sqlite')

db = SqliteDatabase(db_path,
                    pragmas={
                        'journal_mode': 'wal',
                        'cache_size': -1 * 64000,
                        'ignore_check_constraints': 0,
                        'synchronous': 0
                    })


# <!-------- Models --------!>


class BaseModelDB(Model):
    """Database model."""

    class Meta:
        """Set database and use legacy table names."""
        database = db
        legacy_table_names = False


class WaterDB(BaseModelDB):
    """Water table."""
    cups_drank = IntegerField(column_name='cups_drank')
    date_stamp = TextField(column_name='date_stamp')

    class Meta:
        """Name the table 'water'."""
        table_name = 'water'


class MoodDB(BaseModelDB):
    """Mood table."""
    rating = IntegerField(column_name='rating')
    datetime_stamp = TextField(column_name='datetime_stamp')
    comment = TextField(column_name='comment', null=True)

    class Meta:
        """Name the table 'mood'."""
        table_name = 'mood'


class HabitDB(BaseModelDB):
    """Habit table."""
    habit_name = TextField(column_name='habit_name', unique=True)
    completion = BooleanField(column_name='completion')
    start_date = TextField(column_name='start_date')
    completed_on = TextField(column_name='completed_on')
    frequency = TextField(column_name='frequency')

    class Meta:
        """Name the table 'habit'."""
        table_name = 'habit'


# <!-------- Dataclasses --------!>

@attr.s(kw_only=True)
class Water:
    """Water dataclass."""
    cups_drank = attr.ib()
    date_stamp = attr.ib()


@attr.s()
class Mood:
    """Mood dataclass."""
    rating = attr.ib(kw_only=True)
    datetime_stamp = attr.ib(kw_only=True)
    comment = attr.ib()


@attr.s(kw_only=True)
class Habit:
    """Habit dataclass."""
    habit_name = attr.ib()
    completion = attr.ib()
    start_date = attr.ib()
    completed_on = attr.ib()
    frequency = attr.ib()

    @classmethod
    def make_table(cls, **kwargs):
        """Create a table to view habits."""
        table = Table(title="My Habits")
        table.add_column("Habit")
        table.add_column("Complete?")
        table.add_column("Start Date")
        table.add_column("Frequency")


# <!-------- Methods -------->

def _get_or_create(model, **kwargs):
    """Check if today exists. If yes, get it. Else, create new day."""
    if model.lower() == 'water':
        water, _unused_created = WaterDB.get_or_create(**kwargs)
        return water
    if model.lower() == 'mood':
        mood, _unused_created = MoodDB.get_or_create(**kwargs)
        return mood
    if model.lower() == 'habit':
        habit, _unused_created = HabitDB.get_or_create(**kwargs)
        return habit
    raise Exception("The model must be `water`, `mood`, or `habit`.")

