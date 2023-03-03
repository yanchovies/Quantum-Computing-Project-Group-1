import objects.matrices.matrix as mat

if __name__ == "__main__":
    mat1 = mat.Matrix([[3], [5], [7]])
    mat2 = mat.Matrix([[2, 8], [7, 4]])

    result = mat.tensor_product(mat1, mat2)
    print(result)

