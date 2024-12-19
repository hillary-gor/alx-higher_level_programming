#!/usr/bin/python3
"""Defines a JSON file-reading Function."""
import json


def load_from_json_file(filename):
    """Create a Python object From a JSON file."""
    with open(filename) as f:
        return json.load(f)

