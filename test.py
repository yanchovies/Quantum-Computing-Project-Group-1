import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
import numpy as np

from shor import run_shors_algorithm

if __name__ == "__main__":
    # mat1 = mat.Matrix([[1, 3], [4, 5]])
    # mat2 = mat.Matrix([[2, 8], [7, 4]])

    # result = mat1.tensor_product(mat2)
    # print(result)

    #arr1 = np.array([[1, 3], [4, 5]])
    #arr2 = np.array([[2, 8], [7, 4]])

    #result = mat.tensor_product(arr1, arr2)
    #print(result)

    """foo = matEl.MatrixElement(0, 0, 1.)
    bar = matEl.MatrixElement(2, 0, 1.)
    goo = matEl.MatrixElement(0, 2, 1.)
    bab = matEl.MatrixElement(2, 2, 1.)
    hof = matEl.MatrixElement(1, 1, 1.)
    mat = matEl.SparseMatrix([foo, bar, goo, bab, hof])

    print(mat)
    print(mat.numOfRows)
    print(mat.numOfCols)
    print(mat.getRow(0))
    print(mat.getCol(1))"""

    (fac1, fac2) = run_shors_algorithm(134676)
    print(fac1)
    print()
    print(fac2)
