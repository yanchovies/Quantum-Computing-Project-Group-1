import objects.matrices.matrixElement as matEl
import objects.matrices.matrix as mat
import gates as G
import numpy as np
import matplotlib.pyplot as plt
import itertools
import math

if __name__ == "__main__":
    
    n = 4
    #target_state = [ 1,1]
    target_state = (bin(6)[2:])
    state_vector = []
    for i in range(2**n):
        if i == 0:
            state_vector.append([1])
        else:
            state_vector.append([0])
    
    state_vector = mat.Matrix(state_vector)

    
    g = G.Gates(n)
    H = g.Hadamard_gate()
    X = g.X_gate()
    Z = g.phase_gate()
    I = g.identity_gate()

    
    
    
        

    
    

    
    def oracle(n, target_state):
        oracle_matrix = I
        target_index = int("".join(map(str, target_state)), 2)
        t = matEl.MatrixElement(target_index,target_index,-1)
        oracle_matrix.assign(t)
        return oracle_matrix
    
    


    O = oracle(n, target_state)
    
    
    for i in range(1,n):
        H = mat.tensor_product(H, g.Hadamard_gate())
        X = X.tensorProduct(g.X_gate())
    
    
    #superposition state

    state_vector = H.multiply(state_vector)

    
    
    number_iterations = int(np.pi / 4 * np.sqrt(2**n))
 
    
    amplitude = []
    
    
    
    
    for i in range(number_iterations):
        
        #oracle
        state_vector = O.multiply(state_vector)
        #grover gates
        state_vector = H.multiply(state_vector)
        state_vector = X.multiply(state_vector)
        state_vector = Z.multiply(state_vector)
        state_vector = X.multiply(state_vector)
        state_vector = H.multiply(state_vector)
        
        amplitude.append(state_vector.maximum_element())
        
        
            
        
        
    def possible_states(n):
        """
        Returns all possible 1 and 0 combinations for a qubit of size n.
        """
        return list(itertools.product([0, 1], repeat=n))
    
    all_states = possible_states(n)
   
    final_state = []
    state_type = []
    
    for i in range(len(all_states)):
        state_type.append(str(all_states[i]))
        final_state.append(abs(state_vector.get_element(i,0)))
    
    target_position = final_state.index(max(final_state))
    print("The target is " + str(target_position))
    
    plt.bar(state_type, final_state)
    
    
    
    angles = np.arcsin(np.array(amplitude))




    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot a line from (0,0) to (cos(theta), sin(theta)) for each angle theta
    for i in angles:
        x = math.cos(i)
        y = math.sin(i)
        ax.plot([0, x], [0, y], '-o', label=f'{round(math.degrees(i),3)} degrees')

    # Set the limits of the x and y axes
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    # Set the labels for the x and y axes
    ax.set_xlabel('|state perpendicular to target state>')
    ax.set_ylabel('|target state>')
    ax.legend()
    # Set the title of the plot
    ax.set_title('Amplitude amplification of target state ')


    plt.show()
    
    
    
    


    

