# tests/test_console.py
import click.testing 
import pytest 

from hypermodern_python_example import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
