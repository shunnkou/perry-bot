"""Database models and classes for each command."""

import os
from pathlib import Path

import attr
from peewee import BooleanField, IntegerField, Model, SqliteDatabase, TextField
from rich import pretty
from rich.markup import escape
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.logging import RichHandler

from perry_bot.console import console

# <----- Debugging ----->

# import logging
#
# logger = logging.getLogger('peewee')
# logger.setLevel(logging.DEBUG)
# handler = RichHandler()
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     fmt='%(message)s',
#     datefmt="%b %d %Y %H:%M:%S")
# handler.setFormatter(formatter)
# logger.addHandler(handler)

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
    date_stamp = attr.ib()
    cups_drank = attr.ib()

    def query(self, date: str):
        """Query database and append data to self.

        :param date:
        :return:
        """
        with db:
            query = WaterDB.select().where(WaterDB.date_stamp.contains(date))
        for record in query:
            self.id.append(record.id)
            self.cups_drank.append(record.cups_drank)
            self.date_stamp.append(record.date_stamp)

    def get_or_create_cups(self, date: str, cups: int):
        """Get existing record or create a new record of cups drank.

        :param date:
        :param cups:
        :return:
        """
        self.query(date=date)
        if self.id:
            with db:
                WaterDB.update(cups_drank=WaterDB.cups_drank + cups).where(
                    WaterDB.date_stamp.contains(date)).execute()
            self.query(date=date)
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Water log added to database.\n"
                f"[bold]{escape('[perry-bot]:')}[/bold] You've drunk "
                f"{self.cups_drank[-1]} cups of water today, "
                f"keep up the good work!",
                style='default')
        else:
            with db:
                WaterDB.insert(cups_drank=cups, date_stamp=date).execute()
            self.query(date=date)
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Water log added to database.\n"
                f"[bold]{escape('[perry-bot]:')}[/bold] You've drunk "
                f"{self.cups_drank[-1]} cups of water today, "
                f"keep up the good work!",
                style='default')

    def delete_cups(self, date: str, cups: int):
        """Delete num of cups from today's record.

        :param date:
        :param cups:
        :return:
        """
        self.query(date=date)
        if self.id:
            if sum(self.cups_drank) - cups < 0:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Deleting {cups} cups will cause "
                    f"the total cups to be less than zero ({sum(self.cups_drank) - cups})."
                    f"\n[bold]{escape('[perry-bot]:')}[/bold] Reset today's cups drank to 0?",
                    style='default')
                c = Prompt.ask(choices=['y', 'n'])
                if c in ['y']:
                    with db:
                        WaterDB.update(cups_drank=0).where(
                            WaterDB.date_stamp.contains(date)).execute()
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] Cups drank today reset to 0.",
                        style='default')
                elif c in ['n']:
                    return
            else:
                with db:
                    WaterDB.update(cups_drank=WaterDB.cups_drank - cups).where(
                        WaterDB.date_stamp.contains(date)).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] {cups} cups deleted "
                    f"from today's log.",
                    style='default')
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] You haven't recorded any cups drank today yet, "
                f"there's nothing to delete!",
                style="default")

    def view_total(self, date: str):
        """Return total cups in database.

        :param date:
        :return:
        """
        self.query(date=date)
        if self.id:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] You've drunk {sum(self.cups_drank)} "
                f"cups of water on {date}.",
                style='default')
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {date}. Try another date.",
                style='default')

    def edit_cups(self, edit_date: str):
        """Edit number of cups drank in database.

        :param edit_date:
        :return:
        """
        self.query(date=edit_date)
        table = Table(title='Edit Water Records')
        table.add_column('#', justify='center')
        table.add_column('Date')
        table.add_column('Cups drank', justify='center')

        for (number, date, cups) in zip(self.id, self.date_stamp,
                                        self.cups_drank):
            table.add_row(str(number), str(date), str(cups))

        table.add_row(str(len(self.id) + 1),
                      "[b]Cancel Edit[/b]",
                      "[b]----------[/b]",
                      style="cancel")
        if self.id:
            targets = {'choices': ['cups drank']}
            edit_target = edit_existing_entry(self, table, **targets)
            if edit_target is False:
                return
            else:
                with db:
                    WaterDB.update(cups_drank=edit_target[1]).where(
                        WaterDB.id == edit_target[2]).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your number of cups "
                    f"drank has been updated.",
                    style='default')
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {edit_date}. Try another date.",
                style="default")


