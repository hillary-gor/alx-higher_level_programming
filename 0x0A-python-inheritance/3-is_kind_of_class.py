#!/usr/bin/python3
"""Define an is_kind_of_class or  categories class"""

def is_kind_of_class(obj, a_class):
    """function to check if object is the same kind of class
    Arguments:
        param1: object
        param2: a_class that matches the obj
    Return:
    True for isinstance of object  or False if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

