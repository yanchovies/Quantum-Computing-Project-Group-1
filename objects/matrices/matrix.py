class Matrix:
    """
    def __init__(self, numOfRows, numOfCols):
        self.matrix = self.get_matrix(numOfRows, numOfCols)

    def get_matrix(self, numOfRows, numOfCols):
        matrix = [[0 for j in range(numOfCols)] for i in range(numOfRows)]
        return matrix

    def get_readable_matrix_string(self, matrix):
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

    def __init__(self, potentialMatrix):
        self.matrix = self.get_matrix(potentialMatrix)

    def get_matrix(self, potentialMatrix):
        listOfLenghts = []
        for row in potentialMatrix:
            listOfLenghts.append(len(row))
            #listOfLenghts.append(row.shape[0])

        if len(set(listOfLenghts)) > 1:
            raise Exception("The rows of the matrix are of unequal length")

        # TODO: Should also check if entries are floats?

        return potentialMatrix

    def get_readable_matrix_string(self):
        strings = []
        for row in self.matrix:
            strings.append(row)
        #return '\n'.join(strings)
        return strings

    def get_number_of_rows(self):
        # return len(self.matrix.__dict__.get(next(iter(self.matrix.__dict__))))
        return len(self.matrix)

    def get_number_of_columns(self):
        #return len(self.matrix.__dict__.get(next(iter(self.matrix.__dict__)))[0])
        return len(self.matrix[0])

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

    def multiply_matrix_by_constant(self, const):
        result = []
        for i in range(len(self.matrix)):
            resultRow = []
            for j in range(len(self.matrix[0])):
                resultRow.append(const * self.matrix[i][j])
            result.append(resultRow)

        return result


# class Operators:

def tensor_product(matrix, otherMatrix):
    #if (not isinstance(matrix, Matrix)) or (not isinstance(otherMatrix, Matrix)):
    #    raise Exception("The parameters of the function must be matrices")

    # this gives the matrix of the same size as the given matrix, but some of these elements are matrices now
    # matrixOfMatrices = [[otherMatrix.multiply_matrix_by_constant(num) for num in row] for row in matrix.__dict__.get(next(iter(matrix.__dict__)))]
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

    return result
