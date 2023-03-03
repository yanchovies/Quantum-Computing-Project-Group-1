import numpy as np

class Gates:
    def __init__(self):
        pass
    
    
    def Hadamard(self):
        
        H = (1/np.sqrt(2))*np.array([[1,1], [1 , -1]])
        
        return H
    
    def X_gate(self):
        
        X = np.array([[0,1], [1,0]])
        return X
    
    def Y_gate(self):
        
        
        Y = np.array([[0, -1j], [1j , 0]])
        return Y
    
    
    def Z_gate(self):
        
        Z = np.array([[1,0], [0,-1]])
        return Z
        
    
    def P_gate(self, theta):
        
        P = np.array([[1,0], [0, np.exp(1j*theta)]])
        return P
    
    
    
gate = Gates()

        

N = 8
states = np.zeros((N, 2))
states[:, 0] = 1

target = 6


def tensor_product(A , B):
    
    if A.shape[0] == B.shape[0]:
    
        C = np.zeros((B.shape[0],))
        
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                C[i] = C[i] + A[i][j]*B[j]
        
        return C
    
    else:
        print("Cannot perform tensor product")


H = gate.Hadamard()
super = tensor_product(H,states[0])
print(super)


# Define the oracle function
def oracle(x, target):
    if x == target:
        return -1
    else:
        return 1
    
    
    
# superposition of states
for i ,state in enumerate(states):
    #states[i][0] = tensor_product(gate.Hadamard(), state)[0]
    #states[i][1] = tensor_product(gate.Hadamard(), state)[1]
    states[i] = tensor_product(gate.Hadamard(), state)
    
    
    
k = np.sqrt(N)

for i in range(int(k)):
    
    for j in range(N):
        states[j] = states[j]*oracle(j, target)
        
    print(states)
        
    
    #diffuser
    
    # return back to |00> basis
    for i ,state in enumerate(states):
        states[i] = tensor_product(gate.Hadamard(), state)
    
    
    #flipping all states orthogonal to the |00> basis
    #states[1:] = -1*states[1:]
    for i, state in enumerate(states):
        states[i] = tensor_product(gate.Z_gate(),state)
        
    for j in range(N):
        states[j] = states[j]*oracle(j, target)
    
    
    # return back to |s> basis
    for i ,state in enumerate(states):
        #states[i][0] = tensor_product(gate.Hadamard(), state)[0]
        #states[i][1] = tensor_product(gate.Hadamard(), state)[1]
        states[i] = tensor_product(gate.Hadamard(), state)
        
        
        
        
print(states)
    
    
    














