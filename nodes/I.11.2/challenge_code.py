import pennylane as qml
from pennylane import numpy as np
# Creates a device with *two* qubits
dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |+>|1>
    qml.Hadamard(0)
    qml.X(1)
    # RETURN TWO EXPECTATION VALUES, Y ON FIRST QUBIT, Z ON SECOND QUBIT

    return (qml.expval(qml.Y(0)),  qml.expval(qml.Z(1)))


print(two_qubit_circuit())
