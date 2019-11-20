---
description: Coding in the "Real World" and Datascience Pt. I - Numpy Basics
---

# Numpy

The datascience part of this course shall cover the bare minimum of material which should allow you to perform fairly powerful data analysis tasks. A considerably more thorough, and example rich course, can be found at: 

{% embed url="https://jakevdp.github.io/PythonDataScienceHandbook/" %}

## Coding in the "Real World"

Most new code is written to solve new problems. It is rare that these problems don't build on previous work.

In reality, much of your time will probably be spent figuring out how to repurpose code written by strangers, or colleagues, in order to solve the task in front of you.

If you're lucky, there will be thorough **documentation** for the package / modules in question \(and _good comments!_\) - This will certainly be the case for all the packages we'll use, as you'll find out ;\)

## Data Manipulation - Numpy

Numpy is a powerful package which is used in virtually any scenario where one wishes to perform complicated mathematical tasks on datasets.

### Arrays

Numpy introduces an array datatype which can be used to store data of any dimension in a way more powerful than python's built-in lists. 

Arrays allow us to not just neatly store data, but also to handily perform all kinds of manipulations on it, ranging from simple matrix addition, statistics and reshaping, through to Fourier transformations, curve fitting and much more.

We begin by importing numpy with in the conventional fashion, by renaming it to "np", and convert a python list to a numpy array using the **np.array\(\)** function:

```python
import numpy as np

a_list = [[1,2,3],[4,5,6],[7,8,9]]
an_array = np.array(a_list)
```

If we print the list and the array, we see that numpy has recognized the list as a two-dimensional matrix, with rows and columns.

```python
list: 
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

### Array Slicing

The **shape** of arrays is crucial as numpy allows us to peform a generalized form of [list slicing](week-3/extensions.md#List-Slicing) on each dimension \(or axis\) of an array.

For example, the array in the previous section was of shape **\(3, 2\);**  3 rows and 2 columns.

We can slice \(rows, columns\) separately, with the same square bracket syntax we'd use for lists

```python
# Slice using array[row_slice, col_slice]

# Print second column
print(a_array[:, 1]) #[every row, column 2]
```

We can also specify a tuple for a specific dimension, which will extract a subset of the elements - I.e. \(1, 2\) would extract the first and second row/column depending on where in the square brackets we place it:

```python
# We can print the second and third column of the third row:
print(a_array[2, (1,2)])
```

Crucially, this functionality generalizes to higher dimensional arrays, for example, consider the following "cube" in 3D:

![The same logic extends to any number of dimensions](../.gitbook/assets/image%20%285%29.png)

We could represent this as an array in numpy, and slice out a plane \(i.e. face of the cube\):

```python
# array[x_slice, y_slice, z_slice] etc.
my_array = np.array([[['a', 'b'],['c', 'd']],
                     [['e', 'f'],['g', 'h']]])

# Print the x=0, y-z plane square
print(my_array[0, :, :])
```

### Loading Data with Numpy

Given that numpy gives us a natural and powerful way of storing data in python objects, it should come as no surprise that the package is well-equipped to load data from common data formats such as .csv \(comma seperated values\) and .txt.

Consider the following dataset, stored as a csv:

{% file src="../.gitbook/assets/exampledata \(1\).csv" caption="example\_data.csv" %}

| name | age | favorite\_number |
| :--- | :--- | :--- |
| alex | 21 | 17 |
| john | 26 | 32 |
| frank | 37.2 | -238 |
| bob | 920 | 40.23 |

Here we will use the **.genfromtxt\(\)** function to load the csv file into a "structured array" - this is necessary because the datasets contains different datatypes \[both strings and integers\].

{% hint style="info" %}
Numpy arrays can only contain one type of data - E.g. all strings or all integers

If one tries to mix types, then Numpy will store these as "Structured arrays" which behave akin to dictionaries which elements = arrays of a specific type
{% endhint %}

```python
# Use genfromtext to load a csv
my_data = np.genfromtxt("data/exampleData.csv", delimiter=",", 
                         names=True, dtype=None)
    
# Delimiter tells numpy how columns are seperated
# names=True tells numpy that the first row should be used to label the columns
# dtype=None warns numpy that it needs to figure out the kinds of data itself
print(my_data['age']) # prints [ 21.   26.   37.2 920. ]
```

Often it is more convenient to use the **.loadtxt\(\)** function, which behaves very similar, but works more effectively with files containing only one type of data \(i.e. it gives you more direct control of the resulting structure of the array\)

