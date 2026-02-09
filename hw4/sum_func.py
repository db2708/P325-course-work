# function computes & prints the sum of 1/k for k = 1, 2, ..., M for a user input end value M

def sum_1k(M):
    tot = 0
    for k in range(1, M+1):
        tot += 1/k

    return tot




