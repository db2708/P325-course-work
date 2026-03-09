from math import pi, sqrt, e
import numpy as np

def gauss_points():
    """
    function uses np.linspace to calculate the x and h values for a 
    gaussian distribution with 41 evenly spaced points from [-4, 4]

    xvals: list of 41 evenly spaced points from [-4, 4]
    hvals: list of the corresponding h values for each x value.

    """
    xvals = np.linspace(-4, 4, 41)
    hvals = 1/sqrt(2*pi)*e**(-1/2*xvals**2)

    return (xvals, hvals)

