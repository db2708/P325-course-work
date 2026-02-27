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

    R = {'J/(mol*K)' : 8.314, 'L*atm/(mol*K)' : 0.0820574587, 'L*bar/(mol*K)' : 0.08314}

    try:
        R = R[units]
    except KeyError:
        print("Unit not recognized. Please enter one of the following exactly it appears: " 
        "'J/(mol*K)', 'L*atm/(mol*K)', or 'L*bar/(mol*K)'")
        return -1

    try:
        pressure = (n * R * temperature) / volume
        return pressure
    except ZeroDivisionError:
        print("Volume entered cannot be zero. Please enter a non-zero value.")
        return -1
    except TypeError: 
        print("One or more of your entered variables for n, temperature, or volume is not a number. " 
        "Please enter a valid number for each variable.")
        return -1
    
    
    
