import pennylane as qml
from pennylane import numpy as np
@qml.qnode(dev)
def XH_plus_HZ():
    """Apply XH + HZ to |01> and return the state."""
    U_list = [np.kron(qml.PauliX.matrix, qml.PauliX.matrix),
              np.kron(qml.PauliZ.matrix, qml.PauliZ.matrix),
              np.kron(qml.PauliX.matrix, qml.PauliZ.matrix),
              np.kron(qml.PauliZ.matrix, qml.PauliX.matrix)]
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", XH_plus_HZ()[:4], ".")
'''
