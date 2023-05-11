from utils.get_numbers import getNumbers
def numberRangeStrategy(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    
    ub = params['range']['upperbound']
    lb = params['range']['lowerbound']
    if operation == "insertIfEmpty":
        if null_mask.sum() == 0:
            return df
        df.loc[null_mask, colName] = getNumbers(lb, ub, null_mask.sum())
    elif operation == "insert":
        df[colName] = getNumbers(lb, ub, rows)
    else :
        print("Wrong operation used, {}".format(operation))
    return df