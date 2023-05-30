from utils.date_generator import generate_random_date
def date_generator_strategy(params, df, colName, rows, operation, mask=True):
    start_date = params['startDate']
    end_date = params['endDate']
    input_format = params['inputFormat']
    output_format = params['outputFormat']

    null_mask = mask & df[colName].isnull()
    res = []
    
    if operation == "insert":
        for i in range(rows): 
            res.append(generate_random_date(start_date, end_date,input_format, output_format))
        df[colName] = res
    elif operation == "insertIfEmpty":
        for i in range(null_mask.sum()):
            res.append(generate_random_date(start_date, end_date,input_format, output_format))
        df.loc[null_mask, colName] = res
    return df