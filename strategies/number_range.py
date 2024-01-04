from utils.get_numbers import get_numbers
def number_range_strategy(**kwargs):
    """
    Summary:
        generates a random number range

    Args:
        params (dict): holds the arguments on which stratgies are generated.
        df (padans.DataFrame): an empty dataframe or a dataframe which is generated from previous strategy or relation.
        operation (str): type operating the generated to the column.
        mask (pandas.Series, optional): a list of booleans to generate data for some specific rows, came from a relation
          Defaults to `False`.
        colName: column for which the data to be generate.
        rows (int): number of rows to generate.
        
    Returns:
        df (pandas.DataFrame): updted dataframe.
    """
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