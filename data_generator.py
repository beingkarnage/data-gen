import pandas as pd
import random as rd
import sys

from utils.json_loader import read_json
from utils.strategy_module import load_strategy_module

from relations.relation import relation_type

def start():
    configFile = read_json(sys.argv[1])
    columnName = configFile['columnName']
    fileWriter = configFile['fileWriter']
    rows = configFile['numOfRows']
    configs = configFile['configs']
    df = pd.DataFrame(columns = columnName)
    STRATEGIES = read_json("configs/STRATEGIES.json")
    LOGICAL_MAPPING = read_json("configs/STRATEGIES_MAPPING.json")
    for cur_config in configs:
        for col_name in cur_config['names']:
            if 'strategy' in cur_config.keys() and len(cur_config['strategy']) != 0:
                strategy_module = load_strategy_module(STRATEGIES[cur_config['strategy']['name']])
                strategy = getattr(strategy_module, LOGICAL_MAPPING[cur_config['strategy']['name']])
                df = strategy(cur_config['strategy']['params'], df, col_name, rows, cur_config['operation'])
            elif 'relation_type' in cur_config.keys() and len(cur_config['relation_type']) != 0:
                for i in cur_config['relation_type']:
                    df = relation_type(i, df, col_name, rows, STRATEGIES, LOGICAL_MAPPING)
            else:
                print('Neither a strategy nor a relationship is found for {}'.format(cur_config))
    WRITERS = read_json("configs/WRITERS.json")
    WRITERS_MAPPING = read_json("configs/WRITERS_MAPPING.json")
    if len(configs) !=0:
        for i in fileWriter:
            writer_module = load_strategy_module(WRITERS[i['type']])
            writer = getattr(writer_module, WRITERS_MAPPING[i['type']])
            writer(df, i['params'])

if __name__ == '__main__':
    start()