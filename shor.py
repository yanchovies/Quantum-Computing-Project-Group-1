import numpy as np
import gates as G
import random
import math
from fractions import Fraction

from objects.matrices.matrix import Matrix, tensor_product, dot_product


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N


def repeated_hadamard(h, n_of_qubits):
    # tensor product of some number of hadamard gates
    return tensor_product(h, h) if n_of_qubits == 2 else tensor_product(h, repeated_hadamard(h, n_of_qubits - 1))


def controlled_U_gate(a, N, n_of_qubits):
    # diagonal matrix where each diagonal entry is mod_exp(a, i, N)
    return Matrix(
        [[mod_exp(a, i, N) if i == j else 0 for i in range(2 ** n_of_qubits)] for j in range(2 ** n_of_qubits)])


def qft_calculation(n_of_qubits):
    qft = np.zeros((2 ** n_of_qubits, 2 ** n_of_qubits), dtype=complex)
    omega = np.exp(-2j * np.pi / (2 ** n_of_qubits))
    for i in range(2 ** n_of_qubits):
        for j in range(2 ** n_of_qubits):
            qft[i, j] = omega ** (i * j)
    return qft / np.sqrt(2 ** n_of_qubits)


def period_finding(a, N):
    # necessary number of qubits
    n_of_qubits = math.ceil(math.log2(N))

    # initialise register as a vector of dimension 2^n_of_qubits
    register = Matrix([0 for i in range(2 ** n_of_qubits)])  # np.zeros(2 ** n_of_qubits)
    # setting the first element to 1
    register.set_element(0, 0, 1)

    g = G.Gates(n_of_qubits)
    H = g.Hadamard_gate()

    # applying Hadamard gates
    register = dot_product(repeated_hadamard(H, n_of_qubits), register.transpose())

    # applying controlled-U gates
    register = dot_product(controlled_U_gate(a, N, n_of_qubits), register)

    # applying QFT
    register = dot_product(Matrix(qft_calculation(n_of_qubits).tolist()), register)

    # converting the register to a single list, then to a numpy array
    register = np.array(register.transpose().get_row(0))

    # measuring the register
    probabilities = np.abs(register) ** 2
    probabilities_normalized = probabilities / np.sum(probabilities)
    measured = np.random.choice(2 ** n_of_qubits, p=probabilities_normalized)

    # estimating the period
    r = Fraction(measured, 2 ** n_of_qubits).limit_denominator(N).denominator
    return r


def shors_algorithm(N):
    if N < 4:
        raise Exception("Number is too small")

    # if N is even, we can definitely give two factors
    if N % 2 == 0:
        #print("N is divisible by two, so it was easy to find the factors")
        return 2, N // 2

    while True:
        a = random.randint(2, N - 1)
        #print("current a is:", a)
        factor = gcd(a, N)

        # if gcd(a, N) is greater than N, then we get our non-trivial factor
        if factor > 1:
            #print("We managed to find two factors without quantum computation involved")
            return factor, N // factor

        # calculating the period
        r = period_finding(a, N)
        #print("current period is", r)

        if r % 2 == 0:
            # calculating a^(r/2) mod N since r is even
            x = mod_exp(a, r // 2, N)
            if x != N - 1:
                # calculating the non-trivial factors since a^(r/2) mod N is congruent to -1 (mod N)
                factor1 = gcd(x + 1, N)
                factor2 = gcd(x - 1, N)
                if factor1 != 1 and factor1 != N and factor2 != 1 and factor2 != N:
                    # if the factors are indeed non-trivial, we return them
                    #print("These factors were found with quantum computation involved")
                    return factor1, factor2
