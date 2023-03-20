import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
import numpy as np

from shor import shors_algorithm
from grover_sparse import grovers_algorithm

if __name__ == "__main__":

    option = 1

    if option == 1:
        # run Grover's algorithm
        grovers_algorithm(8, 4)

    else:
        # run Shor's algorithm
        factors = shors_algorithm(135)
        print(factors)
