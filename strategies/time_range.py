from utils.time_generator import timeGenerator
def timeRangeStrategy(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    if null_mask.sum() == 0:
        return df
    ub = params['range']['upperbound']
    lb = params['range']['lowerbound']
    res = []
   
    if operation == "insertIfEmpty":
        size = null_mask.sum()
    elif operation == "insert":
        size = rows
        
    while(size > 0) :
        t = timeGenerator(ub, lb)
        res.append(t)
        size-=1
        
    if operation == "insertIfEmpty":
         df.loc[null_mask, colName] = res
    elif operation == "insert":
        df[colName] = res
    return df