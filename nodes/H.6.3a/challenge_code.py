import pennylane as qml
from pennylane import numpy as np
def V(t):
    """Matrix for the PREPARE subroutine."""
    return np.array([[np.sqrt(t)/np.sqrt(t+1), -1/np.sqrt(t+1)],
                    [1/np.sqrt(t+1), np.sqrt(t)/np.sqrt(t+1)]])

def exp_U_first(U, t):
    """Implement the first two terms in the Taylor series for exp(tU).
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        t (float): A time to evolve by.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    pass
'''
