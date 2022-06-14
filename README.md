<h1 align="center">Welcome to Hello Flit 👋</h1>

<p align="center">
<a href="https://testpypi.org/project/hello-flit" target="_blank">
  <img src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue" alt="Python Version">
</a>
<a href="https://en.wikipedia.org/wiki/Command-line_interface" target="_blank">
  <img alt="CLI application" src="https://badgen.net/badge/icon/terminal?icon=terminal&label">
</a>
<a href="https://www.gnu.org/gnu/linux-and-gnu.en.html" target="_blank">
  <img alt="Runs on GNU/Linux" src="https://svgshare.com/i/Zhy.svg">
</a>
<a href="https://support.apple.com/en-us/HT201260" target="_blank">
  <img alt="Runs on Mac OSX" src="https://svgshare.com/i/ZjP.svg">
</a>
<a href="https://www.microsoft.com/en-us/windows" target="_blank">
  <img alt="Runs on Windows" src="https://svgshare.com/i/ZhY.svg">
</a>
<a href="https://github.com/engineervix/hello-flit/actions/workflows/main.yml" target="_blank">
  <img src="https://github.com/engineervix/hello-flit/actions/workflows/main.yml/badge.svg" alt="Build Status">
</a>
<a href="https://codecov.io/gh/engineervix/hello-flit" target="_blank">
  <img src="https://codecov.io/gh/engineervix/hello-flit/branch/main/graph/badge.svg" alt="codecov">
</a>
<a href="https://results.pre-commit.ci/latest/github/engineervix/hello-flit/main" target="_blank">
  <img src="https://results.pre-commit.ci/badge/github/engineervix/hello-flit/main.svg" alt="pre-commit.ci status">
</a>
<a href="https://github.com/engineervix/hello-flit/commits/main" target="_blank">
  <img alt="GitHub commits since latest release (by SemVer)" src="https://img.shields.io/github/commits-since/engineervix/hello-flit/latest/main">
</a>
</p>

<p align="center">
<a href="https://opensource.org/licenses/MIT">
  <img src="https://img.shields.io/github/license/engineervix/hello-flit" alt="License">
</a>
<a href="https://github.com/psf/black">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
</a>
<a href="https://conventionalcommits.org">
  <img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square" alt="Conventional Commits">
</a>
<a href="https://commitizen-tools.github.io/commitizen/">
  <img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" alt="Commitizen friendly">
</a>
</p>

