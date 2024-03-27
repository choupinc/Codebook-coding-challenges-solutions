import pennylane as qml
from pennylane import numpy as np
n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def zz_circuit(alpha, time, init):
    """Circuit for evolving two electrons with a ZZ interaction.
    
    Args:
        alpha (float): The strength of the interaction.
        time (float): The time we evolve the electron wavefunction for.
        init (array[int]): An initial state specified by two bits [x, y]. Prepare the
            system in this state prior to applying the time evolution circuit.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.probs(wires=range(n_bits))
'''
