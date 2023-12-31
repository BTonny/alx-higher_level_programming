#!/usr/bin/python3
""" A module that contains class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square class that inherits  from Rectangle
    """
    def __init__(self, size):
        """
            Instantiation with size(size of square)
        """
        self.integer_validator("size", size)
        self__size = size
        super().__init__(size, size)

    def area(self):
        """
            Returns the area of the square
        """
        return super().area()