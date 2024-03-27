import pennylane as qml
from pennylane import numpy as np
def rotate_and_controls():
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM THE BASIS ROTATION
    qml.CNOT([0,1])
    qml.Hadamard(0)
    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT([1,2])
    qml.CZ([0,2])