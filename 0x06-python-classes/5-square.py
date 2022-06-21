#!/usr/bin/python3
"""Square with size
Practicing private attributes within a class and public method
"""


class Square:
    """Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
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

    def area(self):
            """Calculates the area of this square
            Returns:
            The area of the square
            """
        return self.__size ** 2

    def my_print(self):
            """Prints a visual representation of the square
            Print #'s according to the length of the side of the square,
            self.__size
            """
        print() if self.size == 0 else None
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print()

        @property
        def size(self):
                        """Get private attribute size
                        Returns:
                        The attribute size
                        """
            return self.__size

        @size.setter
        def size(self, value):
                        """Sets this.__size to value
                        Args:
                        value (int): the integer that will be set to size
                        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
