import pennylane as qml
from pennylane import numpy as np
U_list = [np.kron(qml.PauliX.matrix, qml.PauliX.matrix),
          np.kron(qml.PauliZ.matrix, qml.PauliZ.matrix),
          np.kron(qml.PauliX.matrix, qml.PauliZ.matrix),
          np.kron(qml.PauliZ.matrix, qml.PauliX.matrix)]
alpha_list = [1, 0.5, 0.5, 1]

@qml.qnode(dev)
def my_circuit():
    """Apply H(X + Z/2) to the state |11> using LCU."""
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", my_circuit()[:4], ".")
'''
