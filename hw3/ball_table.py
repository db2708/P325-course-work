# program prints nicely formatted table of n+1 uniformly spaced t 
# values and their associated y values from 0 to 2*v_0/g 

# variables given in the problem
v_0 = 5 # m/s
g   = 9.81 # m/s^2
n   = 10 # intervals

# i used the formulas from coor.py to generate my t values from a = 0 to b= 2*v_0/g
a = 0
b = 2 * v_0 / g
h = (b - a) / n

# list of t values to plug into y(t)
t = [a + i*h for i in range(n + 1)]
for i in range(n + 1):
    t.append(a + i*h)

for time in t:
    y = v_0 * time - 0.5 * g * time**2
    print(time, y)

# both initial and final t and y values are their expected values of
# (t_0, y_0) = (0,0) and (t_n, y_n) = (2*v_0/g, 0) = (1.019..., 0.0)