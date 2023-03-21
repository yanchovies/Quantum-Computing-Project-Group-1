class Matrix:
    """
    This class represents matrices. In our implementation of Grover's and Shor's algorithms, we use
    matrices represented by this class interchangeably with matrices that are represented by SparseMatrix class.
    """

    def __init__(self, potentialMatrix):
        self.matrix = self.get_matrix(potentialMatrix)

    def get_matrix(self, potentialMatrix):
        if type(potentialMatrix) != list:
            raise Exception("Input cannot be a matrix")

        # then checking if not all elements inside a list are lists. If that is the case, we add extra dimension
        flag = True
        for elem in potentialMatrix:
            flag = isinstance(elem, list)
        if not flag:
            potentialMatrix = [potentialMatrix]

        # checking if every element is either an int or a float or complex
        for row in potentialMatrix:
            # here also checking if the matrix is a list of lists, hence 2-dimensional
            # if not isinstance(row, list):
            #     raise Exception("a matrix must be a two-dimensional list")
            for col in row:
                if not isinstance(col, int) and not isinstance(col, float) and not isinstance(col, complex):
                    raise Exception("elements of the matrix must be of type int or float")

        # checking if all rows have the same length
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
        return strings

    def get_number_of_rows(self):
        return len(self.matrix)

    def get_number_of_columns(self):
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


def tensor_product(matrix, otherMatrix):
    """
    This function computes a tensor product of two matrices of Matrix class.
    :param matrix, otherMatrix: matrices.
    :return: tensor product.
    """

    if (not isinstance(matrix, Matrix)) or (not isinstance(otherMatrix, Matrix)):
        raise Exception("The parameters of the function must be matrices")

    # this gives the matrix of the same size as the given matrix, but some of these elements are matrices now
    matrixOfMatrices = []
    for row in matrix.get_matrix_as_list():
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

    return Matrix(result)


def dot_product(matrix, otherMatrix):
    """
    This function computes a product of two matrices of Matrix class.
    :param matrix, otherMatrix: matrices.
    :return: a product of two matrices.
    """

    if (not isinstance(matrix, Matrix)) or (not isinstance(otherMatrix, Matrix)):
        raise Exception("The parameters of the function must be matrices")

    # base case
    if (matrix.get_number_of_rows() == 1) and (otherMatrix.get_number_of_columns() == 1):
        return sum([matrix.get_element(0, i) * otherMatrix.get_element(i, 0) for i in range(matrix.get_number_of_columns())])

    # if conditions for matrix multiplication are satisfied
    elif matrix.get_number_of_columns() == otherMatrix.get_number_of_rows():
        result = []
        for i in range(matrix.get_number_of_rows()):
            # empty list that represent rows of resultant matrix
            rows_in_result = []
            for j in range(otherMatrix.get_number_of_columns()):
                # calculating entries
                rows_in_result.append(dot_product(matrix.get_row_as_matrix(i), otherMatrix.get_column_as_matrix(j).transpose()))
            result.append(rows_in_result)

        return Matrix(result)
    else:
        raise Exception("Dimensions are different")
