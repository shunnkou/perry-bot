# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

:::{note}
Instead of using the issue tracker for questions, use [discussions](https://github.com/shunnkou/perry-bot/discussions).
:::

<details><summary>Table of Contents</summary>
<p>

- [](#code-of-conduct)

- [](#types-of-contributions)

  - [](#report-bugs)
  - [](#fix-bugs)
  - [](#implement-features)
  - [](#write-documentation)
  - [](#submit-feedback)
  - [](#questions)
  - [](#feature-requests)

- [](#get-started)

- [](#pull-request-guidelines)

</p>
</details>

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](../code_of_conduct.md).

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/shunnkou/perry-bot/issues.

If you are reporting a bug, use the provided template and please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Perry Bot could always use more documentation, whether as part of the
official Perry Bot docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/shunnkou/perry-bot/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Questions

Start a new [discussion](https://github.com/shunnkou/perry-bot/discussions/categories/q-a) in the Q&A category.

### Feature Requests

Start a new issue with the [feature request tempalte](https://github.com/shunnkou/perry-bot/issues/new?assignees=shunnkou&labels=enhancement&template=feature_request.md&title=Feature+Request+Summary)

## Get Started!

Ready to contribute? Here's how to set up `perry_bot` for local development.

1. Fork the `perry-bot` repo on GitHub.
1. Clone your fork locally:

```console
git clone git@github.com:your_name_here/perry-bot.git
```

3. Install your local copy into a virtualenv. Assuming you have pipenv installed, this is how you set up your fork for local development:

```console
mkdir perry_bot
cd perry_bot
pipenv console
pipenv install -r requirements_dev.txt
```

4. Create a branch for local development:

```console
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

5. Set up pre-commit

1. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox:

```console
flake8 perry_bot tests
python setup.py test or python -m pytest
tox
```

To get flake8 and tox, just pip install them from `requirements_dev.txt`.

6. Commit your changes and push your branch to GitHub:

```console
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
1. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in [`README.md`](README.md#perry-bot).

````{note} To run a subset of tests:
```console
pytest tests.test_perry_bot
```
````

<!---
## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in [`HISTORY.md`](HISTORY.md#history)).
Then run:
```console
bump2version patch # possible: major / minor / patch
git push
git push --tags
```
--->
