def diff(poly):
    
    """
    function takes a polynomial represented as a dictionary and returns its derivative as a new dictioanry.
    the keys of the dictionary represent the power x is being raised to while the values represent the coefficients.

    poly: dictionary containing original polynomial exponents and coefficients
    derivative: dictionary containing the exponents and coefficients of the derivative of poly,
        where the keys equal the original key minus one and the values equal the original key times the original value.
    
    """
    
    # l1 represents the original polynomial
    # poly dict = {l1_key,l1_value}
    # deriv dictioary = {l2_key,l2_value}
    # where l2_key = l1_key - 1 & l2_value = l1_key*l1_value
   
    derivative = {}
    for l1_key, l1_value in poly.items():
        if l1_key != 0:
            l2_key = l1_key - 1
            l2_value = l1_key * l1_value
            derivative[l2_key] = l2_value
    return derivative

