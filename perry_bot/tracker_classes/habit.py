"""Habit dataclass."""
import collections
import re
import typing

import attr

# from perry_bot.class_helpers import EditExistingEntry
import peewee
import arrow
from rich.markup import escape
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

from perry_bot.console import Console, main_console
from perry_bot.db_models import HabitDB, db

console: Console = main_console()


@attr.s(kw_only=True, auto_attribs=True)
class Habit:
    """Habit dataclass."""

    id: typing.Any
    habit_name: typing.Any
    completion: typing.List[bool]
    start_date: typing.Any
    completed_on: typing.List[str]
    frequency: typing.List[str]
    next_due: typing.List[str]

    # query all habits = HabitDB.select()
    # query on name = HabitDB.select().where(HabitDB.habit_name.contains(name))
    # query on id = HabitDB.select().where(HabitDB.id.contains(id_))

    def query(self, selection: collections.Iterable) -> None:
        """Query database and append data to self.

        :return:
        """
        with db.atomic():
            query = selection
            for record in query:
                self.id.append(record.id)
                self.habit_name.append(record.habit_name)
                self.completion.append(record.completion)
                self.start_date.append(record.start_date)
                self.completed_on.append(record.completed_on)
                self.frequency.append(record.frequency)
                self.next_due.append(record.next_due)

    # ---------- View ----------

    def make_table(self, title: str) -> Table:
        """Create 'Habit' table.

        A simple habit table.

        :param title:
        :return:
        """
        table = Table(title=title)
        table.add_column("[b]#[/b]", justify="center")
        table.add_column("[b]Habit[/b]", justify="center")
        table.add_column("[b]Next due on[/b]", justify="center")
        table.add_column("[b]Complete[/b]?", justify="center")

        for (number, name, complete, next_) in zip(
            self.id, self.habit_name, self.completion, self.next_due
        ):
            self.table_add_row(
                table=table,
                number=number,
                name=name,
                complete=complete,
                next_=next_,
            )

        return table

    def make_table_details(self, title: str) -> Table:
        """Create 'Habit Details' table.

        A habit table with all database columns.

        :param title:
        :return:
        """
        table = Table(title=title)
        table.add_column("[b]#[/b]", justify="center")
        table.add_column("[b]Habit[/b]", justify="center")
        table.add_column("[b]Frequency[/b]", justify="center")
        table.add_column("[b]Start date[/b]", justify="center")
        table.add_column("[b]Next due on[/b]", justify="center")
        table.add_column("[b]Completed on[/b]", justify="center")
        table.add_column("[b]Complete?[/b]", justify="center")

        for (number, name, complete, start, freq, next_, complete_on) in zip(
            self.id,
            self.habit_name,
            self.completion,
            self.start_date,
            self.frequency,
            self.next_due,
            self.completed_on,
        ):
            self.table_add_row_details(
                table=table,
                number=number,
                name=name,
                complete=complete,
                next_=next_,
                start=start,
                completed_on=complete_on,
                freq=freq,
            )

        return table

    def view_habit_table(self, detailed: bool) -> None:
        """View existing habits as a table.

        :return:
        """
        self.query(selection=HabitDB.select())
        if detailed:
            table = self.make_table_details(title="Habits Details")
        else:
            table = self.make_table(title="Habits")
        if self.id:
            console.print(table, style="default")
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"No habits found! Create a habit with "
                f"[i][b]perry-bot habit -a 'habit name'[/b][/i].",
                style="default",
            )

    @staticmethod
    def table_add_row(table: Table, number, name, complete, next_) -> None:
        """Add a row.

        :param table:
        :param number:
        :param name:
        :param complete:
        :param next_:
        """
        if complete in [0]:
            complete_status = ":x: Incomplete"
            table.add_row(
                str(number), str(name), str(next_), str(complete_status)
            )
        elif complete in [1]:
            complete_status = ":heavy_check_mark: Done"
            table.add_row(
                str(number), str(name), str(next_), str(complete_status)
            )

    @staticmethod
    def table_add_row_details(
        table: Table, number, name, complete, next_, start, freq, completed_on
    ) -> None:
        """Add a detailed row.

        :param completed_on:
        :param table:
        :param number:
        :param name:
        :param complete:
        :param next_:
        :param start:
        :param freq:
        """
        format_start_date = arrow.get(start).format("YYYY-MM-DD")
        if complete in [0]:
            complete_status = ":x: Incomplete"
            table.add_row(
                str(number),
                str(name),
                str(freq),
                str(format_start_date),
                str(next_),
                str(completed_on),
                str(complete_status),
            )
        elif complete in [1]:
            complete_status = ":heavy_check_mark: Done"
            table.add_row(
                str(number),
                str(name),
                str(freq),
                str(format_start_date),
                str(next_),
                str(completed_on),
                str(complete_status),
            )

    # ---------- Add ----------

    def create_new_habit(self, date_today: arrow.Arrow) -> None:
        """Main function for creating new a new habit.

        :param date_today:
        :return:
        """
        self.new_habit_freq_start_date(date_today=date_today)
        self.new_habit_next_due()
        new_habit = self.insert_new_habit()
        if new_habit:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"New habit has been added to database.",
                style="default",
            )
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"Sorry, that habit already exists, please "
                f"choose another habit name.",
                style="default",
            )

    def new_habit_freq_start_date(self, date_today: arrow.Arrow) -> None:
        """Get new frequency and start date.

        :param date_today:
        :return:
        """
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] "
            f"How frequent is this habit?",
            style="default",
        )
        console.print(
            "[b]1.[/b] Daily\n[b]2.[/b] Weekly\n[b]3.[/b] "
            "Every other week\n[b]4.[/b] Monthly\n"
            "[b]5.[/b] Every other month\n[b]6.[/b] Yearly",
            style="default",
        )
        frequency = IntPrompt.ask(
            choices=["1", "2", "3", "4", "5", "6"],
            default=1,
            show_default=True,
        )
        freq_str = self.new_habit_freq_to_string(frequency=frequency)
        self.frequency.append(freq_str)
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] "
            f"What's the start date (YYYY-MM-DD) of this habit?",
            style="default",
        )
        start_date_input = Prompt.ask(
            default=date_today.format("YYYY-MM-DD"), show_default=True
        )
        start_date = self.check_date_format(
            start_date_input=start_date_input, date_today=date_today
        )
        self.start_date.append(start_date)

    def check_date_format(
        self, start_date_input: typing.Any, date_today: arrow.Arrow
    ) -> arrow.Arrow:
        """Check input date format.

        :param start_date_input:
        :param date_today:
        :return:
        """
        date_string = re.match(r"\d{4}-\d{2}-\d{2}", start_date_input)
        if start_date_input == date_today.format("YYYY-MM-DD"):
            return date_today
        if date_string:
            return arrow.get(start_date_input, "YYYY-MM-DD")
        return self.wrong_date_format_loop(
            date_today=date_today, start_date_input=start_date_input
        )

    @staticmethod
    def wrong_date_format_loop(
        date_today: arrow.Arrow, start_date_input: str
    ) -> arrow.Arrow:
        """Wrong input date format loop.

        :param start_date_input:
        :param date_today:
        """
        date_string = re.match(r"\d{4}-\d{2}-\d{2}", start_date_input)
        while not date_string:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Please enter"
                f" a valid start date in the format YYYY-MM-DD.",
                style="default",
            )
            start_date_input_again = Prompt.ask(
                default=date_today.format("YYYY-MM-DD"), show_default=True
            )
            date_string_again = re.match(
                r"\d{4}-\d{2}-\d{2}", start_date_input_again
            )
            if date_string_again:
                return arrow.get(start_date_input_again)

        return arrow.get(start_date_input)

    @staticmethod
    def new_habit_freq_to_string(frequency: int) -> str:
        """Convert frequency choice to string.

        :param frequency:
        :return:
        """
        frequencies = [
            "daily",
            "weekly",
            "every other week",
            "monthly",
            "every other month",
            "yearly",
        ]
        if frequency == 1:
            return frequencies[0]
        if frequency == 2:
            return frequencies[1]
        if frequency == 3:
            return frequencies[2]
        if frequency == 4:
            return frequencies[3]
        if frequency == 5:
            return frequencies[4]
        if frequency == 6:
            return frequencies[5]
        return "False"

    def new_habit_next_due(self) -> None:
        """Shift given date for next due date.

        :return:
        """
        habit_frequency: str = self.frequency[0]
        if habit_frequency in ["daily"]:
            args = {"days": +1}
            self.shift_date(**args)
        elif habit_frequency in ["weekly"]:
            args = {"weeks": +1}
            self.shift_date(**args)
        elif habit_frequency in ["every other week"]:
            args = {"weeks": +2}
            self.shift_date(**args)
        elif habit_frequency in ["monthly"]:
            args = {"months": +1}
            self.shift_date(**args)
        elif habit_frequency in ["every other month"]:
            args = {"months": +2}
            self.shift_date(**args)
        elif habit_frequency in ["yearly"]:
            args = {"years": +1}
            self.shift_date(**args)

    def shift_date(self, **kwargs) -> None:
        """Shift date.

        :param kwargs:
        :return:
        """
        start_date = self.start_date[0]
        next_due = start_date.shift(**kwargs)
        self.next_due.append(next_due.format("YYYY-MM-DD"))

    def insert_new_habit(self) -> bool:
        """Insert a new habit into the database.

        :return:
        """
        try:
            with db.atomic():
                HabitDB.insert(
                    habit_name=self.habit_name,
                    start_date=self.start_date[0],
                    frequency=self.frequency[0],
                    next_due=self.next_due[0],
                ).execute()
            return True
        except peewee.IntegrityError:
            return False  # habit name already exists

    # ---------- Complete / Incomplete ----------

    def mark_complete_or_incomplete(self, str_name_or_id: str) -> None:
        """Main function for marking a habit as complete or incomplete.

        :param str_name_or_id: Either 'id' or 'name'
        :return: None
        """
        exists = self.check_if_exists(str_name_or_id=str_name_or_id)
        if not exists:
            self.doesnt_exist_response(str_name_or_id=str_name_or_id)
            return
        with db.atomic():
            if str_name_or_id == "id":
                HabitDB.update(completion=self.completion[0]).where(
                    HabitDB.id == self.id
                ).execute()
            elif str_name_or_id == "name":
                HabitDB.update(completion=self.completion[0]).where(
                    HabitDB.habit_name.contains(self.habit_name)
                ).execute()
        self.complete_incomplete_response()

    def complete_incomplete_response(self) -> None:
        """Perry-bot response after marking a habit.

        :return:
        """
        if True in self.completion:
            if self.habit_name:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Habit "
                    f"'{self.habit_name}' has been marked "
                    f"as complete.",
                    style="default",
                )
            if self.id:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Habit "
                    f"'{self.id}' has been marked as complete.",
                    style="default",
                )
        elif False in self.completion:
            if self.habit_name:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Habit "
                    f"'{self.habit_name}' has been marked "
                    f"as incomplete.",
                    style="default",
                )
            if self.id:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Habit "
                    f"'{self.id}' has been marked "
                    f"as incomplete.",
                    style="default",
                )

    def check_if_exists(self, str_name_or_id: str) -> typing.Union[bool, None]:
        """Check if habit name or id exists in database.

        :param str_name_or_id:
        :return:
        """
        if str_name_or_id == "id":
            exists = HabitDB.get_or_none(HabitDB.id == self.id)
            return exists
        if str_name_or_id == "name":
            exists = HabitDB.get_or_none(
                HabitDB.habit_name.contains(self.habit_name)
            )
            return exists
        return None

    def doesnt_exist_response(self, str_name_or_id: str) -> None:
        """Perry-bot response if habit doesn't exist.

        :param str_name_or_id:
        :return:
        """
        if str_name_or_id == "id":
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, "
                f"there is no habit "
                f"with the ID of '{self.id}'.",
                style="default",
            )
        elif str_name_or_id == "name":
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, "
                f"there is no "
                f"habit named '{self.habit_name}.",
                style="default",
            )
        return None
