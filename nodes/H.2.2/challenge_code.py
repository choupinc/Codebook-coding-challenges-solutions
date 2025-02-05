import pennylane as qml
from pennylane import numpy as np
n_bits = 1
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def unitary_circuit(operator):
    """Applies a matrix to the state if it is unitary and correctly sized.
    
    Args:
        operator (array[complex]): A square complex-valued array.

    Returns:
        array[complex]: The state of the quantum system, after applying the
        operator, if valid.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    return qml.state()
'''
