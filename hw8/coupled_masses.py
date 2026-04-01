import numpy as np
from math import sqrt

def calculate_frequencies(mass, k):
    
    """

    function calculates the frequencies of a system of two masses coupled w/ three springs. 
    the frequencies are calculated by taking the square root of the eigenvalues of the k/m matrix.
    
    mx: 2x2 matrix representing the coupling of the masses and springs in the system
    k_over_m_mx: mx multiplied by k/m

    eigvals: list of the eigenvalues of the k/m matrix
    eigvecs: list of the eigenvectors of the k/m matrix

    """
    
    mx = np.array([[2,-1], [-1, 2]])
    k_over_m_mx = k/mass * mx

    eigvals, eigvecs = np.linalg.eig(k_over_m_mx)
    return tuple(sqrt(eigval) for eigval in eigvals)
