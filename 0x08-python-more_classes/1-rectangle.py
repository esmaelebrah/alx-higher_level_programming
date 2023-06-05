#!/usr/bin/python3
""" defining a rectangle class """


class Rectangle:
    """ representes a rectangle

    Attributes:
      __width (int): width of the rectangle
      __height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """ initializes a rectangle

        args:
           width (int): width of the rectangle
           height (int): heigtht of the rectangle

        return: None
        """
        self.width = width
        self.height = height

    def height(self):
        """a public class

        return: height of the rectangle
        """
        return (self.__height)

    def height(self, value):
        """ a puiblic class

        return: None
        set: height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def width(self, value):
        """ a puiblic class

        return: None
        set: width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def width(self):
        """ a puiblic class

        return: width of the rectangle
        """
        return (self.__width)
