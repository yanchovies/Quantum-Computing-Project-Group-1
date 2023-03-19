class Matrix:

    def __init__(self, potentialMatrix):
        self.matrix = self.get_matrix(potentialMatrix)

    def get_matrix(self, potentialMatrix):
        if type(potentialMatrix) != list:
            raise Exception("Input cannot be a matrix")
        elif type(potentialMatrix[0]) != list:
            potentialMatrix = [potentialMatrix]

        listOfLenghts = []
        for row in potentialMatrix:
            listOfLenghts.append(len(row))

        if len(set(listOfLenghts)) > 1:
            raise Exception("The rows of the matrix are of unequal length")

        return potentialMatrix

    def get_matrix_as_list(self):
        return list(self.matrix)

    def get_readable_matrix_string(self):
        strings = []
        for row in self.matrix:
            strings.append(row)
        # return '\n'.join(strings)
        return strings

    def get_number_of_rows(self):
        # return len(self.matrix.__dict__.get(next(iter(self.matrix.__dict__))))
        return len(self.matrix)

    def get_number_of_columns(self):
        # return len(self.matrix.__dict__.get(next(iter(self.matrix.__dict__)))[0])
        return len(self.matrix[0])

    def get_element(self, i, j):
        return self.matrix[i][j]

    def set_element(self, i, j, element):
        self.matrix[i][j] = element

    def get_row(self, i):
        return self.matrix[i]

    def get_column(self, j):
        result = []
        for i in range(len(self.matrix)):
            result.append(self.matrix[i][j])

        return result

    def get_row_as_matrix(self, i):
        return Matrix(self.matrix[i])

    def get_column_as_matrix(self, j):
        result = []
        for i in range(len(self.matrix)):
            result.append(self.matrix[i][j])

        return Matrix(result)

    def transpose(self):
        matrix = self.matrix
        return Matrix([list(i) for i in zip(*matrix)])

    """def get_transpose(self):
        # return self.get_readable_matrix_string(self.transpose(self.matrix))
        return self.transpose(self.matrix)"""

    def multiply(self, otherMatrix):
        result = [[0 for j in range((otherMatrix.get_number_of_columns()))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range((otherMatrix.get_number_of_columns())):
                for k in range((otherMatrix.get_number_of_rows())):
                    result[i][j] += self.matrix[i][k] * otherMatrix.get_element(k, j)
        return Matrix(result)

    def get_multiply(self, otherMatrix):
        # return self.get_readable_matrix_string(self.multiply(matrix))
        return self.multiply(otherMatrix)

    def maximum_element(self):

        max_abs_val = 0

        for row in self.matrix:
            for num in row:
                abs_val = abs(num)
                if abs_val > max_abs_val:
                    max_abs_val = abs_val
        return max_abs_val

    def multiply_matrix_by_constant(self, const):
        result = []
        for i in range(len(self.matrix)):
            resultRow = []
            for j in range(len(self.matrix[0])):
                resultRow.append(const * self.matrix[i][j])
            result.append(resultRow)

        return result


# class Operators:
import numpy as np


def tensor_product(matrix, otherMatrix):
    use_ndarrays = False
    if isinstance(matrix, np.ndarray) and isinstance(otherMatrix, np.ndarray):
        use_ndarrays = True
        matrix = Matrix(matrix.tolist())
        otherMatrix = Matrix(otherMatrix.tolist())

    if (not isinstance(matrix, Matrix)) or (not isinstance(otherMatrix, Matrix)):
        raise Exception("The parameters of the function must be matrices")

    # this gives the matrix of the same size as the given matrix, but some of these elements are matrices now
    # matrixOfMatrices = [[otherMatrix.multiply_matrix_by_constant(num) for num in row] for row in
    # matrix.__dict__.get(next(iter(matrix.__dict__)))]
    matrixOfMatrices = []
    for row in matrix.__dict__.get(next(iter(matrix.__dict__))):
        helper = []
        for num in row:
            helper.append(otherMatrix.multiply_matrix_by_constant(num))
        matrixOfMatrices.append(helper)

    # splitting interior matrices into elements of one "big" matrix
    result = []
    for currentRow in matrixOfMatrices:

        # creating an empty list of lists which will then turn into our resultant matrix
        intermediateResult = []
        for i in range(otherMatrix.get_number_of_rows()):
            intermediateResult.append([])

        for matrixInternal in currentRow:
            for j in range(len(matrixInternal)):  # note that len(matrixInternal) = len(otherMatrix)
                intermediateResult[j].extend(matrixInternal[j])

        result.extend(intermediateResult)

    if use_ndarrays:
        return np.array(result)
    else:

        return Matrix(result)


def dot_product(matrix, otherMatrix):
    if (not isinstance(matrix, Matrix)) or (not isinstance(otherMatrix, Matrix)):
        raise Exception("The parameters of the function must be matrices")

    if (matrix.get_number_of_rows() == 1) and (otherMatrix.get_number_of_columns() == 1):

        """if matrix.get_number_of_rows() != otherMatrix.get_number_of_rows():
            raise Exception("Dimensions do not match")
        else:"""
        return sum([matrix.get_element(0, i) * otherMatrix.get_element(i, 0) for i in range(matrix.get_number_of_columns())])

    elif matrix.get_number_of_columns() == otherMatrix.get_number_of_rows():
        result = []
        for i in range(matrix.get_number_of_rows()):
            rows_in_result = []
            for j in range(otherMatrix.get_number_of_columns()):
                rows_in_result.append(dot_product(matrix.get_row_as_matrix(i), otherMatrix.get_column_as_matrix(j).transpose()))
            result.append(rows_in_result)

        return Matrix(result)
    else:
        raise Exception("Dimensions are different")


# tensor product with numpy array
def tensor_product_numpy(A, B):
    m, n = A.shape
    p, q = B.shape
    C = [[0 for _ in range(n * q)] for _ in range(m * p)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                for l in range(q):
                    C[i * p + k][j * q + l] = A[i][j] * B[k][l]

    C = np.array(C)
    return C
