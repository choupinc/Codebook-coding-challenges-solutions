import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # PREPARE THE STATE
    prepare_psi()
    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS

    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES
    qml.adjoint(y_basis_rotation)()
    return qml.probs(0)

print(measure_in_y_basis())
