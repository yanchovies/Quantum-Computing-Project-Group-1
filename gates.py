import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
import numpy as np


class Gates:
    def __init__(self, n):
        self.n = n
    
    def Hadamard_gate(self):
         H = [[1/(2**(1/2)), 1/(2**(1/2))], [1/(2**(1/2)), -1/(2**(1/2))]]
         H = mat.Matrix(H)
         return H
     
    def X_gate(self):
            
        el1 = matEl.MatrixElement(0, 1, 1.)
        el2 = matEl.MatrixElement(1, 0, 1.)   
        return matEl.SparseMatrix([el1, el2])
    
    def phase_gate(self):
        
        P = []
        for i in range(2**self.n):
            if i == (2**self.n - 1):
                P.append(matEl.MatrixElement(i, i, -1))
            else:
                P.append(matEl.MatrixElement(i, i, 1))
                
        
        return matEl.SparseMatrix(P)
    
    def identity_gate(self):
        I = []
        for i in range(2**self.n):
            I.append(matEl.MatrixElement(i, i, 1))
        
        return matEl.SparseMatrix(I)





