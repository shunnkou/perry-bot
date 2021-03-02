"""Console script for perry_bot."""

import click
from click.exceptions import BadOptionUsage
import arrow
import re
from perry_bot import backend as be


def validate_edit_habit(ctx, param, value):
    """Check input is in the correct format.

     Format = 'option, str'

    :param ctx:
    :param param:
    :param value:
    :return:
    """
    # TODO: Switch this to something like validate_date()
    check_comma = re.search(",", value)
    if check_comma:
        option, habit_name = value.split(",")
        check_option = re.search("name|frequency|start date", value)
        if check_option:
            return option, habit_name
        raise click.BadParameter(
            message="The value to change needs to be "
            "'name', 'frequency', or 'start date'."
        )
    raise click.BadParameter(
        message="Separate your option and your new habit name with a comma.",
        param=param,
        ctx=ctx,
    )


def validate_date(value: str) -> str:
    """Check date is in the correct format.

    :param value:
    :return:
    """
    valid_strings = ["today"]
    view_year = re.match(r"\d{4}", value)
    view_month = re.match(r"\d{4}-\d{2}", value)
    view_day = re.match(r"\d{4}-\d{2}-\d{2}", value)

    if view_year:
        return value
    if view_month:
        return value
    if view_day:
        return value
    if value.lower() == valid_strings[0]:
        return str(arrow.now("local").format("YYYY-MM-DD"))
    raise click.BadParameter(
        message="Date is incorrectly formatted. "
        "Accepted formats = YYYY-MM-DD, YYYY-MM, YYYY, today."
    )


@click.group()
@click.version_option(version="v0.1.0", prog_name="perry-bot")
def cli():
    """
    \b
    Perry Bot - a commandline self-care tracker bot.
    Use `perry-bot COMMAND --help` to view options for the command.

    \b
    See documentation at
    https://perry-bot.readthedocs.io/en/latest/usage.html
    for further help.
    """
    return 0


@click.command(name="water")
@click.option(
    "-a",
    "--add",
    help="Add NUM cup(s) of water to today's log",
    type=click.IntRange(1, None),
)
@click.option(
    "-d",
    "--delete",
    help="Delete NUM cup(s) of water from today's log.",
    type=click.IntRange(1, None),
)
@click.option(
    "-v", "--view", help="View cups of water drank on the given " "date."
)
@click.option(
    "-e", "--edit", help="Edit cups of water drank on the given " "date."
)
def log_water(add, delete, view, edit):
    """
    \b
    Log cups of water drank.
    Get reminders to drink water.
    See the documentation for more information on scheduling reminders.

    \f

    :param edit:
    :param view:
    :param add:
    :param delete:
    :return:
    """
    dt = arrow.now("local").format("YYYY-MM-DD")

    if add:
        new_record = be.Water(id=[], cups_drank=[], date_stamp=[])
        be.Water.get_or_create_cups(new_record, date=dt, cups=add)
    if delete:
        delete_cups = be.Water(id=[], cups_drank=[], date_stamp=[])
        be.Water.delete_cups(delete_cups, date=dt, cups=delete)
    if view:
        date = validate_date(view)
        view_date = be.Water(id=[], cups_drank=[], date_stamp=[])
        be.Water.view_total(view_date, date=date)
    if edit:
        edit_date = validate_date(edit)
        edit_model = be.Water(id=[], cups_drank=[], date_stamp=[])
        be.Water.edit_cups(edit_model, edit_date=edit_date)


@click.command(name="mood")
@click.option(
    "-r",
    "--rating",
    help="Your mood's rating. A number from 1-10",
    type=click.IntRange(1, 10),
)
@click.option("-c", "--comment", help="Add a comment.", type=str)
@click.option(
    "-av", "--average", help="View your average" " mood on a given date."
)
@click.option(
    "-vt",
    "--view-table",
    help="View a table of your mood and comments on a given date.",
)
@click.option(
    "-e", "--edit", help="Edit a mood rating or " "comment on a given date."
)
def log_mood(rating, comment, average, edit, view_table):
    """
    Rate your mood.

    \f

    :param view_table:
    :param edit:
    :param rating:
    :param comment:
    :param average:
    :return:
    """
    datetime = arrow.now("local").format("YYYY-MM-DD HH-mm-ss")
    if rating:
        new_entry = be.Mood(
            id=[], rating=rating, comment=comment, datetime_stamp=datetime
        )
        be.Mood.new_entry(new_entry)
    if average:
        view_option = validate_date(value=average)
        mood = be.Mood(id=[], rating=[], datetime_stamp=[], comment=[])
        be.Mood.view_average_mood(mood, view_date=view_option)
    if view_table:
        date_option = validate_date(value=view_table)
        table = be.Mood(id=[], rating=[], datetime_stamp=[], comment=[])
        be.Mood.view_mood_table(table, view_date=date_option)
    if edit:
        edit_date = validate_date(value=edit)
        edit_mood = be.Mood(id=[], rating=[], datetime_stamp=[], comment=[])
        be.Mood.edit_mood(edit_mood, edit_date=edit_date)


