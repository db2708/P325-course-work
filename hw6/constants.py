from pathlib import Path
import json

def update_constant(name, value):
    
    """
    function updates the value of a user entered constat to the constonts.json dictionary
    if the constant is already in the dictionary, its current value is updated to the new value.
    otherwise, the new constant's name and value are added to the dictionary. The updated dictionary is then written back to the json file.

    name: name of the constant to be updated or added
    value: new value of the constant being updated or added
    
    """
    path = Path("constants.json")
    lines = json.loads(path.read_text())
    
    for key, val in lines.items():
        if key == name:
            lines[key] = value
            break
        if key != name:
            lines[name] = value
            
    contents = json.dumps(lines, indent = 4)
    path.write_text(contents)

