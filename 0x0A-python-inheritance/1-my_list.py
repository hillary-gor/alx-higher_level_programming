#!/usr/bin/python3
"""Define an inherited List class MyList"""

class MyList(list):
    """Type class MyList with prt_sorted function"""

    def print_sorted(self):
        print(sorted(self))
