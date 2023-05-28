import pandas as pd
import random as rd
import sys

from utils.file_readers import readExcel, readJson
from utils.file_writers import excelWriter, jsonWriter, csvWriter, parquetWriter, sqlWriter
from utils.strategy_module import load_strategy_module

from relations.relation import relationType

def start():
    configFile = readJson(sys.argv[1])
    columnName = configFile['columnName']
    fileReader = configFile['fileReader']
    fileWriter = configFile['fileWriter']
    rows = configFile['numOfRows']
    configs = configFile['configs']
    df = None
    
    if fileReader['fileName'].endswith("xlsx"):
        df = readExcel(fileReader['fileName'],fileReader['sheetName'],fileReader['rowSkip'])
    elif fileReader['fileName'].endswith("csv"):
        print("Implement csv file reader")
    else :
        print("WARNING : Unsupported file format used, creating empty dataframe")
        df = pd.DataFrame(columns = columnName)
    STRATEGIES = readJson("configs/STRATEGIES.json")
    LOGICAL_MAPPING = readJson("configs/LOGICAL_MAPPING.json")
    for curConfig in configs:
        for colName in curConfig['names']:
            if 'strategy' in curConfig.keys() and len(curConfig['strategy']) != 0:
                strategy_module_path = STRATEGIES[curConfig['strategy']['name']]
                strategy_module = load_strategy_module(strategy_module_path)
                strategy_function = getattr(strategy_module, LOGICAL_MAPPING[curConfig['strategy']['name']])
                df = strategy_function(curConfig['strategy']['params'], df, colName, rows, curConfig['operation'])
            elif 'relationType' in curConfig.keys() and len(curConfig['relationType']) != 0:
                for i in curConfig['relationType']:
                    df = relationType(i, df, colName, rows, STRATEGIES, LOGICAL_MAPPING)
            else:
                print('Neither a strategy nor a relationship is found for {}'.format(curConfig))

    if len(configs) !=0:
        for i in fileWriter:
            if i['type'].endswith("xlsx"):
                excelWriter(df, i['params'])
            elif i['type'].endswith("csv"):
                csvWriter(df, i['params'])
            elif i['type'].endswith("json"):
                jsonWriter(df, i['params'])
            elif i['type'].endswith("parquet"):
                parquetWriter(df, i['params'])
            elif i['type'].endswith("sql"):
                sqlWriter(df, i['params'])

if __name__ == '__main__':
    start()