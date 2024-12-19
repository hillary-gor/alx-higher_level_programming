#!/usr/bin/python3
"""Defines a File-writing function."""


def write_file(filename="", text=""):
    """Write a String to a UTF8 text file.

    Args:
        filename (str): The Name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of Characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

