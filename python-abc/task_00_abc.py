#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Animal from ABC"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class Dog from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class cat from Animal"""
    def sound(self):
        return "Meow"
