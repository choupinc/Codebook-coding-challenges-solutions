import pennylane as qml
from pennylane import numpy as np
input = 0 # MODIFY EXAMPLE

trials = 100 # INCREASE TRIALS TO IMPROVE APPROXIMATION
print("On input", input, "the approximate probability distribution is")
# We will secretly apply the function and return the result!

def random_box(bit):
    """Guess the secret random rule.
    
    Args:
        bit (int): A bit representing the initial condition.
         
    Returns: 
        int: The output bit measured after random evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return bit # MODIFY THIS
'''
