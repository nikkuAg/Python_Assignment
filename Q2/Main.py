
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

