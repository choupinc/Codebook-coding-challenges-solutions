import pennylane as qml
from pennylane import numpy as np
dev = qml.device('default.qubit', wires=3)

@qml.qnode(dev)
def controlled_rotations(theta, phi, omega):
    """Implement the circuit above and return measurement outcome probabilities.

    Args:
        theta (float): A rotation angle
        phi (float): A rotation angle
        omega (float): A rotation angle

    Returns:
        array[float]: Measurement outcome probabilities of the 3-qubit 
        computational basis states.
    """
    
    ##################
    # YOUR CODE HERE #
    ##################
    
    # APPLY THE OPERATIONS IN THE CIRCUIT AND RETURN MEASUREMENT PROBABILITIES
    qml.Hadamard(0)
    qml.CRX(theta, [0,1])
    qml.CRY(phi, [1,2])
    qml.CRZ(omega, [2,0])
    return qml.probs()

theta, phi, omega = 0.1, 0.2, 0.3
print(controlled_rotations(theta, phi, omega))