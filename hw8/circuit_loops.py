import numpy as np

def solve_circuit(v1, v2, r1, r2, r3):

    """
    
    function solves for the currents in a circuit with two loops and three resistors. current is
    solved for by taking the inverse of the resistance matrix and multiplying it by the voltage matrix.
    
    v1, v2: voltage sources in the circuit
    r1, r2, r3: resistances in the circuit
    R_mx: 2x2 matrix of the resistances in the circuit
    V_mx: 2x1 matrix of the voltage sources in the circuit
    
    I_mx: calculated 2x1 matrix of the currents in the circuit
    
    """
 
    # creates the resistance and voltage matrices based on the input values
    R_mx = np.array([[r1+r2, -r2],[-r2, r2+r3]]).reshape(2,2)
    V_mx = np.array([v1, -v2]).reshape(2,1)

    # calculates the currents by taking the inverse of R_mx and multiplying it by V_mx
    I_mx = np.linalg.inv(R_mx) @ V_mx

    return I_mx

# solve_circuit(9, 1.5, 100, 220, 330)