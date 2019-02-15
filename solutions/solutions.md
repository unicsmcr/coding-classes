---
description: Solutions to Python Basics - Conditional Logic and Input
---

# Week 2

## Exercise 1 - Login System

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ex1.py" %}
```python
# we store the name and password in 2 separate variables
name = "Alex"
password = "1234"

# first we will get the user to enter their name
# and then check it with the one we have stored in 'name'
input_name = input("Enter your name:")
if not input_name == name:
    # the input_name does not equal the name
    print("You have entered an incorrect username")
else:
    # the input_name does equal the name so we ask for the password
    input_password = input("Enter your password")
    if input_password == password:
         # the password is correct, so we print a secret message
         print("this is a secret")
     else:
         # the password didn't match so print an error
         print("You have entered an incorrect password")

```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension Exercise 1 - Case Sensitivity 

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext1.py" %}
```python
# we store the name and password in 2 separate variables
# name must be lowercase
name = "alex"
password = "1234"

# first we will get the user to enter their name
# and then check it with the one we have stored in 'name'
input_name = input("Enter your name:")
# we then take the input and convert it all to lowercase
input_name = input_name.lower()

if not input_name == name:
    # the input_name does not equal the name
    print("You have entered an incorrect username")
else:
    # the input_name does equal the name so we ask for the password
    input_password = input("Enter your password")
    if input_password == password:
         # the password is correct, so we print a secret message
         print("this is a secret")
     else:
         # the password didn't match so print an error
         print("You have entered an incorrect password")

```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension Exercise 2 - Two users

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext2.py" %}
```python
# we store the name and password in 2 separate variables for each user
# name must be lowercase
name1 = "alex"
password1 = "1234"
name2 = "joe"
password2 = "5678"

# first we will get the user to enter their name
# and then check it with the one we have stored in 'name'
input_name = input("Enter your name:")
# we then take the input and convert it all to lowercase
input_name = input_name.lower()

# check if the input matches the first user, and not the second
if input_name == name1 and not input_name == name2:
    # input_name is name1 and not name2, check password of name2
    input_password = input("Enter your password: ")
    if input_password == password1:
        print("Welcome")
    else:
        print("You have entered an incorrect password")

# not the first user, so check input matches second user, and not first
elif input_name == name2 and not input_name == name1:
    # input_name is name2 and not name1
    input_password = input("Enter your password:")
    if input_password == password2:
        print("Welcome")
    else:
        print("You have entered an incorrect password")

else:
    # input_name is either not correct, or the names match
    print("You have entered an incorrect username")


```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 3 - Bad Passwords

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext3.py" %}
```python
# we store the name and password in 2 separate variables for each user
# name must be lowercase
name1 = "alex"
password1 = "1234"
name2 = "joe"
password2 = "5678"

# first we will get the user to enter their name
# and then check it with the one we have stored in 'name'
input_name = input("Enter your name:")
# we then take the input and convert it all to lowercase
input_name = input_name.lower()

# check if the input matches the first user, and not the second
if input_name == name1 and not input_name == name2:
    # input_name is name1 and not name2, check password of name2
    input_password = input("Enter your password: ")
    if input_password == password1:
        print("Welcome")
        
        # check if the password contains a bad password component
        if "1234" in password1 or "pass" in password1 or "word" in password1:
            # ask if they want to change it
            change_password = input("This is a rubbish password, change it?(y/n):")
            if change_password == "y":
                # get a new password, and print it out to show its changed
                password1 = input("Enter new password: ")
                print("Password changed to:" + password1)
    else:
        print("You have entered an incorrect password")

# not the first user, so check input matches second user, and not first
elif input_name == name2 and not input_name == name1:
    # input_name is name2 and not name1
    input_password = input("Enter your password:")
    if input_password == password2:
        print("Welcome")
        
        # check if the password contains a bad password component
        if "1234" in password2 or "pass" in password2 or "word" in password2:
            # ask if they want to change it
            change_password = input("This is a rubbish password, change it?(y/n):")
            if change_password == "y":
                # get a new password, and print it out to show its changed
                password2 = input("Enter new password: ")
                print("Password changed to:" + password2)
    else:
        print("You have entered an incorrect password")

else:
    # input_name is either not correct, or the names match
    print("You have entered an incorrect username")



```
{% endcode-tabs-item %}
{% endcode-tabs %}

