import os

import pytest
from typer.testing import CliRunner

from hello_flit import core
from hello_flit.cli import app
from hello_flit.core import which_quarter

from .conftest import MONTH_QTR_DATA, WORKING_DIR

runner = CliRunner()


@pytest.mark.parametrize("month, quarter", MONTH_QTR_DATA)
def test_which_quarter(month, quarter):
    """
    For a given month, test that the quarter in which it falls is correctly determined
    """
    output_dir = "2022"
    quarter_prefix = "qtr_"
    result = f"{output_dir}{os.sep}{quarter_prefix}{quarter:02d}"
    assert which_quarter(month, output_dir, quarter_prefix) == result


def test_app_no_args(temp_location, monkeypatch):
    """If no year is provided, the app should run, using current year as default"""

    monkeypatch.setattr(core, "CURRENT_DIR", WORKING_DIR)

    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "" in result.stdout


def test_app_with_year(temp_location, monkeypatch):

    monkeypatch.setattr(core, "CURRENT_DIR", WORKING_DIR)

    result = runner.invoke(app, ["2023"])
    assert result.exit_code == 0
    assert "" in result.stdout


def test_app_with_bad_arg():
    result = runner.invoke(app, ["foo"])
    assert result.exit_code == 2
    assert "Invalid value for '[YEAR]': 'foo' is not a valid integer range." in result.stdout


# more tests
