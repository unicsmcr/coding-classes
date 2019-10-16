---
description: Solutions to Functions and Imports
---

# Week 6

## Exercise 1.1 - Maximal Entertainment

We create a function to print the maximum value in a given list. 

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ex1\_1.py" %}
```python
# define function to print out the max value in the list 
def print_max_in_list(a_list):
    # initialise the current_best to be the first item
    current_best = a_list[0]
    
    for item in a_list:
        # update the current best if we see a bigger value
        if item > current_best:
            current_best = item
            
    print("Max Value:" + str(current_best))
    
# test the function with the following
# expect '376' to be printed
example_list = [4, 9, 376, 12, 234, 124, 94, 3]
print_max_in_list(example_list)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 1.1 - Returning max value

Here we return the max value instead, and then print it.

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ext1\_1.py" %}
```python
# define function to return the max value in a list
def get_max_value_in_list(a_list):
    # initialise the current_best to be the first item
    max_value = a_list[0]
    
    for item in a_list:
        # update the current best if we see a bigger value
        if item > current_best:
            max_value = item
            
    return max_value
    
# test the function with the following
# expect '376' to be printed
example_list = [4, 9, 376, 12, 234, 124, 94, 3]
print("Max value: " + str(get_max_value_in_list(example_list)))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 1.2 - Sum thing to do

Here we print the sum of all the values in a list

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ex1\_2.py" %}
```python
# define function to print the sum of all values in a list
def print_sum_of_list(a_list):
    current_sum = 0
    
    for item in a_list:
        # add the item to the current sum, store it
        current_sum = current_sum + item
        
    print("Sum: " + str(current_sum))
    
# test the function with the following
# expected value is 31
example_list = [1, 2, 4, 8, 16]
print_sum_of_list(example_list)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 1.2 - Returning Average

Now we average the values in the list and return the result

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ext1\_2.py" %}
```python
# define function to return the average of values in the list
def get_average_of_list(a_list):
    current_sum = 0
    
    for item in a_list:
        # add the item to the current sum, store it
        current_sum = current_sum + item
        
    return current_sum / len(list)
    
# test the function with the following
# expected value is 6.4
example_list = [1, 2, 5, 10, 14]
print("Average:" + str(get_average_of_list(example_list)))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 1.3 - Developing a range of skills

Here we define a function to mimic the range function - which returns a list of integers from the minimum to the max - 1.

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ex1\_3.py" %}
```python
# define the range function, which takes a min and max argument
# returns a list of values between min and max-1
def my_range(min_val, max_val):
    the_list = []
    current_val = min_val
    
    while current_val < max_val:
        the_list.append(current_val)
        current_val = current_val + 1
    
    return the_list
    
# test the function with the following
# expect a list of [6, 7, 8, 9, 10, 11]
a_list = my_range(6, 12)
print(a_list)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 1.3.1 - Default arguments

Add default arguments to our range function, such that if min is not given then the function counts from 0 - We need to alter the function definition and modify our max and min values

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ext1\_3\_1.py" %}
```python
............
def my_range(min_val, max_val=None):
    # set max to be min as only 1 argument was given
    # also default min to 0
    if max_val is None:
        max_val = min_val
        min_val = 0
    
    the_list = []
    current_val = min_val
............

# we can test this by elimintating the first argument in the function call
# expect list of [0, 1, 2, 3, 4, 5, 6, 7, 8]
a_list = my_range(9)
print(a_list)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 1.3.2 - Recursive Range function

Here we implement the range function using recursion - the function must call itself, and have a terminating condition.

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ext1\_3\_2.py" %}
```python
# define the recursive range function
def my_recrusive_range(min_val, max_val):
    if min_val == max_val:
        return []
        
    return [min_val] + my_recursive_range(min_val+1, max_val)
    
# test the function with range 0, 10
# expect a list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_recursive_range(0, 10))
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2 - Import-ant Syntax

Here we rename some imports and run the 'scary block of awful code'

{% code-tabs %}
{% code-tabs-item title="week5\_solutions\_ex2.py" %}
```python
import numpy as np
import matplotlib.pyplot as plt

# Scary block of awful code
plt.scatter([0.35 * (2/7) + 0.15, 0.5 - 0.35 * (2/7) ], [2, 2], c='b', marker='s', s=300 )
plt.scatter(0.325, 0.75, c='k', marker='^', s=150);l = np.arange(0.15, 0.51, 0.01)
plt.plot(l ,np.sin(np.linspace(np.pi, 2*np.pi, len(l))), c="r")
plt.axis('off');plt.margins(0.25);plt.title("?sracs eseht tog I woh wonk annaW"[::-1])
plt.show()
```
{% endcode-tabs-item %}
{% endcode-tabs %}

