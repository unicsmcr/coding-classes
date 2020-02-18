---
description: Solutions to Python Basics - Conditional Logic and Input
---

# Week 2

## Exercise 1 - Login System

Here we create a simple username-password checker by comparing **user input** to **stored variables,** using **nested** if-statements. 

{% code title="week2\_solutions\_ex1.py" %}
```python
# 1. Declare username and password
username = "Alex"
password = "1234"

# 2. Get username input
username_input = input("Enter your username >>> ")

# 3. Compare to see if username entered is correct
if username_input == username:

    # 4. if username correct, get password
    password_input = input("Enter your password >>> ")
    
    # 4.a compare to our password
    if password_input == password:
        print("logged in successfully")
    else:
        print("Password incorrect")

# 5. If not correct print error
else:
    print("incorrect username")
    
```
{% endcode %}

## Extension Exercise 1 - Case Sensitivity 

Here we use the **.lower\(\)** function to ensure that our system isn't sensitive to capitalization in usernames - this also means that we need to store lowercase usernames in our "database".  
  
Note that the ****.lower\(\) function **does not reassign** the value of a variable automatically, so we have to reassign manually.

{% code title="week2\_solutions\_ext1.py" %}
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
         # Password is correct -> print a secret message
         print("this is a secret")
     else:
         # Password didn't match -> print an error
         print("You have entered an incorrect password")

```
{% endcode %}

## Extension Exercise 2 - Two users

The aim of this extension and the next is to become comfortable with many different levels of nested statements, and more complicated logical expressions.  
  
**Note:** These examples are fairly ugly and contrived - in future weeks we will see how we could make this system far more efficient, and our code far more elegant.

{% code title="week2\_solutions\_ext2.py" %}
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
{% endcode %}

## Extension 3 - Bad Passwords

This is a fairly grueling exercise, but quickly recognizing the logical exclusivity which is implied by the **indentation level** of a piece of code is an essential skill for python programmers - so try and make sure you fully understand why this solution works!

{% code title="week2\_solutions\_ext3.py" %}
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
            # Ask if they want to change their password
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
{% endcode %}

