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


def test_create_water_log():
    """Test creating a water entry."""
    import datetime
    Water.get_or_create(cups_drank=3, datestamp='2021-02-20')
    query = [(water.cups_drank, water.datestamp) for water in Water.select()]

    assert 3 in query[0]
    assert datetime.date(2021, 2, 20) in query[0]


def test_update_water_log():
    """Test updating a water entry."""
    pass


def test_delete_water_log():
    """Test the delete function."""
    pass


# <!-------- Habit Table --------!>


def test_create_habit_log():
    """Test creating a new habit."""
    pass


def test_update_habit_name():
    """Test updating an existing habit's name."""
    pass


def test_update_habit_frequency():
    """Test updating an existing habit's frequency."""
    pass


def test_update_habit_start_date():
    """Test updating an existing habit's start date."""
    pass


# <!-------- Mood Table --------!>


def test_create_mood_log():
    """Test create a new mood entry."""
    pass


def test_update_mood_log():
    """Test update an existing mood entry."""
    pass
