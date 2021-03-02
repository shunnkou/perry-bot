"""Database models."""

import os
from pathlib import Path

from peewee import BooleanField, IntegerField, Model, SqliteDatabase, TextField

# db_path = os.path.join(Path(__file__).parent, 'files', 'perry-bot.sqlite')
db_path = os.path.join(Path(__file__).parent, "files", "test_perry-bot.sqlite")

db = SqliteDatabase(
    db_path,
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1 * 64000,
        "ignore_check_constraints": 0,
        "synchronous": 0,
    },
)


# <!-------- Models --------!>


class BaseModelDB(Model):
    """Database model."""

    class Meta:
        """Set database and use legacy table names."""

        database = db
        legacy_table_names = False


class WaterDB(BaseModelDB):
    """Water table."""

    cups_drank = IntegerField(column_name="cups_drank")
    date_stamp = TextField(column_name="date_stamp")

    class Meta:
        """Name the table 'water'."""

        table_name = "water"


class MoodDB(BaseModelDB):
    """Mood table."""

    rating = IntegerField(column_name="rating")
    datetime_stamp = TextField(column_name="datetime_stamp")
    comment = TextField(column_name="comment", null=True)

    class Meta:
        """Name the table 'mood'."""

        table_name = "mood"


class HabitDB(BaseModelDB):
    """Habit table."""

    habit_name = TextField(column_name="habit_name", unique=True)
    completion = BooleanField(column_name="completion")
    start_date = TextField(column_name="start_date")
    completed_on = TextField(column_name="completed_on")
    frequency = TextField(column_name="frequency")
    next_due = TextField(column_name="next_due")

    class Meta:
        """Name the table 'habit'."""

        table_name = "habit"


# def create_tables():
#     with db:
#         db.create_tables([MoodDB])
#     print("Mood DB created.")
#
#
# def drop_mood():
#     with db:
#         db.drop_tables([MoodDB])
#     print("Mood DB dropped.")
