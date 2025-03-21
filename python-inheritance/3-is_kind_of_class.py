#!/usr/bin/python3
"""
Defines a function to check if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class,
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        bool:True if obj is an instance of a_class or its subclass,
        False otherwise.
    """
    return isinstance(obj, a_class)
