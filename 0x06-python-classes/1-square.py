#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes the square's
        Args:
        size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
