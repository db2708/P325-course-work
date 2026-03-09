from pathlib import Path
from math import sqrt

def read_data(filename):

    """
    program reads in data from a file and calculates the mean and standard deviation of the data set.
    if the file is empty, a warning message is printed and the function returns a tuple of None, None.
    if the file contains any NULL or NaN values, a warning message is printed for each instance and those values are passed.

    temp: a list that hold the temperature data from the file
    mu_sum: variable that holds the sum of the temperature data for calculating the mean
    mu: the mean of the temperature data
    sigma_sum: variable that holds the sum of the squared differences between the mean and each temp
    sigma: the standard deviation of the temperature data

    """

    temp = []
    mu_sum, sigma_sum = 0, 0

    path = Path(filename)
    contents = path.read_text().splitlines()[1:]
    if contents == []:
        print("Warning: No data found in selected file. Please check the contents and file name and try again.")
        return None, None
    else:
        for line in contents:
            key, val = line.split(' ')

            # checks the lower case values for null and nan incase capitalization varies in the file
            if val.lower() == 'null' or val.lower() == 'nan':
                print(f"Warning: NULL or Nan value found at key: {key}. This value will be skipped during the calculations.")
                pass
            else:
                temp.append(float(val))
        
        N = len(temp)

        for i in range(0, N):
            mu_sum += temp[i]
            mu = mu_sum/N

        for i in range(0, N):    
            sigma_sum += (temp[i] - mu)**2
            sigma = sqrt(sigma_sum/N)
        
        return mu, sigma


