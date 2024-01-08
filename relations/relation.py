from utils.strategy_module import load_strategy_module
from pandas import DataFrame
def relation_type(relation: dict, df: DataFrame, colName:str,rows, STRATEGIES: dict, LOGICAL_MAPPING: dict) -> DataFrame:
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