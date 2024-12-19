#!/usr/bin/python3
"""Define a class that checks for the same obj"""

def is_same_class(obj, a_class):
    """function to check if object is the same class
    Arguments:
        param1: object
        param2: a_class that matches the object
    Return:
    True for coopy of obj or False if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False

