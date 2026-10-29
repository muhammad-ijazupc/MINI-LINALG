from mini_linalg import Vector, Matrix

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1 + v2)
print(v1 - v2)

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(A @ B)