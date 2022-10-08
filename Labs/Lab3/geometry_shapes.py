from __future__ import annotations
from dataclasses import dataclass
import math

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


class Square(Shape):
    
    def __init__(self, position: tuple, width: float|int, height: float|int) -> None:
        super().__init__(position, width, height)

        self.area = super().width*super().height
        self.circumference = (super().width*2)+(super().height*2)

    @property
    def area(self):
        #print("area getter")
        return self._area

    @area.setter
    def area(self, value):
        #print("area setter")
        self._area = value

    @property
    def circumference(self):
        #print("circumference getter")
        return self._circumference

    @circumference.setter
    def circumference(self, value):
        #print("circumference setter")
        self._circumference = value

    def is_square(self) -> bool:
        if self.width == self.height:
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

        self.area = ((super().width/2)**2)*math.pi
        self.circumference = super().width * math.pi

    @property
    def area(self):
        #print("area getter")
        return self._area

    @area.setter
    def area(self, value):
        #print("area setter")
        self._area = value

    @property
    def circumference(self):
        #print("circumference getter")
        return self._circumference

    @circumference.setter
    def circumference(self, value):
        #print("circumference setter")
        self._circumference = value

    def is_unit_circle(self) -> bool:
        if self.position == (0,0) and self.width == 2:
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

s1 = Shape((1,2), 1, 1)
print(s1)

print("="*100)

try:
    s2 = Shape((2,1),"a", 1)
except TypeError as err:
    print(err)
try:
    s1.move_position((1,2))
except TypeError as err:
    print(err)

print("="*100)

sq1 = Square((1,1), 8,2)
sq1.move_position((1,2))
print(sq1.circumference, sq1.area)
print(sq1.is_square())

print("="*100)

sq2 = Square((1,2), 1 , 2)

# should not happen fix 
sq2.area = 2
print(sq2.area)

print("="*100)

sq3 = Square((0,0), 8, 1)
sq4 = Square((0,0), 1, 3)
print(sq3 > sq4)

print("="*100)

cir1 = Circle((0,0), 2)
print(cir1.is_unit_circle())
print(cir1.area)
print(cir1.circumference)

print("="*100)

cir2 = Circle((2,2), 2)
print(cir1 <= cir2)

print("="*100)
