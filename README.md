# Quantum-Computing-Project-Group-1

This project is from the Quantum computing Project from the University of Edinburgh. This aim of the project is to implement, and test a program to simulate a quantum computer. Grover's algorithm is then run to search an unordered list on the simulator. Shor's method for factorisation was also implemented on the quantum simulator. A web app was made to allow a user interact with the quantum simulator.

### BACKEND CODE

The objects folder contains the two matrices that was used in writing the simulators:

matrix.py
   
    This class represents matrices. In our implementation of Grover's and Shor's algorithms, we use
    matrices represented by this class.
    
    Within the matrix.py, we have a tensor_product function that computes a tensor product of two matrices of the Matrix class
    We also have a dot_product function that computes a product of two matrices of Matrix class.

matrixElement.py
   This file contains the MatrixElement class and the SparseMatrix class
   The Matrixelement class represents elements of a sparse matrix
   The SparseMatrix class represents lists of the Matrixelement objects.
   

gates.py
  This file contains a class called Gates, whose functions are the Hadamard gate, X gate, phase gate and the identity gate. The hadamard gate returns the hadamard operator for two qubits in our Matrix object form. The other functions returns their corresponding gates in the Sparse Matrix object form. 
  
grover_sparse.py
  oracle function
   
    This function produces the oracle gate.
    :param g: an object of Gates class.
    :param target_state: the target state.
    :return: the oracle gate.
   
   
    
    The grover_algorithm runs the grover algorithm on the quantum simulator.
    
Shor.py runs the shor algorithm on the quantum simulator. 

### Frontend

Flask framework in python combined with html, css and Javascript was used to provide an interactive process for a user.
    



