def interest_calculator(A, p, n):
    # A: initial deposit
    # p: interest rate 
    # n: number of years
    final_bal = A * (1 + p/100) ** n
    print(f"The bank account will contain ${round(final_bal,2)} after {n} years.")

interest_calculator(1000, 5, 3)

