import unittest
from peewee import SqliteDatabase

from perry_bot.backend import WaterDB, MoodDB, HabitDB

MODELS = [WaterDB, MoodDB, HabitDB]


# skipqc
class BaseTestCase(unittest.TestCase):
    """Base class for testing DB."""

    def setUp(self):
        """Set up database."""
        super(BaseTestCase, self).setUp()
        self.conn = SqliteDatabase(':memory:')
        self.conn.bind(MODELS, bind_refs=False, bind_backrefs=False)
        self.conn.connect()
        self.conn.create_tables(MODELS)

    def tearDown(self):
        """Cleanup database."""
        self.conn.drop_tables(MODELS)
        self.conn.close()

#
#     # <!-------- Water Table --------!>
#
#     def test_create_water_log(self):
#         """Test creating a water entry."""
#         import datetime
#         WaterDB(cups_drank=3, datestamp='2021-02-20')
#         query = [(water.cups_drank, water.datestamp)
#                  for water in WaterDB.select()]
#
#         assert 3 in query[0]
#         assert datetime.date(2021, 2, 20) in query[0]
#
#
# def test_update_water_log():
#     """Test updating a water entry."""
#     pass
#
#
# def test_delete_water_log():
#     """Test the delete function."""
#     pass
#
#
# # <!-------- Habit Table --------!>
#
# def test_create_habit_log():
#     """Test creating a new habit."""
#     pass
#
#
# def test_update_habit_name():
#     """Test updating an existing habit's name."""
#     pass
#
#
# def test_update_habit_frequency():
#     """Test updating an existing habit's frequency."""
#     pass
#
#
# def test_update_habit_start_date():
#     """Test updating an existing habit's start date."""
#     pass
#
#
# # <!-------- Mood Table --------!>
#
# def test_create_mood_log():
#     """Test create a new mood entry."""
#     pass
#
#
# def test_update_mood_log():
#     """Test update an existing mood entry."""
#     pass
