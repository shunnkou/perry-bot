"""Helper classes."""

import attr
from rich.markup import escape
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
import typing

from perry_bot.console import Console, main_console

console: Console = main_console()


@attr.s()
class EditExistingEntry:
    """Edit an existing entry."""

    table: Table = attr.ib()
    id: typing.List[int] = attr.ib()
    column_choices: typing.List[str] = attr.ib()
    new_value: typing.Union[str, int] = attr.ib()
    number_to_edit: int = attr.Factory(int)
    column_to_edit: str = attr.Factory(str)
    max_row: int = attr.ib(default=20)

    def edit_table(self):
        """Main function."""
        length = self.check_length
        if not length:
            return False
        console.print(self.table, style="default")
        cancel_edit = self.get_num_to_edit()
        if not cancel_edit:
            return False
        self.get_column_to_edit()
        return self.column_to_edit, self.new_value, self.number_to_edit

    def check_length(self) -> bool:
        """Check number of rows in table.

        :return:
        """
        if len(self.table.rows) < self.max_row:
            return True
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] The table has more "
            f"than 20 rows. Would you like to continue editing your "
            f"records on this date?",
            style="default",
        )
        q = Prompt.ask(choices=["y", "n"], default="y")
        if q in ["n"]:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] --edit cancelled.",
                style="default",
            )
            return False
        return True

    def check_cancel_edit(self, num) -> bool:
        """Check if user cancels edit.

        :param num:
        :return:
        """
        cancel_number: int = self.id[-1] + 1
        if num == cancel_number:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Editing cancelled!",
                style="default",
            )
            return False
        return True

    def wrong_num_loop(self, num: int) -> bool:
        """Loop while user enters a number that doesn't exist.

        :param num:
        :return:
        """
        check_cancel = self.check_cancel_edit(num=num)
        if not check_cancel:
            return False
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Please enter "
            f"a valid number from the table",
            style="default",
        )
        num_again = IntPrompt.ask()
        check_cancel_again = self.check_cancel_edit(num=num_again)
        if not check_cancel_again:
            return False
        if num_again in self.id:
            self.number_to_edit = num_again
            return True
        return False

    def get_num_to_edit(self):
        """Get the number user wants to edit.

        :return:
        """
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Enter the number of "
            f"the entry you want to edit.",
            style="default",
        )
        num = IntPrompt.ask()
        while num not in self.id:
            wrong_id = self.wrong_num_loop(num=num)
            if self.number_to_edit in self.id:
                break
            if not wrong_id:
                return False
        self.number_to_edit = num
        return True

    def get_new_value(self):
        """Get the new value.

        :return:
        """
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Enter the new value",
            style="default",
        )
        if (
            len(self.column_choices) == 2
            and self.column_to_edit in self.column_choices[1]
        ):
            self.new_value = Prompt.ask()
        elif (
            len(self.column_choices) == 2
            and self.column_to_edit in self.column_choices[0]
            or len(self.column_choices) == 1
        ):
            self.new_value = IntPrompt.ask()

    def check_new_value(self):
        """Check new value is valid for their column.

        :return:
        """
        if (
            self.column_to_edit.lower() == "rating"
            and self.new_value not in range(1, 11)
        ):
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] The mood rating has "
                f"to be between 1 and 10.",
                style="default",
            )
            return False
        if self.column_to_edit.lower() == "cups drank" and self.new_value < 0:
            console.print(
                f"[bold]{escape('[perry-bot]:')}[/bold] Cups drank cannot be "
                f"below 0.",
                style="default",
            )
            return False
        return True

    def get_column_to_edit(self):
        """Get the column to edit.

        :return:
        """
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] Which category would "
            f"you like to edit?",
            style="default",
        )
        self.column_to_edit = Prompt.ask(
            choices=self.column_choices, default=self.column_choices[0]
        )
        self.get_new_value()
        check_value = self.check_new_value()
        while check_value is False:
            self.get_new_value()
            check_value_again = self.check_new_value()
            if check_value_again:
                break
        self.check_edit_target_and_value()

    def check_edit_target_and_value(self):
        """Check user has inputted everything correctly.

        :return:
        """
        console.print(
            f"[bold]{escape('[perry-bot]:')}[/bold] You would like to "
            f"change the {self.column_to_edit} for entry "
            f"#{self.number_to_edit} to '{self.new_value}'. Correct?",
            style="default",
        )
        check = Prompt.ask(choices=["y", "n"], default=["y"])
        if check in ["n"]:
            self.get_column_to_edit()
