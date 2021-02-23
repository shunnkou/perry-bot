=====
Usage
=====

Track and manage water
======================

Use the ``water`` command:

.. code-block::

    $ perry-bot water [OPTIONS]


Log a cup of water
^^^^^^^^^^^^^^^^^^

| To log cups of water drank, use the ``-a`` or ``--add`` option.
| For example, to log 1 cup of water:


.. code-block::

    $ perry-bot water -a 1


Delete a cup
^^^^^^^^^^^^

| If you made a mistake and want to remove a log, use ``-d`` or ``--delete``.
| For example, to delete 1 cup of water:

.. code-block::

    $ perry-bot water --delete 1


View your cups drank
^^^^^^^^^^^^^^^^^^^^

To view the number of cups you've drank, use ``-v`` or ``--view`` and a date, month, or year:

.. code-block::

    $ perry-bot water --view 2021-02-05


Start reminder
^^^^^^^^^^^^^^

To start a reminder, use the ``--start`` option:

.. code-block::

    $ perry-bot water --start


Stop reminder
^^^^^^^^^^^^^

To stop a reminder, use the ``--stop`` option:

.. code-block::

    $ perry-bot water --stop


Edit schedule
^^^^^^^^^^^^^

TO edit the reminder's schedule, use the ``-e`` or ``--edit`` option:

.. code-block::

    $ perry-bot water --edit




Track mood
==========

Use the ``mood`` command:

.. code-block::

    $ perry-bot mood [OPTIONS]


To rate your mood on a scale from 1 - 10, use the ``-r`` or ``--rating`` option:

.. code-block::

    $ perry-bot mood -r 6


Add a comment
^^^^^^^^^^^^^

To add a comment/explanation for your mood, use the ``-c`` or ``--comment`` option:

.. code-block::

    $ perry-bot -c "Failed an exam today..." -r 3



Track and manage habits
=======================

Use the ``habit`` command:

.. code-block:: shell

    $ perry-bot habit [OPTIONS]

If the habit is more than one word, enclose it in quotes.

Once your habit has been created, you can refer to it with its number for quicker inputs.


.. margin::

    .. note::

        Habit names must be unique. Creation will fail if the name isn't unique.


Add a habit
^^^^^^^^^^^

| To add a habit, use the ``-a`` or ``--add`` option.
| For example, to add a habit called "Water plants":

.. code-block::

    $ perry-bot habit -a "Water plants"


.. note::

    The ``--add`` option is also used to specify the name (or index) of a habit when you want to `edit`_ it.


View habits
^^^^^^^^^^^

| To view your habits existing habits, use the ``-v`` or ``--view`` option:

.. code-block::

    $ perry-bot habit -v


.. _edit: https://perry-bot.readthedocs.io/en/develop/usage.html#edit-a-habit


Delete a habit
^^^^^^^^^^^^^^

| To delete a habit, use the ``-d`` or ``--delete`` option.
| For example, to delete a habit called "Water plants":

.. code-block::

    $ perry-bot habit -d "Water plants"



Schedule a habit
^^^^^^^^^^^^^^^^

| If you want to repeat a habit on a specific day, use the ``-sd``, or ``--start-date`` option.
| For example, to schedule "Water plants" to repeat bi-weekly:

.. code-block:: shell

    $ perry-bot -f bi-weekly -sd 2021-02-18 -a "Water plants"


If no frequency is specified, the default is daily.



Edit a habit
^^^^^^^^^^^^

| To edit a habit, use the ``-e`` or ``--edit`` option with the target to edit
  - ``name``, ``frequency``, or ``start date``, and the name or index of the original habit,
  separated by a comma.

To change the name of a habit, remember to add the name or number of the original habit with ``-a``:

.. code-block::

    $ perry-bot habit -e "name,Water plants!!!" -a "Water plants"


To change the frequency of a habit to weekly:

.. code-block::

    $ perry-bot habit -e "frequency,Water plants!!!" -f weekly


To change the start date of a habit:

.. code-block::

    $ perry-bot habit -e "start date,Water plants!!!" -sd 2021-02-14



Visualize your data
===================

Use the ``viz`` command where ``LOG_TYPE`` is either ``habit`` or ``water``:

.. code-block::

    $ perry-bot viz [OPTIONS] [LOG_TYPE]

| If no date range is provided, the last 7 days will be shown.
| For example, to see data for the last 7 days:

.. code-block::

    $ perry-bot viz water
    $ perry-bot viz habit
    $ perry-bot viz mood


To see data on a specific day:

.. code-block::

    $ perry-bot viz --on 2021-02-03 water


.. attention::

    When visualizing ``habit``, the date must be a year (``2021``) or a month (``2021-02``), not a day.


To see data in a specific date range:

.. code-block::

    $ perry-bot viz --from 2021-01-02 --to 2021-02-02 mood


Compare data from two dates
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``--compare`` option and separate your dates with a comma.

To compare days:

.. code-block::

    $ perry-bot viz --compare "2021-02-02,2021-02-05" water


To compare months:

.. code-block::

    $ perry-bot viz --compare "2021-01,2021-02" habit


To compare years:

.. code-block::

    $ perry-bot viz --compare "2020,2021" mood


.. margin::

    .. note::

        Basically, everything is in the format of "Year-Month-Date"


Date Formats
============

.. list-table::
    :header-rows: 1

    * - Command
      - Option
      - Accepted Format
      - Example
    * - ``habit``
      - ``-sd``, ``--start-date``
      - %Y-%m-%d
      - 2021-03-01
    * - ``water``
      - ``-v``, ``--view``
      - x%Y-%m-%d,

        %Y-%m,

        %Y
      - 2021-02-04,

        2021-02,

        2021

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
      - ``-c``, ``--compare``
      - "%Y-%m-%d,%Y-%m-%d",

        "%Y-%m,%Y-%m",

        "%Y,%Y"
      - "2021-02-04,2021-02,05",

        "2021-02,2021-01",

        "2021,2020"



Full list of commands and options
=================================

To see a full list of commands, type ``perry-bot --help``

.. code-block::

    Usage: perry-bot [OPTIONS] COMMAND [ARGS]...

      Perry Bot.
      Use `perry-bot COMMAND --help` to view options for the command.

      See documentation at
      https://perry-bot.readthedocs.io/en/latest/usage.html#cli-usage
      for further help.

    Options:
      --help  Show this message and exit.

    Commands:
      habit  Log and manage habits.
      mood   Rate your mood.
      viz    Visualize your records.
      water  Log cups of water drank.


Habit options
^^^^^^^^^^^^^

.. code-block::

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



Mood options
^^^^^^^^^^^^

.. code-block::

    Usage: perry-bot mood [OPTIONS]

      Rate your mood.

    Options:
      -r, --rating INTEGER RANGE      Your mood's rating. A number from 1-10
      -c, --comment TEXT              Add a comment.
      -v, --view [%Y-%m-%d|%Y-%m|%Y]  View average mood.
      --help                          Show this message and exit.


Data visualization options
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

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



Water options
^^^^^^^^^^^^^

.. code-block::

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
