import pennylane as qml
from pennylane import numpy as np
def ham_close_spins(B, J):
    """Creates the Hamiltonian for two close spins.

    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (list[float]): A vector of couplings [J_X, J_Y, J_Z].

    Returns:
        qml.Hamiltonian: The Hamiltonian of the system.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    coeffs = [] # MODIFY THIS
    obs = [] # MODIFY THIS
    return qml.Hamiltonian(coeffs, obs)
'''