> A python project created with the sole purpose of testing out [Flit](https://flit.pypa.io/en/latest/index.html)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [What's Flit?](#whats-flit)
- [What does this project do?](#what-does-this-project-do)
- [Project features](#project-features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
  - [First things first](#first-things-first)
  - [Getting Started](#getting-started)
  - [Tests](#tests)
  - [Code Formatting](#code-formatting)
- [Contributing](#contributing)
- [TODO](#todo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What's Flit?

According to the official docs:

> **Flit** is a simple way to put Python packages and modules on PyPI. It tries to require less thought about packaging and help you avoid common mistakes. See [Why use Flit?](https://flit.readthedocs.io/en/latest/rationale.html) for more about how it compares to other Python packaging tools.

## What does this project do?

Well, what this project does isn't very important. The main point of this project is to try out packaging with Flit. However, since you asked, this project provides a simple CLI utility to create a directory tree suitable for organizing your work using the Year / Quarter / Month / Week convention, for instance:

```txt
2017/
├── qtr_01
│   ├── 01_Jan
│   │   ├── wk01_01Jan-07Jan
│   │   ├── wk02_08Jan-14Jan
│   │   ├── wk03_15Jan-21Jan
│   │   ├── wk04_22Jan-28Jan
│   │   └── wk05_29Jan-04Feb
│   ├── 02_Feb
│   │   ├── wk05_29Jan-04Feb
│   │   ├── wk06_05Feb-11Feb
│   │   ├── wk07_12Feb-18Feb
│   │   ├── wk08_19Feb-25Feb
│   │   └── wk09_26Feb-04Mar
│   └── 03_Mar
│       ├── wk09_26Feb-04Mar
│       ├── wk10_05Mar-11Mar
│       ├── wk11_12Mar-18Mar
│       ├── wk12_19Mar-25Mar
│       └── wk13_26Mar-01Apr
├── qtr_02
│   ├── 04_Apr
│   │   ├── wk13_26Mar-01Apr
│   │   ├── wk14_02Apr-08Apr
│   │   ├── wk15_09Apr-15Apr
│   │   ├── wk16_16Apr-22Apr
│   │   ├── wk17_23Apr-29Apr
│   │   └── wk18_30Apr-06May
│   ├── 05_May
│   │   ├── wk18_30Apr-06May
│   │   ├── wk19_07May-13May
│   │   ├── etc, you get the picture!
```

## Project features

- This is more-or-less a **typical python package**, with a structure similar to that created using [@audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- Supports Python 3.6+
- tests written using [Pytest], Linting with Black, Flake8, Isort
- Uses [tox](https://tox.wiki/en/latest/) for test automation
- The CLI is powered by [Typer](https://typer.tiangolo.com)

## Installation

```bash
pip install -i https://test.pypi.org/simple/ hello-flit
```

## Usage

```txt
Usage: cli.py [OPTIONS] [YEAR]

Arguments:
  [YEAR]  the year for which you'd like to create a directory tree  [default: <current_year>]

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

## Development

### First things first

- ensure that you have [Python 3.6+](https://www.python.org/) on your machine, and that you are able to configure python [**virtual environment**](https://realpython.com/python-virtual-environments-a-primer/)s.
- ensure that you have [git](https://git-scm.com/) setup on your machine.

### Getting Started

First, [fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) this repository, then fire up your command prompt and ...

1. Clone the forked repository
2. Navigate to the cloned project directory: `cd hello-flit`
3. activate your python virtual environment and `pip install --upgrade pip`
4. Install dependencies: `pip install -r requirements_dev.txt`
5. Setup [pre-commit](https://pre-commit.com/) by running `pre-commit install` followed by `pre-commit install --hook-type commit-msg`. Optionally run `pre-commit run --all-files` to make sure your pre-commit setup is okay.

At this stage, hopefully everything should be working fine, and you should be able to start hacking on the project.

You can run the application via `inv run [options]` or

```sh
python hello-flit/cli.py [YEAR]
```

### Tests

Simply run `pytest` or `inv test` to run tests in your virtual environment.

Test other Python versions by running `tox`.

### Code Formatting

- Run `invoke lint` to run [`flake8`](https://flake8.pycqa.org/en/latest/), [`black`](https://black.readthedocs.io/en/stable/), [`isort`](https://pycqa.github.io/isort/) and [`mypy`](https://mypy.readthedocs.io/en/stable/) on the code.
- If you get any errors from `black` and/or `isort`, run `invoke lint --fix` or `invoke lint -f` so that black and isort can format your files. Alternatively, just run `pre-commit`. You can take a look at [.pre-commit-config.yaml](https://github.com/engineervix/hello-flit/blob/main/.pre-commit-config.yaml).

## Contributing

Contributions, issues and feature requests are most welcome!

Feel free to check the [issues page](https://github.com/engineervix/hello-flit/issues) and take a look at the [contributing guide](https://github.com/engineervix/hello-flit/blob/main/CONTRIBUTING.md) before you get started. In addition, please note the following:

- if you're making code contributions, please try and write some tests to accompany your code, and ensure that the tests pass. Also, were necessary, update the docs so that they reflect your changes.
- commit your changes via `cz commit`. Follow the prompts. When you're done, `pre-commit` will be invoked to ensure that your contributions and commits follow defined conventions. See `pre-commit-config.yaml` for more details.
- your commit messages should follow the conventions described [here](https://www.conventionalcommits.org/en/v1.0.0/). Write your commit message in the imperative: "Fix bug" and not "Fixed bug" or "Fixes bug." This convention matches up with commit messages generated by commands like `git merge` and `git revert`.
Once you are done, please create a [pull request](https://github.com/engineervix/hello-flit/pulls).

## TODO

- [ ] Replicate this but with a Wagtail / Django package
