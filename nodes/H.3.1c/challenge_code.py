import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def mag_z_0_v2(B, time):
    """Simulates an electron (initial state |0>) in a magnetic field, using a 
    Z rotation.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        array[complex]: The state of the system after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

B, t = 0.1, 0.6
if np.allclose(mag_z_0_v1(B, t), mag_z_0_v2(B, t)):
    print("The two circuits give the same answer!")
'''
