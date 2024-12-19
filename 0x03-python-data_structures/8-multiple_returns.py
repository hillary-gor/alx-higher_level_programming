#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character."""
    tup = ()
    length = len(sentence)
    first = ""

    if not sentence:
        length = 0
        first = None
        tup = tup + (length, first)

    else:
        first = sentence[0]
        tup = tup + (length, first)

    return tup
