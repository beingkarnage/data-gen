import numpy as np
def deletionStrategy(df, colName, rows, operation, mask):
    if operation == 'insert':
        df.loc[mask, colName] = np.nan
    else :
        print("Error Invalid Operation {}".format(operation))
    return df