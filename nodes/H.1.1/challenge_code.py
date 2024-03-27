import pennylane as qml
from pennylane import numpy as np
input = [1, 1, 0] # MODIFY EXAMPLE
print("The result of applying the secret box to ", input, "is ")
# We will secretly apply the function and return the result!

def deterministic_box(bits):
    """Guess the secret deterministic rule.
    
    Args:
        bits (list[int]): A list of bits representing an initial condition.
         
    Returns: 
        list[int]: The output bits measured after deterministic evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return bits # MODIFY THIS
'''
