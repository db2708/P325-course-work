a = 3.3 
a_sq = a**2
b = 5.3
b_sq = b**2

eq1_sum = a_sq + 2*a*b + b_sq
eq2_sum = a_sq - 2*a*b + b_sq
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print(f'First equation: {eq1_sum}, {eq1_pow}')
print(f'Second equation: {eq2_sum}, {eq2_pow}')