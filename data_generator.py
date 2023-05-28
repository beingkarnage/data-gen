import pandas as pd
import random as rd
import sys

from utils.file_readers import readExcel, readJson
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
    WRITERS = readJson("configs/WRITERS.json")
    WRITERS_MAPPING = readJson("configs/WRITERS_MAPPING.json")
    if len(configs) !=0:
        for i in fileWriter:
            strategy_module_path = WRITERS[i['type']]
            strategy_module = load_strategy_module(strategy_module_path)
            strategy_function = getattr(strategy_module, WRITERS_MAPPING[i['type']])
            strategy_function(df, i['params'])

if __name__ == '__main__':
    start()