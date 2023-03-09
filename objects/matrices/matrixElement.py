class MatrixElement:
    def __init__(self, i, j, value):
        self.i = int(i)
        self.j = int(j)
        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __float__(self):
        try:
            return float(self.value)
        except ValueError:
            raise ValueError("Invalid matrix element: " + str(self.value))


class SparseMatrix:
    def __init__(self, elements):
        self.elements = self.get_elements(elements)
        self.numOfRows = self.get_number_of_rows()
        self.numOfCols = self.get_number_of_columns()

    def __str__(self):
        matrix = "["
        for i in range(0, self.numOfRows):
            row = self.get_raw_row(i)
            for idx, elem in enumerate(row):
                if type(elem) == MatrixElement:
                    row[idx] = elem.value
            matrix = matrix + str(row)
            if i != self.numOfRows - 1:
                matrix = matrix + "\n "
            else:
                matrix = matrix + "]"
        return str(matrix)

    def get_elements(self, elements):
        matrix = []
        for element in elements:
            if type(element) != MatrixElement:
                raise TypeError("Invalid matrix element: " + str(element))
            matrix.append(element)
        return matrix

    def get_matrix(self):
        matrix = []
        for i in range(0, self.numOfRows):
            row = self.get_raw_row(i)
            for idx, elem in enumerate(row):
                if type(elem) == MatrixElement:
                    row[idx] = elem.value
            matrix.append(row)
        return matrix

    def get_number_of_rows(self):
        return max([element.i for element in self.elements]) + 1

    def get_number_of_columns(self):
        return max([element.j for element in self.elements]) + 1

    def get_raw_row(self, i):
        row = []
        for j in range(0, self.numOfCols):
            val = 0.
            for element in self.elements:
                if element.i == i and element.j == j:
                    val = element
            row.append(val)
        return row

    def get_raw_col(self, j):
        row = []
        for i in range(0, self.numOfCols):
            val = 0.
            for element in self.elements:
                if element.j == j and element.i == i:
                    val = element
            row.append(val)
        return row

    def getRow(self, i):
        raw = self.get_raw_row(i)
        for idx, elem in enumerate(raw):
            if type(elem) == MatrixElement:
                raw[idx] = elem.value
        return raw

    def getCol(self, i):
        raw = self.get_raw_col(i)
        for idx, elem in enumerate(raw):
            if type(elem) == MatrixElement:
                raw[idx] = elem.value
        return raw
    
    def addEl(self, element):
        for preElem in self.elements:
            if (preElem.i == element.i and preElem.j == element.j):
                Exception("Element already exists at given position")
            else:
                self.elements.append(element)
                self.numOfRows = self.get_number_of_rows()
                self.numOfCols = self.get_number_of_columns()

    def tensorProduct(self, other):
        if type(other) != SparseMatrix:
            raise TypeError("Invalid matrix type: " + str(type(other)))
        elements = []
        for element in self.elements:
            for otherElement in other.elements:
                elements.append(MatrixElement(element.i * other.numOfRows + otherElement.i, element.j * other.numOfCols + otherElement.j, element.value * otherElement.value))
        return SparseMatrix(elements)
