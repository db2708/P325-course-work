import numpy as np
import matplotlib.pyplot as plt
from fill_arrays_vectorized import gauss_points

# script creates a plot of the Gaussian function using the x and h values calculated in fill_arrays_vectors

xvals, hvals = gauss_points()


plt.plot(xvals, hvals, color = 'cornflowerblue')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Gaussian Function')
plt.savefig('pretty_gauss.png')