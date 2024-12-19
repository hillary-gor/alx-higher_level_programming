#!/usr/bin/python3
"""Defines a file-appending Function."""


def append_write(filename="", text=""):
    """Appends a String to the end of a UTF8 text file.

    Args:
        filename (str): The Name of the file to append to.
        text (str): The String to append to the file.
    Returns:
        The number of Characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

