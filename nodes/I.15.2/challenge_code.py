import pennylane as qml
from pennylane import numpy as np
def entangle_qubits():
    ##################
    # YOUR CODE HERE #
    ##################

    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    qml.Hadamard(1)
    qml.CNOT([1,2])
