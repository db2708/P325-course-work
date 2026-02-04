# program creates a list of epsilons from 10^0 to 10^-20 then calculates and
# prints the value of 1 + epsilon for all epsilons before printing the first
# value of 1 + epsilon that truncates to 1 due to finite memory limitations

# creates list of epsilons using list comprehension
epsilons = [10**(-i) for i in range(21)]

# calculates and prints the values for epsilon and 1 + epsilon for a given epsilon
for eps in epsilons:
    value = 1+ eps
    print(f'1 + {eps} = {value}')

# prints first epsilon that causes 1 + epsilon to truncate to 1
print(epsilons[16])
