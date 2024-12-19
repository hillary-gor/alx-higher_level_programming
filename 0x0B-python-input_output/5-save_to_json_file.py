#!/usr/bin/python3
"""Defines a JSON file-writing Function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a txt file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

