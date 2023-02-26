class Matrix:
    def __init__(self, numOfRows, numOfCols):
        self.matrix = self.get_matrix(numOfRows, numOfCols)

    def get_matrix(self, numOfRows, numOfCols):
        matrix = [[0 for j in range(numOfCols)] for i in range(numOfRows)]
        return matrix

    """def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item] """

    def get_element(self, i, j):
        return self.matrix[i - 1][j - 1]

    def set_element(self, i, j, element):
        self.matrix[i - 1][j - 1] = element

    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def get_transpose(self):
        # return self.get_readable_matrix_string(self.transpose(self.matrix))
        return self.transpose(self.matrix)

    # def doTranspose(self):
    #    self.matrix = self.transpose(self.matrix)

    def multiply(self, otherMatrix):
        result = [[0 for j in range(len(otherMatrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(otherMatrix[0])):
                for k in range(len(otherMatrix)):
                    result[i][j] += self.matrix[i][k] * otherMatrix[k][j]
        return result

    def get_multiply(self, otherMatrix):
        # return self.get_readable_matrix_string(self.multiply(matrix))
        return self.multiply(otherMatrix)

    """def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num * other for num in row] for row in self.matrix]) """

    def tensor_product(self, otherMatrix):
        # this gives the matrix of the same size as the given matrix, but some of these elements are matrices now
        result = [[num * otherMatrix for num in row] for row in self.matrix]

        # splitting interior matrices into elements of one "big" matrix
        # TODO: implement this

        return result
