from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Shape:
    #def __init__(self, yaxis: float, xaxis: float, *radius: float) -> None:
        # self._yaxis = yaxis
        # self._xaxis = xaxis
        # self._radius = tuple(float(r) for r in radius)
    
    position: tuple = (0,0) # form (x,y)
    radius: tuple|float|int = (1,1)

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
    def radius(self):
        #print("radius getter")
        return self._radius

    @radius.setter
    def radius(self, radius):
        #print("radius setter")
        if not isinstance(radius, (tuple,float,int)):
            raise TypeError(f"radius must be an tuple or float not {type(radius).__name__}")
        self._radius = radius

s1 = Shape((1,2), (1,1))
print(s1)

try:
    s2 = Shape((2,1),"a")
except TypeError as err:
    print(err)