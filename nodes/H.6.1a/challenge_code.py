import pennylane as qml
from pennylane import numpy as np
aux = 0
main = 1
n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

def add_two_unitaries(U, V):
    """A circuit to apply the sum of two unitaries non-deterministically.
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        V (array): A unitary matrix, stored as a complex array.
    """
    qml.Hadamard(wires=aux)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=aux)
'''
