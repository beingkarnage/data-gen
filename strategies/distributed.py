import numpy as np
def distributedStrategy(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    if sum(params['choices'].values())==100:
        choicesWithDist = {}
        choices = []
        for key in params['choices']:
            choicesWithDist[key] = (params['choices'][key]/100)
            choices.append(key)
        alreadyPresent = df.value_counts().to_dict()
        for i in choices:
            if i in alreadyPresent.keys():
                choicesWithDist[i] -= alreadyPresent[i]

    else :
        print("Error : Invalid distribution given, distributions sum should be equal to 100, but got {}".format(distSum))
    if operation == "insertIfEmpty" :
        newGenerated = np.random.choice(choices, size=null_mask.sum(), p=list(choicesWithDist.values()))
        df.loc[null_mask, colName] = newGenerated
    elif operation == "insert":
        newGenerated = np.random.choice(choices, size=rows, p=list(choicesWithDist.values()))
        df[colName] = newGenerated
    return df