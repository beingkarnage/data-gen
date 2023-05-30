from utils.time_generator import timeGenerator
def time_range_strategy(params, df, col_name, rows, operation, mask=True):
    null_mask = mask & df[col_name].isnull()
    if null_mask.sum() == 0:
        return df
    upperbound = params['range']['upperbound']
    lowerbound = params['range']['lowerbound']
    res = []
   
    if operation == "insertIfEmpty":
        size = null_mask.sum()
    elif operation == "insert":
        size = rows
        
    while(size > 0) :
        t = timeGenerator(upperbound, lowerbound)
        res.append(t)
        size-=1
        
    if operation == "insertIfEmpty":
         df.loc[null_mask, col_name] = res
    elif operation == "insert":
        df[col_name] = res
    return df