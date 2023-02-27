import objects.matrices.matrix as mat

if __name__ == "__main__":
    mat1 = mat.Matrix([[1, 3], [4, 5]])
    mat2 = mat.Matrix([[2, 8], [7, 4]])

    result = mat1.tensor_product(mat2)
    print(result)

