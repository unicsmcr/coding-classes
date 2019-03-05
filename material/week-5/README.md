---
description: 'Functions, Import'
---

# Week 5

## Functions <a id="Functions"></a>

If we want to do the same thing in multiple places in our code then we can use _functions_ rather than _copy pasting._ 

This also allows us to **abstract away complexity**, as we can make a function perform some complicated operations, and then forget about how it actually works.

### Definition <a id="Declaration"></a>

We create functions using the **def** keyword - This process is called "definition"

```python
# "Declare" a function
def my_function():
    print("I'm nOT DysFUnctIonaL!")

# "Call" the function twice
my_function()
my_function()

# This will print the sentence twice
```

### Returning <a id="Returning"></a>

Most of the time, we use functions to carry out an operation and collect the result. **return** allows us to get the function to give us an output.

```python
# Return lower-case user input from the function
def get_lowercase_input():
    user_input = input("All good in the hood? ")
    user_input = user_input.lower() # Convert to lowercase
    return user_input # <---
```

Then we can use the function, storing the output in a variable

```python
lowered_input = get_lowercase_input()
print(lowered_input)
```

### "Passing arguments" <a id="&quot;Passing-parameters&quot;"></a>

If we want our function to manipulate some data, we can add **"parameters"** into the definition of the function. Then any time we try and call it, we will need to provide something - doing so is referred to as **passing arguments**.

We've already seen examples of this:

```python
# Some in-built python functions
input("We can pass a string to the input function")
len(['need', 'to', 'pass', 'something', 'to', 'get', 'its', 'length'])
```

In order to add this functionality to our functions, we include the parameters in the definition of the function - specifically, inside the brackets next to the function's name:

```python
# Function prints the first and last character in string
def first_and_last(some_string):
    print(some_string[0] + some_string[-1])

first_and_last("abcde")
# Prints ae
```

{% hint style="info" %}
If the function takes arguments, then we **have to** provide them. \(unless we use default arguments - see [extensions](extensions.md#default-arguments)\)
{% endhint %}

It's also important to remember that the type of variable you pass to the function matches what the person who defined it \(probably you\) expected:

```python
# But, we HAVE to pass something compatible!
first_and_last()     # ERROR - Need to pass something!
first_and_last(1321) # ERROR - We can't use variable[index] on integers
```

It can be a good idea to add [type checking](../week-3/extensions.md#basic-error-handling) to your functions to make sure that the arguments a user passes in are compatible with the operations that your function performs:

```python
# Need to think about these things!
def first_and_last_v2(mebbe_string):
    defo_string = str(mebbe_string) # Throws error if not a valid type cast
    print(defo_string)
```

## Modules and Packages <a id="Modules-and-Packages"></a>

We don't want to reinvent the wheel - If someone has implemented something for us, then we can just use that. But first, some definitions:

* **Module** - a file containing functions. The filename is module\_name.py
* **Package** - a collection of modules
* **Library** - a collection of packages \(doesn’t necessarily provide just one functionality\)

### Import <a id="Import"></a>

If we want to use modules/packages in our scripts, then once we've installed them \(either using anaconda's navigator software, or[ PIP](extensions.md#pip)\) we need to **import** them. This is done by using the **import** statement, e.g.:

```python
# "time" is a package which comes with python

import time   # We import the time module
time.sleep(3) # sleep function is part of time module
```

### From <a id="From"></a>

Sometimes we don't want to import everything from a package - we can pick specific modules using **from**

* E.g. if we have our own function, also called sleep\(\), we probably don't want to import the sleep\(\) function from time

Additionally, if we use from, we don't need to explicitly call the function via the module

```python
# All I want to do is sleep
from time import sleep
sleep(3)  # Don't need to call via time module
```

### As <a id="As"></a>

If we want to refer to the imported functions or modules using a different name, then we can import them **as** something else

```python
# Zen
from time import sleep as meditate
meditate(3)
```

This can be useful if you have a function with the same name, or if the name of the module/function is annoyingly long

```python
import time as t # Can change module name
t.sleep(3)
```



