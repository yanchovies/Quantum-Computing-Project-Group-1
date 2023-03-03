import numpy as np

def get_Hadamard():
    
    H = (1 / np.sqrt(2) * np.array([[1, 1],[1, -1]]))
    return H

def get_CNOT():
 
    
    CNOT =(np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0, ]]))

    return CNOT


def grover_gate(n):
    
    N = 2**n

    matrix_G = np.ones((N, N)) * 2 / N

    for i in range(N):
        matrix_G[i, i] -= 1

    G = (matrix_G)

    return 