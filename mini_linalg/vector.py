
class Vector:
    def __init__(self, values):
        self.values = list(values)

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same dimension")
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same dimension")
        return Vector([a - b for a, b in zip(self.values, other.values)])

    @staticmethod
    def batch_add(vectors_a, vectors_b):
        if len(vectors_a) != len(vectors_b):
            raise ValueError("Batch sizes must match")
        return [a + b for a, b in zip(vectors_a, vectors_b)]

    def __repr__(self):
        return f"Vector({self.values})"
