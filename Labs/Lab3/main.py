from geometry_shapes import Shape,Circle, Square
import os,sys

os.system("cls||clear")


"""
TODO:
- change or fix circle inheritance so that height does not exist, if kept hiden change __repr__/__str__ so it does not print
- write documentation for all classes and testing? with justifications for choices made  
- *implement drawfonction for clarification. Either as main function or as class methods 
- lookover and maybe improve error handeling
- *implement bonus assignments

"""

s1 = Shape((1,2), 1, 1)
print(s1)

print("="*100)

try:
    s2 = Shape((2,1),"a", 1)
except TypeError as err:
    print(err)
try:
    s1.move_position((2,2,2))
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)

print("="*100)

sq1 = Square((1,1), 8,2)
sq1.move_position((1,2))
print(sq1.circumference, sq1.area)
print(sq1.is_square())

print("="*100)

sq2 = Square((1,2), 1 , 2)

sq3 = Square((0,0), 8, 1)
sq4 = Square((0,0), 1, 3)
print(sq3 > sq4)

print("="*100)

cir1 = Circle((0,0), 2)
print(cir1)
print(cir1.is_unit_circle())
print(cir1.area)
print(cir1.circumference)

print("="*100)

cir2 = Circle((2,2), 2)
print(cir1 <= cir2)

print("="*100)
try:
    cir3 = Circle((1), 2)
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)

print("="*100)

cir4 = Circle((0,0), 2)
print(cir4.is_inside((0,1)))
print(cir4.is_inside((2,2)))
print(cir4.is_inside((.5,-.5)))

print("="*100)

sq5 = Square((0,0), 2, 2)
print(sq5.is_inside((-.5,-.5)))
print(sq5.is_inside((1,0)))
print(sq5.is_inside((3,2)))
sq5.move_position((4,4))
print(sq5.is_inside((1,0)))

