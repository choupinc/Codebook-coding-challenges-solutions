import pennylane as qml
from pennylane import numpy as np
n_bits = 5
dev = qml.device("default.qubit", wires=n_bits)
    
##################
# YOUR CODE HERE #
##################
coeffs = [1] # MODIFY THIS
obs = [qml.PauliZ(0)] # MODIFY THIS
H = qml.Hamiltonian(coeffs, obs)

@qml.qnode(dev)
def energy(init):
    """Circuit for measuring expectation value of Hamiltonian in a given state.
    
    Args:
        init (list[int]): An initial computational basis state, specified by five bits.

    Returns: 
        float: Expectation value of the Hamiltonian H.
    """
    qml.BasisState(init, wires=range(n_bits))
    return qml.expval(H)'''
