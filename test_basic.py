
from mini_linalg import Vector, Matrix


def test_vector_addition():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert (v1 + v2).values == [5, 7, 9]


def test_vector_subtraction():
    v1 = Vector([4, 5, 6])
    v2 = Vector([1, 2, 3])
    assert (v1 - v2).values == [3, 3, 3]


def test_matrix_multiplication():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    assert (A @ B).values == [[19, 22], [43, 50]]


def test_vector_scalar_multiplication():
    v = Vector([1, 2, 3])
    assert (v * 2).values == [2, 4, 6]
    assert (2 * v).values == [2, 4, 6]


def test_vector_dot_product():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1.dot(v2) == 32
