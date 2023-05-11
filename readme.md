
# Data generator

Data generator is a script for data generation with a set of strategies and relations defined for generating data for columns in a dataframe.

A short brief about the functions:
### About the script

1. readConfigFile: reads a JSON configuration file.
2. readInputFile: reads an input Excel file.
3. map_values: a helper function for the regexStrategy function to map the generated values to the dataframe.
4. regexStrategy: generates data based on a regular expression pattern.
5. getNames: generates a list of random first names.
6. randomNameStrategy: generates random first names for a column.
7. relationType: applies a data generation strategy based on a relation between columns.
8. getNumbers: generates random numbers within a given range.
9. distributedNumberRange: generates random numbers based on a distribution.
10. distributedStrategy2: generates data based on a distribution.
11. main: the main function that reads the configuration file, input file, and applies data generation strategies based on the configuration file.

The script reads a configuration file in JSON format and applies data generation strategies based on the configuration file to the columns in the input Excel file. The script uses various data generation strategies such as regular expression, random names, and distribution-based data generation. The script generates data for each column based on the relation between the columns and the data generation strategy defined in the configuration file.

The Data can be generated based on primarily two ways
 **Strategies** or **Relationships**

Relationships allows to establish, a certain set of dependency on one or more columns which are already generated previously for the column we need. 

**Note** : A column can have either a strategy or a relationship witih its respective strategies.

**Config Examples**
Config examples can be find in the examples/config folder