"""
Find a package in the Python standard library for dealing with JSON.
Import the library module and inspect the attributes of the module. Use the help function to learn more about how
to use the module. Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string.
Deserialize the JSON back into Python.
"""

import json
info = {"Name": "Saurav Adhikari" , "age": 23}
serialized_json = json.dumps(info)
print(serialized_json)
deserialized_json = json.loads(serialized_json)
print(deserialized_json)
