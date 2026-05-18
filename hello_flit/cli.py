"""Console script for hello_flit."""

import os
import sys
from datetime import date
from typing import Optional

import typer
from colorama import init

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from hello_flit import __app_name__, __version__  # noqa:E402
from hello_flit.config import configure_logging  # noqa:E402
from hello_flit.core import create_dirs  # noqa:E402

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def main(
    year: int = typer.Argument(
        date.today().year,
        min=1999,
        max=2999,
        help="the year for which you'd like to create a directory tree",
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """
    This program is used to create a directory tree suitable for organizing
    your work using the Year / Quarter / Month / Week convention, for instance:

    2017/\n
    ├── qtr_01\n
    │   ├── 01_Jan\n
    │   │   ├── wk01_01Jan-07Jan\n
    │   │   ├── wk02_08Jan-14Jan\n
    │   │   ├── wk03_15Jan-21Jan\n
    │   │   ├── wk04_22Jan-28Jan\n
    │   │   └── wk05_29Jan-04Feb\n
    │   ├── 02_Feb\n
    │   │   ├── wk05_29Jan-04Feb\n
    │   │   ├── wk06_05Feb-11Feb\n
    │   │   ├── wk07_12Feb-18Feb\n
    │   │   ├── wk08_19Feb-25Feb\n
    │   │   └── wk09_26Feb-04Mar\n
    │   └── 03_Mar\n
    │       ├── wk09_26Feb-04Mar\n
    │       ├── wk10_05Mar-11Mar\n
    │       ├── wk11_12Mar-18Mar\n
    │       ├── wk12_19Mar-25Mar\n
    │       └── wk13_26Mar-01Apr\n
    ├── qtr_02\n
    │   ├── 04_Apr\n
    │   │   ├── wk13_26Mar-01Apr\n
    │   │   ├── wk14_02Apr-08Apr\n
    │   │   ├── wk15_09Apr-15Apr\n
    │   │   ├── wk16_16Apr-22Apr\n
    │   │   ├── wk17_23Apr-29Apr\n
    │   │   └── wk18_30Apr-06May\n
    │   ├── 05_May\n
    │   │   ├── wk18_30Apr-06May\n
    │   │   ├── wk19_07May-13May\n
    │   │   ├── etc, you get the picture!\n
    """
    init()
    configure_logging()
    create_dirs(year)


if __name__ == "__main__":
    typer.run(main)
