from pathlib import Path

def read_densities(filename):
    
    """
    DOCSTRING HERE
    
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


