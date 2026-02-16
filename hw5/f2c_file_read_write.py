from pathlib import Path
import json

Fdeg_path = Path('Fdeg.txt')
Cdeg_path = Path('Cdeg.txt')
lines = Fdeg_path.read_text().splitlines()

def f2c(lines):

    '''
    code reads in a list of Farenheit temps from a text file, converts them to 
    Celcius, then writes the celsius values line by line to a new text file
    
    contents: string of celsius temps to be written to the new text file one line at a time
    f: temp read in from Fdeg.txt converted into a float
    c: converts F to C using the standard formula
    
    '''

    contents = ''
    for line in lines:
        f = float(line)
        c = ((f - 32) * 5/9)
        contents += f'{c}\n'

    return Cdeg_path.write_text(contents)

f2c(lines)
