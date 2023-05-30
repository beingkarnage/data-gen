from utils.strategy_module import load_strategy_module

def relation_type(relation, df, colName,rows, STRATEGIES, LOGICAL_MAPPING):
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

    strategy_module_path = STRATEGIES[relation['strategy']['name']]
    strategy_module = load_strategy_module(strategy_module_path)
    strategy_function = getattr(strategy_module, LOGICAL_MAPPING[relation['strategy']['name']])
    df = strategy_function(relation['strategy']['params'],
                            df, colName, rows, relation['operation'],mask=mask)
    return df