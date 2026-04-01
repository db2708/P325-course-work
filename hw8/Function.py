from math import e, sin

class Function:

    """
    
    function takes in two parameters, a & w, & calculates the value of e^(-ax)sin(wx) for a given x value.
    
    self.a: parameter a in the function
    self.w: parameter w in the function
    value(x): method that calculates the value of e^(-ax)sin(wx) for a, w, and x
    
    """
    def __init__(self, a, w):
        self.a = a
        self.w = w
    
    def value(self,x):
        val = e**(-self.a*x)*sin(self.w*x)
        return val
    
# func = Function(a=1.0, w=2.0)
# print(func.value(2))