"""Console script for perry_bot."""
import click
from click.exceptions import UsageError
import pendulum
# skipcq
from perry_bot import main as pb


@click.group()
def main():  # skipcq: FLK-D301, FLK-D400
    """
    \b
    Perry Bot.
    Use `perry-bot COMMAND --help` to view options for the command.

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
@click.option('-d', '--delete', help='Delete NUM cup(s) of water.', is_flag=True)
@click.option('-v', '--view', help='View cups of water drank.', is_flag=True)
@click.argument('cups', type=int)
def log_water(cups, delete):  # skipcq: FLK-D301, FLK-D400
    """
    Log cups of water drank.

    [CUPS] = Integer

    \f

    :param cups:
    :param delete:
    :return:
    """
    click.echo(f"Delete = {delete}")
    click.echo(f"Number of cups to log: {cups}")
    return 0


@click.command(name='mood')
@click.option('-v', '--view', help="View today's mood.", is_flag=True)
@click.option('-c', '--comment', help='Add a comment.')
@click.argument('rating')
def log_mood(rating, comment, view):  # skipcq: FLK-D301, FLK-D400
    """
    Rate your mood.

    [RATING] = Integer from 1 - 10. Use `all` to view today's mood.

    \f

    :param rating:
    :param comment:
    :param view:
    :return:
    """
    # TODO: Implement a check to make sure user has entered the correct number
    datetime = pendulum.now()
    click.echo(f"Datetime = {datetime}")
    click.echo(f"Rating = {rating}")
    click.echo(f"Comment = {comment}")
    if view and rating.isdigit():
        raise UsageError("The --view flag and a rating cannot be used together.")
    if view and rating.lower() == 'all':
        click.echo("Return today's mood.")


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
@click.option('-sd',
              '--start-date',
              help='Set the state date for weekly, bi-weekly, monthly, or yearly habits.',
              type=click.DateTime(formats=['%Y-%m-%d'])
              )
@click.argument('habit')
def log_habit(view, complete, add, delete, habit, start_date, edit, frequency):  # skipcq: FLK-D301, FLK-D400
    """
    Log and manage habits.

    Default frequency is set to daily.

    [HABIT] = Name of habit. Use `all` for all habits.

    \f

    :param frequency:
    :param edit:
    :param view:
    :param complete:
    :param add:
    :param delete:
    :param habit:
    :param start_date:
    :return:
    """
    click.echo(f"Habit = {habit}")
    click.echo(f"Complete = {complete}")
    click.echo(f"View = {view}")
    click.echo(f"Add = {add}")
    click.echo(f"Delete = {delete}")
    if add and delete:
        raise UsageError('The --add and --delete flags cannot be used together.')
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
# TODO: Month and year flags for comparison
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
def dataviz(from_, to, on, month, year, log_type, habit):  # skipcq: FLK-D301, FLK-D400
    """
    Visualize your water or habit records.

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
    click.echo(f'From = {from_}')
    click.echo(f'To = {to}')
    click.echo(f'On = {on}')
    click.echo(f'Type = {log_type}')
    click.echo(f'Month = {month}')
    click.echo(f'Year = {year}')
    if habit and log_type != 'habit':
        raise UsageError('The --habit option requires LOG_TYPE to be habit.')

    if log_type == 'water' and habit is True:
        raise UsageError("The --habit option cannot be used with `water`")
    return 0


main.add_command(start_gui)
main.add_command(log_water)
main.add_command(log_mood)
main.add_command(log_habit)
main.add_command(dataviz)


if __name__ == '__main__':
    main()
