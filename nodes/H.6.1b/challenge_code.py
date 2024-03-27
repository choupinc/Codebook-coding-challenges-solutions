import pennylane as qml
from pennylane import numpy as np
@qml.qnode(dev)
def X_plus_Z():
    """Apply X + Z to |0> and return the state."""
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

print("The amplitudes on the main register are proportional to", X_plus_Z()[:2], ".")
'''
