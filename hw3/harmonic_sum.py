# program corrects the code given in the assignment 
# using the equation of the truncated harmonic sum

''' corrected code: '''

# defining & changing the names of starter variables to make them more descriptive
sum = 0
start = 1
end = 100

# changed 1/k to 1/value & indented sum+= line to be within the for loop
for value in range(start, end+1):
    sum += (1/value)
print(sum)

# using desmos sum should ≈ 5.18737751764, which matches the output of the corrected code


''' original code: '''

''' variables are not indicative of their purpose '''
# s = 0
# k = 1
# M = 100

''' line below is missing a colon at the end & the range should go to M+1, not M '''
# for value in range(k,M)

''' line below calculating s is not indented under the for loop. '''
''' s should be += 1/value b/c of the for value in range statement, not 1/k'''
# s += 1/k
# print(s)

