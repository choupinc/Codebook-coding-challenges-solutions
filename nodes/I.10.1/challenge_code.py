import pennylane as qml
from pennylane import numpy as np
dev = qml.device('default.qubit', wires=1)

@qml.qnode(dev)
def circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE AND MEASURE PAULI Y
    qml.RX(np.pi/4,0)
    qml.Hadamard(0)
    qml.Z(0)
    return qml.expval(qml.PauliY(0))

print(circuit())
