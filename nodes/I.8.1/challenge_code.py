import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE
    qml.RX(np.pi/2, wires = 0)
    qml.adjoint(qml.T)(wires = 0)
    return qml.state()
