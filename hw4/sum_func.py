

def sum_1k(M):

    '''
    function computes & prints the sum of 1/k for k = 1, 2, ..., M for a user input value of M
    M - the upper limit of the sum
    tot - the total sum of 1/k for the current k
    '''

    tot = 0
    for k in range(1, M+1):
        tot += 1/k

    return tot