@click.command(name="habit")
@click.option(
    "-v", "--view", help="View existing habit(s) and its status.", is_flag=True
)
@click.option("-c", "--complete", help="Mark habit as complete.")
@click.option("-ic", "--incomplete", help="Mark habit as incomplete")
@click.option("-a", "--add", help="Add a habit.")
@click.option("-d", "--delete", help="Delete a habit.")
@click.option(
    "-f",
    "--frequency",
    help="Frequency of the habit.",
    type=click.Choice(
        ["Daily", "Bi-Weekly", "Weekly", "Monthly", "Yearly"],
        case_sensitive=False,
    ),
    default="Daily",
)
@click.option(
    "-sd",
    "--start-date",
    help="Set the start date for weekly, bi-weekly, "
    "monthly, or yearly habits.",
    type=click.DateTime(formats=["%Y-%m-%d"]),
)
@click.option(
    "-e",
    "--edit",
    help="Edit a habit's name, frequency, start date. "
    "Separate your choice and the name (or number) of the habit with a comma.",
    nargs=2,
    callback=validate_edit_habit,
)
def log_habit(
    view, complete, incomplete, add, delete, start_date, edit, frequency
):
    """
    \b
    Log and manage habits.
    Default frequency is set to daily.

    Tip: The number of the habit can be used instead of its name.

    \f

    :param incomplete:
    :param frequency:
    :param edit:
    :param view:
    :param complete:
    :param add:
    :param delete:
    :param start_date:
    :return:
    """
    # If editing name, the `-a` option has to be supplied as well
    click.echo(f"Complete = {complete}")
    click.echo(f"View = {view}")
    click.echo(f"Add = {add}")
    click.echo(f"Delete = {delete}")
    click.echo(f"Edit = {edit[0]}, {edit[1]}")
    return 0


@click.command(name="viz")
@click.option(
    "-o",
    "--on",
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m", "%Y"]),
    help="Show records on this date.",
)
@click.option(
    "-f",
    "--from",
    "from_",
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m", "%Y"]),
    help="Show records after, or on, this date",
)
@click.option(
    "-t",
    "--to",
    type=click.DateTime(formats=["%Y-%m-%d", "%Y-%m", "%Y"]),
    help="Show records before, or on, this date.",
)
@click.option(
    "-c",
    "--compare",
    help="Compare records. Separate values with a comma.",
    type=(
        click.DateTime(formats=["%Y-%m-%d", "%Y-%m", "%Y"]),
        click.DateTime(formats=["%Y-%m-%d", "%Y-%m", "%Y"]),
    ),
)
@click.option("-h", "--habit", help="Show records of a specific habit.")
@click.argument("log_type")
def dataviz(from_, to, on, month, year, log_type, habit):
    """
    Visualize your records.

    If no date or date range is provided, the last 7 days will be shown.
    See documentation for date formatting.

    [LOG_TYPE] = `water` or `mood` or `habit`

    \f

    :param from_:
    :param to:
    :param on:
    :param month:
    :param year:
    :param log_type:
    :param habit:
    :return:
    """
    click.echo(f"From = {from_}")
    click.echo(f"To = {to}")
    click.echo(f"On = {on}")
    click.echo(f"Type = {log_type}")
    click.echo(f"Month = {month}")
    click.echo(f"Year = {year}")
    if habit and log_type != "habit":
        raise BadOptionUsage(
            message="LOG_TYPE must be habit if the habit flag is used.",
            option_name="--habit",
        )
    return 0


cli.add_command(log_water)
cli.add_command(log_mood)
cli.add_command(log_habit)
cli.add_command(dataviz)
