from pathlib import Path
import matplotlib.pyplot as plt 
import json

def plot_temperatures(plotname, filename):

    """
    
    function takes in a plot and filename that contains temperature data for NYC & Mexico city
    and plots and savesthe data on a graph with time on the x-axis and temperature on the y-axis. 
    
    times: list containing the time data from the fil.e
    temps_nyc: list containing temp data for NYC from the file
    temps_mex: list containing temp data for Mexico City from the file

    plotname: string containing the name of the plot to be saved
    filename: string containing the name of the file with temp data for NYC and Mexico City
    
    """

    times = []
    temps_nyc = []
    temps_mex = []

    path = Path(filename)
    lines = json.loads(path.read_text())

    for row in lines:
        temps_nyc.append(row["temperature_newyorkcity"])
        temps_mex.append(row["temperature_mexicocity"])
        times.append(row["time"])
    
    # plots both sets of temp data on the same plot w/ different colors 
    fig, ax = plt.subplots()
    ax.plot(times, temps_nyc, ".", color="cornflowerblue",label = "New York City")
    ax.plot(times, temps_mex, ".", color="lightcoral", label = "Mexico City")

    # sets axis labels, plot title, and legend
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (C)")
    ax.set_title("Temperatures in New York City and Mexico City")
    ax.legend(loc="upper left")
    
    plt.savefig(plotname)
    

# plot_temperatures('temp_plot.png', 'weather_data.json')