from pathlib import Path
import json

def clean_data(filename):
    
    """
    function takes in a file name, reads it as a json object, and calculates the average magnitude of the data.
    if the value of a magnitue isn't a valid number or isnt a number it is skipped and not counted in the calculation

    filename: name of the file thats going to be read
    tot: variable that keeps track of the total magnitude
    len: variable that keeps track of the number of valid magnitude values
    avg: the average of all magnitudes
    """
    tot = 0 
    len = 0
    path = Path(filename)
    lines = json.loads(path.read_text())

    for line in lines:
        for key, value in line.items():
            if key == "mag":
                try:
                    tot += float(value)
                    len += 1
                except ValueError or TypeError:
                    continue

    avg = tot/len
    return avg

clean_data('tele_data.json')