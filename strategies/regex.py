import numpy as np
import rstr
from utils.map_to_null import map_values
def regexStrategy(params, isUnique, df,colName, operation, rows, mask= True):
    df = df.replace('#VALUE!',np.nan)
    null_mask = mask & df[colName].isnull()
    already_present = []
    new_generated = []
    total_missing = None

    if operation == 'insertIfEmpty' :
        already_present = [set(df.dropna())]
        total_missing = df[colName].isna().sum()
    elif operation == 'insert':
        total_missing = rows
    else :
        print("Error : Wrong Operation mentioned {}".format(operation))
    
    while total_missing > 0 :
        temp = rstr.xeger(params['regex'])
        if isUnique:
            if temp not in already_present :
                already_present.append(temp)
                new_generated.append(temp)
                total_missing-=1
        else: ## t2bd
            new_generated.append(temp)
            total_missing-=1
    if operation == 'insertIfEmpty':
        df[colName] = df[colName].apply(map_values, args=(new_generated,))
    elif operation == 'insert':
        df[colName] = new_generated
    return df