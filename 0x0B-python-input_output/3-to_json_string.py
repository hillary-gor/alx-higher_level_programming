#!/usr/bin/python3
"""Defines a Str-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a str object."""
    return json.dumps(my_obj)

