import numpy

arrayOfZeros = numpy.zeros(10)
print(arrayOfZeros)

arrayOfOnes = numpy.ones(10)
print(arrayOfOnes)

arrayOfFives = numpy.ones(10)
arrayOfFives = arrayOfFives * 5
print(arrayOfFives)

arra10to50 = numpy.arange(10,51)
print(arra10to50)

arra10to50E = numpy.arange(10,51,2)
print(arra10to50E)

array33 = numpy.arange(0,9)
matrix33 = array33.reshape((3,3))
print(matrix33)

id33 = numpy.eye(3)
print(id33)

random1 = numpy.random.rand(1)
print(random1)

random25 = numpy.random.randn(25)
print(random25)

array100 = numpy.arange(0.01,1.01,0.01)
matrix1010 = array100.reshape(10,10)
print(matrix1010)

array1002 = numpy.linspace(0.01,1,100)
matrix10102 = array1002.reshape(10,10)
print(matrix10102)

array20 = numpy.linspace(0,1,20)
print(array20)

mat = numpy.arange(1,26).reshape(5,5)
mat1 = mat[2:,1:]
print(mat1)
print(mat[3,4])
print(mat[0:3,1:2])
print(mat[-1])
print(mat[3:5])

print(mat.sum())
print(mat.std())
print(mat.sum(axis=0))


