#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of a side of the square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """public class

        return: area of the square
        """
        return (self.__size * self.__size)
    @property
    def size(self):
        """ get nalue fun

        return: size of square
        """
        return (self.__size)
    @size.setter
    def size(self, value):
        """ the setter method 

        sets the value of size
        """
        self.__size = value
