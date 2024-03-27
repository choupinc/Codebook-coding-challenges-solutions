import pennylane as qml
from pennylane import numpy as np
k_bits = 2
n_bits = 2
all_bits = k_bits + n_bits
aux = range(k_bits)
main = range(k_bits, all_bits)
dev = qml.device("default.qubit", wires=all_bits)

def PREPARE(alpha_list):
    """Create the PREPARE oracle as a matrix.
    
    Args:
        alpha_list (array[float]): A list of coefficients.

    Returns: 
        array[complex]: The matrix representation of the PREPARE routine.
    """
    zero_vec = np.array([1] + [0]*(2**k_bits - 1))
    ##################
    # YOUR CODE HERE #
    ##################
'''