@attr.s(kw_only=True)
class Mood:
    """Mood dataclass."""

    id = attr.ib()
    rating = attr.ib()
    datetime_stamp = attr.ib()
    comment = attr.ib()

    def query(self, date: str):
        """Query database and append data to self.

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
        """Create 'Mood' table.

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
        """Create a new entry in the database.

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
        """View average mood based on the given date.

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
                f"records matching {view_date}. Try another date.",
                style="default")

    def view_mood_table(self, view_date: str):
        """Print a mood table given a date.

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
                if q in ['n']:
                    console.print(
                        f"[bold]{escape('[perry-bot]:')}[/bold] --view-table cancelled.",
                        style='default')
                    return
            console.print(table, style='default')
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {view_date}. Try another date.",
                style="default")

    def edit_mood(self, edit_date: str):
        """Edit a specific mood rating.

        Based on a date by inputting the number of the rating.

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
            targets = {'choices': ['rating', 'comment']}
            edit_target = edit_existing_entry(self, table, **targets)
            if edit_target is False:
                return
            if edit_target[0] in ['rating']:
                with db:
                    MoodDB.update(rating=edit_target[1]).where(
                        MoodDB.id == edit_target[2]).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your rating has been updated.",
                    style='default')
            elif edit_target[0] in ['comment']:
                with db:
                    MoodDB.update(comment=edit_target[1]).where(
                        MoodDB.id == edit_target[2]).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your comment has been updated.",
                    style='default')

        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no records "
                f"matching {edit_date}. Try another date.",
                style="default")


def edit_existing_entry(self, table, **kwargs):
    """Edit an existing entry.

    :param self:
    :param table:
    :param kwargs:
    :return:
    """
    choices = kwargs['choices']
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
            return False
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Please enter "
            f"a valid number from the table",
            style="default")
        num_again = IntPrompt.ask()
        if num_again == len(self.id) + 1:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Editing cancelled!",
                style="default")
            return False
        if num_again in self.id:
            num = num_again
            break
    console.print(
        f"[bold]{escape('[perry-bot]:')}[/bold] Which category would "
        f"you like to edit?",
        style="default")
    edit_target = Prompt.ask(choices=choices)
    console.print(f"[bold]{escape('[perry-bot]:')}[/bold] Enter the new value",
                  style="default")
    edit_input = ''
    if len(choices) == 2:
        if edit_target in choices[1]:
            edit_input = Prompt.ask()
        elif edit_target in choices[0]:
            edit_input = IntPrompt.ask()
    elif len(choices) == 1:
        edit_input = IntPrompt.ask()
    console.print(
        f"[bold]{escape('[perry-bot]:')}[/bold] You would like to "
        f"change the {edit_target} for entry #{num} to '{edit_input}'. Correct?",
        style="default")
    check = Prompt.ask(choices=["y", "n"])
    while check.lower() in ['n']:
        edit_target = Prompt.ask(choices=choices)
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Enter the new value",
            style="default")
        edit_input = ''
        if len(choices) == 2:
            if edit_target in choices[1]:
                edit_input = Prompt.ask()
            elif edit_target in choices[0]:
                edit_input = IntPrompt.ask()
        elif len(choices) == 1:
            edit_input = IntPrompt.ask()
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] You would like to "
            f"change the {edit_target} for entry #{num} to '{edit_input}'. Correct?",
            style="default")
        check = Prompt.ask(choices=["y", "n"])
        if check.lower() in ['y']:
            break
    return edit_target, edit_input, num


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
