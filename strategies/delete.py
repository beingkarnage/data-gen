import numpy as np
def deletion_strategy(**kwargs):
    df = kwargs.get('df')
    if kwargs.get('operation') == 'insert':
        df.loc[kwargs.get('mask'), kwargs.get('colName')] = np.nan
    else :
        print("Error Invalid Operation {}".format(kwargs.get('operation')))
    return df