from Main import Matrix

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


M11 = Matrix(1,1,x=1, myList=m11)
M12 = Matrix(1,2,x=1, myList=m12)
M13 = Matrix(1,3,x=1, myList=m13)
M21 = Matrix(2,1,x=1, myList=m21)
M22 = Matrix(2,2,x=1, myList=m22)
M221 = Matrix(2,2,x=1, myList=m221)
M23 = Matrix(2,3,x=1, myList=m23)
M231 = Matrix(2,3,x=1, myList=m231)
M32 = Matrix(3,2,x=1, myList=m32)
M33 = Matrix(3,3,x=1, myList=m33)
M331 = Matrix(3,3,x=1, myList=m331)