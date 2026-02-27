from pathlib import Path
import json

# script allows user to input a name, mass, charge, and spin for a given set of particle(s)
# then saves the information to a json file called particles.json

save_path = Path("particles.json")

particles = {}

while True:
        
    name = input("Enter the name of the particle as a string, or enter 'q' to quit. \n")
    
    if name.lower() == 'q':
        break
    
    mass = float(input("Enter the mass of the particle as a float. \n"))
    charge = int(input("Enter the charge of the particle in units of e as an int.\n"))
    spin = float(input("Enter the spin of the particle as a float.\n"))

    particles[name] = {'mass': mass, 'charge': charge, 'spin': spin}


    contents = json.dumps(particles, indent = 4)
    save_path.write_text(contents)
