import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires=1, shots=100000)

dev = qml.device("default.qubit", wires=1, shots=100000)

@qml.qnode(dev)
def circuit():
    qml.RX(np.pi/4, wires=0)
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)

    ##################
    # YOUR CODE HERE #
    ##################

    # RETURN THE MEASUREMENT SAMPLES OF THE CORRECT OBSERVABLE

    return qml.sample(qml.PauliY(0))


def compute_expval_from_samples(samples):
    """Compute the expectation value of an observable given a set of 
    sample outputs. You can assume that there are two possible outcomes,
    1 and -1. 
    
    Args: 
        samples (array[float]): 100000 samples representing the results of
            running the above circuit.
        
    Returns:
        float: the expectation value computed based on samples.
    """

    estimated_expval = 0
    plusOne = 0
    minusOne = 0
    
    ##################
    # YOUR CODE HERE #
    ##################

    # USE THE SAMPLES TO ESTIMATE THE EXPECTATION VALUE
    for i in samples:
        if i == 1:
           plusOne+=1
        if i == -1:
            minusOne+=1
    
    estimated_expval = (plusOne-minusOne) / len(samples)
        
        
    return estimated_expval


samples = circuit()
print(compute_expval_from_samples(samples))
