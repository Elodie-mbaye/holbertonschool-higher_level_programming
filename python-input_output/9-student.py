#!/usr/bin/python3
"""Modules that defines a student class"""


class Student:
    """Defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
