import pandas as pd
import random as rd
import json
import sys
from utils.file_readers import jsonReader, readExcel, readJson
from strategies.number_range import numberRangeStrategy
from strategies.number_range import numberRangeStrategy
from strategies.distributed import distributedStrategy
from strategies.regex import regexStrategy
from strategies.random_name import randomNameStrategy
from strategies.distributed_number_range import distributedNumberRange
from relations.relation import relationType
from strategies.time_range import timeRangeStrategy

from utils.file_writers import excelWriter, jsonWriter, csvWriter, parquetWriter, sqlWriter

def start():
    configFile = readJson(sys.argv[1])
    columnName = configFile['columnName']
    fileReader = configFile['fileReader']
    fileWriter = configFile['fileWriter']
    rows = configFile['numOfRows']
    configs = configFile['configs']
    df = None

    if fileReader[0]['fileName'].endswith("xlsx"):
        df = readExcel(fileReader[0]['fileName'],fileReader[0]['sheetName'],fileReader[0]['rowSkip'])
    elif fileReader[0]['fileName'].endswith("csv"):
        print("Implement csv file reader")
    else :
        print("WARNING : Unsupported file format used, creating empty dataframe")
        df = pd.DataFrame(columns = columnName)

    for curConfig in configs:
        for colName in curConfig['names']:
            if "strategy" in curConfig.keys() and len(curConfig['strategy'])!=0:
                if curConfig['strategy']['name'] == "regex":
                    df = regexStrategy(
                            curConfig['strategy']['params'],
                            curConfig['strategy']['isUnique'],
                            df,colName,
                            curConfig["operation"],
                            rows)

                elif curConfig['strategy']['name'] == "distributed":
                    df = distributedStrategy(
                        curConfig['strategy']['params'],
                        df,
                        colName,rows,curConfig['operation'],True)

                elif curConfig['strategy']['name'] == "numberRange":
                    df = numberRangeStrategy(
                        curConfig['strategy']['params'],
                        df,
                        colName, rows,
                        curConfig['operation']
                    )

                elif curConfig['strategy']['name'] == "timeRange":
                    df = timeRangeStrategy(
                        curConfig['strategy']['params'],
                        df,
                        colName, rows,
                        curConfig['operation']
                    )

                elif curConfig['strategy']['name'] == "randomNameGenerator":
                    df = randomNameStrategy(df, colName, rows, curConfig['operation'])

                elif curConfig['strategy']['name'] == "distributedNumberRange":
                    df = distributedNumberRange(
                        curConfig['strategy']['params'],
                        df,
                        colName,rows,
                        curConfig['operation']
                    )
            elif "relationType" in curConfig.keys() and len(curConfig["relationType"])!=0:
                for i in curConfig["relationType"]:
                    df = relationType(i,df,colName,rows, i['operation'])
            else :
                print('Neither a strategy, nor a relationship is found, for {}'.format(curConfig))
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