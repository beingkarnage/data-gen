import json
import pandas as pd

def jsonReader(data):
    return pd.read_json(data) 

def readJson(filename) :
    with open(filename, 'r') as f:
        return json.load(f)

def readExcel(filename, sheetName, skiprows) :
    return pd.read_excel(filename, sheet_name=sheetName, skiprows=skiprows)