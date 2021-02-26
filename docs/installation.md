# Installation


## Stable release
Install the latest release of [Perry Bot](https://pypi.org/project/perry-bot/) with pipx:

```shell
$ pipx install perry-bot
```

Perry Bot's command is:

```shell
$ perry-bot
```


Use the `--help` flag to see all commands:

```shell
$ perry-bot --help
```

This is the preferred method to install Perry Bot, as it will
automatically create a virtual environment for Perry Bot and add the binary to your PATH.

If you don't have [pipx](https://pipxproject.github.io/pipx/) installed,
see pipx's [installation guide](https://pipxproject.github.io/pipx/installation/).


## From sources
The sources for Perry Bot can be downloaded from the [Github repo](https://github.com/shunnkou/perry-bot).

You can either clone the public repository:

```shell
$ git clone git://github.com/shunnkou/perry-bot
```

Or download the [tarball](https://github.com/shunnkou/perry-bot/tarball/master):

```shell
$ curl -OJL https://github.com/shunnkou/perry-bot/tarball/master
```

Once you have a copy of the source, you can install it with:

```shell
$ python setup.py install
```
