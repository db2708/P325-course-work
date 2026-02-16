from math import cos, sin, pi, sqrt

def trapezint1(func, a, b):

    """
    code approximates the integral of some function from point a to point b using trapezoids
    
    a: starting point
    b: ending point
    func: function being integrated over

    """

    integral = (b-a/2) * (func(a) + func(b))
    return integral

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
    for i in range(0, n-1):
        integral += 1/2 * h * (func(a + i*h) + func(a + (i + 1) * h))
    return integral

def adaptive_trapezint(func, a, b, eps=1e-5):
    N = 1000
    h_0 = (b-a)/N
    double_derivative = []
    
    for i in range(1,N):
        x = a + i*h_0
        double_derivative.append((func(x + h_0) - 2*func(x) + func(x - h_0)) / (h_0**2))
    
    max_dub_deriv = max(abs(x) for x in double_derivative)

    h = sqrt(12*eps) * ((b-a)*max_dub_deriv)**(-1/2)
    n = (b-a)/h

    return print(trapezint(func, a, b, int(n)))

adaptive_trapezint(sin, 0, pi)