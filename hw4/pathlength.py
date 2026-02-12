from math import sqrt

def pathlength(x, y):

    '''
    function computes & returns the length of a path defined
    by two user inputted lists of x and y coordinates

    length - the total length of the path defined by the x and y coordinates
    x - list of all x path coordinates 
    y - list of all y path coordinates 
    '''

    length = 0 
    for i in range(1, len(x)):
        length += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return length
