#!/usr/bin/python3
"""DEFIINES CLASS STUDENT."""


class Student:
    """REP STUDENT."""

    def __init__(self, first_name, last_name, age):
        """INIT A STUDENT.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get STUDENT DICTIONARY."""
        return self.__dict__
