import pennylane as qml
from pennylane import numpy as np
m_list = range(3)
opt_steps = []

for m_bits in m_list:
    combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2**m_bits)]
    step_list = range(1,10)
    ##################
    # YOUR CODE HERE #
    ##################
    pass

print("The optimal number of Grover steps for the number of solutions in", [1,2,4], "is", opt_steps, ".")
'''
