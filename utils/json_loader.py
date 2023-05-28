import json
def readJson(filename) :
    with open(filename, 'r') as f:
        return json.load(f)

