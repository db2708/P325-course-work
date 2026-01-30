# program to calculate the time required to cook an egg starting from fridge and room temperature

from math import log, pi
M_sm = 47 # g small egg
M_lg = 67 # g large egg
rho  = 1.038 # g/cm**3 density of egg
c    = 3.7 # J/gK
k    = 5.4*10**-3 # W/cmK
T_w  = 100 # C 
T_y  = 70 # C
T_o  = [4, 20] # C

# first part of the equation thats present in both calculations for simplicity

t_eq_1     = (M_lg**(2/3) * c * rho**(1/3)) / (k * pi**2 * (4*pi/3)**(2/3))

# calculated time for both fridge and room temperature eggs
t_fridge   = t_eq_1 * log(0.76*(T_o[0] - T_w)/(T_y - T_w))
t_roomtemp = t_eq_1 * log(0.76*(T_o[1] - T_w)/(T_y - T_w))

print(t_fridge, t_roomtemp)