import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def mag_z_0_v1(B, time):
    """Simulates an electron (initial state |0>) in a magnetic field, using a 
    unitary matrix.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        array[complex]: The state of the system after evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    return qml.state()
'''
