"""Water dataclass."""
import typing

import attr
from rich.markup import escape
from rich.prompt import Prompt
from rich.table import Table

from perry_bot.class_helpers import EditExistingEntry
from perry_bot.console import Console, main_console
from perry_bot.db_models import WaterDB, db

console: Console = main_console()


@attr.s(kw_only=True, auto_attribs=True)
class Water:
    """Water dataclass."""

    id: list
    date_stamp: typing.List[str]
    cups_drank: typing.List[int]

    def query(self, date: str) -> None:
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

    def get_or_create_cups(self, date: str, cups: int) -> None:
        """Get existing record or create a new record of cups drank.

        :param date:
        :param cups:
        :return:
        """
        self.query(date=date)
        if self.id:
            with db:
                WaterDB.update(cups_drank=WaterDB.cups_drank + cups).where(
                    WaterDB.date_stamp.contains(date)
                ).execute()
        else:
            with db:
                WaterDB.insert(cups_drank=cups, date_stamp=date).execute()

        self.query(date=date)
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Water log added to "
            f"database.\n"
            f"[bold]{escape('[perry-bot]:')}[/bold] You've drunk "
            f"{self.cups_drank[-1]} cups of water today, "
            f"keep up the good work!",
            style="default",
        )

    def delete_cups(self, date: str, cups: int) -> None:
        """Delete num of cups from today's record.

        :param date:
        :param cups:
        :return:
        """
        self.query(date=date)
        if self.id:
            check_cups = self.check_cups_less_than_zero(date=date, cups=cups)
            if not check_cups:
                return
            with db:
                WaterDB.update(cups_drank=WaterDB.cups_drank - cups).where(
                    WaterDB.date_stamp.contains(date)
                ).execute()
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] {cups} cups deleted "
                f"from today's log.",
                style="default",
            )
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] You haven't recorded "
                f"any cups drank today yet, "
                f"there's nothing to delete!",
                style="default",
            )

    def check_cups_less_than_zero(self, date: str, cups: int) -> bool:
        """Check total number of cups.

        :param date:
        :param cups:
        :return:
        """
        total_cups = sum(self.cups_drank) - cups
        if total_cups < 0:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Deleting {cups} cups "
                f"will cause the total cups to be "
                f"less than zero ({sum(self.cups_drank) - cups})."
                f"\n[bold]{escape('[perry-bot]:')}[/bold] Reset today's cups "
                f"drank to 0?",
                style="default",
            )
            c = Prompt.ask(choices=["y", "n"], default="y")
            if c in ["y"]:
                with db:
                    WaterDB.update(cups_drank=0).where(
                        WaterDB.date_stamp.contains(date)
                    ).execute()
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Cups drank today "
                    f"reset to 0.",
                    style="default",
                )
                return False
            elif c in ["n"]:
                console.print(
                    f"[bold]{escape('[perry-bot]:')}[/bold] Deleting cups "
                    f"cancelled.",
                    style="default",
                )
                return False
        return True

    def view_total(self, date: str) -> None:
        """Return total cups in database.

        :param date:
        :return:
        """
        self.query(date=date)
        if self.id:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] "
                f"You've drunk {sum(self.cups_drank)} "
                f"cups of water on {date}.",
                style="default",
            )
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no "
                f"records "
                f"matching {date}. Try another date.",
                style="default",
            )

    def edit_cups(self, edit_date: str) -> None:
        """Edit number of cups drank in database.

        :param edit_date:
        :return:
        """
        self.query(date=edit_date)
        table = Table(title="Edit Water Records")
        table.add_column("#", justify="center")
        table.add_column("Date")
        table.add_column("Cups drank", justify="center")

        for (number, date, cups) in zip(
            self.id, self.date_stamp, self.cups_drank
        ):
            table.add_row(str(number), str(date), str(cups))
        if self.id:
            table.add_row(
                str(self.id[-1] + 1),
                "[b]Cancel Edit[/b]",
                "[b]----------[/b]",
                style="cancel",
            )
            setup_edit = EditExistingEntry(
                table=table,
                id=self.id,
                column_choices=["cups drank"],
                new_value="",
            )
            edit_target = EditExistingEntry.edit_table(setup_edit)
            if edit_target is False:
                return
            with db:
                WaterDB.update(cups_drank=edit_target[1]).where(
                    WaterDB.id == edit_target[2]
                ).execute()
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Your number of cups "
                f"drank has been updated.",
                style="default",
            )
        else:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Sorry, there are no "
                f"records "
                f"matching {edit_date}. Try another date.",
                style="default",
            )
