from pandas import Series
def series(**kwargs):
    """
    Summary:
        generates a number seriese from a range or 0

    Args:
        params (dict): holds the arguments on which stratgies are generated.
        df (padans.DataFrame): an empty dataframe or a dataframe which is generated from previous strategy or relation.
        operation (str): type operating the generated to the column.
        mask (pandas.Series, optional): a list of booleans to generate data for some specific rows, came from a relation
          Defaults to `False`.
        colName: column for which the data to be generate.
        rows (int): number of rows to generate.
        start (int): start of series
        end (int): end of series
        
    Returns:
        df (pandas.DataFrame): updted dataframe.
    """
    df = kwargs.get('df')
    colName = kwargs.get('colName')
    null_mask = kwargs.get('mask',False) & df[colName].isnull()
    if kwargs.get('operation') == "insertIfEmpty":
        if null_mask.sum() == 0:
            return df
        df.loc[null_mask, colName] = Series(
            range(
                kwargs.get('params').get('start',0),
                min(kwargs.get('params').get('end'), null_mask.sum())
                )
            )
    
    elif kwargs.get('operation') == "insert":
        df[colName] = Series(
                    range(
                        kwargs.get('params').get('start', 0),
                        kwargs.get('rows') + kwargs.get('params').get('start', 0)
                    )
                  )
    else :
        print("Wrong operation used, {}".format(kwargs.get('operation')))
    return df