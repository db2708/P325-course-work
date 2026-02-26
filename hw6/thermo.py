def pressure(n, temperature, volume, units):

    """

    function calculates the pressure of an ideal gas using the Ideal Gas Law and checks for 
    valid inputs, else it raises a key, type, or zero division error.

    R: dictionary of ideal gas constants in different units
    n: number of moles or gas
    temperature: temperature of the gas in degrees kelvin
    volume: volume of the gas in liters
    units: units of desired ideal gas constant, must be one of the following: 
            'J/(mol*K)', 'L*atm/(mol*K)', or 'L*bar/(mol*K)'
    pressure: calculated pressure of the gas in units of the used constant

    """

    R = {'J/(mol*K)' : 8.31446, 'L*atm/(mol*K)' : 0.082057, 'L*bar/(mol*K)' : 0.0831446}

    if units not in R.keys():
        print(-1)
        raise KeyError("Unit not recognized. Please enter one of the following exactly it appears: " 
        "'J/(mol*K)', 'L*atm/(mol*K)', or 'L*bar/(mol*K)'")
    else:
        R = R[units]

    if type(n) not in [int, float] or type(temperature) not in [int, float] or type(volume) not in [int, float]:    
            print(-1)
            raise TypeError("One or more of your entered variables for n, temperature, or volume is not a number. " 
            "Please enter a valid number for each variable.")
    
    if volume == 0:
        print(-1)
        raise ZeroDivisionError("Volume entered cannot be zero. Please enter a non-zero value.")
    
    pressure = (n * R * temperature) / volume
    
    return pressure


