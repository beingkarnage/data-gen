import pandas as pd
def readExcel(filename, sheetName, skiprows) :
    return pd.read_excel(filename, sheet_name=sheetName, skiprows=skiprows)