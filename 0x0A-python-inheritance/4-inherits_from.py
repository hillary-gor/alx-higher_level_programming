#!/usr/bin/python3
"""Define an inherits_from class"""

def inherits_from(obj, a_class):

    """function to check if obj is inherited from a class
    Arguments:
        param1: obj
        param2: a_class that matches the obj
    Return:
    True for issubclass of obj or False if not
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
