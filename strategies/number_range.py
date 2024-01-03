from utils.get_numbers import get_numbers
def number_range_strategy(**kwargs):
    df = kwargs.get('df')
    colName = kwargs.get('colName')
    null_mask = kwargs.get('mask',False) & df[colName].isnull()
    ub = kwargs.get('params').get('range').get('upperbound')
    lb = kwargs.get('params').get('range').get('lowerbound')
    if kwargs.get('operation') == "insertIfEmpty":
        if null_mask.sum() == 0:
            return df
        df.loc[null_mask, colName] = get_numbers(lb, ub, null_mask.sum())
    elif kwargs.get('operation') == "insert":
        df[colName] = get_numbers(lb, ub, kwargs.get('rows'))
    else :
        print("Wrong operation used, {}".format(kwargs.get('operation')))
    return df