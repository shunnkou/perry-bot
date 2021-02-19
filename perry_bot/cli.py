"""Console script for perry_bot."""
import click
# skipcq
from perry_bot import main as pb


@click.group()
def main():
    """
    \b
    Perry Bot.
    Use `perry-bot [command] --help` to view options for the command.

    \b
    See documentation at
    https://perry-bot.readthedocs.io/en/latest/usage.html#cli-usage
    for further help.
    """
    return 0


@click.command(name='gui')
def start_gui():
    """Start GUI."""
    click.echo("Start GUI")


@click.command(name='water')
@click.option('-d', '--delete', help='Delete # cup(s) of water.', is_flag=True)
@click.option('-v', '--view', help='View cups of water drank.', is_flag=True)
@click.argument('cups', type=int)
def log_water(cups, delete):
    """
    Log cups of water drank.

    [CUPS] = Integer
    """
    click.echo(f"Delete = {delete}")
    click.echo(f"Number of cups to log: {cups}")
    return 0


@click.command(name='habit')
@click.option('-v',
              '--view',
              help='View existing habit and its status.',
              is_flag=True)
@click.option('-c/-ic',
              '--complete/--incomplete',
              help='Mark habit as complete or incomplete.')
@click.option('-a', '--add', help='Add a habit.', is_flag=True)
@click.option('-d', '--delete', help='Delete a habit.', is_flag=True)
@click.option('-e',
              '--edit',
              help='Edit a habit',
              is_flag=True,
              type=click.Choice(['Name', 'Frequency', 'Start date'],
                                case_sensitive=False))
@click.option('-f',
              '--frequency',
              help='Frequency of the habit.',
              type=click.Choice(
                  ['Daily', 'Bi-Weekly', 'Weekly', 'Monthly', 'Yearly'],
                  case_sensitive=False),
              default='Daily')
@click.option(
    '-sd',
    '--start-date',
    help='Set the state date for weekly, bi-weekly, monthly, or yearly habits.',
    type=click.DateTime(formats=['%Y-%m-%d']),
)
@click.argument('habit')
def log_habit(view, complete, add, delete, habit, start_date):
    """
    Log and manage habits.

    Default frequency is set to daily.

    [HABIT] = Name of habit. Use `all` for all habits.
    """
    click.echo(f"Habit = {habit}")
    click.echo(f"Complete = {complete}")
    click.echo(f"View = {view}")
    click.echo(f"Add = {add}")
    click.echo(f"Delete = {delete}")
    return 0


@click.command(name='viz')
@click.option('-o',
              '--on',
              type=click.DateTime(formats=['%Y-%m-%d']),
              help='Show entries on this date.')
@click.option('-f',
              '--from',
              'from_',
              type=click.DateTime(formats=['%Y-%m-%d']),
              help='Show entries after, or on, this date')
@click.option('-t',
              '--to',
              type=click.DateTime(formats=['%Y-%m-%d']),
              help='Show entries before, or on, this date.')
@click.option('-m',
              '--month',
              type=click.DateTime(formats=['%m', '%b', '%B']),
              help='Show entries on this month of any year.')
@click.option('-y',
              '--year',
              type=click.DateTime(formats=['%Y', '%y']),
              help='Show entries of a specific year.')
@click.option('-h', '--habit', help='Show entries of a specific habit.')
@click.argument('log_type')
def dataviz(from_, to, on, month, year, log_type, habit):
    """
    Visualize your water or habit records.

    If no date or date range is provided, the last 7 days will be shown.
    See documentation for date formatting.

    [LOG_TYPE] = `water` or `habit`
    """
    click.echo(f'From = {from_}')
    click.echo(f'To = {to}')
    click.echo(f'On = {on}')
    click.echo(f'Type = {log_type}')
    click.echo(f'Month = {month}')
    click.echo(f'Year = {year}')

    if log_type == 'water' and habit is True:
        click.echo("The --habit option cannot be used with `water`")
    return 0


main.add_command(start_gui)
main.add_command(log_water)
main.add_command(log_habit)
main.add_command(dataviz)
