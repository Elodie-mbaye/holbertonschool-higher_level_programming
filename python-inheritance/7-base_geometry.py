#!/usr/bin/python3
"""
Defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): The name of the paramater.
            name (int): The parameter to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
