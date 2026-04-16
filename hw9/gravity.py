import numpy as np
from scipy.optimize import curve_fit

def fit_data(filename):
    
    """
    function reads in data from a csv file containing time, position, and uncertainty data for a falling ball,
        then fits the data to a model and returns the value of gravity.
    
    filename: string containing the name of the csv file with the data
    time: list of time data from the file (units of seconds)
    position: list of position data from the file (units of meters)
    uncertainty: list of uncertainty data from the file (units of meters)

    model: function the data is fit to.
    y_0: ball's initial position
    v_0: ball's initial velocity
    g: acceleration due to gravity

    """
    
    # reads in data and saves each quantity into a separate list
    time, position, uncertainty = np.genfromtxt(filename, skip_header=1, delimiter = ',', unpack=True)
    
    # defines the model the data is fit to
    def model(t, y_0, v_0, g):
        y = y_0 + v_0*t + 1/2*g*t**2
        return y
    
    # fits the data to the model and saves the best fit parameters
    (y_0, v_0, g), pcov = curve_fit(model, time, position, sigma=uncertainty, absolute_sigma=True)
    
    return float(g)

# fit_data('ball.csv')
