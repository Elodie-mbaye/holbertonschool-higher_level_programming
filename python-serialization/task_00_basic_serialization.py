#!/usr/bin/python3
"""
Module for basic serialization and deserialization function.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize a Python dictionary to a JSON file and
    deserialize the JSON file to recreate the Python Dictionary.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from the specified file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.Loads(file)
