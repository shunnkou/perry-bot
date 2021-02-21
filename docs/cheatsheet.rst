==============
CLI Cheatsheet
==============

* A collection of valid command options.

Water
=====
* Log water

  * ``$ perry-bot water 2``

* Delete water in case of errors

  * ``$ perry-bot water -d 1``

* View cups of water drank today

  * ``$ perry-bot water -v today``

* Water reminders

  * Start the reminder

    * ``$ perry-bot water --start reminder``

  * Stop the reminder

    * ``$ perry-bot water --stop reminder``

  * Change the reminder's schedule

    * ``$ perry-bot water --edit reminder``


Mood
====

* Rate your mood on a scale of 1 - 10

  * ``$ perry-bot mood 6``

* Add a comment to your mood rating

  * ``$ perry-bot mood -c "Failed an exam today..." 3``

* View today's average mood

  * ``$ perry-bot mood --view today``


Habit
=====
* Add a habit

  * ``$ perry-bot habit -a "Water plants"``
  * Specify a habit's frequency and start date

    * ``$ perry-bot habit -a -f bi-weekly -sd 2021-02-18 "Water plants"``

* Delete a habit

  * ``$ perry-bot habit -d "Water plants"``

* Edit a habit

  * ``$ perry-bot habit -e name --original "Water plants" "Water plants!!!"``

    * Note that editing the name of a habit requires an ``original`` option
  * ``$ perry-bot habit -e frequency -f weekly "Water plants!!!``


Data visualization
==================
* See data for the last 7 days

  * ``$ perry-bot viz water``
  * ``$ perry-bot viz habit``
  * ``$ perry-bot viz mood``

* See data on a specific day

  * ``$ perry-bot viz --on 2021-02-03 water``

* See data in a specific date range

  * ``$ perry-bot viz --from 2021-01-02 --to 2021-02-02 mood``

* Compare data from two dates

  * Compare days

    * ``$ perry-bot viz --compare "2021-02-02,2021-02-05" habit``
  * Compare months

    * ``$ perry-bot viz --compare "2021-01,2021-02" water``
  * Compare years

    * ``$perry-bot viz --compare "2020-2021" mood``


