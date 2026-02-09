# function computes & prints the product of (x - r_i) for i = 0, 1, ..., n for 
# a user input value of x and a list of n + 1 roots r_i

def poly(x, roots):
    # sets polynomial to 1 inside to ensure product isnt being multiplied by previous test case list
    polynomial = 1
    for r_i in roots:
        polynomial *= x - r_i 
    print(polynomial)


