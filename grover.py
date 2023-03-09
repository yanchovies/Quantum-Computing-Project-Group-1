import objects.matrices.matrixElement as matEl
import objects.matrices.matrix as mat

import numpy as np

if __name__ == "__main__":
    
    n = 3
    target_state = [ 0, 1,0]
    state_vector = np.zeros(2**n, dtype = 'complex')
    state_vector[0] = 1
    
    
    
    
    def Hadamard_gate():
        
        H =  1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
        return H
    
    
    def X_gate():
        
        el1 = matEl.MatrixElement(0, 1, 1.)
        el2 = matEl.MatrixElement(1, 0, 1.)
        
        return mat.SparseMatrix([el1, el2])
    
    
    def phase_gate(n):
        
        Z = np.eye(2**n)
        
        Z[-1][-1] = -1
        
        return Z
        
    def tensor_product(A, B):
        m, n = A.shape
        p, q = B.shape
        C = [[0 for _ in range(n*q)] for _ in range(m*p)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    for l in range(q):
                        C[i*p+k][j*q+l] = A[i][j] * B[k][l]
                        
        C = np.array(C)
        return C
    
    

    
    def oracle(n, target_state):
        oracle_matrix = np.identity(2 ** n)
        target_index = int("".join(map(str, target_state)), 2)
        oracle_matrix[target_index, target_index] = -1
        return oracle_matrix
    
    

    H = Hadamard_gate()
    X = X_gate()
    Z = phase_gate(n)
    O = oracle(n, target_state)
    
    
    for i in range(1,n):
        H = tensor_product(H,  Hadamard_gate())
        X = tensor_product(X,X_gate())
    
    
       
    state_vector = H @ state_vector
    

    
    number_iterations = int(np.pi / 4 * np.sqrt(2**n))
    
    
    
    
    for i in range(number_iterations):
        
        #oracle
        state_vector = O @ state_vector
        
        
        #grover gates
        state_vector = H @ state_vector
        state_vector = X @ state_vector
        state_vector = Z @ state_vector
        state_vector = X @ state_vector
        state_vector = H @ state_vector
        
        
    
    print(state_vector)
    idx = np.argmax(np.abs(state_vector))  # Find the index of the element with largest magnitude
    target = bin(idx)[2:]
    print(target)
    
    

