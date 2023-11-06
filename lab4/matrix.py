class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of range")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of range")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                dot_product = sum(self.get(i, k) * other_matrix.get(k, j) for k in range(self.cols))
                result.set(i, j, dot_product)
        return result

    def apply_function(self, func):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set(i, j, func(self.get(i, j)))
        return result

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


def main():
    matrix = Matrix(2, 3)

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("Main matrix is:")
    print(matrix)

    transpose_matrix = matrix.transpose()
    print("Transposed matrix is:")
    print(transpose_matrix)

    multiply_matrix = matrix.matrix_multiply(transpose_matrix)
    print("Matrix Multiplication self with transposed:")
    print(multiply_matrix)

    transformed_matrix = matrix.apply_function(lambda x: x * 2)
    print("Transformed Matrix using lambda:")
    print(transformed_matrix)


if __name__ == "__main__":
    main()
