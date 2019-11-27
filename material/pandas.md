# Pandas

## Pandas - What and Why?

* Pandas is a popular library for doing data manipulation in Python
* Works with tabular data, i.e. rows and columns
* Commonly used with Matplotlib, numpy, scipy and many others

## DataFrames

DataFrames are the main data type in Pandas and hold data as a set of columns called series.

```python
import pandas as pd

data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
```

To create a DataFrame from hard coded values, pass a dictionary to the `DataFrame()` function. Each key should correspond to a column name, and each value to a list of row values.

## Loading Data From File

Pandas lets us create DataFrames from csv files using the `read_csv()` function.

```python
import pandas as pd

# Get column names from file
data_one = pd.read_csv('my_file_with_column_names')

# Give the column names explicitly
columns = ['first_column', 'second_column']
data_two = pd.read_csv('my_file_without_column_names', header=None, names=columns)
```

## Selecting Columns

Sometimes we may want to work with only a single column from a DataFrame, we can use indexing like we have seen with lists and dictionaries to get a column by its name.

```python
import panas as pd

data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Get the column A as a series
a_as_series = data['A']

# Get the column A as a list
a_as_list = list(data['A'])
```

## Selecting Rows

We can also select a specific subset of rows from DataFrame using the indexing similar to lists. We use the `iloc()` function to enable us to select rows by index.

```python
import panas as pd

data = pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8]})

first_row = pd.iloc()[0]

middle_rows = pd.iloc()[1:3]
```

## Filtering Rows

Sometimes the rows we want may not be grouped together or we might not know their indices. In these cases we may be able to create an expression for filtering out the rows we aren't interested in.

```python
import panas as pd

data = pd.DataFrame({'A': [1, 5, 2, 6], 'B': [3, 4, 7, 8]})

# Get all the rows where A is greater than 2
selected_rows = pd[data.A > 2]
```

