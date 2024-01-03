import numpy as np
from utils.get_numbers import get_numbers
def distributed_number_range(**kwargs):
    df = kwargs.get('df')
    colName = kwargs.get('colName')
    null_mask = kwargs.get('mask',False) & df[colName].isnull()
    dist_sum = 0
    ranges =[]
    for i in kwargs.get('params').get("ranges"):
        t = [i['lowerbound'],i['upperbound'],i['distribution']]
        ranges.append(tuple(t))
        dist_sum += i['distribution']
    if dist_sum!=100:
        print("Error : Invalid distribution given, distributions sum should be equal to 100, but got {}".format(distSum))
        return df

    generated = []
    if kwargs.get('operation') == "insert":
        size = kwargs.get("rows")
    elif kwargs.get('operation') == "insertIfEmpty":
        size = null_mask.sum() 
    for r in ranges:
        x = get_numbers(r[0],r[1], int(size*r[2]/100))
        generated.extend(x)

    np.random.shuffle(generated)
    if kwargs.get('operation') == "insert":
        df[colName] = generated
    elif kwargs.get('operation') == "insertIfEmpty":
        while(len(generated)!=null_mask.sum()):
            generated.append(generated[-1]) 
        df.loc[null_mask, colName] = generated
    return df