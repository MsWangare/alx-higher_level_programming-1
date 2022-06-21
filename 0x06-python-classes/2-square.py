#!/usr/bin/python3
"""Square with size
Practicing private attributes within a class
"""


class Square:
    """Square with size attribute, throws exceptions if size is not valid
    """
    def __init__(self, size=0):
        """ _size is initialized with size
        Args:
        size (int): size of the side of the square, should be greater
        than zero, ValueError is raised. If it's not an integer,
        a TypeError is raised.
        Attributes:
        size (int): the size of the square of this class set
        by the initializer.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
