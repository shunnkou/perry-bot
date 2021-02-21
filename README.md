# Perry Bot

[![Documentation Status](https://readthedocs.org/projects/perry-bot/badge/?version=develop)](https://perry-bot.readthedocs.io/en/develop/?badge=develop)
[![CodeFactor](https://www.codefactor.io/repository/github/shunnkou/perry-bot/badge)](https://www.codefactor.io/repository/github/shunnkou/perry-bot)
[![DeepSource](https://deepsource.io/gh/shunnkou/perry-bot.svg/?label=active+issues)](https://deepsource.io/gh/shunnkou/perry-bot/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/shunnkou/perry-bot.svg/?label=resolved+issues)](https://deepsource.io/gh/shunnkou/perry-bot/?ref=repository-badge)

A self-care bot.

* Free software: GPL-3.0 license
* Documentation: https://perry-bot.readthedocs.io.

# Under active development, not functional yet


## Features
* CLI and GUI
* Trackers
  * Water tracker
  * Mood tracker
  * Habit tracker
    * Daily, weekly, bi-weekly, monthly, and yearly habits
* Water reminders
* Visualize your tracked data
* [You feel like sh*t's](https://youfeellikeshit.com/) interactive self-care
* Local data storage with a SQLite database


## Installation
Install using pipx:

```shell
pipx install perry-bot
```

## Usage
* See a list of commands
  * `perry-bot --help`
* See options and help for a specific command
  * `perry-bot [COMMAND] --help`
### GUI
Start the GUI with:
```
perry-bot gui
```

### CLI Commands
See more commands and information in the [docs](https://perry-bot.readthedocs.io/en/latest/usage.html#cli-usage).

#### Water
```
perry-bot water [OPTIONS] ARG
```

#### Mood
```
perry-bot mood [OPTIONS] ARG
```

#### Habit
```
perry-bot habit [OPTIONS] HABIT
```

#### Data visualization
```
perry-bot viz [OPTIONS] LOG_TYPE
```

#### You feel like sh*t
```
perry-bot yfls [OPTIONS]
```


## Credits
This package was created based on a modified
[audreyr/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
project template using [Cookiecutter](https://github.com/cookiecutter/cookiecutter).
