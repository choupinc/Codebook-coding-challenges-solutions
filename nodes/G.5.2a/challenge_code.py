import pennylane as qml
from pennylane import numpy as np
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires, shots=None)

def grover_iter_multi(combos, num_steps):
    """Run Grover search for multiple secret combinations and a number 
    of Grover steps.
    
    Args:
        combos (list[list[int]]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns: 
        array[float]: Probability for observing different outcomes.
    """
    @qml.qnode(dev)
    def inner_circuit():
        qml.PauliX(wires=n_bits)
        qml.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            ##################
            # YOUR CODE HERE #
            ##################
            diffusion(n_bits)
        return qml.probs(wires=query_register)
    
    return inner_circuit()
'''
