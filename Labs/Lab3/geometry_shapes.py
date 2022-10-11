from __future__ import annotations
from dataclasses import dataclass
import math
from turtle import width

@dataclass
class Shape:
    #def __init__(self, yaxis: float, xaxis: float, *radius: float) -> None:
        # self._yaxis = yaxis
        # self._xaxis = xaxis
        # self._radius = tuple(float(r) for r in radius)
    
    position: tuple # form (x,y)
    width: float|int
    height: float|int

    @property
    def position(self):
        #print("position getter")
        return self._position

    @position.setter
    def position(self, position):
        #print("position setter")
        if not isinstance(position, tuple):
            raise TypeError(f"position must be a tuple not {type(position).__name__}")
        if len(position) != 2:
            raise ValueError(f"position must consist of an x value and y value")
        self._position = position

    @property
    def width(self):
        #print("radius getter")
        return self._width

    @width.setter
    def width(self, width):
        #print("radius setter")
        if not isinstance(width, (float,int)):
            raise TypeError(f"width must be an int or float not {type(width).__name__}")
        self._width = width

    @property
    def height(self):
        #print("radius getter")
        return self._height

    @height.setter
    def height(self, height):
        #print("radius setter")
        if not isinstance(height, (float,int)):
            raise TypeError(f"width must be an int or float not {type(height).__name__}")
        self._height = height

    def move_position(self, position) -> tuple:
        self.position = position
        return self.position

@dataclass
class Square(Shape):
    
    # def __init__(self, position: tuple, width: float|int, height: float|int) -> None:
    #     super().__init__(position, width, height)

        #self.area = self.width*self.height
        #self.circumference = (super().width*2)+(super().height*2)

    @property
    def area(self):
        #print("area getter")
        return self.width*self.height

    # @area.setter
    # def area(self):
    #     #print("area setter")
    #     value = self.width*self.height
    #     self._area = value

    @property
    def circumference(self):
        #print("circumference getter")
        return self.width*2 + self.height*2

    # @circumference.setter
    # def circumference(self, value):
    #     #print("circumference setter")
    #     self._circumference = value

    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        else:
            return False

    def is_inside(self, point: tuple) -> bool:
        min = (self.position[0]-self.width/2, self.position[1]-self.height/2)
        max = (min[0]+self.width, min[1]+self.width)
        if min[0] <= point[0] <= max[0] and min[1] <= point[1] <= max[1]:
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
    
    def __init__(self, position: tuple, width: float|int) -> None:
        super().__init__(position, width, width)

        #self.area = ((super().width/2)**2)*math.pi
        #self.circumference = super().width * math.pi

    @property
    def area(self):
        #print("area getter")
        return ((self.width/2)**2) *math.pi

    # @area.setter
    # def area(self, value):
    #     #print("area setter")
    #     self._area = value

    @property
    def circumference(self):
        #print("circumference getter")
        return self.width * math.pi

    # @circumference.setter
    # def circumference(self, value):
    #     #print("circumference setter")
    #     self._circumference = value

    def is_unit_circle(self) -> bool:
        if self.position == (0,0) and self.width == 2:
            return True
        else:
            return False

    def is_inside(self, point: tuple) -> bool:
        distance = math.hypot(point[0]-self.position[0], point[1]-self.position[0])
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
