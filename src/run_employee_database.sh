#!/bin/bash

if [[ -x "$(command -v python3)" ]]
then
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r ./requirements.txt
    python3 main.py
else
    echo "Error:
        This program runs on Python 3, but it looks like Python 3 is not installed.
        To install Python 3, check out https://www.python.org/downloads/" >&2
    exit 1
fi
