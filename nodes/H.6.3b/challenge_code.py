import pennylane as qml
from pennylane import numpy as np
def exp_U_second(U, t):
    """Implement the second-order approximation of exp(tU).
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        t (float): A time to evolve by.
    """
    qml.QubitUnitary(V(t), wires=aux[0])    
    def subcircuit():
        ##################
        # YOUR CODE HERE #
        ##################
        pass
    qml.PauliX(wires=aux[0])
    # ADD CONTROLLED OPERATION HERE
    qml.PauliX(wires=aux[0])
    qml.QubitUnitary(np.transpose(V(t)), wires=aux[0])
'''
