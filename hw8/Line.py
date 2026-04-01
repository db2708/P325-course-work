class Line:

    """
    
    function defines a line by two points and calculates the slope and y-intercept, then calculates the y value for any given x using y = mx + b
    
    p1, p2: tuples containing the x and y coords of the two points defining the line
    m: slope of the line 
    b: y-intercept of the line
    
    value(x): method that calculates the y value for a given x using the line equation y
    """
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
        # calculate slope & y-intercept
        self.m = (self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0])
        self.b = self.p1[1] - self.m*self.p1[0]

    def value(self, x):
        y = self.m * x + self.b
        return y
    
# line = Line(p1=(1,2), p2=(3,4))
# print(line.value(2))