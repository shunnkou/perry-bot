"""Console script for perry_bot."""
import click
from click.exceptions import BadOptionUsage
import pendulum
# skipcq
from perry_bot import main as pb

# def validate_date(ctx, param, value):
#     pass
#
#
# def validate_delete(ctx, param, value):
#     pass


def validate_edit_habit(ctx, param, value):
    """
    Check that input is in the format of 'option, str' and that
    the option chosen is valid.
    """
    option_list = ['name', 'frequency', 'start date']
    try:
        option, habit_name = value.split(',')
        assert option in option_list
    except AssertionError:
        raise click.BadParameter(message="Value to change needs to be "
                                 "'name', 'frequency', or 'start date'.",
                                 param=param,
                                 ctx=ctx)
    except ValueError:
        raise click.BadParameter(message="Separate your option and your "
                                 "new habit name with a comma.",
                                 param=param,
                                 ctx=ctx)


@click.group()
@click.version_option(version='v0.1.0', prog_name='perry-bot')
def main():
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


@click.command(name='water')
@click.option('-a',
              '--add',
              help='Add NUM cup(s) of water',
              type=click.IntRange(1, None))
@click.option('-d',
              '--delete',
              help='Delete NUM cup(s) of water.',
              type=click.IntRange(1, None))
@click.option('-v',
              '--view',
              help='View cups of water drank.',
              type=click.DateTime(['%Y-%m-%d', '%Y-%m, %Y']))
@click.option('--start', help='Start water reminder.', is_flag=True)
@click.option('--stop', help='Stop water reminder.', is_flag=True)
@click.option('-e',
              '--edit',
              help='Edit water reminder schedule.',
              is_flag=True)
def log_water(add, delete, view, start, stop, edit):
    """
    \b
    Log cups of water drank.
    Get reminders to drink water.
    See the documentation for more information on scheduling reminders.

    \f

    :param edit:
    :param stop:
    :param start:
    :param view:
    :param add:
    :param delete:
    :return:
    """
    click.echo(f"Delete = {delete}")
    click.echo(f"Number of cups to log: {add}")

    return 0


@click.command(name='mood')
@click.option('-r',
              '--rating',
              help="Your mood's rating. A number from 1-10",
              type=click.IntRange(1, 10))
@click.option('-c', '--comment', help='Add a comment.', type=str)
@click.option('-v',
              '--view',
              help="View average mood.",
              type=click.DateTime(['%Y-%m-%d', '%Y-%m', '%Y']))
def log_mood(rating, comment, view):
    """
    Rate your mood.

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


@click.command(name='habit')
@click.option('-v',
              '--view',
              help='View existing habit(s) and its status.',
              is_flag=True)
@click.option('-c', '--complete', help='Mark habit as complete.')
@click.option('-ic', '--incomplete', help='Mark habit as incomplete')
@click.option('-a', '--add', help='Add a habit.')
@click.option('-d', '--delete', help='Delete a habit.')
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
    help='Set the start date for weekly, bi-weekly, monthly, or yearly habits.',
    type=click.DateTime(formats=['%Y-%m-%d']))
@click.option(
    '-e',
    '--edit',
    help="Edit a habit's name, frequency, start date. "
    "Separate your choice and the name (or number) of the habit with a comma.",
    nargs=2,
    callback=validate_edit_habit)
def log_habit(view, complete, incomplete, add, delete, start_date, edit,
              frequency):
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
    click.echo(f"Complete = {complete}")
    click.echo(f"View = {view}")
    click.echo(f"Add = {add}")
    click.echo(f"Delete = {delete}")
    click.echo(f"Edit = {edit[0]}, {edit[1]}")
    return 0


@click.command(name='viz')
@click.option('-o',
              '--on',
              type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m', '%Y']),
              help='Show records on this date.')
@click.option('-f',
              '--from',
              'from_',
              type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m', '%Y']),
              help='Show records after, or on, this date')
@click.option('-t',
              '--to',
              type=click.DateTime(formats=['%Y-%m-%d', '%Y-%m', '%Y']),
              help='Show records before, or on, this date.')
@click.option('-c',
              '--compare',
              help='Compare records. Separate values with a comma.',
              type=(click.DateTime(formats=['%Y-%m-%d', '%Y-%m', '%Y']),
                    click.DateTime(formats=['%Y-%m-%d', '%Y-%m', '%Y'])))
@click.option('-h', '--habit', help='Show records of a specific habit.')
@click.argument('log_type')
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
    click.echo(f'From = {from_}')
    click.echo(f'To = {to}')
    click.echo(f'On = {on}')
    click.echo(f'Type = {log_type}')
    click.echo(f'Month = {month}')
    click.echo(f'Year = {year}')
    if habit and log_type != 'habit':
        raise BadOptionUsage(message='LOG_TYPE must be habit.',
                             option_name='--habit')
    return 0


main.add_command(log_water)
main.add_command(log_mood)
main.add_command(log_habit)
main.add_command(dataviz)
