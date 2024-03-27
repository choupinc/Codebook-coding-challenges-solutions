import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

input = 0 # MODIFY EXAMPLE
reps = 1
print("The probability distribution after applying the secret box to ", input)
print("a total of ", reps, "time(s) is ")
# We will secretly apply the function and return the result!

@qml.qnode(dev)
def quantum_box(bit, reps):
    """Implements the secret quantum rule on a single (qu)bit.
    
    Args:
        bit (int): A bit representing an initial condition.
        reps (int): Number of times gate is repeated.

    Returns:
        list[float]: The output probability distribution.
    """
    if bit == 1:
        qml.PauliX(wires=0)
    for _ in range(reps):
        ##################
        # YOUR CODE HERE #
        ##################
        pass
    return qml.probs(wires=0)
'''
