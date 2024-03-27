import pennylane as qml
from pennylane import numpy as np
def SELECT(U_list):
    """Implement the SELECT oracle for 2^k unitaries."""
    for index in range(2**k_bits):
        ctrl_str = np.binary_repr(index, k_bits) # Create binary representation
        qml.ControlledQubitUnitary(U_list[index], control_wires=aux, 
                                   wires=main, control_values=ctrl_str)

def LCU(alpha_list, U_list):
    """Implement LCU using PREPARE and SELECT oracles for 2^k unitaries.
    
    Args:
        alpha_list (list[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices, stored as 
        complex arrays.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    pass
'''
