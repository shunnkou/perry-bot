.. highlight:: shell

============
Installation
============


Stable release
--------------

Install `Perry Bot`_, with `pipx`_:

.. code-block:: shell

    $ pipx install perry-bot


Perry Bot's command is:

.. code-block:: shell

    $ perry-bot


Use the ``--help`` flag to see all commands:

.. code-block:: shell

    $ perry-bot --help


This is the preferred method to install Perry Bot, as it will
automatically create a virtual environment for Perry Bot and add the binary to your PATH.

If you don't have `pipx`_ installed, see pipx's `installation guide`_

.. _pipx: https://pipxproject.github.io/pipx/
.. _installation guide: https://pipxproject.github.io/pipx/installation/


From sources
------------

The sources for Perry Bot can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/shunnkou/perry-bot

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/shunnkou/perry-bot/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/shunnkou/perry-bot
.. _tarball: https://github.com/shunnkou/perry-bot/tarball/master
.. _Perry Bot: https://pypi.org/project/perry-bot/
