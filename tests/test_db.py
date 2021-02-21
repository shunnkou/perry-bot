import unittest
from peewee import SqliteDatabase

from perry_bot.backend import Water, Mood, Habit

MODELS = [Water, Mood, Habit]

test_db = SqliteDatabase(':memory:')


class BaseTestCase(unittest.TestCase):
    """Base class for testing DB."""
    def setUp(self):
        """Set up database."""
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        """Cleanup database."""
        test_db.drop_tables(MODELS)
        test_db.close()

    # <!-------- Water Table --------!>

    def test_create_water_log(self):
        import datetime
        Water.get_or_create(cups_drank=3, datestamp='2021-02-20')
        query = [(water.cups_drank, water.datestamp)
                 for water in Water.select()]

        assert 3 in query[0]
        assert datetime.date(2021, 2, 20) in query[0]

    def test_update_water_log(self):
        pass

    # <!-------- Habit Table --------!>

    def test_create_habit_log(self):
        pass

    def test_update_habit_log(self):
        pass

    # <!-------- Mood Table --------!>

    def test_create_mood_log(self):
        pass

    def test_update_mood_log(self):
        pass
