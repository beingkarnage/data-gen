import numpy as np
import rstr
from utils.map_to_null import map_values
def regexStrategy(params, isUnique, df,colName, operation, rows, mask= True):
    df = df.replace('#VALUE!',np.nan)
    null_mask = mask & df[colName].isnull()
    alreadyPresent = []
    newGenerated = []
    totalMissing = None

    if operation == 'insertIfEmpty' :
        alreadyPresent = [set(df.dropna())]
        totalMissing = df[colName].isna().sum()
    elif operation == 'insert':
        totalMissing = rows
    else :
        print("Error : Wrong Operation mentioned {}".format(operation))
    
    while totalMissing > 0 :
        temp = rstr.xeger(params['regex'])
        if isUnique:
            if temp not in alreadyPresent :
                alreadyPresent.append(temp)
                newGenerated.append(temp)
                totalMissing-=1
        else: ## t2bd
            newGenerated.append(temp)
            totalMissing-=1
    if operation == 'insertIfEmpty':
        df[colName] = df[colName].apply(map_values, args=(newGenerated,))
    elif operation == 'insert':
        df[colName] = newGenerated
    return df