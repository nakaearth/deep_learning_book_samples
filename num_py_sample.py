import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 8.0])

print(x + y)
print(y - x)
print(x * y)
print(x / y)

xx = np.array([[1, 2], [3, 4], [5, 6]])
print(xx)
print(xx.shape)
print(xx.dtype)
yy = np.array([[2, 4], [6, 8], [10, 12]])
print(xx + yy)
print(xx * yy)
print(yy * xx)
print(xx * 10)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

for row in A:
    print(row)

print ((A * B).flatten())
X = (A * B).flatten()
print(X[np.array([0, 2, 3])])
Y = X[np.array([0, 2, 3])]
print(Y[Y > 30])
