"""import objects.matrices.matrixElement as matEl
import objects.matrices.matrix as mat
from gates import Gates

from qiskit import QuantumCircuit, Aer, transpile, assemble, circuit


import math
import random
from math import gcd


def finding_quantum_period(N, a):
    # Find the smallest power of 2 greater than or equal to 2*(N^2)
    n_count = 8 * [math.ceil(math.log2(N**2))]

    # Quantum circuit
    qc = QuantumCircuit(4 * len(n_count), len(n_count))

    # Initialize the first register
    qc.h(range(len(n_count)))

    # Initialize the second register
    qc.x(3 * len(n_count))

    for q in range(4 * len(n_count)):
        qc.append(controlled_U_op(N, a), [q] + [i + len(n_count) for i in range(3 * len(n_count))])

    qc.append(circuit.library.QFT(len(n_count), do_swaps=False).inverse(), range(len(n_count)))

    qc.measure(range(len(n_count)), range(len(n_count)))

    qasm_sim = Aer.get_backend('qasm_simulator')
    t_qc = transpile(qc, qasm_sim)
    qobj = assemble(t_qc, shots=2048)
    results = qasm_sim.run(qobj).result()
    counts = results.get_counts()
    return counts


def controlled_U_op(N, a):
    U = QuantumCircuit(4 * len(bin(N)[2:]))

    for p in range(N):
        U.append(c_amodN(a ** p % N, N), range(3 * len(bin(N)[2:])))

    return U.to_gate().control()


def c_amodN(a, N):
    if a == 0:
        return QuantumCircuit(3 * len(bin(N)[2:])).to_gate()
    elif a == 1:
        qc_temp = QuantumCircuit(3 * len(bin(N)[2:]))
        qc_temp.x(2 * len(bin(N)[2:]))
        return qc_temp.to_gate()
    else:
        raise NotImplementedError


def run_shors_algorithm(N):
    # Step 1 - Choosing a random integer a such that 1 < a < N
    a = random.randint(2, N - 1)
    print(a)

    # Step 2 - Checking if a and N share any common factors using the Euclidean algorithm
    factor = math.gcd(a, N)
    print(factor)
    if factor != 1:
        return factor, N // factor

    # Step 3 - Finding the period (r) of the function f(x) = a^x mod N
    period = finding_quantum_period(N, a)

    # Step 4 - Finding the best rational approximation p/q of y/2^m, where m is #qubits in the first register
    # We use Continued Fraction Algorithm for that
    r = None
    for output in period:
        frac = output / (2**len(bin(N)[2:]))
        candidate = int(frac * (2**(2 * len(bin(N)[2:]))))
        r = math.gcd(candidate, 2**(2 * len(bin(N)[2:])))
        if r != 1:
            break

    # Step 5 - Checking if the period is even. Otherwise, we run the algorithm again.
    if r % 2 != 0:
        return run_shors_algorithm(N)

    # Step 6 - Using the Euclidean algorithm to calculate the greatest common divisor (GCD)
    # of the integers (a^(r/2) ± 1) and N.
    factor1 = math.gcd(a**(r//2) + 1, N)
    factor2 = math.gcd(a**(r//2) - 1, N)

    # If any of the factors are trivial, we repeat the algorithm
    if factor1 == 1 or factor1 == N or factor2 == 1 or factor2 == N:
        return run_shors_algorithm(N)

    # The end - returning the factors
    return run_shors_algorithm(factor1), run_shors_algorithm(factor2)"""

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
        return 2, N // 2

    while True:
        a = random.randint(2, N - 1)
        print("current a is:", a)
        factor = gcd(a, N)

        # if gcd(a, N) is greater than N, then we get our non-trivial factor
        if factor > 1:
            return factor

        # calculating the period
        r = period_finding(a, N)
        print("current period is", r)

        if r % 2 == 0:
            x = mod_exp(a, r // 2, N)
            if x != N - 1:
                factor1 = gcd(x + 1, N)
                factor2 = gcd(x - 1, N)
                if factor1 != 1 and factor1 != N and factor2 != 1 and factor2 != N:
                    return factor1, factor2
