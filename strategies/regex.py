import numpy as np
import rstr
from utils.map_to_null import map_values
def regex(**kwargs):
    df = kwargs.get('df')
    df = df.replace('#VALUE!',np.nan)
    already_present = []
    new_generated = []
    total_missing = None
    colName = kwargs.get('colName')

    if kwargs.get('operation') == 'insertIfEmpty' :
        already_present = [set(df.dropna())]
        df = kwargs.get('df')        
        total_missing = df[colName].isna().sum()
    elif kwargs.get('operation') == 'insert':
        total_missing = kwargs.get('rows')
    else :
        print("Error : Wrong Operation mentioned {}".format(kwargs.get('operation')))
    
    while total_missing > 0 :
        temp = rstr.xeger(kwargs.get('params').get('regex'))
        if kwargs.get('isUnique'):
            if temp not in already_present :
                already_present.append(temp)
                new_generated.append(temp)
                total_missing-=1
        else: ## t2bd
            new_generated.append(temp)
            total_missing-=1
    if kwargs.get('operation') == 'insertIfEmpty':
        df[colName] = df[colName].apply(map_values, args=(new_generated,))
    elif kwargs.get('operation') == 'insert':
        df[colName] = new_generated
    return df