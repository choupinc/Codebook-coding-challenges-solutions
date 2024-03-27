import pennylane as qml
from pennylane import numpy as np
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def naive_circuit():
    """Create a uniform superposition and return the probabilities.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    for wire in range(n_bits):

        ##################
        # YOUR CODE HERE #
        ##################

        pass # REPLACE PASS

    return qml.probs(wires=range(n_bits))
'''
