import pennylane as qml
from pennylane import numpy as np
k_bits = 2
n_bits = 2
all_bits = k_bits + n_bits
aux = range(k_bits)
main = range(k_bits, all_bits)
dev = qml.device("default.qubit", wires=all_bits)

def SELECT_uniform(U_list):
    """Implement the SELECT subroutine for 2^k unitaries.
    
    Args:
        U_list (list[array[complex]]): A list of unitary matrices, stored as 
        complex arrays.
    """
    for index in range(2**k_bits):
        ctrl_str =  np.binary_repr(index, k_bits) # Create binary representation
        ##################
        # YOUR CODE HERE #
        ##################
'''
