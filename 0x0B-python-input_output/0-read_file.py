#!/usr/bin/python3
"""Defines a Text file-reading function."""


def read_file(filename=""):
    """Print the Contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

