import pennylane as qml
from pennylane import numpy as np
@qml.qnode(dev)
def two_close_spins_X(B, J, time, n):
    """Circuit for evolving the state of two electrons with an X coupling.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (float): The strength of the coupling between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    beta = -J*hbar/4
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()
'''
