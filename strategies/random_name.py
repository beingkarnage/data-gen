from utils.get_names import get_names
def random_name_strategy(**kwargs):
    df = kwargs.get('df')
    colName = kwargs.get('colName')

    null_mask = kwargs.get('mask',False) & df[colName].isnull()
    if null_mask.sum() == 0:
        return df
    
    if kwargs.get('operation') == "insertIfEmpty":
        df.loc[null_mask, colName] = get_names(null_mask.sum())
    elif kwargs.get('operation') == "insert":
        df[colName] = get_names(kwargs.get('rows'))
    return df