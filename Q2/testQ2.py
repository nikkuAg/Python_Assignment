import unittest
import constants
from Main import Matrix

class Test_Matrix(unittest.TestCase):
    def test_add(self):
        self.assertEqual(constants.M11+constants.M11, [4])
        self.assertEqual(constants.M23 + constants.M231, [[5,7,9],[11,13,15]])
        with self.assertRaises(Exception):
            constants.M23+constants.M11
            constants.M32+constants.M33
    
    def test_sub(self):
        self.assertEqual(constants.M22-constants.M22, [[0,0],[0,0]])
        self.assertEqual(constants.M331 - constants.M33, [[3,-1,0],[4,-3,-1], [2,-2,-2]])
        with self.assertRaises(Exception):
            constants.M21-constants.M22
            constants.M32-constants.M23
    
    def test_determinant(self):
        self.assertEqual(constants.M11.det(), 2)
        self.assertEqual(constants.M33.det(), 0)
        self.assertEqual(constants.M221.det(), -2)
        with self.assertRaises(Exception):
            constants.M21.det()
            constants.M23.det()
    
    def test_multiplication(self):
        self.assertEqual(constants.M11*constants.M12, [2,4])
        self.assertEqual(constants.M33*constants.M32, [[40,46],[94,109],[148,172]])
        self.assertEqual(constants.M23*constants.M32, [[40,46],[94,109]])
        with self.assertRaises(Exception):
            constants.M21*constants.M331
            constants.M221*constants.M33

    def test_exponent(self):
        self.assertEqual(constants.M11**2, [4])
        self.assertEqual(constants.M33**1, [[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(constants.M33**3, [[468,576,684],[1062,1305,1548],[1656,2034,2412]])
        self.assertEqual(constants.M221**2, [[67,78],[91,106]])
        self.assertEqual(constants.M22**1, [[1,2],[3,4]])
        with self.assertRaises(Exception):
            constants.M21**2
            constants.M23**1

    def test_dimList(self):
        with self.assertRaises(Exception):
            Matrix(1,1,x=0, myList=constants.m22)
            Matrix(3,3,x=0, myList=constants.m23)
        


if __name__ == '__main__':
    unittest.main()
