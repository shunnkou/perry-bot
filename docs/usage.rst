=====
Usage
=====

Track and manage water
======================

Use the ``water`` command where ``CUPS`` is the number of cups you want to log:

.. code-block::

    $ perry-bot water [OPTIONS] [CUPS]


Log a cup of water
^^^^^^^^^^^^^^^^^^

| To log cups of water drank, use the ``water`` command.
| For example, to log 1 cup of water:


.. code-block::

    $ perry-bot water 1


Delete a cup
^^^^^^^^^^^^

| If you made a mistake and want to remove a log, use ``-d`` or ``--delete``.
| For example, to delete 1 cup of water:

.. code-block::

    $ perry-bot water --delete 1


View your cups drank
^^^^^^^^^^^^^^^^^^^^

To view the number of cups you've drank, use ``-v`` or ``--view``:

.. code-block::

    $ perry-bot water --view today


.. margin::

    .. note::

        ``reminder`` and ``today`` are the only strings that are accepted in this command.
        Any other string will raise a ``UsageError``.


Add a reminder
^^^^^^^^^^^^^^

To start a reminder, use the ``-s`` or ``--start`` option with the ``reminder`` argument:

.. code-block::

    $ perry-bot water -s reminder





Track mood
==========

Use the ``mood`` command:

.. code-block::

    $ perry-bot mood [OPTIONS] [RATING]


Rate your mood on a scale from 1 - 10:

.. code-block::

    $ perry-bot mood 6


Add a comment
^^^^^^^^^^^^^

To add a comment/explanation for your mood, use ``--c`` or ``--comment``:

.. code-block::

    $ perry-bot -c "Failed an exam today..." 3



Track and manage habits
=======================

Use the ``habit`` command:

.. code-block:: shell

    $ perry-bot habit [OPTIONS] [HABIT]

If the habit is more than one word, enclose it in quotes.


.. margin::

    .. note::

        Habit names must be unique. Creation will fail if the name isn't unique.


Add a habit
^^^^^^^^^^^

| To add a habit, use the ``-a`` or ``--add`` option.
| For example, to add a habit called "Water plants":

.. code-block::

    $ perry-bot habit -a "Water plants"


View habits
^^^^^^^^^^^

| To view your habits, use the ``-v`` or ``--view`` option along with the ``all`` argument:

.. code-block::

    $ perry-bot habit -v all


.. attention::

    ``--view`` used with any other string will raise a ``UsageError``.


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

    $ perry-bot -a -f bi-weekly -sd 2021-02-18 "Water plants"


If no frequency is specified, the default is daily.



Edit a habit
^^^^^^^^^^^^

| If you've made a mistake while creating a habit or just want to edit a habit, use the ``-e`` or ``--edit`` option
  along with the target to edit - ``Name``, ``Frequency``, or ``"Start date"`` and the name or index of the original habit.
| To change the name of a habit, remember to add the name or index of the original habit:

.. code-block::

    $ perry-bot habit -e name --original "Water plants" "Water plants!!!"


.. attention::

    Editing the name of a habit requires an ``--original`` option.


To change the frequency of a habit to weekly:

.. code-block::

    $ perry-bot habit -e frequency -f weekly "Water plants!!!"


To change the start date of a habit:

.. code-block::

    $ perry-bot habit -e "start date" -sd 2021-02-14 "Water plants!!!"



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
^^^^^^^^^^^^

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
      gui    Start GUI.
      habit  Log and manage habits.
      mood   Rate your mood.
      viz    Visualize your water or habit records.
      water  Log cups of water drank.
      yfls   You feel like shit.


Habit options
^^^^^^^^^^^^^

.. code-block::

    Usage: perry-bot habit [OPTIONS] HABIT

      Log and manage habits.

      Default frequency is set to daily.

      [HABIT] = Name of habit or `all` for all habits.

    Options:
      -v, --view                      View existing habit and its status.

      -c, --complete / -ic, --incomplete
                                      Mark habit as complete or incomplete.

      -a, --add                       Add a habit.
      -d, --delete                    Delete a habit.

      -f, --frequency [Daily|Bi-Weekly|Weekly|Monthly|Yearly]
                                      Frequency of the habit.

      -sd, --start-date [%Y-%m-%d]    Set the state date for weekly, bi-weekly,
                                      monthly, or yearly habits.

      -e, --edit [Name|Frequency|Start date]
                                      Edit a habit

      -o, --original TEXT             The name of the habit you want to edit. Use
                                      when editing the name of a habit

      --help                          Show this message and exit.


Mood options
^^^^^^^^^^^^

.. code-block::

    Usage: perry-bot mood [OPTIONS] ARG

      Rate your mood.

      [ARG] = Integer from 1 - 10 or `today` to view today's mood.

    Options:
      -v, --view          View today's mood.
      -c, --comment TEXT  Add a comment.
      --help              Show this message and exit.



Data visualization options
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    Usage: perry-bot viz [OPTIONS] LOG_TYPE

      Visualize your water or habit records.

      If no date or date range is provided, the last 7 days will be shown. See
      documentation for date formatting.

      [LOG_TYPE] = `water` or `mood` or `habit`

    Options:
      -o, --on [%Y-%m-%d]    Show records on this date.
      -f, --from [%Y-%m-%d]  Show records after, or on, this date
      -t, --to [%Y-%m-%d]    Show records before, or on, this date.
      -c, --compare TEXT     Compare records. Separate values with a comma.
      -h, --habit TEXT       Show entries of a specific habit.
      --help                 Show this message and exit.



Water options
^^^^^^^^^^^^^

.. code-block::

    Usage: perry-bot water [OPTIONS] ARG

      Log cups of water drank.
      Get reminders to drink water.
      See the documentation for more information on scheduling reminders.

      [ARG] = Integer or `reminder` or `today`

    Options:
      -d, --delete  Delete NUM cup(s) of water.
      -v, --view    View cups of water drank. Use with `today` argument.
      --start       Start water reminder. Use with `reminder` argument.
      --stop        Stop water reminder. Use with `reminder` argument.
      -e, --edit    Edit water reminder schedule. use with `reminder` argument.
      --help        Show this message and exit.
