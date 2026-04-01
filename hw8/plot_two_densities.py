import matplotlib.pyplot as plt 
import numpy as np


def plot_densities(plotname, file_water, file_air):
    
    """
    
    script reads in data from two files containing temp and density data for water and air, separates each quantity into a list, and plots the data.
    the x axis is temp and the y axis is density in a log scale. the plot is then saved as a png with its name specified by the user.

    plotname: string containing the name of the plot to be saved
    file_water: string containing the name of the file with water data
    file_air: string containing the name of the file with air data
    
    w_data: 2D array containing the temp and density data for water
    w_density: list containing the density data for water
    w_temps: list containing the temp data for water
    
    a_data: 2D array containing the temp and density data for air
    a_density: list containing the density data for air
    a_temps: list containing the temp data for air
   
    """
    
    # here i read in the data files and separate the the temp & density data into separate lists
    w_data =  np.genfromtxt(file_water, skip_header=4, skip_footer=1, delimiter = '   ')
    w_density = w_data[:,0]
    w_temps = w_data[:,1]

    a_data = np.genfromtxt(file_air, skip_header=4, skip_footer=1, delimiter = '   ')


    a_density = a_data[:,0]
    a_temps = a_data[:,1]

    # here i convert the lists into arrays so i can plot them
    w_density_array = np.array(w_density)
    w_temp_array = np.array(w_temps)

    a_density_array = np.array(a_density)
    a_temp_array = np.array(a_temps)

    # plots the temp and density data for both files on the same plot w/ different colors and labels
    fig, ax = plt.subplots()
    ax.scatter(w_density_array, w_temp_array, color="cornflowerblue", label = "Water Densities")
    ax.scatter(a_density_array, a_temp_array, color="lightcoral", label = "Air Densities")

    ax.set_xlabel("Temperature (C)")
    ax.set_ylabel("Material Density")
    ax.set_title("Densities of Water and Air at Different Temperatures")
    ax.legend()

    plt.yscale("log")
    plt.savefig(plotname)

# plot_densities('density_plot.png', 'density_water.dat', 'density_air.dat',)