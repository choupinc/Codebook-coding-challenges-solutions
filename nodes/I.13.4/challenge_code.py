import pennylane as qml
from pennylane import numpy as np
dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def four_qubit_mcx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT ABOVE USING A 4-QUBIT MULTI-CONTROLLED X
    qml.broadcast(qml.Hadamard,'single', [0,1,2])
    qml.MultiControlledX([0, 1, 2], wires=3, control_values="001")
    return qml.state()


print(four_qubit_mcx())
