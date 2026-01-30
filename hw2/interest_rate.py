# program calculates the final balance of an account with a 
# starting balance of $1000 at 5% interest rate after 3 years

def interest_calculator(A, p, n):
    # A: initial deposit
    # p: interest rate 
    # n: number of years
    final_bal = A * (1 + p/100) ** n
    return print(final_bal)


interest_calculator(1000, 5, 3)

