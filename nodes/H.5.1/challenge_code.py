import pennylane as qml
from pennylane import numpy as np
n_bits=2
dev = qml.device("default.qubit", wires=range(n_bits))

@qml.qnode(dev)
def two_distant_spins(B, time):
    """Circuit for evolving the state of two distant electrons in a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron wavefunction for.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
