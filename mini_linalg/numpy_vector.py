import numpy as np


class NumPyVector:
    def __init__(self, values):
        self.values = np.array(values)

    def __add__(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Vectors must have the same dimension")
        return NumPyVector(self.values + other.values)

    def __sub__(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Vectors must have the same dimension")
        return NumPyVector(self.values - other.values)

    def dot(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Vectors must have the same dimension")
        return np.dot(self.values, other.values)

    def __repr__(self):
        return f"NumPyVector({self.values.tolist()})"
