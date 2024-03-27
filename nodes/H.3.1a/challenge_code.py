import pennylane as qml
from pennylane import numpy as np
def mag_z_unitary(B, time):
    """Creates a unitary operator to evolve the state of an electron in 
    a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time (t) we evolve the electron state for.
        
    Returns:
        array[complex]: The unitary matrix implementing time evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    matrix = np.array([[0, 0], [0, 0]]) # CHANGE THIS
    return matrix

B, t = 0.1, 0.6
if unitary_check(mag_z_unitary(B, t)):
    print("The output is unitary for B =", B, "and t =", t, ".")
'''
