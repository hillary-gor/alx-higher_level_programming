#!/usr/bin/python3
"""Defines a Python class-to-JSON Function."""


def class_to_json(obj):
    """Return the dictionary Represntation of a simple data structure."""
    return obj.__dict__

