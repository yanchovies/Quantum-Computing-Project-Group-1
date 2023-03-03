# Import required modules
import math
import random

# Define the oracle function
def oracle(x, target):
    if x == target:
        return -1
    else:
        return 1

# Define the diffusion operator
def diffusion(n):
    H = [[2/n for i in range(n)] for j in range(n)]
    for i in range(n):
        H[i][i] -= 1
    return H

# Define the Grover search function
def grover_search(N, oracle_func):
    # Set the number of qubits and iterations
    n = math.ceil(math.log2(N))
    k = round(math.pi/4 * math.sqrt(N))
    
    # Initialize the state vector
    state = [1/math.sqrt(N) for i in range(N)]
    
    # Choose a random target value
    target = random.randint(0, N-1)
    print("The target is: " + str(target))
    
    # Apply the Grover iterations
    for i in range(k):
        # Apply the oracle function
        for j in range(N):
            state[j] *= oracle_func(j, target)
        
        # Apply the diffusion operator
        H = diffusion(N)
        #break
        #state = [[sum([H[j][k]*state[k] for k in range(N)])] for j in range(N)]
        
        
        for j in range(N):
            inner_list = []
            for k in range(N):
                inner_list.append(H[j][k] * state[k])
            state[j] = ([sum(inner_list)])

            
    # Measure the result
    return state.index(max(state))

# Test the function
N = 16
result = grover_search(N, oracle)
print(f"Found {result} as the target value.")
