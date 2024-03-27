import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE
    qml.RX(np.arccos(3**(1/2)/2)*2, wires = 0)
    return qml.state()