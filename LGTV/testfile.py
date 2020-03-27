import json, os
file="data.json"
if os.path.isfile(file) == True:
    with open(file) as f:
        devices = json.load(f)
        print(devices[0]['website'])