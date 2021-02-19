=====
Usage
=====

GUI Usage
---------

Start Perry Bot's GUI with:

.. code-block:: shell

    $ perry-bot gui



* TODO



CLI Usage
---------

Track and manage habits
^^^^^^^^^^^^^^^^^^^^^^^

Use the ``habit`` command:

.. code-block:: shell

    $ perry-bot habit [OPTIONS] [HABIT]

If the habit is more than one word, enclose it in quotes.


Add a habit
"""""""""""

| To add a habit, use the ``-a`` or ``--add`` command.
| For example, to add a habit called "Water plants":

.. code-block::

    $ perry-bot habit -a "Water plants"


Delete a habit
""""""""""""""

| To delete a habit, use the ``-d`` or ``--delete`` command.
| For example, to delete a habit called "Water plants":

.. code-block::

    $ perry-bot habit -d "Water plants"



Schedule a habit
""""""""""""""""

| If you want to repeat a habit on a specific day, use the ``-sd``, or ``--start-date`` command.
| For example, to schedule "Water plants" to repeat bi-weekly:

.. code-block:: shell

    $ perry-bot -a -f bi-weekly -sd 2021-02-18 "Water plants"


If no frequency is specified, the default is daily.


Edit a habit
""""""""""""

| If you've made a mistake while creating a habit or just want to edit a habit, use the ``-e`` or ``--edit`` option
  along with the target to edit - ``Name``, ``Frequency``, or ``"Start date"``
| For example, to change the name of a habit:

.. code-block::

    $ perry-bot habit -e name "Water plants!!!"


To change the frequency of a habit to weekly:

.. code-block::

    $ perry-bot habit -e frequency -f weekly "Water plants!!!"


To change the start date of a habit:

.. code-block::

    $ perry-bot habit -e "start date" -sd 2021-02-14


Track your water intake
^^^^^^^^^^^^^^^^^^^^^^^

Use the ``water`` command where ``CUPS`` is the number of cups you want to log:

.. code-block::

    $ perry-bot water [OPTIONS] [CUPS]


Log a cup of water
""""""""""""""""""

| To log cups of water drank, use the ``water`` command.
| For example, to log 1 cup of water:


.. code-block::

    $ perry-bot water 1


Delete a cup
""""""""""""

| If you made a mistake and want to remove a log, use ``-d`` or ``--delete``.
| For example, to delete 1 cup of water:

.. code-block::

    $ perry-bot water --delete 1


View your cups drank
""""""""""""""""""""

To view the number of cups you've drank, use ``-v`` or ``--view``

.. code-block::

    $ perry-bot water --view


Visualize your data
^^^^^^^^^^^^^^^^^^^

Use the ``viz`` command where ``LOG_TYPE`` is either ``habit`` or ``water``

.. code-block::

    $ perry-bot viz [OPTIONS] [LOG_TYPE]

If no date range is provided, the last 7 days will be shown.



Date Formats
^^^^^^^^^^^^

.. list-table::
    :header-rows: 1

    * - Command
      - Option
      - Accepted Format(s)
      - Example
    * - ``habit``
      - ``-sd``, ``--start-date``
      - %Y-%m-%d
      - 2021-03-01
    * - ``viz``
      - ``-o``, ``--on``
      - %Y-%m-%d
      - 2021-12-11
    * - ``viz``
      - ``-f``, ``--from``
      - %Y-%m-%d
      - 2021-12-11
    * - ``viz``
      - ``-t``, ``--to``
      - %Y-%m-%d
      - 2021-12-11
    * - ``viz``
      - ``-m``, ``--month``
      - %m, %b, %B
      - 12, Dec, December
    * - ``viz``
      - ``-y``, ``--year``
      - %Y, %y
      - 2021, 21



Full list of commands and options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To see a full list of commands, type ``perry-bot --help``

.. code-block::

    Usage: perry-bot [OPTIONS] COMMAND [ARGS]...

      Perry Bot.

      Use `perry-bot [command] --help` to view options for the command.

      See documentation at
      https://perry-bot.readthedocs.io/en/latest/usage.html#cli-usage for
      further help.

    Options:
      --help  Show this message and exit.

    Commands:
      gui    Start GUI.
      habit  Log and manage habits.
      log    Log cups of water drank.
      viz    Visualize your water or habit records.


Habit options
"""""""""""""

.. code-block::

    Usage: perry-bot habit [OPTIONS] HABIT

      Log and manage habits.

      [HABIT] = Name of habit. Use `all` for all habits.

    Options:
      -v, --view                      View existing habit and its status.

      -c, --complete / -ic, --incomplete
                                      Mark habit as complete or incomplete.

      -a, --add                       Add a habit.
      -d, --delete                    Delete a habit.

      -e, --edit [Name|Frequency|Start date]
                                      Edit a habit.

      -f, --frequency [Daily|Bi-Weekly|Weekly|Monthly|Yearly]
                                      Frequency of the habit.

      -sd, --start-date [%Y-%m-%d]    Set the state date for weekly, bi-weekly,
                                      monthly, or yearly habits.

      --help                          Show this message and exit.


Water options
"""""""""""""

.. code-block::

    Usage: perry-bot log [OPTIONS] CUPS

      Log cups of water drank.

      [CUPS] = Integer

    Options:
      -d, --delete  Delete # cup(s) of water.
      -v, --view    View cups of water drank.
      --help        Show this message and exit.


Data visualization options
"""""""""""""""""""""""""""

.. code-block::

    Usage: perry-bot viz [OPTIONS] LOG_TYPE

      Visualize your water or habit records.

      If no date or date range is provided, the last 7 days will be shown. See
      documentation for date formatting.

      [LOG_TYPE] = `water` or `habit`

    Options:
      -o, --on [%Y-%m-%d]     Show entries on this date.
      -f, --from [%Y-%m-%d]   Show entries after, or on, this date
      -t, --to [%Y-%m-%d]     Show entries before, or on, this date.
      -m, --month [%m|%b|%B]  Show entries on this month of any year.
      -y, --year [%Y|%y]      Show entries of a specific year.
      -h, --habit TEXT        Show entries of a specific habit.
      --help                  Show this message and exit.
