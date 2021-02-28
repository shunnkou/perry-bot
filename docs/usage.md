# Usage

<details><summary>Table of Contents</summary>
<p>

- [](#track-and-manage-water)

  - [](#log-a-cup-of-water)
  - [](#delete-a-cup)
  - [](#view-your-cups-drank)

- [](#track-mood)

  - [](#add-a-comment)

- [](#track-and-manage-habits)

  - [](#add-a-habit)
  - [](#view-habits)
  - [](#delete-a-habit)
  - [](#schedule-a-habit)
  - [](#edit-a-habit)

- [](#visualize-your-data)

  - [](#compare-data-from-two-dates)

- [](#date-formats)

- [](#full-list-of-commands-and-options)

  - [](#habit-options)
  - [](#mood-options)
  - [](#data-visualization-options)
  - [](#water-options)

</p>
</details>

## Track and manage water

Use the `water` command:

```console
perry-bot water [OPTIONS]
```

### Log a cup of water

To log cups of water drank, use the `-a` or `--add` option.
For example, to log 1 bottle/cup of water:

```console
perry-bot water -a 1
```

### Delete a cup

If you made a mistake and want to remove a log, use `-d` or `--delete`.
For example, to delete 1 bottle/cup of water:

```console
perry-bot water --delete 1
```

### View your cups drank

To view the number of cups you've drunk, use `-v` or `--view` and a date:

```console
perry-bot water --view 2021-02-05
```

## Track mood

Use the `mood` command:

```console
perry-bot mood [OPTIONS]
```

Use the `-r` or `--rating` option and rate your mood on a scale from 1 to 10:

```console
perry-bot mood -r 6
```

### Add a comment

To add a comment/explanation for your mood, use the `-c` or `--comment` option:

```console
perry-bot -c 'Failed an exam today...' -r 3
```

## Track and manage habits

Use the `habit` command:

```console
perry-bot habit [OPTIONS]
```

If the habit is more than one word, enclose it in quotes.

Once your habit has been created, you can refer to it with its number for quicker inputs.

### Add a habit

To add a habit, use the `-a` or `--add` option.
For example, to add a habit called 'Water plants':

```console
perry-bot habit -a 'Water plants'
```

Habit names must be **unique**. Creation will fail if the name isn't unique.

:::{note}
The `--add` option is also used to specify the name (or number) of a habit when you want to [edit](#edit-a-habit) it.
:::

### View habits

To view your habits existing habits, use the `-v` or `--view` option:

```console
perry-bot habit -v
```

### Delete a habit

To delete a habit, use the `-d` or `--delete` option.
For example, to delete a habit called 'Water plants':

```console
perry-bot habit -d 'Water plants'
```

### Schedule a habit

If you want to repeat a habit on a specific day, use the `-sd`, or `--start-date` option.
For example, to schedule 'Water plants' to repeat bi-weekly:

```console
perry-bot -f bi-weekly -sd 2021-02-18 -a 'Water plants'
```

If no frequency is specified, the default is daily.

### Edit a habit

To edit a habit, use the `-e` or `--edit` option with the target to edit,
`name`, `frequency`, or `start date`, and the name or number of the habit
separated by a comma.

To change the name of a habit, remember to add the name or number of the original habit with `-a`:

```console
perry-bot habit -e 'name,Water plants!' -a 'Water plants'
```

To change the frequency of a habit to weekly:

```console
perry-bot habit -e 'frequency,Water plants!' -f weekly
```

To change the start date of a habit:

```console
perry-bot habit -e 'start date,Water plants!' -sd 2021-02-14
```

## Visualize your data

Use the `viz` command where `LOG_TYPE` is either `habit` or `water`:

```console
perry-bot viz [OPTIONS] [LOG_TYPE]
```

If no date range is provided, the last 7 days will be shown.
For example, to see data for the last 7 days:

```console
perry-bot viz water
    perry-bot viz habit
    perry-bot viz mood
```

To see data on a specific day:

```console
perry-bot viz --on 2021-02-03 water
```

:::{attention}
When visualizing `habit`, the date must be a year (`2021`) or a month (`2021-02`), not a day.
:::

To see data in a specific date range:

```console
perry-bot viz --from 2021-01-02 --to 2021-02-02 mood
```

### Compare data from two dates

Use the `--compare` option and separate your dates with a comma.

To compare days:

```console
perry-bot viz --compare '2021-02-02,2021-02-05' water
```

To compare months:

```console
perry-bot viz --compare '2021-01,2021-02' habit
```

To compare years:

```console
perry-bot viz --compare '2020,2021' mood
```

````{margin}
```{note}
Basically, everything is in the format of 'Year-Month-Date'
```
````

## Date Formats

| Command | Option                | Accepted Format                                 | Example                                                     |
| ------- | --------------------- | ----------------------------------------------- | ----------------------------------------------------------- |
| `habit` | `-sd`, `--start-date` | %Y-%m-%d                                        | 2021-03-01                                                  |
| `water` | `-v`, `--view`        | x%Y-%m-%d<br>%Y-%m<br>%Y                        | 2021-02-04<br>2021-02<br>2021                               |
| `viz`   | `-o`, `--on`          | %Y-%m-%d                                        | 2021-12-11                                                  |
| `viz`   | `-f`, `--from`        | %Y-%m-%d                                        | 2021-12-11                                                  |
| `viz`   | `-t`, `--to`          | %Y-%m-%d                                        | 2021-12-11                                                  |
| `viz`   | `-c`, `--compare`     | '%Y-%m-%d,%Y-%m-%d'<br>'%Y-%m,%Y-%m'<br>'%Y,%Y' | '2021-02-04,2021-02,05'<br>'2021-02,2021-01'<br>'2021,2020' |

## Full list of commands and options

To see a full list of commands, type `perry-bot --help`

```console
Usage: perry-bot [OPTIONS] COMMAND [ARGS]...

  Perry Bot.
  Use `perry-bot COMMAND --help` to view options for the command.

  See documentation at
  https://perry-bot.readthedocs.io/en/latest/usage.html
  for further help.

Options:
  --help  Show this message and exit.

Commands:
  habit  Log and manage habits.
  mood   Rate your mood.
  viz    Visualize your records.
  water  Log cups of water drank.
```

### Habit options

```
Usage: perry-bot habit [OPTIONS]

  Log and manage habits.
  Default frequency is set to daily.

  Tip: The number of the habit can be used instead of its name.

Options:
  -v, --view                      View existing habit(s) and its status.
  -c, --complete TEXT             Mark habit as complete.
  -ic, --incomplete TEXT          Mark habit as incomplete
  -a, --add TEXT                  Add a habit.
  -d, --delete TEXT               Delete a habit.

  -f, --frequency [Daily|Bi-Weekly|Weekly|Monthly|Yearly]
                                  Frequency of the habit.

  -sd, --start-date [%Y-%m-%d]    Set the start date for weekly, bi-weekly,
                                  monthly, or yearly habits.

  -e, --edit TEXT...              Edit a habit's name, frequency, start date.
                                  Separate your choice and the name (or number)
                                  of the habit with a comma.

  --help                          Show this message and exit.
```

### Mood options

```
Usage: perry-bot mood [OPTIONS]

  Rate your mood.

Options:
  -r, --rating INTEGER RANGE      Your mood's rating. A number from 1-10
  -c, --comment TEXT              Add a comment.
  -v, --view [%Y-%m-%d|%Y-%m|%Y]  View average mood.
  --help                          Show this message and exit.
```

### Data visualization options

```console
Usage: perry-bot viz [OPTIONS] LOG_TYPE

  Visualize your records.

  If no date or date range is provided, the last 7 days will be shown. See
  documentation for date formatting.

  [LOG_TYPE] = `water` or `mood` or `habit`

Options:
  -o, --on [%Y-%m-%d|%Y-%m|%Y]    Show records on this date.
  -f, --from [%Y-%m-%d|%Y-%m|%Y]  Show records after, or on, this date
  -t, --to [%Y-%m-%d|%Y-%m|%Y]    Show records before, or on, this date.
  -c, --compare <DATETIME DATETIME>...
                                  Compare records. Separate values with a
                                  comma.

  -h, --habit TEXT                Show records of a specific habit.
  --help                          Show this message and exit.
```

### Water options

```console
Usage: perry-bot water [OPTIONS]

  Log cups of water drank.
  Get reminders to drink water.
  See the documentation for more information on scheduling reminders.

Options:
  -a, --add INTEGER RANGE         Add NUM cup(s) of water
  -d, --delete INTEGER RANGE      Delete NUM cup(s) of water.
  -v, --view [%Y-%m-%d|%Y-%m, %Y]
                                  View cups of water drank.
  --start                         Start water reminder.
  --stop                          Stop water reminder.
  -e, --edit                      Edit water reminder schedule.
  --help                          Show this message and exit.
```
