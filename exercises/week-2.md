---
description: Python Basics - Conditional Logic and Input
---

# Week 2

## Spyder setup

1. Start by creating a new folder somewhere on your computer called "python\_classes" and then create another folder inside called "week2" - This is where you'll be placing the python scripts \(.py files\) which you write today
2. Open up Spyder and create a new file inside the _week2_ folder called "hello\_world.py"
3. Add a print statement which outputs **hello world** to the console, and make sure that it runs by pressing the green arrow in the toolbar and checking for the print output in the console

## Login system

This week we're going to create a simple login system by using the **input\(\)** function, and if statements.

### Storing user information

For the time being, we're going to store user information in separate variables. Let's start by adding a user with the following details:

_**Name:**_ Alex  
**Password:** 1234

{% hint style="info" %}
In order to check the name and password in two separate steps, you'll have to store this information in two separate variables
{% endhint %}

### Checking the username

Using the **input\(\)** function, ask users to enter their username, then check that the value they entered **exactly matches** the one in the database \(e.g. "Alex"\) - use print statements to let the user know if they entered an incorrect username

### Checking the password

Now use **input\(\)** again when the user has entered the correct username, but this time ask for the password. If the user succeeds in typing in a correct username-password pair, you should print a _secret_ message.

## Extension 1 - Case sensitivity

Using the **.lower\(\)** function \(see [extension material](../material/week-2/week-2-extension.md#sub-component-checking-with-in)\), make the username check non-caps sensitive.

{% hint style="info" %}
1. Try and use the function only once, by reassigning the input immediately after gathering it
2. Make sure that your database only contains lowercase usernames - otherwise some people will never be able to login
{% endhint %}

## Extension 2 - Two users

Using the logical **and/or** operations, add the ability for another user \(with a distinct username-password pair\) to login

{% hint style="info" %}
You'll need to make use of nested if-statements to ensure the password matches the username
{% endhint %}

We'll see a far more elegant way of adding more users to our database in subsequent weeks \(using dictionaries!\).

## Extension 3 - Bad Passwords

### Warning

Using the **in** operation \(see[ ](../material/week-2/week-2-extension.md#sub-component-checking-with-in)[extension material](../material/week-2/week-2-extension.md#sub-component-checking-with-in)\), have a go at users who have passwords containing the substrings **"1234"** _or  **"**_**pass"** _or_  **"word",** but only once they've logged in successfully

### Password Change

Instead of just berating the user for their poor choice of password, give them the **option** to **change** their password \(i.e. override the old one\). 

Once they've changed their password, print it out to confirm it worked.



### 







