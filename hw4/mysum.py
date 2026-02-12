
def mysum(values):

    '''
    function allows user to input a list of values that is then summed and printed
    tot - the total sum of the values in the list
    num - the current number being added to the total sum
    '''
    
    # sets total to zero to ensure sum isnt being added to the sum of a previous test case
    tot = 0

    for num in values:
        tot += num
    return tot



