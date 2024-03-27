import pennylane as qml
from pennylane import numpy as np
n_list = range(3,7)
opt_steps = []

for n_bits in n_list:
    combo = "0"*n_bits # A simple combination
    step_list = range(1,10) # Try out some large number of steps
    ##################
    # YOUR CODE HERE #
    ##################
    pass

print("The optimal number of Grover steps for qubits in", [3,4,5,6], "is", opt_steps, ".")
'''
