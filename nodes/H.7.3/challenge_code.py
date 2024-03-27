import pennylane as qml
from pennylane import numpy as np
@qml.qnode(dev)
def quantum_memory(beta_list):
    """Produce a data state with positive coefficients beta_list.

    Args:
        beta_list (array[float]): The amplitudes for our superposition.

    Returns: 
        array[float]: The state on both address and data registers.
    """
    U_list = [np.identity(2), np.identity(2), 
              np.identity(2), np.identity(2)] # MODIFY THIS
    ##################
    # YOUR CODE HERE #
    ##################
    return qml.state()

beta_list = [1, 0, 0, 1]
normalized_coefficients = [quantum_memory(beta_list)[i].item() for i in range(0, 20, 5)]
print("The amplitudes on the main register are proportional to", normalized_coefficients, ".")
'''
