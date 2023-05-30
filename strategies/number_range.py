from utils.get_numbers import get_numbers
def number_range_strategy(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    
    ub = params['range']['upperbound']
    lb = params['range']['lowerbound']
    if operation == "insertIfEmpty":
        if null_mask.sum() == 0:
            return df
        df.loc[null_mask, colName] = get_numbers(lb, ub, null_mask.sum())
    elif operation == "insert":
        df[colName] = get_numbers(lb, ub, rows)
    else :
        print("Wrong operation used, {}".format(operation))
    return df