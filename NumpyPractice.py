import numpy as np

# making ndarrays in numpy
a = np.array([1, 2, 3]) # 3x1 ndarray
b = np.array([1.1, 2.2, 3.3]) # 3x1 ndarray with floats
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3 ndarray
d = np.zeros([3, 5]) # 3x5 ndarray (all 0)
e = np.ones([2, 3, 5]) # 2x3x5 ndarray (all 1)
f = np.empty([3, 4]) # 3x4 ndarray (random from memory)
g = np.arange(3, 10) # evenly spaced 1d ndarray from 3-10 (stepsize = 1)
h = np.arange(10, 20, 2.5) # evenly spaced 1d ndarray from 3-10 (stepsize = 2.5)
j = np.linspace(2, 8, 12) # evenly spaced 1d ndarray from 2-12 with 12 steps
i = np.ones_like(j) # creates ndarray of ones in the shape of j
k = np.arange(6) # evenly spaced 1d ndarray from 0-6
l = k.reshape(2, 3) # reshape k to a 2x3 ndarray
m = np.arange(24).reshape(2, 3, 4) # creates a 2x3x4 ndarray
n = np.random.random([2, 3, 4]) # 2, 3, 4 ndarray (random from 0-1)
o = np.random.random([2, 3, 4]).reshape(-1, 8) # reshapes ndarray to _x8 (must be possible)

numpyArrs = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
for index, arr in enumerate(numpyArrs):
    print(chr(ord('a') + index).upper()+", shape:", np.shape(arr))
    print(arr, "\n")

# make an ndarray from a function
func = lambda a, b, c : a + 2*b + 3*c # doesn't have to be a lambda function
a = np.fromfunction(func, (2, 3, 2))
print(a)
for entry in a.flat: print(entry)
for subarr in a: print(subarr)

# matrix business: (All arithmetic operations are elementwise)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.arange(16).reshape(4,4)
print(a * b) # elementwise multiplication
print(a**2) # elementwise exponentiation
print(a+2) # elementwise addition
a*=b # set a to a*b
print(a)
# various numerical niceties
print(a.min(), a.max(), a.sum(), a.mean()) 
print(c, c.sum(axis=0), c.cumsum(axis=1), sep="\n")
print(c.min(axis=0), c.max(axis=1), sep="\n")

# universal functions: also operate elementwise
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.exp(a), np.sqrt(a), np.add(a, b), np.sin(a), sep="\n")
a[0, 1] = -33
a[1, :] = 100
print(a)

# shallow copy vs deep copy
a = np.arange(12).reshape(3, 4)
b = a[:,0]
b[:] = -100
print(a)    # shallow copy
a = np.arange(12).reshape(3, 4)
b = a[:,0].copy()
b[:] = -100
print(a)    # deep copy

# linalg submodule!
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([0.8, -3])
print(np.dot(a, b), a.dot(b), a @ b, np.matmul(a, b), sep="\n") # matrix multiplication (a @ b shortcut requires python 3.5 or higher)
print(np.transpose(a), a.transpose(), a.T, sep="\n") # matrix transpose
print(np.eye(3)) # identity matrix
print(np.linalg.inv(a)) # inverse of a
print(np.linalg.norm(a)) # norm of a
print(np.linalg.cond(a)) # condition number of a
print(np.linalg.det(a)) # determinant of a
print(np.linalg.matrix_rank(a)) # rank of a
print(np.trace(a)) # sum over diagonal of a
print(np.linalg.solve(a, c)) # solving linear equations