import numpy as np
from utils.get_numbers import getNumbers
def distributedNumberRange(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    distSum = 0
    ranges =[]
    for i in params['ranges']:
        t = [i['lowerbound'],i['upperbound'],i['distribution']]
        ranges.append(tuple(t))
        distSum += i['distribution']
    if distSum!=100:
        print("Error : Invalid distribution given, distributions sum should be equal to 100, but got {}".format(distSum))
        return df

    generated = []
    if operation == "insert":
        size = rows
    elif operation == "insertIfEmpty":
        size = null_mask.sum() 
    for r in ranges:
        print(">>>> size {}".format(size*r[2]/100))
        x = getNumbers(r[0],r[1], int(size*r[2]/100))
        generated.extend(x)

    np.random.shuffle(generated)
    if operation == "insert":
        df[colName] = generated
    elif operation == "insertIfEmpty":
        while(len(generated)!=null_mask.sum()):
            generated.append(generated[-1]) 
        df.loc[null_mask, colName] = generated
    return df