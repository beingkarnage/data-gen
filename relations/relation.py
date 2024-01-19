from utils.strategy_module import load_strategy_module
from utils.args_to_dict import args_to_dict


def compare_type(val):
    if type(val) == str:
        return str(val)
    elif type(val) == int:
        return int(val)
    
def relation_type(relation, df, colName,rows, STRATEGIES, LOGICAL_MAPPING):
    """ 
    Summary:
        creates a set of boolean values also referred as `mask` in the code, to generate some other column based on this mask    
        
    Args:
        relation: holds filter dict which have left hand side operartor referred as `col`, and rhs the value which is going .
        df: an empty dataframe or a dataframe which is generated from previous strategy or relation.
        colName: column for which the data to be generate.
        rows: number of rows to generate.
        STRATEGIES: type of strategy which is used to generate colName.
        LOGICAL_MAPPING: a constant wrapper for strategy file config.

    Returns:
        df : an updated dataframe.
    """
    filter_dict = relation['filter']
    mask = None

    for i in range(len(filter_dict['lhs'])):
        col = filter_dict['lhs'][i]
        value = filter_dict['rhs'][i]
        op = filter_dict['operation'][i]
        if mask is None:
            if op == "!=":
                mask = (df[col] != compare_type(value))
            elif op == "<":
                mask = (df[col] < compare_type(value))
            elif op == ">":
                mask = (df[col] > compare_type(value))
            else:
                mask = (df[col] == compare_type(value))
        else:
            if op == "!=":
                temp = (df[col] != compare_type(value))
            elif op == ">":
                temp = (df[col] > compare_type(value))
            elif op == "<":
                temp = (df[col] < compare_type(value))
            else: 
                temp = (df[col] == compare_type(value))
            
            boolean_op = filter_dict['boolean'][i-1]
            mask = mask & temp if boolean_op == "&" else mask | temp

    strategy_module_path = STRATEGIES[relation['strategy']['name']]
    strategy_module = load_strategy_module(strategy_module_path)
    strategy_function = getattr(strategy_module, LOGICAL_MAPPING[relation['strategy']['name']])
    params = args_to_dict(params=relation['strategy']['params'], df=df,colName=colName, rows=rows, operation=relation['operation'], debug=relation.get("debug", False), mask=mask)
    df = strategy_function(**params)
    return df