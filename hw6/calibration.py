import json
from pathlib import Path

def check_sensor(filename):
    
    """
    function takes in a filename and checks and returns the voltage offset of the sensor. if the file 
    isn't found or isn't a valid json file it raises a file not found or json decode error and returns None.
    
    path: defines the file name as the objects path
    lines: reads the file's text and loads it as a json object
    key, value: iterates thru the object to find the voltage offset key and returns its value
    
    """
    
    path = Path(filename)
    try:
    
        lines = json.loads(path.read_text())
        print(lines)
        for key, value in lines.items():
            if key == "voltage_offset":
                return value
            
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
        return None
    
    except json.JSONDecodeError:
        print("File may be corrupted or isn't in valid JSON format. Please enter a valid file name.")
        return None 
    
    
