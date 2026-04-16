class Instrument:
    
    """
    defines class of lab instruments with methods to power on and calibrate the instrument.
    
    attributes:
    self.name: name of the instrument as a string
    self.is_on: boolean variable that tracks whether or not the instrument is on or off. initially set to False until power_switch is ran.
    
    methods:
    power_switch(): turns the instrument on
    calibrate(): prints a message stating the instrument is being calibrated.
    """

    def __init__(self, name):
        self.name = str(name)
        self.is_on = False

    def power_switch(self):
        self.is_on = True
    
    def calibrate(self):
        print(f"Calibrating {self.name}... Standard protocols applied.") 
    
class Thermometer(Instrument):
    
    """
    defines a thermometer as a subclass of the instrument class

    attributes:
    self.unit: the unit of the temperature measurement as a string
    
    methods:
    take_reading(value): checks if the thermometer is on, takes a temp reading and prints the value and its unit then returns true. 
        if the thermometer is off it prints an error message then returns false.
    
    """

    def __init__(self, name, unit='Celcius'):
        super().__init__(name)
        self.unit = unit
        
    def take_reading(self, value):
        if self.is_on == True:
            print(f"Reading: {value} {self.unit}")
            return True
        elif self.is_on == False:
            print("Error: Thermometer is off.")
            return False

class Spectrometer(Instrument):

    """
    defines a spectrometer as a subclass of the instrument class. 
    function runs the calibrate method from the parent class and prints an additional message about aligning the grating.

    super.calibrate(): runs the calibrate method from the parent class

    attributes:
    self.name: name of the spectrometer as a string
    
    methods:
    take_reading(wavelength): checks if the spectrometer is on then takes a reqading and prints a message before returning true.
        if the spectrometer is off an error message is printed and false is returned.
    """

    def __init__(self, name):
        super().__init__(name)

    def calibrate(self):
        super().calibrate()
        print("Aligning optical diffraction grating...")
    
    def take_reading(self, wavelength):
        if self.is_on == True:
            print(f"Scanning intensity at {wavelength} nm.")
            return True
        
        elif self.is_on == False:
            print("Error: Spectrometer is off.")
            return False