
# Data Generator
Data generator or data-gen, is a tool focused towards generating data, either based a on relation on some other column, or a strategy.

#### What is a relation or `relation_type` in data-gen
> relation_type : optional : list

Relation allows to establish, a certain set of dependency on one or more columns which are already present, then generates the specified column based on the dependencies.

------------
#### What is strategy or `strategy` in data-gen
>strategy : required : dict

A strategy defines how the data is going to be generated

### About the tool

The `data_generator.py` reads a config file in `json` format and applies data generation strategies based on the config file to the columns, The script uses various data generation strategies such as regular expression, series, random names, and distribution-based data generation. it is capable of generating data independenlty or based on some other column, i.e. `relation`

#### Config Examples
Config examples can be found in the examples/config folder, which involves all the examples for generating data based on each type of strategies and relations.

##### Config explaination
	{
	  "column_name": [ ALL_COLUMNS ],
	  "file_writer": [ 
	  "type" : FILE_FORMAT ,
  
	  "params" : {
			"path_or_buf": FILENAME.FILE_FORMAT
		  }
	  ],
  
	 "num_of_rows": NUMBER_OF_ROWS,
	 
	"configs": [
	 	{
			<--- STRATEGY ONLY EXAMPLE --->
      		"names": [
      			INDEPENDENT_COLUMN(S)
      		],
      "strategy": {
	  		<--- STRATEGY DETAILS & EXTRA_PARAMS --->
        "is_unique": "False", 
        "name": STRATEGY_NAME,
        "params": {
          <--- STRATEGY SPECIFIC PARAMS --->
        }
      },
      "operation": MODE_OF_INSERTION
    },
    {	<--- STRATEGY WITH RELATIONSHIP EXAMPLE --->
      "names": [
        DEPENDENT_COLUMN(S)
      ],
      "relation_type": [
	  <--- LIST OF RELATIONS -->
        {
          "filter": {
            "lhs": [
              COLUMNS_TO_BE_COMPARED
            ],
            "rhs": [
              VALUE_TO_COMPARE
            ],
            "operation": [
              RELATIONAL_OPERATOR
            ],
            "boolean": [
			BOOLEAN_OPERATORS
            ]
          },
          "strategy": {
			RELATIONAL_STRATEGY
          },
          "operation": MODE_INSERT_FOR_RELATIONAL_STRATEGY
       	 }
      	]
    	}
  	]
	}

###### Placeholder definitions
- ALL_COLUMNS : List of all the columns that are going to be in the final output, column will be empty in output, if no generation definition supplied.
- FILE_FORMAT : Type of format the output should be in.
- FILENAME.FORMAT : Name of file with its format.
- NUMBER_OF_ROWS : Number of rows in output, defaults to 100 and cannot be smaller than 100.
- STRATEGY ONLY EXAMPLE : Example of simple strategy
- INDEPENDEN_COLUMN(S) : Independent column which can be generated, without the dependency of another column.
- STRATEGY DETAILS & EXTRA_PARAMS : Strategy definition and extra parameters.
- STRATEGY_NAME : Logical name of the strategy.
- STRATEGY SPECIFIC PARAMS : Parameters which requires to run a particular strategy.
- MODE_OF_INSERTION : Mode of insertion, either insert or inser_if_empty, insert will always overwrites the value, while insert_if_empty only fills the null values present in the column.
- STRATEGY WITH RELATIONSHIP EXAMPLE : Strategy within a relation.
- DEPENDENT_COLUMN(S) : Columns which requires to be generated via a relation.
- LIST OF RELATIONS : List of relations for a column.

*Rest is selft explainatory*

### Getting Started
**Step 1** : `pip install -r requirements.txt`.

**Step 2** Create a copy of examples/config.json.example to examples/config.json , or create your own config you can refer to examples folder for more info.

**Step 3** Now you are all set to run the script, pass down the config path to the script for example :`python data_generator.py ./examples/config.json`
