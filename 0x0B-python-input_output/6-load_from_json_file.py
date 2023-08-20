#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Creates a Python obj from JSON file

    Args:
        filename: file
    """
    with open(filename) as a_file:
        return json.load(a_file)
