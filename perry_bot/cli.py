"""Console script for perry_bot."""
import click
import datetime as dt
# skipcq
from perry_bot import main as pb


@click.group()
def main():
    """
    Perry Bot.

    Use `perry-bot [command] --help` to view options for the command.

    See documentation at
    https://perry-bot.readthedocs.io/en/latest/usage.html#cli-usage
    for further help.
    """
    return 0


@click.command(name='gui')
def start_gui():
    """Start GUI."""
    click.echo("Start GUI")


@click.command(name='log')
@click.argument('cups', type=int)
def log_water(cups):
    """
    Log cups of water drank.

    [CUPS] = Integer
    """
    click.echo(f"Number of cups to log: {cups}")
    return 0


@click.command(name='habit')
@click.option('-v', '--view', help='View existing habit and its status. Use `all` to view all habits.', is_flag=True)
@click.option('-c/-ic', '--complete/--incomplete', help='Mark habit as complete or incomplete.')
@click.option('-a', '--add', help='Add a habit.')
@click.option('-d', '--delete', help='Delete a habit.')
@click.argument('habit')
def log_habit(view, complete, add, delete, habit):
    """Log and manage habits."""
    click.echo(f"Habit = {habit}")
    click.echo(f"Complete = {complete}")
    click.echo(f"View = {view}")
    click.echo(f"Add = {add}")
    click.echo(f"Delete = {delete}")
    return 0


@click.command(name='viz')
@click.option('-o', '--on', type=dt.date, help='Show entries on this date.')
@click.option('-t', '--to', type=dt.date, help='Show entries before, or on, this date.')
@click.option('-m', '--month', type=dt.date, help='Show entries on this month of any year.')
@click.option('-y', '--year', type=dt.date, help='Show entries of a specific year.')
@click.option('-h', '--habit', help='Show entries of a specific habit.')
@click.argument('type')
def dataviz(from_, to, on, month, year, type_):
    """
    Visualize your water or habit records.

    If no date or date range is provided, the last 7 days will be shown.

    [TYPE] = `water` or `habit`
    """
    click.echo(f'From = {from_}')
    click.echo(f'To = {to}')
    click.echo(f'On = {on}')
    click.echo(f'Type = {type_}')
    click.echo(f'Month = {month}')
    click.echo(f'Year = {year}')
    return 0


main.add_command(start_gui)
main.add_command(log_water)
main.add_command(log_habit)
main.add_command(dataviz)
