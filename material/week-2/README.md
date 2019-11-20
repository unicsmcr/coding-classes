---
description: Programming Languages and Python
---

# Week 2

## Recap

Last time we discussed how we can use pseudocode to break down complex tasks into manageable chunks, before starting to issue exact instructions. We saw this in action during the jam sandwich demonstration.

And while pseudocode is nice, we ultimately need a consistent way of telling computers what to do - To this end, programming languages have been developed which allow allow programmers to write fairly readable code which is then converted into in machine-level binary code by a compiler \(luckily, we don't need to worry about this\).

## Python

### Why Python?

**Easy to learn**   
Python reads almost like English, just with a few extra rules thrown in - at least when compared to some other popular programming languages!

**Fairly fast**   
As a rule of thumb, one can usually assume that the more readable a language is, the slower and less customization it is. However, python manages can still be very fast when used sensibly, especially for routine data science and machine learning tasks.

**Popular**  
Python's popularity means that many libraries have been written for it - these allow us to do everything from data science through to interacting with spotify and twitter.  
  
Additionally, python is an increasingly popular language in industry. It is used extensively for data science and machine learning work \(especially at Google\) as well as for prototyping new technologies \(because it's quick and easy to get stuff working in it\).

### How Python?

For the purposes of this course we'll be using the **Anaconda** python distribution, with python version 3.7

This is because the Anaconda distribution comes with many packages pre-installed which will come in handy later, and because it comes with the **Spyder** IDE \(integrated-development-environment\), which makes writing and running python code a breeze.

## Python - Baby Steps

### Syntax and Comments

The **syntax** of a language describes the rules and instructions which can be used when coding.

All programming languages have specific ways of including normal English inside your **scripts** \(i.e. files filled with code\) which can be used to explain the function of the code. These are referred to as **comments,** because they allow us to comment on the code.

In python, single-line comments are started with hashtag \(\#\) symbols and cause following text on the same line to be ignored by python. This allows the programmer to add explanations / notes to their code such that other programmers can understand it more easily. \(Comments also serve as useful reminders for the programmers themselves\)

Additionally, and text enclosed between a pair of triple-double \("""\) quotes forms a comment \(which can be multi-line\):

```python
# Hashtags denote one-line comments - These are ignored by python
# Use comments to explain what the code is doing

""" Triple quotes can be used for multi-line comments
    These are usually used for file headers or when declaring fuctions 
"""
```

### Hello World

In Python, the **print** statement allows us to output text to the console:

{% code title="hello\_world.py" %}
```python
# Say "Hello World!" to the user, via the terminal, when the code runs
print("Hello World!")
```
{% endcode %}

When specifying the **string** which is being printed, we need to be careful to ensure that the enclosing quotes are identical - otherwise python gets confused and doesn't think the string has ended.

{% code title="string\_quotes.py" %}
```python
print('I am a string')
print("So am I!")
print("Hey, can I join you guys?') # This wont work!

# You can have different quotes as part of your string
print("Gnomic as ever, Alex moaned 'Alea Iacta Est'")
```
{% endcode %}

{% hint style="danger" %}
#### Indentation

Other languages have lots of brackets \({\[\]}\) all over the place - python only cares about **indentation;** I.e. things need to lined up nicely, or indented if they are **nested** in each other:

{% code title="" %}
```python
# Indentation needs to be consistent
print("Hello World!")
    print("Python won't run this!")
```
{% endcode %}
{% endhint %}

**Variables**

Variables are what we use to store information within our code, and can be thought of as labelled boxes containing data.

![Variables can be thought of as labelled boxes containing data](../../.gitbook/assets/image%20%2815%29.png)

**Declaration**

{% code title="declaration\_example.py" %}
```python
# Create some variables
my_string = "Hello World"
my_integer = 1239082
my_boolean = True

# Reassign a variable to different value
my_boolean = 47
```
{% endcode %}

**pascal case vs camelcase**

{% code title="pascal\_vs\_camel.py" %}
```python
# Camel case and pascal case are the two most common variable naming schemes
# They don't affect how your code runs, but "code readability" is important!

aCamelCaseVariable = "This is not the python way"
a_pascal_case_variable = "This is the python way"
```
{% endcode %}

### Maths

| Operator | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| + | Addition | 17 + 3 | 20 |
| - | Subtraction | 14 - 21 | -7 |
| \* | Multiplication | 3 \* 24 | 72 |
| / | Division | 10 / 4 | 2.5 |
| \*\* | Exponentiation | 2 \*\* 4 | 16 |
| % | Modulo | 22 % 3 | 1 |

{% hint style="warning" %}
In the case of division, the output has a decimal point even though the operands are both integers - python is nice like that.

 You will often need to be careful to not mix decimal and integer values when performing certain operations, as you may incur rounding error \(we will discuss this more later on when we cover data types, and the difference between "int"s and "float"s\).
{% endhint %}

### Boolean Logic and Conditions

Mathematical logic essentially allows us to compare things in a well-defined, consistent way. The ability to do this is essential for allowing us to build useful computer programmes. The types of comparison operations that we can perform in python are outlines in the following table:

| Operator | Description | Example | Output |
| :--- | :--- | :--- | :--- |
| &lt; | less than | 5 &lt; 8   | True |
| &gt; | greater than | 4.3 &gt; 2 | True |
| == | equals | "Hello" == "there" | False |
| &lt;= | less than or equal to | 5 &lt;= 5 | True |
| &gt;= | greater than or equal to | 8 &gt;= 110 | False |
| != | not equal | "General" != "Kenobi" | True |

For example

{% code title="logic\_example.py" %}
```python
# An example of using logic

is_this_true = 3 > 10 # Let us see if 3 is > 10; The result should be False
print(is_this_true) # Print out the result, hopefully it will say False
```
{% endcode %}

### If and Else

If statements execute code provided that the specified condition is satisfied

```python
if (True):
    print("Condition was met")
else:
    print("Condition wasn't met")
```

We can use conditional operators to determine when an if statement should trigger.

```python
if (7 > 4):
    print("Computer is clever")
else:
    print("I thought 'it just works' steve?!")
```

Coupled with variables, this allows us to **control** the flow of our code.

#### Else if

In the script above, we used an "if-else" statement, but in some cases we might want to multiple possible specific answers differently. For this we can use "elif" \(short for else if\) :

{% code title="elif\_example.py" %}
```python
user_name = "Augustus" # We don't need humans!

if (user_name == "Alex"):
    print("I've been expecting you...")
elif (user_name == "Augustus"):
    print("Ad omnes Ave Caesar")
else:
    print("Nice to meet you " + user_name)
```
{% endcode %}

### Input

Sometimes we want the user to give us some information, which we then use somehow in our code. Luckily, python has a built in _function_ \(aka method\) which easily allows us to do this:

```python
# Input returns a string
user_input = input()
```

Now we are ready to create programs which respond differently based on the user's input

{% code title="if\_else\_example.py" %}
```python
user_answer = input("What is 7 + 3? ")

if (user_answer == "10"):
    print("Check you out!") 
else: # Catch all inputs which aren't 10
    print("Happens to the best of us") # Lie to the user

```
{% endcode %}

Finally, it is worth noting that we can concatenate string by using the + operator:

{% code title="input\_example.py" %}
```python
# This code will compliment our human user

name_of_user = input("Hi! What is your name? ") # Get user input

output_string = "Nice to meet you " + name_of_user + " - Looking good! ;)"
print(output_string) # Print our compliment string

```
{% endcode %}





