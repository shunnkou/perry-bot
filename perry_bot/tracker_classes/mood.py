"""Mood dataclass."""
import typing

import attr
from rich.markup import escape
from rich.prompt import Prompt
from rich.table import Table

from perry_bot.class_helpers import EditExistingEntry
from perry_bot.console import Console, main_console
from perry_bot.db_models import MoodDB, db

console: Console = main_console()


@attr.s(kw_only=True, auto_attribs=True)
class Mood:
    """Mood dataclass."""

    id: typing.List[int]
    rating: typing.Any
    datetime_stamp: typing.Any
    comment: typing.Any

    def query(self, date: str) -> None:
        """Query database and append data to self.

        :param date:
        :return:
        """
        with db.atomic():
            query = MoodDB.select().where(MoodDB.datetime_stamp.contains(date))
            for record in query:
                self.id.append(record.id)
                self.rating.append(record.rating)
                self.datetime_stamp.append(record.datetime_stamp)
                self.comment.append(record.comment)

    def make_table(self, title: str) -> Table:
        """Create 'Mood' table.

        :param title:
        :return:
        """
        table = Table(title=title)
        table.add_column("#", justify="center")
        table.add_column("Datetime stamp", justify="center")
        table.add_column("Rating", justify="center")
        table.add_column("Comment", justify="center")

        for (number, date, rate, comment) in zip(
            self.id, self.datetime_stamp, self.rating, self.comment
        ):
            table.add_row(str(number), str(date), str(rate), str(comment))

        return table

    def new_entry(self) -> None:
        """Create a new entry in the database.

        :return:
        """
        with db.atomic():
            MoodDB.insert(
                rating=self.rating,
                datetime_stamp=self.datetime_stamp,
                comment=self.comment,
            ).execute()
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Mood entry added to "
            f"database.",
            style="default",
        )

    def view_average_mood(self, view_date: str) -> None:
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
                style="default",
            )
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no "
                f"records matching {view_date}. Try another date.",
                style="default",
            )

    def view_mood_table(self, view_date: str) -> None:
        """Print a mood table given a date.

        :param view_date:
        :return:
        """
        self.query(date=view_date)
        table = self.make_table(title="Mood Records")
        if self.id:
            check_long_table = self.long_table_confirmation
            if not check_long_table:
                return
            console.print(table, style="default")
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"Sorry, there are no records "
                f"matching {view_date}. Try another date.",
                style="default",
            )

    @staticmethod
    def long_table_confirmation(table: Table) -> bool:
        """Check max table length.

        :param table:
        :return:
        """
        max_table_length = len(table.rows)
        if max_table_length < 20:
            return True
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] The table has more "
            f"than 20 rows. Would you like to continue displaying the table?",
            style="default",
        )
        q = Prompt.ask(choices=["y", "n"], default=["y"])
        if q in ["n"]:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"--view-table cancelled.",
                style="default",
            )
            return False
        return True

    def edit_mood(self, edit_date: str) -> None:
        """Edit a specific mood rating.

        Based on a date by inputting the number of the rating.

        :param edit_date:
        :return:
        """
        self.query(date=edit_date)
        table = self.make_table(title="Edit a Mood Rating")
        if self.id:
            table.add_row(
                str(self.id[-1] + 1),
                "[b]----------[/b]",
                "[b]Cancel Edit[/b]",
                "[b]----------[/b]",
                style="cancel",
            )
            setup_edit = EditExistingEntry(
                table=table,
                id=self.id,
                column_choices=["rating", "comment"],
                new_value="",
            )
            edit_target = EditExistingEntry.edit_table(setup_edit)
            if not edit_target:
                return
            if edit_target[0] in ["rating"]:
                with db.atomic():
                    MoodDB.update(rating=edit_target[1]).where(
                        MoodDB.id == edit_target[2]
                    ).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your rating has "
                    f"been updated.",
                    style="default",
                )
            elif edit_target[0] in ["comment"]:
                with db.atomic():
                    MoodDB.update(comment=edit_target[1]).where(
                        MoodDB.id == edit_target[2]
                    ).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Your comment has "
                    f"been updated.",
                    style="default",
                )

        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no "
                f"records matching {edit_date}. "
                f"Try another date.",
                style="default",
            )
