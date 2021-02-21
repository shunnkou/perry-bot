import os
from pathlib import Path
from peewee import BooleanField, DateField, DateTimeField, IntegerField, Model, SqliteDatabase, TextField

db_path = os.path.join(
    Path(__file__).parent.parent, 'tests', 'test_perry-bot.sqlite')

db = SqliteDatabase(db_path,
                    pragmas={
                        'journal_mode': 'wal',
                        'cache_size': -1 * 64000,
                        'ignore_check_constraints': 0,
                        'synchronous': 0
                    })

# <!-------- Models --------!>


class BaseModel(Model):
    class Meta:
        database = db
        legacy_table_names = False


class Water(BaseModel):
    cups_drank = IntegerField(column_name='cups_drank')
    datestamp = DateField(column_name='datestamp')


class Mood(BaseModel):
    rating = IntegerField(column_name='rating')
    datetime_stamp = DateTimeField(column_name='datetime_stamp')
    comment = TextField(column_name='comment', null=True)


class Habit(BaseModel):
    habit_name = TextField(column_name='habit_name', unique=True)
    completion = BooleanField(column_name='completion')
    start_date = DateField(column_name='start_date')
    completed_on = TextField(column_name='completed_on')
    frequency = TextField(column_name='frequency')
