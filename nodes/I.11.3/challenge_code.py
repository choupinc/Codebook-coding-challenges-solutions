import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def create_one_minus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |1>|->
    # PREPARE |1>|->
    qml.X(0)
    
    qml.X(1)
    qml.Hadamard(1)
    
    #why it doesn't work?
    #qml.adjoint(qml.RY)(np.pi/2, 1)
    
    # RETURN A SINGLE EXPECTATION VALUE Z \otimes X

    return qml.expval(qml.Z(0) @ qml.X(1))


print(create_one_minus())