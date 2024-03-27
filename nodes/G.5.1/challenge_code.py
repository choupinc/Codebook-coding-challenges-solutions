import pennylane as qml
from pennylane import numpy as np
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires)

def oracle_multi(combos):
    """Implement multi-solution oracle using sequence of multi-controlled X gates.
    
    Args:
        combos (list[list[int]]): A list of solutions.
    """
    for combo in combos:
        combo_str = ''.join(str(j) for j in combo)
        ##################
        # YOUR CODE HERE #
        ##################
        pass
'''
