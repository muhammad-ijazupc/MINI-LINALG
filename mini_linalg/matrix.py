class Matrix:
    def __init__(self, values):
        self.values = [list(row) for row in values]

        if self.values:
            cols = len(self.values[0])
            if any(len(row) != cols for row in self.values):
                raise ValueError("All rows must have the same length")

    def __matmul__(self, other):
        if not self.values or not other.values:
            raise ValueError("Matrices cannot be empty")

        if len(self.values[0]) != len(other.values):
            raise ValueError("Incompatible matrix dimensions")

        result = []
        for row in self.values:
            result_row = []
            for col in zip(*other.values):
                result_row.append(sum(a * b for a, b in zip(row, col)))
            result.append(result_row)

        return Matrix(result)

    def __repr__(self):
        return f"Matrix({self.values})"
