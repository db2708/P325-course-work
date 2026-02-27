from pathlib import Path
import json

def update_constant(name, value):
    
    """
    function updates the value of a constant in the constants.json file, if the
    constant isnt already present in the file it is added to the dictionary.

    name: name of the constant to be updated or added
    value: new value of the constant being updated or added
    
    """
    path = Path("constants.json")
    lines = json.loads(path.read_text())
    
    lines[name] = value
            
    contents = json.dumps(lines, indent = 4)
    path.write_text(contents)

