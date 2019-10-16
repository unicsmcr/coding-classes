---
description: Control - while and for
---

# Week 5

## Control

### While

While loops allow us to do something **while** a condition is met - providing the first statement which can drastically _control_ the flow of our program. The syntax for these is very similar if statements, with the important distinction that the code inside runs continuously until the condition becomes False:

```python
while condition:
    print("Repeated until condition = false")
```

It's important to note that if the condition never becomes false, then the loop will run forever!

```python
# This will run forever! - "infinite while loop"
while True:
    print ("Shame...")
```

In this case, you can abort with ctrl+c \(in the console\) or by pressing the stop button in most IDEs.

Here's an example of how we can use a "counter" with a while loop:

```python
number = 0

# Keep looping until number has reached the value of 5
while number < 5:
    number += 1
    print(number)
```

And an example of waiting for a correct user input:

```python
acceptance = "" # Keep track of condition

print("I know these python classes are the highlight of your week!")
while (acceptance != "It's true"): 
    acceptance = input("Confess! ")
```

We can use and/or to make the while statement's **loop condition** more sophisticated. For example, we could allow users to type their passwords in up to three times.

```python
password = "hello"
user_pass = input("Please enter your password")
remaining_attempts = 3

while (user_pass != password) and (remaining_attempts > 0):
    user_pass = input("Try again: ")
    remaining_attempts = remaining_attempts - 1
```

Notice, however, that in this example we don't know why we left the while loop, as it can occur as a result of the user entering the correct password, or having tried too many times. This means we'd need to add additional if statements below. \(this can be circumvented by using [break statements](extensions.md#break-and-continue)

We often use while statements to do things a certain number of times \(again, using a counter\):

```python
# Remove all 4 limbs 
limbs_remaining = 4

while limbs_remaining > 0: # Run until the blacknight dies
    print("Come on then!") 
    limbs_remaining = limbs_remaining - 1 # Increment the counter
    
print("We'll call it a draw")
```

Finally, we can use such counters to loop through lists using a while statement:

```python
my_list = ['She', 'sells', 'sea', 'shells']
index = 0 # "counter" to keep track of index

# Loop through our list
while index < len(my_list):
    print(my_list[index])
    index = index + 1
```

But there is a far more natural way of looping through lists in python:

### For

A far more elegant way of looping through data structures that contain some number of elements is to use "for" loops. Think of these as "**for** _**each item**_ **in** _**data structure**_**"**

```python
# We can use for loops to get things directly from a list
for item in ["Python", "classes", "ftw"]:
    print(item)
```

The same syntax can also be used on dictionaries \(and other "iterable" objects\) - going through the **keys** by default

```python
my_dict = {"hi" : 1, "fish" : "frog"}

# Can also use for loops to loop through dictionaries
for thing in my_dict: # gives same as my_dict.keys()
    print(thing)
```

### Range

The python **range\(\)** function gives us a useful way of creating a list of numbers. **Note:** the function returns integers ranging from the first parameter to the second, but not including the second!

```python
for num in range(2, 6):
    print(num)
# prints 2 3 4 5
```

Technically range doesn't actually create a list data structure, as such, if you want to create a list of number by using range, you'll need to **typecast** using list\(\)

```python
numbers = list(range(2,14)) # Create a list of integers
print(numbers)
```

Here's an example of using a for loop with range, to print even numbers in a range:

```python
# Print even numbers <= 20
for num in range(0, 20):
    if num % 2 == 0: 
        print(str(num) + " is an even number")
```

And here's a better way \(there often is one!\):

```python
# Better way to print even numbers <= 20
for num in range(0, 10):
    print(str(num * 2))
```

### Length

If we want to find out how many items are in a data structure we can use the length function, **len\(\)**:

```python
my_list = ['Size', 'doesn\'t', 'matter']

size = len(my_list) # size = 3
```

### Duplicate Search

Here's an example making use of **nested for loops** to find duplicated items in a list -&gt; Here we explicitly use range\(len\(\)\) so that we can index the list, rather than access its items. We do this because we want to avoid checking the same list index against itself \(as this will always be equal\):

```python
# Another example - a duplicate search
sentence = ['She', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shore']

# Use indices explicitly, to avoid checking the same word against itself
for i in range(len(sentence)):
    for j in range(len(sentence)):
        if (i != j) and (sentence[i] == sentence[j]):
              print(sentence[i] + " is duplicated!")
```

### 

