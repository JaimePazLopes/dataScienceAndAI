import numpy

my_list = [1,2,3]
arr = numpy.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = numpy.array(my_mat)
print(mat)

zeroTen = numpy.arange(0,11)
print(zeroTen)
zeroTenSkipTwo = numpy.arange(0,11,2)
print(zeroTen)

zeros = numpy.zeros(3)
print(zeros)
zeros = numpy.zeros((2,3))
print(zeros)

ones = numpy.ones(3)
print(zeros)
ones = numpy.ones((3,2))
print(ones)

zeroToOne = numpy.linspace(0,1,13)
print(zeroToOne)

id = numpy.eye(5)
print(id)

rand = numpy.random.rand(5,3)
print(rand)

rand = numpy.random.randint(1,101, 25)
print(rand)
rerand = rand.reshape(5,5)
print(rerand)

print(rand.argmax(), rand.max(), rand.argmin(), rand.min())
print(rand.shape, rerand.shape)
print(rand.dtype)

rand[0:5] = 99
print(rand)

rand2 = rand[0:5]
rand2[:] = 0
print(rand, rand2)

rand2 = rand.copy()[0:5]
rand2[:] = 33
print(rand, rand2)

arrayOf5 = numpy.arange(5,46,5)
print(arrayOf5)
arrayOf52D = arrayOf5.reshape(3,3)
print(arrayOf52D)

print(arrayOf52D[0], arrayOf52D[1,1], arrayOf52D[2][2])
print(arrayOf52D[:2])
print(arrayOf52D[:2,1:])

boolOf5 = arrayOf52D > 20
print(boolOf5)
print(arrayOf52D[boolOf5])
print(arrayOf52D[arrayOf52D>37])

arr = numpy.arange(0,11)
print(arr+arr)
print(arr-arr)
print(arr*arr)
print(arr/arr)
print(arr+33)
print(arr**2)
print(numpy.sqrt(arr))
print(numpy.sin(arr))












