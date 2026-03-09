import numpy as np
import matplotlib.pyplot as plt

# script calculates the height of a ball thrown upwards as a fucntion of time then plots it


v_0 = 10 # m/s
g = 9.8 # m/s^2

y = []

# generates 50 evenly spaced points between 0 and 2*v_0/g

t = np.linspace(0, 2*v_0/g, 50)

for time in t:
    y.append(v_0*time - 1/2*g*time**2)


plt.plot(t, y, color = 'cornflowerblue')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height of a Ball Thrown Upwards')
plt.savefig('plot_ball1.png')