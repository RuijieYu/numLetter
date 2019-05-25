# numLetter

## Requirements

This script requires Python 3.7. Go to its
[official website](https://www.python.org/downloads/)
to download the latest release for your platform.
See [this page](docs/python.md) for direct links for Python 3.7.3.

This script is best used with `git` to sync updates.
Go to its [official website](https://git-scm.com/downloads/) and
download the latest release
(preferably with GUI; git bash highly recommend) for your platform.

## What It Does

Converts a number less than established "maximum"
(different per language) into a word or phrase of a given language.

This word or phrase is then appended to "output.txt"
at current working directory for later use, as well as
displayed on screen for immediate use.

## How to Use

### How to Obtain

Open file manager and go to a convenient location.

Open (linux-styled) terminal.

    Windows:
        Within explorer, right click and select Git Bash

    Mac OS:
        Press `command + SPACE` at the same time and type `terminal`

    Linux:
        Press `Ctrl + Alt + T`; if not successful refer to the manual from your system

`cd` to your convenient location if not there yet.

Type `git clone https://github.com/JAMESY9868/numLetter.git` and return

### How to Run

Open (native) terminal.

    Windows:
        Shift + right click within explorer at your convenient location
        select PowerShell, and type `cmd` in the blue window

    Mac OS and Linux:
        Refer to the previous section for opening the terminal.

Type `python -m numLetter` or `python3 -m numLetter` and follow the prompts.

### How to Update

Open (linux-styled) terminal, and `cd` to the outside of numLetter
(your convenient location).

Type `git pull` and wait.