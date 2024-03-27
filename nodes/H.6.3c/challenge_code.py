import pennylane as qml
from pennylane import numpy as np
aux = [0, 1]
main = 2
all_bits = range(3)
dev = qml.device("default.qubit", wires=all_bits)

# Part (i)

@qml.qnode(dev)
def first_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

# Part (ii)

@qml.qnode(dev)
def second_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

# Part (iii)

@qml.qnode(dev)
def full_series(t):
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

##################
# HIT SUBMIT FOR #
# PLOTTING MAGIC #
##################
'''
