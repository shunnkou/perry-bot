# Perry Bot

[![Documentation Status](https://readthedocs.org/projects/perry-bot/badge/?version=develop)](https://perry-bot.readthedocs.io/en/develop/?badge=develop)
[![CodeFactor](https://www.codefactor.io/repository/github/shunnkou/perry-bot/badge)](https://www.codefactor.io/repository/github/shunnkou/perry-bot)
[![DeepSource](https://deepsource.io/gh/shunnkou/perry-bot.svg/?label=active+issues)](https://deepsource.io/gh/shunnkou/perry-bot/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/shunnkou/perry-bot.svg/?label=resolved+issues)](https://deepsource.io/gh/shunnkou/perry-bot/?ref=repository-badge)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

A commandline self-care bot.

* Free software: GPL-3.0 license
* Documentation: https://perry-bot.readthedocs.io/en/develop/.

# Under active development, not functional yet


## Features
* Commandline dashboard
* Trackers
  * Water tracker
  * Mood tracker
  * Habit tracker that allows you to schedule habits as daily, weekly, bi-weekly, monthly, or yearly habits
* Visualize your tracked data with matplotlib graphs
* Local data storage with a SQLite database


## Installation
Install using pipx:

```shell
$ pipx install perry-bot
```

## Quickstart
* See a list of commands
  * `perry-bot --help`
* See options and help for a specific command
  * `perry-bot [COMMAND] --help`

### Commands
See more information about each command's options in the
[usage](docs/usage.md#Usage) section
of the docs.

#### Water
```
perry-bot water [OPTIONS]
```

#### Mood
```
perry-bot mood [OPTIONS]
```

#### Habit
```
perry-bot habit [OPTIONS]
```

#### Data visualization
```
perry-bot viz [OPTIONS] LOG_TYPE
```


## Credits
See [credits](AUTHORS.md#credits).
