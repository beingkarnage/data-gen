from utils.get_names import getNames
def randomNameStrategy(df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    if null_mask.sum() == 0:
        return df
    
    if operation == "insertIfEmpty":
        df.loc[null_mask, colName] = getNames(null_mask.sum())
    elif operation == "insert":
        df[colName] = getNames(rows)
    return df