a, b, n = 0, 76, 16

# formula for step size between values
h = (b - a) / n

loop_vals = []

# loop method
for i in range(n + 1):
    loop_vals.append(a + i*h)

# comprehension method
comp_vals = [a + i*h for i in range(n + 1)]

print(loop_vals)
print(comp_vals)