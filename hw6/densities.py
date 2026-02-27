from pathlib import Path

def read_densities(filename):
    
    """
    function reads in a text file containing the names and densities of various materials.
    it then splits each line of the file into its name and density components and stores 
    them in a dictionary, where the keys are the names of the material and the values are the densities.
    
    """
    
    path = Path(filename)
    lines = path.read_text().splitlines()
    densities = {}

    for line in lines:
        parts = line.rsplit(' ', 1)
        
        name = parts[0]
        density = float(parts[1])
        densities[name] = density

    return densities


