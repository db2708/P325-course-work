from math import cos, sin, pi, sqrt, ceil

# 1a

def trapezint1(func, a, b):

    """
    code approximates the integral of some function from point a to point b using trapezoids
    
    a: starting point
    b: ending point
    func: function being integrated over

    """

    integral = ((b-a)/2) * (func(a) + func(b))
    return integral


# 1b

def trapezint2(func, a, b):

    """
    code approximates the integral of some function from point a to point b using two trapezoids w/ equal base lengths
    
    a: starting point
    b: ending point
    func: function being integrated over
    h: width of the trapezoids
    midpt: midpoint of the interval [a, b]

    """

    h = (b-a)/2
    midpt = a + h

    integral = (h/2) * (func(a) + 2*func(midpt) + func(b))
    return integral

# 1c

def trapezint(func, a, b, n):


    '''
    code approximates the integral of some function from point a to point b using n equal sized trapezoids
    
    a: starting point
    b: ending point
    func: function being integrated over
    h: width of the trapezoids

    '''

    h = (b-a)/n
    integral = 0
    for i in range(0, n):
        integral += (1/2) * h * (func(a + i*h) + func(a + (i + 1) * h))
    return integral


# 2

def adaptive_trapezint(func, a, b, eps=1e-5):

    '''
    function approximates the integral from point a to b using the adaptive trapezoid method
    to calculate the number of intervals needed to reach the desired accuracy of E <= epsilon

    a: starting point
    b: ending point
    func: function being integrated over
    h_0: some initial step size used to calculate f''(x)
    n: number of intervals needed to reach the desired accuracy
    double_derivative: list of f''(x) values 

    '''

    N = 1000
    h_0 = (b-a)/N
    double_derivative = []
    
    for i in range(0,N):
        x = a + i*h_0
        double_derivative.append((func(x + h_0) - 2*func(x) + func(x - h_0)) / (h_0**2))
    
    max_dub_deriv = max(abs(x) for x in double_derivative)

    h = sqrt((12*eps) / ((b-a)*max_dub_deriv))
    
    n = int(ceil((b-a)/h))
    return trapezint(func, a, b, n)
