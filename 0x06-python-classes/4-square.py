#!/usr/bin/python3

"""DEFINING A SQUARE."""


class Square:
    """FOR SQUARE."""

    def __init__(self, size=0):
        """SQUARE INITIALISING.

        Args:
            size (int): SIZE OF NEW SQUARE.
        """
        self.size = size

    @property
    def size(self):
        """Get/SET CURRENT SQUARE SIZE"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """RETURN CURRENT AREA."""
        return (self.__size * self.__size)
