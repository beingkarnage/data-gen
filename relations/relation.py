from strategies.number_range import numberRangeStrategy
from strategies.distributed import distributedStrategy2
from strategies.regex import regexStrategy
from strategies.random_name import randomNameStrategy

def relationType(relation, df, colName,rows, operation):
    filter_dict = relation['filter']
    mask = None
    for i in range(len(filter_dict['lhs'])):
        col = filter_dict['lhs'][i]
        value = filter_dict['rhs'][i]
        op = filter_dict['operation'][i]
        if mask is None:
            mask = (df[col] != value) if op == "!=" else (df[col] == value)
        else:
            temp = (df[col] != value) if op == "!=" else (df[col] == value)
            boolean_op = filter_dict['boolean'][i-1]
            mask = mask & temp if boolean_op == "&" else mask | temp
    
    if relation['strategy']['name'] == 'numberRange':
        df = numberRangeStrategy(relation['strategy']['params'], df, colName,rows, operation, mask)
    elif relation['strategy']['name'] == 'distributed':
        print("Running distributed for {}".format(colName))
        df = distributedStrategy2(relation['strategy']['params'], df,
                                   colName, rows,
                                   operation, mask)
    elif relation['strategy']['name'] == 'regex':
        df = regexStrategy(relation['strategy']['params'], relation['strategy']['isUnique']
                           , df, colName, operation, rows, mask)
    elif relation['strategy']['name'] == 'randomName':
        df = randomNameStrategy(df,colName, rows, operation, mask)
    return df