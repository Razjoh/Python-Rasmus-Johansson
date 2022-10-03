from __future__ import annotations
import sys, os
import unittest


#print(__file__)

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# we define a path that is on step up
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)
#print(path_to_vector_module)

from vector import Vector 

class TestVector(unittest.TestCase):

    def setUp(self):
        self.x, self.y = 1, 2

    def create_2D_vector(self) -> Vector:
        return Vector(self.x, self.y)

    def test_create_2D_vector(self):
        #v = Vector(1,2)
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (self.x, self.y))

    def test_create_3D_vector(self):
        v = Vector(1,2,3)
        self.assertEqual(v.numbers, (1,2,3))

    def test_create_empty_vector(self):
        with self.assertRaises(ValueError):
            v = Vector()

    def test_eaqual_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1, 2)
        self.assertEqual(v1, v2)

    def test_not_eaqual_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(-1, -2)
        self.assertNotEqual(v1, v2)

    def test_add_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1, 3)
        self.assertEqual(v1+v2, Vector(self.x+1, self.y+3))

    def test_getitem(self):
        v1 = self.create_2D_vector()
        for i, number in enumerate((1,2)):
            self.assertEqual(v1[i], number)

    #TODO: many more tests to be performed



if __name__ == "__main__":
    unittest.main()