from math import pi, sqrt, e

def gauss_points():
    
    """
    function uses list comprehension to calculate the x and h values for a 
    gaussian distribution with 41 evenly spaced points from [-4, 4]

    step_size: calculates the distance to be used to evevnly space the 41 points
    xvals: list of 41 evenly spaced points from [-4, 4]
    hvals: list of the corresponding h values for each x value.
    
    """
    
    step_size = (-4 -4)/40

    xvals = [-4 + i*step_size for i in range(41)]
    hvals = [1/sqrt(2*pi)*e**(-1/2*x**2) for x in xvals]
    return xvals, hvals

