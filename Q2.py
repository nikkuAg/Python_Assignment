import unittest


class Matrix:
    def __init__(self, row, column,x=0, myList=[]):
        self.row = row
        self.column = column
        if(row!=1):
            self.matrix = [[0 for x in range(column)] for y in range(row)]
        else:
            self.matrix = [0 for x in range(column)]
        if x==1:
            self.matrix = myList


    def __str__(self):
        if(self.row !=1):
            for x in range(self.row):
                print(self.matrix[x])
        else:
            print(self.matrix)
        return ""
        
    def __add__(self, other):
        if(other.row == self.row) and (other.column == self.column):
            Smatrix = Matrix(self.row, self.column, 0) 
            if(self.row==1):
                for x in range(self.row):
                    Smatrix.matrix[x] = self.matrix[x] + other.matrix[x]
            else:
                for x in range(self.row):
                    for y in range(self.column):
                        Smatrix.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
            return Smatrix.matrix
            
        else:
            print("Matries are not compatible for addition")

    def __sub__(self, other):
        if(other.row == self.row) and (other.column == self.column):
            SUmatrix = Matrix(self.row, self.column, 0)
            if(self.row==1):
                for x in range(self.row):
                    SUmatrix.matrix[x] = self.matrix[x] + other.matrix[x]
            else:
                for x in range(self.row):
                    for y in range(self.column):
                        SUmatrix.matrix[x][y] = self.matrix[x][y] - other.matrix[x][y]
            return SUmatrix.matrix
            
        else:
            print("Matries are not compatible for subtraction")

    def multiplication(self, row, column):
        sum = int(0)
        x=y=0
        while((x<len(row)) and (y<len(column))):
            sum += row[x] * column[y]
            x += 1
            y += 1
        return sum

    def __mul__(self, other):
        if(self.column == other.row):
            Mmatrix = Matrix(self.row, other.column, 0)
            test = []
            if(self.row==1 and other.row==1):
                for x in range(other.column):
                    Mmatrix.matrix[x] = self.matrix[0]*other.matrix[x]
            elif(self.row==1 and other.row !=1):
                for y in range(other.column):
                    test.clear()
                    for a in range(other.row):
                        test.append(other.matrix[a][y])
                    Mmatrix.matrix[y] = self.multiplication(self.matrix, test)
            elif(self.row!=1 and other.row==1):
                for x in range(self.row):
                    for y in range(other.column):
                        Mmatrix.matrix[x][y] = self.matrix[x][0] * other.matrix[y]
            else:
                for x in range(self.row):
                    for y in range(other.column):
                        test.clear()
                        for a in range(other.row):
                            test.append(other.matrix[a][y])
                        Mmatrix.matrix[x][y] = self.multiplication(self.matrix[x], test)
            return Mmatrix.matrix
        else:
            print("Matries are not compatible for multiplication")

    def __pow__(self, other):
        if(self.row == self.column):
            test = Matrix(self.row, self.column, 0)
            if(other == 1):
                test.matrix = self.matrix.copy()
                return test.matrix
            elif other == 2:
                test.matrix = self.__mul__(self)
                return test.matrix
            else:
                test.matrix = self ** (int(other)-1)
                test.matrix = (self * test)
                return test.matrix
        else:
            print("Matrix is not compatible for finding exponential")


    def coFactor(self, r, c):
        if(self.row == 1):
            return self.matrix[0]
        a = int(self.row) - 1
        test = Matrix(a, a, 0)
        i=j=0
        for x in range(self.row):
            if(x != r):
                for y in range(self.column):
                    if(y != c):
                        test.matrix[i][j] = self.matrix[x][y]
                        j += 1
                i += 1
            j=0
        return test.matrix

    def det(self):
        if(self.row==self.column):
            if(self.row == 1):
                return self.matrix[0]
            elif (self.row == 2):
                return (self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0])
            else:
                sum = 0
                for x in range(self.column):
                    sign = int(-1) ** int(x)
                    a = int(self.row) - 1
                    co_factor = Matrix(a, a, 0)
                    co_factor.matrix = self.coFactor(0, x)
                    sum += sign * self.matrix[0][x] * co_factor.det()
                return sum       
        else:
            print("Matrix is not compatible for finding determinant")

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


if __name__ == '__main__':
    unittest.main()
