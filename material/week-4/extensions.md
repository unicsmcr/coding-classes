---
description: 'Break, Continue, Enumerate, Strings as Lists, List comprehension'
---

# Extensions

## Break and Continue

Sometimes we want to **exit a for/while loop** before the defining condition is met, or skip some of the iteration steps. **Break and Continue** statements provide this functionality respectively - **Note** it is not good practice to use these unnecessarily, as you can usually just define the **loop condition** differently.

### Break

If we want to exit a loop prematurely, we can use the **break** statement. 

```text
# break statement use
num = 0
while num < 10:
    if num == 5:
        break
    print(num)
    num = num + 1

# This code will print "0 1 2 3 4" - I.e. the loop  is cut short
```

For an actual usage example, suppose we want to find a prime number greater than 9000, but less than 10000 \(not knowing if there is one in this range\):

```python
num = 9000
while num < 10000: 
    if is_prime(num): # suppose we have an is_prime() function
        print(str(num) + " is a prime number")
        break
    num = num + 1
```

### Continue

**Continue** allows us to skip iteration steps inside a loop. This might be helpful if we have a complicated for loop which shouldn't carry out its usual operation in a certain case.

For example, we could print the even numbers &lt; 10:

```python
for num in range(0,10):
    if num % 2 != 0: # Number is odd
        continue 
    print(num)
```

**Note:** This is not actually a sensible use of continue, as there are far better ways of printing even numbers in a range \(for example, x2 every element in range/2\).

## Enumerate

Sometimes we want to iterate through a list, accessing its elements but also keeping track of the corresponding index. Whilst we could use a counter variable to do this manually, Python's built-in **enumerate\(\)** function provides and elegant way of doing this:

```python
my_list["Reduce", "Reuse", "Recycle"]

for index, item in enumerate(my_list):
    print("Item " + index " is " + item)
```

## Strings as lists of characters 

Some of you may have noticed that we can use the "in" function on strings as well as lists:

```python
# Remember this?
if "a" in "alex":
    print("Yeehaa")
```

Equivalent to 

```python
# What about
if "a" in ['a','l','e','x']:
    print("Strange")
```

For our purposes, we can think of strings as lists of characters, and manipulate them as we would lists - slicing and all!

Here's a simple example demonstrating reverse iteration through a string:

```python
# Strings are a lists
the_dream = "desserts"
university = the_dream[::-1] # Step backwards from end

print(university)
```

And another example showing some contrived list slicing:

```python
# Can use list slicing syntax on strings
my_string = "Luke is on a roll"

daily_mail_string = my_string[0:8] + my_string[11:13] + "t" + my_string[13:]
print(daily_mail_string) # "Luke is a troll"
```



