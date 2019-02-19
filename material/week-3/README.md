---
description: 'Types, Lists and Dictonaries'
---

# Week 3

## Types

The different kinds \(or representations\) of data which programming languages are able to store and manipulate are referred to as types, and we have already encountered a few of these.   


### Simple Types

The types we've encountered so far can be though of as the building blocks for more complicated types - in the same way you might think of a string as being built out of characters.   
  
These **"simple" types** are shown in the following example:

```python
# Basic Types
a_string = "Hello World"
a_character = "Z" # Characters are strings of length 1
a_integer = 32
a_float = 18.032
a_boolean = True  # Booleans are just integers 1 (True) or 0 (False)
```

Little tip:

```python
another_bool = (242 == "frog") # False
```

**Fun fact:** Booleans are actually implemented as integers, with 1 = True and 0 = False:

```text
if 0:
    print("I won't get printed")
else:
    print("I will!")
```

### Typecasting

Python, like many other languages, has the ability to transform one type of data to another - although it will only work if this conversion **makes sense**. For example, you could convert a string containing a number to an integer:

```python
# Suppose the user gave us a number via input()
user_number = "12314"

# Cast the string to an integer and store the result
user_number_converted = int(user_number)
```

But, if you tried to convert a string containing letters or symbols to a number, python will get confused and **throw an error** \(see [extension material](extensions.md#basic-error-handling) for more detail\). Here's an example that results in an error:

```python
# Can only cast to other types if compatible
user_input = "Woops"

# Trying to cast this str -> int will cause a "ValueError"
user_input_converted = int(user_input)
```

For reference, here's a table of casts that can \(and will\) come in handy:

| Type | Cast | Example Use case |
| :--- | :--- | :--- |
| Integer Number | int\(\) | Do maths on user input |
| Floating Point Number | float\(\) | Output numbers with decimal places |
| String | str\(\) | Concatenate numbers with text when printing |
| Boolean | bool\(\) | \(Not often in practice - output formatting?\) |
| Characters | chr\(\) | Convert integer to ASCII character \[string\] |
| List | list\(\) | Convert tuples / arrays / range\(\) objects to lists |

## Lists

Lists are the first proper "data structure" that we will cover:

* Lists allow us to store multiple values in one object
* Lists can change size without us needing to re-declare them all the time
* Lists can also be used for carrying out vector and matrix arithmetic \(though in practice there are libraries like numpy which are far better for such things

Lists are created by using square brackets, \[\], and in python they can contain multiple different types of items:

```python
# Create an empty list
my_first_list = []

# Create a list containing some items
my_second_list = [1, 423.32, "Hiya", True]
```

### Accessing list items <a id="Accessing-list-items"></a>

In python \(and many other programming languages\) we **count from 0**. So the first item in a list is always at the **"zeroeth" position**. For example:

```python
# Create a list
some_list = [0, 1, 2, 3, "Great Movie", 8, 13]
```

Can be visualized as:

![](../../.gitbook/assets/image%20%2812%29.png)

Then. If we wish to get items from a specific location in our list, we can do this by using square brackets next to the list's name: e.g. **list\[index\]**

```python
print(some_list[4]) # Print the fifth element
# outputs: Great Movie
```

A more involved example:

```python
# A great reference
sentence = ["A", "Wizard", "Is","Never","Late","!"]

# Explicity store specific elements in new variables
first_word = sentence[0]
second_word = sentence[1]
fifth_word = sentence[4]

print(first_word + " " + fifth_word + " " + second_word)
# outputs: A Late Wizard
```

### Append

To add items to the end of a list, we use the .append\(\) function:

```python
my_list = []
my_list.append("hello")

# Now my_list = ["hello"]
```

### Pop

We can remove items from a list by using **.pop\(index\)** to remove the item at the specified index. \(**Note:** the function also returns the value that it removes\)

```text
my_list = [3, 5, 2, 6, 4]
my_list.pop(2)

# Now my_list = [3, 5, 6, 4]
```

### Reverse Iteration

If you want to iterate backwards through a list, the following syntax allows it.

```text
# Strings are effectively lists of characters
the_dream = "desserts"
university = the_dream[::-1] # We can go backwards too
```

This syntax is a special case of a general language feature called **list slicing** \(see [extensions](extensions.md#List-Slicing) for detail\).

## Dictionaries

Along with lists, dictionaries are among the most useful and commonly used datastructures. Dictionaries allow us to store _Key : Value_ pairs.

Whereas lists are created using \[\], we create dictionaries using {}

```python
# Create an empty dictionary
empty_dict = {}

# Create a dictionary with some info inside
my_dict = {"name" : "alex", "age" : 22, 1 : "one"}
```

### Pop

```python
my_dict = {"hello" : 231, "fish" : "frog"}

# Remove the key-value pair corresponding to "hello"
my_dict.pop("hello")

# Now my_dict = {"fish" : "frog"}
```

