---
description: Solutions to Python Basics - Conditional Logic and Input
---

# Week 2

## Exercise 1 - Login System

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ex1.py" %}
```python
# Store the name and password in 2 separate variables
name = "Alex"
password = "1234"

# First get the user to enter their name
input_name = input("Enter your name:")

# Check against the name we have stored in 'name'
if input_name != name:
    # The input_name does not equal the name
    print("You have entered an incorrect username")
else:
    # The input_name matches the name -> ask for password
    input_password = input("Enter your password")
    
    if input_password == password:
         # Password is correct -> print a secret message
         print("this is a secret")
     else:
         # Password didn't match -> print an error
         print("You have entered an incorrect password")

```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension Exercise 1 - Case Sensitivity 

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext1.py" %}
```python
# Store the name and password in 2 separate variables
name = "alex" # name must be lowercase
password = "1234"

# First get the user to enter their name
input_name = input("Enter your username: ")
input_name = input_name.lower() # Convert to lowercase

if input_name != name:
    # input_name does not equal the name
    print("You have entered an incorrect username")
else:
    # input_name matches name -> ask for password
    input_password = input("Enter your password")
    
    if input_password == password:
         # password is correctw -> print a secret message
         print("this is a secret")
     else:
         # password didn't match -> print an error
         print("You have entered an incorrect password")

```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension Exercise 2 - Two users

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext2.py" %}
```python
# For each user, store the name and password seperately
# Again, name must be lowercase
name1 = "alex"
password1 = "1234"

name2 = "joe"
password2 = "5678"

# First get user to enter their name
input_name = input("Enter your username: ")
input_name = input_name.lower() # Convert to lowercase

# Check if the username matches one we have stored
if input_name == name1 or input_name == name2:
    # Valid username -> Ask for password
    input_password = input("Enter your password: ")
    
    # Now check that the password matches for the corresponding user
    if input_name == name1 and input_password == password1:
        print("Welcome, First user")
    elif input_name == name2 and input_password == password2:
        print("Hey there, Second user")
    else:
        # Password didn't match 
        print("You have entered an incorrect password")
else:    
    # Username didn't match
    print("You have entered an invalid username")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 3 - Bad Passwords

{% code-tabs %}
{% code-tabs-item title="week2\_solutions\_ext3.py" %}
```python
# For each user, store the name and password seperately
# Again, name must be lowercase
name1 = "alex"
password1 = "1234"

name2 = "joe"
password2 = "5678"

# First get user to enter their name
input_name = input("Enter your username: ")
input_name = input_name.lower() # Convert to lowercase

# Check if the username matches one we have stored
if input_name == name1 or input_name == name2:
    # Valid username -> Ask for password
    input_password = input("Enter your password: ")
    
    # Now check that the password matches for the corresponding user
    # Do it in one big check, so we don't have to repeat the password check
    if ((input_name == name1 and input_password == password1) or
        (input_name == name2 and input_password == password2)):
        print("Welcome, " + input_name)

        # Check if the password contains a bad component
        if ("1234" in input_password or 
            "pass" in input_password or 
            "word" in input_password):
            # Ask if they want to change it
            change_password = input("Warning: Password Sucks, change?(y/n): ")
            if change_password == "y":
                # Get a new password, and print it out to show its changed
                new_password = input("Enter new password: ")
                
                # Need to change the correct password
                if input_name == name1:
                    password1 = new_password
                else: # Know this must be user2
                    password2 = new_password
                
                print("Succesfully change password to :"  + new_password)                   
    
    else:
        # Password didn't match 
        print("You have entered an incorrect password")
else:    
    # Username didn't match
    print("You have entered an invalid username")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

