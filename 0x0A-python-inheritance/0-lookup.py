#!/usr/bin/python3
"""
Contains definition of funtion lookup
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj(any): objects whose attributes and methords are returned
    """

    return (dir(obj))
