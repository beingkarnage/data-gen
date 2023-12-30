from utils.date_generator import generate_random_date
def date_generator_strategy(params, df, colName, rows, operation, mask=True):
    param = {}
    param["start_date"] = params['startDate']
    param["end_date"] = params['endDate']

    if "inputFormat" in params :
        param["input_format"] = params['inputFormat']
    
    if 'outputFormat' in params :
        param["output_format"] = params['outputFormat']

    null_mask = mask & df[colName].isnull()
    res = []
    
    if operation == "insert":
        for i in range(rows): 
            res.append(generate_random_date(**param))
        df[colName] = res
    elif operation == "insertIfEmpty":
        for i in range(null_mask.sum()):
            res.append(generate_random_date(**param))
        df.loc[null_mask, colName] = res
    return df