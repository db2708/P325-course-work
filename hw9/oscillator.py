import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def fit_data(filename, plotname):
    
    """
    function reads in data from a csv file containing time, position, and uncertainty data for a mass on a spring
        then fits the data to a model and plots the data with error bars, its best fit curve, and the envelope and saves the plot.
    
    filename: string containing the name of the csv file with the data
    plotname: string containing the name of the plot to be saved

    time: list of time data from the file (units of seconds)
    position: list of position data from the file (units of meters)
    uncertainty: list of uncertainty data from the file (units of meters)
    
    model: function the data is fit to
    A: amplitude of oscillation
    gamma: damping coefficient
    omega: angular frequency
    phi: phase shift

    """
    
    # reads in data and saves each quantity into a separate list
    time, position, uncertainty = np.genfromtxt(filename, skip_header=1, delimiter = ',', unpack=True)
    
    # defines the model the data is fit to
    def model(t, A, gamma, omega, phi):
        x = A * np.exp(-gamma * t) * np.cos(omega * t + phi)
        return x
    
    # fits the data to the model and saves the best fit parameters
    (A, gamma, omega, phi), pcov = curve_fit(model, time, position, sigma=uncertainty, absolute_sigma=True)

    # calculates the best fit curve and the envelope using parameters from the fit
    fit_position = model(time, A, gamma, omega, phi)
    envelope = A * np.exp(-gamma * time)
    
    # plots the data with error bars, the best fit curve, and the envelope to the same plot
    fig, ax = plt.subplots()

    ax.errorbar(time, position, yerr=uncertainty, c='palevioletred', fmt='o', alpha=0.9, label='Measured')
    ax.plot(time, fit_position, c='cornflowerblue', label='Best fit')
    ax.plot(time, envelope, c='lightcoral', ls='--', label='Envelope')
    ax.plot(time, -envelope, c='lightcoral', ls='--')
   
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Position (cm)')
    ax.legend()
   
    fig.savefig(plotname)
    plt.show()
    
# fit_data('spring.csv', 'fit_plot.png')
