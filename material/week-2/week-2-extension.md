---
description: Basic String Manipulation & and/or
---

# Extensions

## More on Modulo

The modulo operator provides a useful way of checking whether something a multiple of something else - it essentially returns the remainder after as many steps of division as possible:

{% code-tabs %}
{% code-tabs-item title="modulu\_example.py" %}
```python
test1 = 12 % 2 # this will equal 0 as 2 divides 12 exactly
test2 = 13 % 2 # this will return 1 as 13 = (6 * 2) + 1

# We can use this to check if something is even or odd!
number = 10
if (number % 2) == 0:
    print("Number divisible by 2. That means it's even!")
else:
    print("How odd ¯\_(ツ)_/¯")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## More Logic with _and_ & _or_

The logical **and** & **or** operators allow us to increase the complexity of logic in our programmes, without needing to a bunch of **nested** \(one inside another\) if statements. These can be used at declaration, or in our logical conditions, just as with the previously encountered operands \(==, != etc.\)

* **and** is true when both following statements are true
* **or** is true when at least one of the following statements is true

{% code-tabs %}
{% code-tabs-item title="and\_or\_example.py" %}
```python
# Use in declaration
try_and1 = (7 > 6) and ("hi" != "bye") # will be true
try_and2 = (6 > 7) and ("hi" != "bye") # will be false
try_or = (6 < 7) or ("hi" != "bye") # will be true!

# Use in comparison
is_scary = False
has_scales = True

if has_scales and is_scary:
    print("GODZILLA!!! \0/ \0/ \0/")
elif has_scales or is_scary: # one or the other, as "and" wasn't true
    print("Get it away from me!")
else:
    print("How boring...")
```
{% endcode-tabs-item %}
{% endcode-tabs %}



## Sub-component checking with _in_

**in** allows us to check if a substring or item is contained in a specified object. This will be useful when we discuss lists shortly, but we've already seen how this can be used:

{% code-tabs %}
{% code-tabs-item title="in\_examply.py" %}
```python
# For strings
if ("a" in "alex") or ("b" in "bobby"):
    print("I can spell!")
else:
    print("Weird alphabet..")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

String manipulation & 

Here we see an example of how we can **nest** control statements**,** and use the **.lower\(\)** function to ensure our if statements are not sensitive to the capitalization of user input.

{% code-tabs %}
{% code-tabs-item title="string\_manip.py" %}
```python
fav_num = 17

my_string = "SoMeMeSS"
my_string = my_string.lower() # Make it lowercase for easier comparison

if "mess" in my_string: # use *in* 
    print("My life")
elif my_string == "doggo": # else-if
    if fav_num == 17: # so-called "nested" if statement
        print("Doggos are awesome, and so is the number 17")
else:
    print("I'm running out of ideas :<")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Putting it all together

{% code-tabs %}
{% code-tabs-item title="advanced\_input\_example.py" %}
```python
""" Robust and more Complicated example 
    Taking user input and check against different kinds of cases
"""

# Get the user's name
user_name = input("What's your name? ")
user_name = user_name.lower() # Make the string lowercase - overwrite

# Do some conditional logic
if user_name in ['alex', 'luke']: # Can check multiple cases in one
    print("Your Majesty...")
elif ("z" in user_name) or ("q" in user_name): # Check multiple substring cases
    print("Shame your name isn't allowed in scrabble!")
else:
    print("Heyo")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

