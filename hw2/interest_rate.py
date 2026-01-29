def interest_calculator(A, p, n):
    # A: initial deposit
    # p: interest rate 
    # n: number of years
    final_bal = A * (1 + p/100) ** n
    return print(final_bal)


interest_calculator(1000, 5, 3)

