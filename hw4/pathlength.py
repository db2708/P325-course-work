# function computes & prints the length of a path defined 
# by two lists of x and y coordinates

from math import sqrt

def pathlength(x, y):
    length = 0 
    for i in range(1, len(x)):
        length += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return length
