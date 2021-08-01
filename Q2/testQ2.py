import unittest
from Main import Matrix


class Test_Matrix(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(M11+M11, [4])
        self.assertEqual(M23 + M231, [[5,7,9],[11,13,15]])
        self.assertEqual(M23+M11, None)
        self.assertEqual(M32+M33, None)
    
    def test_sub(self):
        self.assertEqual(M22-M22, [[0,0],[0,0]])
        self.assertEqual(M331 - M33, [[3,-1,0],[4,-3,-1], [2,-2,-2]])
        self.assertEqual(M21-M22, None)
        self.assertEqual(M32-M23, None)
    
    def test_determinant(self):
        self.assertEqual(M11.det(), 2)
        self.assertEqual(M33.det(), 0)
        self.assertEqual(M21.det(), None)
        self.assertEqual(M23.det(), None)
        self.assertEqual(M221.det(), -2)
    
    def test_multiplication(self):
        self.assertEqual(M11*M12, [2,4])
        self.assertEqual(M33*M32, [[40,46],[94,109],[148,172]])
        self.assertEqual(M21*M331, None)
        self.assertEqual(M23*M32, [[40,46],[94,109]])
        self.assertEqual(M221*M33, None)

    def test_exponent(self):
        self.assertEqual(M11**2, [4])
        self.assertEqual(M33**1, [[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(M33**3, [[468,576,684],[1062,1305,1548],[1656,2034,2412]])
        self.assertEqual(M21**2, None)
        self.assertEqual(M23**1, None)
        self.assertEqual(M221**2, [[67,78],[91,106]])
        self.assertEqual(M22**1, [[1,2],[3,4]])

m11 = [2]
m12 = [1,2]
m13 = [1,2,3]
m21 = [[1], [2]]
m22 = [[1,2],[3,4]]
m221 = [[5,6], [7,8]]
m23 = [[1,2,3],[4,5,6]]
m231 = [[4,5,6], [7,8,9]]
m33 = [[1,2,3],[4,5,6],[7,8,9]]
m331 = [[4,1,3],[8,2,5],[9,6,7]]
m32 = [[4,5],[6,7], [8,9]]

M11 = Matrix(1,1,1, m11)
M12 = Matrix(1,2,1, m12)
M13 = Matrix(1,3,1, m13)
M21 = Matrix(2,1,1, m21)
M22 = Matrix(2,2,1, m22)
M221 = Matrix(2,2,1, m221)
M23 = Matrix(2,3,1, m23)
M231 = Matrix(2,3,1, m231)
M32 = Matrix(3,2,1, m32)
M33 = Matrix(3,3,1, m33)
M331 = Matrix(3,3,1, m331)


if __name__ == '__main__':
    unittest.main()
