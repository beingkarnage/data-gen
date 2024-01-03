from utils.date_generator import generate_random_date
from utils.args_to_dict import args_to_dict
def date_generator_strategy(**kwargs):
    param = {}
    param['start_date'] = kwargs.get('params').get('startDate')
    param['end_date'] = kwargs.get('params').get('endDate')

    if "inputFormat" in kwargs.get("params") :
        param["input_format"] = kwargs.get('params').get('inputFormat')
    
    if 'outputFormat' in kwargs.get("params") :
        param['output_format'] = kwargs.get('params').get('outputFormat')
    
    df = kwargs.get('df')
    colName = kwargs.get('colName')

    null_mask = kwargs.get('mask') & (df[colName].isnull())
    res = []
    
    if kwargs.get("operation") == "insert":
        for i in range(kwargs.get("rows")): 
            res.append(generate_random_date(**param))
        df[colName] = res
    elif kwargs.get("operation") == "insertIfEmpty":
        for i in range(null_mask.sum()):
            res.append(generate_random_date(**param))
        df.loc[null_mask, colName] = res
    return df