from utils.date_generator import generate_random_date
def dateGeneratorStrategy(params, df, colName, rows, operation, mask=True):
    startDate = params['startDate']
    endDate = params['endDate']
    inputFormat = params['inputFormat']
    outputFormat = params['outputFormat']

    null_mask = mask & df[colName].isnull()
    res = []
    
    if operation == "insert":
        for i in range(rows): 
            res.append(generate_random_date(startDate, endDate,inputFormat, outputFormat))
        df[colName] = res
    elif operation == "insertIfEmpty":
        for i in range(null_mask.sum()):
            res.append(generate_random_date(startDate, endDate,inputFormat, outputFormat))
        df.loc[null_mask, colName] = res
    return df