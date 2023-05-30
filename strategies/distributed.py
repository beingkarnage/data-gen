import numpy as np
def distributed_strategy(params, df, colName, rows, operation, mask=True):
    null_mask = mask & df[colName].isnull()
    if sum(params['choices'].values())==100:
        choices_with_dist = {}
        choices = []
        for key in params['choices']:
            choices_with_dist[key] = (params['choices'][key]/100)
            choices.append(key)
        already_present = df.value_counts().to_dict()
        for i in choices:
            if i in already_present.keys():
                choices_with_dist[i] -= already_present[i]

    else :
        print("Error : Invalid distribution given, distributions sum should be equal to 100, but got {}".format(sum(params['choices'].values())))
    if operation == "insertIfEmpty" :
        newGenerated = np.random.choice(choices, size=null_mask.sum(), p=list(choices_with_dist.values()))
        df.loc[null_mask, colName] = newGenerated
    elif operation == "insert":
        newGenerated = np.random.choice(choices, size=rows, p=list(choices_with_dist.values()))
        df[colName] = newGenerated
    return df