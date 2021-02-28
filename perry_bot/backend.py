"""Database models and classes for each command."""

import os
from pathlib import Path

import attr
from peewee import BooleanField, IntegerField, Model, SqliteDatabase, TextField
from rich import pretty
from rich.markup import escape
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

from perry_bot.console import console

# <----- Debugging ----->

# import logging
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

# -----------------------

pretty.install()
console = console()

# db_path = os.path.join(Path(__file__).parent, 'files', 'perry-bot.sqlite')
db_path = os.path.join(Path(__file__).parent, 'files', 'test_perry-bot.sqlite')

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
    next_due = TextField(column_name='next_due')

    class Meta:
        """Name the table 'habit'."""

        table_name = 'habit'


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

# <!-------- Dataclasses --------!>


@attr.s(kw_only=True)
class Water:
    """Water dataclass."""

    id = attr.ib()
    cups_drank = attr.ib()
    date_stamp = attr.ib()


@attr.s(kw_only=True)
class Mood:
    """Mood dataclass."""

    id = attr.ib()
    rating = attr.ib()
    datetime_stamp = attr.ib()
    comment = attr.ib()

    def query(self, date: str):
        """
        Query database and append data to self.

        :param date:
        :return:
        """
        with db:
            query = MoodDB.select().where(MoodDB.datetime_stamp.contains(date))
            for record in query:
                self.id.append(record.id)
                self.rating.append(record.rating)
                self.datetime_stamp.append(record.datetime_stamp)
                self.comment.append(record.comment)

    def make_table(self, title: str):
        """
        Create 'Mood' table.

        :param title:
        :return:
        """
        table = Table(title=title)
        table.add_column("#", justify="center")
        table.add_column("Datetime stamp", justify='center')
        table.add_column("Rating", justify='center')
        table.add_column("Comment", justify='center')

        for (number, date, rate, comment) in zip(self.id, self.datetime_stamp,
                                                 self.rating, self.comment):
            table.add_row(str(number), str(date), str(rate), str(comment))

        return table

    def new_entry(self):
        """
        Create a new entry in the database.

        :return:
        """
        with db:
            MoodDB.create(rating=self.rating,
                          datetime_stamp=self.datetime_stamp,
                          comment=self.comment)
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Mood entry added to database.",
            style="default")

    def view_average_mood(self, view_date: str):
        """
        View average mood based on the given date.

        :param view_date:
        :return:
        """
        self.query(date=view_date)
        if self.id:
            average = int(sum(self.rating) / len(self.rating))
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Your average mood "
                f"on {view_date} is {average}.",
                style="default")
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no "
                f"records matching {view_date}. Try another one.",
                style="default")

    def view_mood_table(self, view_date: str):
        """
        Print a mood table given a date.

        :param view_date:
        :return:
        """
        self.query(date=view_date)
        table = self.make_table(title="Mood Records")
        if self.id:
            if len(table.rows) >= 20:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] The table has more "
                    f"than 20 rows. Would you like to continue displaying the table?",
                    style='default')
                q = Prompt.ask(choices=['y', 'n'])
                # if q in ['y']:
                #     console.print(table, style="default")
                # elif q in ['n']:
                if q in ['n']:
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] --view-table cancelled.",
                        style='default')
                    return
            console.print(table, style='default')
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {view_date}. Try another one.",
                style="default")

    def edit_mood(self, edit_date: str):
        """
        Edit a specific mood rating based on a date by inputting the number of the rating.

        :param edit_date:
        :return:
        """
        self.query(date=edit_date)
        table = self.make_table(title="Edit a Mood Rating")

        table.add_row(str(len(self.id) + 1),
                      "[b]----------[/b]",
                      "[b]Cancel Edit[/b]",
                      "[b]----------[/b]",
                      style="cancel")
        if self.id:
            if len(table.rows) >= 20:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] The table has more "
                    f"than 20 rows. Would you like to continue editing your "
                    f"records on this date?",
                    style='default')
                q = Prompt.ask(choices=['y', 'n'])
                if q in ['n']:
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] --edit cancelled.",
                        style='default')
                    return
            console.print(table, style="default")
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Enter the number of "
                f"the entry you want to edit",
                style="default")
            num = IntPrompt.ask()
            while num not in self.id:
                if num == len(self.id) + 1:
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] Editing cancelled!",
                        style="default")
                    return
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Please enter "
                    f"a valid number from the table",
                    style="default")
                num_again = IntPrompt.ask()
                if num_again == len(self.id) + 1:
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] Editing cancelled!",
                        style="default")
                    return
                if num_again in self.id:
                    num = num_again
                    break
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Which category would "
                f"you like to edit?",
                style="default")
            edit_target = Prompt.ask(choices=["rating", "comment"])
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Enter the new value",
                style="default")
            edit_input = ''
            if edit_target in ['comment']:
                edit_input = Prompt.ask()
            elif edit_target in ['rating']:
                edit_input = IntPrompt.ask()
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] You would like to "
                f"change the {edit_target} for entry #{num} to '{edit_input}'. Correct?",
                style="default")
            check = Prompt.ask(choices=["y", "n"])
            while check.lower() in ['n']:
                edit_target = Prompt.ask(choices=["rating", "comment"])
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Enter the new value",
                    style="default")
                edit_input = ''
                if edit_target in ['comment']:
                    edit_input = Prompt.ask()
                elif edit_target in ['rating']:
                    edit_input = IntPrompt.ask()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] You would like to "
                    f"change the {edit_target} for entry #{num} to '{edit_input}'. Correct?",
                    style="default")
                check = Prompt.ask(choices=["y", "n"])
                if check.lower() in ['y']:
                    break
            if edit_target.lower() in ['rating']:
                with db:
                    update = MoodDB.update(rating=edit_input).where(
                        MoodDB.id == num)
                    update.execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your rating has been updated.",
                    style='default')
            elif edit_target.lower() in ['comment']:
                with db:
                    update = MoodDB.update(comment=edit_input).where(
                        MoodDB.id == num)
                    update.execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your comment has been updated.",
                    style='default')

        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {edit_date}. Try another one.",
                style="default")


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
