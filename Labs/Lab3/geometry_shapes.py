from __future__ import annotations
from dataclasses import dataclass
import math
from turtle import position, width

@dataclass
class Shape:
    """
    A class used as base and parent for different shapes

    ...

    Attributes
    -----------
    position : tuple
        a tuple containing the xy coordinates of the shape
    width : float | int
        the width of the shape
    height : float | int
        the height of the shape

    Methods
    --------
    validate_position(position)
        errorhandling to check if given position is given as propper xy coordinates
    move_position(position)
        changes the xy coordinates of the shape
    """

    position: tuple # form (x,y)
    width: float|int
    height: float|int

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self.validate_position(position)
        self._position = position

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, (float,int)):
            raise TypeError(f"width must be an int or float not {type(width).__name__}")
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, (float,int)):
            raise TypeError(f"width must be an int or float not {type(height).__name__}")
        self._height = height

    def validate_position(self, position):
        if not isinstance(position, tuple):
            raise TypeError(f"position must be a tuple containing an xy value not {type(position).__name__}")
        if not isinstance(position[0], (int,float)) or not isinstance(position[1], (int,float)):
            raise TypeError(f"position xy value must be int or float not {type(position[0]).__name__},{type(position[1]).__name__}")
        if len(position) != 2:
            raise ValueError(f"position must consist of an x value and y value")

    def move_position(self, position) -> tuple:
        self.position = position
        return self.position

@dataclass
class Square(Shape):
    # i know that i should've probably named it rectangle not square
    """
    Childclass of Shape
    A class used to represent squares

    ...

    Attributes
    -----------
    position : tuple
        a tuple containing the xy coordinates of the square
    width : float | int
        the width of the square
    height : float | int
        the height of the square
    
    area
        the calculated area of the square based on width and height
    circumference
        the calculated circumference of the square based on width and height

    Methods
    --------
    validate_position(position)
        errorhandling to check if given position is given as propper xy coordinates
    move_position(position)
        changes the xy coordinates of the square
    is_square()
        returns true if the square is square and not a rectangle
    is_inside(position)
        checks if a xy coordinate is inside of this square
    __eq__
        overloads == operator to compare two squares and check if they are equal
    __lt__
        overloads < operator to compare if one square is smaller
    __gt__
        overloads > operator to compare if one square is larger
    __le__
        overloads <= operator to compare if one square is smaller or equal
    __ge__
        overloads >= operator to compare if one square is larger or equal
    """

    @property
    def area(self):
        return self.width*self.height

    @property
    def circumference(self):
        return self.width*2 + self.height*2

    def __str__(self) -> str:
        return f"Square with the xy coordinates{self.position}, width of {self.width} and height of {self.height}"

    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            return False
 
    def is_inside(self, position : tuple) -> bool:
        self.validate_position(position)

        min = (self.position[0]-self.width/2, self.position[1]-self.height/2)
        max = (min[0]+self.width, min[1]+self.width)
        if min[0] <= position[0] <= max[0] and min[1] <= position[1] <= max[1]:
            return True
        else:
            return False

    def __eq__(self, other: Square) -> bool:
        if self.width == other.width and self.height == other.height:
            return True
        else:
            return False

    def __lt__(self, other: Square) -> bool:
        if self.area < other.area:
            return True
        else:
            return False

    def __gt__(self, other: Square) -> bool:
        if self.area > other.area:
            return True
        else:
            return False

    def __le__(self, other: Square) -> bool:
        if self.area <= other.area:
            return True
        else:
            return False

    def __ge__(self, other: Square) -> bool:
        if self.area >= other.area:
            return True
        else:
            return False


class Circle(Shape):
    """
    Childclass of Shape
    A class used to represent circles

    ...

    Attributes
    -----------
    position : tuple
        a tuple containing the xy coordinates of the circle
    width : float | int
        the width or diameter of the circle
    
    area
        the calculated area of the circle based on diameter
    circumference
        the calculated circumference of the circle based on diameter

    Methods
    --------
    validate_position(position)
        errorhandling to check if given position is given as propper xy coordinates
    move_position(position)
        changes the xy coordinates of the circle
    is_unit_circle
        checks if the circle meets the requirements of a unit circle
    is_inside(position)
        checks if a xy coordinate is inside of this circle
    __eq__
        overloads == operator to compare two circles and check if they are equal
    __lt__
        overloads < operator to compare if one circle is smaller
    __gt__
        overloads > operator to compare if one circle is larger
    __le__
        overloads <= operator to compare if one circle is smaller or equal
    __ge__
        overloads >= operator to compare if one circle is larger or equal
    """
    
    # did not use dataclass inorder to override width and height from parent class
    def __init__(self, position: tuple, width: float|int) -> None:
        super().__init__(position, width, width)


    @property
    def area(self):
        return ((self.width/2)**2) *math.pi

    @property
    def circumference(self):
        return self.width * math.pi

    def __repr__(self) -> str:
        return f"Circle(position={self.position}, width={self.width})"

    def __str__(self) -> str:
        return f"Circle with the xy coordinates{self.position} and a diameter of {self.width}"

    def is_unit_circle(self) -> bool:
        if self.position == (0,0) and self.width == 2:
            return True
        else:
            return False

    def is_inside(self, position: tuple) -> bool:
        self.validate_position(position)

        distance = math.hypot(position[0]-self.position[0], position[1]-self.position[0])
        if distance <= self.width/2:
            return True
        else:
            return False

    def __eq__(self, other: Circle) -> bool:
        if self.width == other.width:
            return True
        else:
            return False

    def __lt__(self, other: Circle) -> bool:
        if self.area < other.area:
            return True
        else:
            return False

    def __gt__(self, other: Circle) -> bool:
        if self.area > other.area:
            return True
        else:
            return False

    def __le__(self, other: Circle) -> bool:
        if self.area <= other.area:
            return True
        else:
            return False

    def __ge__(self, other: Circle) -> bool:
        if self.area >= other.area:
            return True
        else:
            return False


cir = Circle((0,0), 2)
#cir.width = 3
#print(cir.height, cir.width)
