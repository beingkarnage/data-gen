import numpy as np
def distributed_choice_strategy(**kwargs):
    df = kwargs.get('df')
    colName = kwargs.get('colName')
    null_mask = kwargs.get('mask',False) & df[colName].isnull()

    if sum(kwargs.get('params').get('choices').values())==100:
        choices_with_dist = {}
        choices = []
        for key in kwargs.get('params').get('choices'):
            choices_with_dist[key] = (kwargs.get('params').get('choices')[key]/100)
            choices.append(key)
        already_present = df.value_counts().to_dict()
        for i in choices:
            if i in already_present.keys():
                choices_with_dist[i] -= already_present[i]

    else :
        print("Error : Invalid distribution given, distributions sum should be equal to 100, but got {}".format(sum(params['choices'].values())))
    if kwargs.get('operation') == "insertIfEmpty" :
        newGenerated = np.random.choice(choices, size=null_mask.sum(), p=list(choices_with_dist.values()))
        df.loc[null_mask, colName] = newGenerated
    elif kwargs.get('operation') == "insert":
        newGenerated = np.random.choice(choices, size=kwargs.get('rows'), p=list(choices_with_dist.values()))
        df[colName] = newGenerated
    return df