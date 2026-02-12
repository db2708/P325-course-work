# function computes path length of a polygon consisting of n + 1 points along 
# a circle with r = 0.5 and its error compared to pi for a user input value n

from math import cos, sin, pi, sqrt

def pi_estimate(n):

    '''
    function computes path length of a polygon consisting of n + 1 points along 
    circle with r = 0.5 and its error compared to pi for a user input value n.

    n - number of points along the circle
    length - the total length of the path defined by the x and y coordinates
    error - fractional error between calculated length and pi
    '''

    length = 0 
    x_list = []
    y_list = []

    for i in range(0, n+1):
        x_list.append(0.5 * cos((2*pi*i)/n))
        y_list.append(0.5 * sin((2*pi*i)/n))

    for i in range(0, n+1):
        length += sqrt((x_list[i] - x_list[i-1])**2 + (y_list[i] - y_list[i-1])**2)
        
    error = abs(length - pi)    
    return length, error



