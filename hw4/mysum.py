# function allows user to imput a list of values that is then summed and printed

def my_sum(values):
    # sets total to zero to ensure sum isnt being added to the sum of a previous test case
    tot = 0
    for num in values:
        tot += num
    print(tot)



