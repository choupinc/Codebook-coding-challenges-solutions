import pennylane as qml
from pennylane import numpy as np
num_wires = 3
dev = qml.device('default.qubit', wires=num_wires)

@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.
    
    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    b = list(map(int, np.binary_repr(basis_id, 3)))
    print(b)
    # CREATE THE BASIS STATE
    qml.BasisStatePreparation(b, range(3))
    return qml.state()


basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")