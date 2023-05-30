from utils.get_names import get_names
def random_name_strategy(df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    if null_mask.sum() == 0:
        return df
    
    if operation == "insertIfEmpty":
        df.loc[null_mask, colName] = get_names(null_mask.sum())
    elif operation == "insert":
        df[colName] = get_names(rows)
    return df