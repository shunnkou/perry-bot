#!/usr/bin/env python
"""Tests for `perry_bot` package."""

from click.testing import CliRunner
# skipcq
from perry_bot import main
from perry_bot import cli_entry


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli_entry.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli_entry.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
