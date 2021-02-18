.. highlight:: shell

============
Installation
============


Stable release
--------------

To install Perry Bot, download the ``.tar.gz`` of the `latest release`_ and run this command in your terminal:

.. code-block:: console

    # Navigate to the directory containing perry_bot

    $ pipx install ./perry_bot


Start Perry Bot with:

.. code-block:: console

    $ perry-bot


This is the preferred method to install Perry Bot, as it will automatically create a virtual environment for Perry Bot and add the binary to your PATH.

If you don't have `pipx`_ installed, see pipx's `installation guide`_

.. _pipx: https://pipxproject.github.io/pipx/
.. _installation guide: https://pipxproject.github.io/pipx/installation/
.. _latest release: https://github.com/shunnkou/perry-bot/releases


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
