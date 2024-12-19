#!/usr/bin/python3
"""
add_integer module
this function adds two integers

"""
def add_integer(first_number: int, second_number: int = 98) -> int:
    """Adds two integers and returns the result.

    Raises:
        TypeError: If either input is not an integer.
    """

    if not isinstance(first_number, int):
        raise TypeError("first_number must be an integer")
    if not isinstance(second_number, int):
        raise TypeError("second_number must be an integer")

    return first_number + second_number
