import objects.matrices.matrixElement as matEl
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
        U.append(c_amod15(a ** p % N, N), range(3 * len(bin(N)[2:])))

    return U.to_gate().control()


def c_amod15(a, N):
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

    # Step 2 - Checking if a and N share any common factors using the Euclidean algorithm
    factor = math.gcd(a, N)
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
    return factor1, factor2



