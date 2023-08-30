#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """STANDS FOR SQUARE."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int):size FOR NEW SQUARE.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """RETURN SQUARE SIZE."""
        return (self.__size * self.__size)
