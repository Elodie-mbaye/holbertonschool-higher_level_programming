#!/usr/bin/python3
"""
Defines a function to check if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    The function checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        bool: true if the object is an instance of a class that inherited,
        otherwise false.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
