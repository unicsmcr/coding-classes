---
description: 'Solutions to Lists, Dictionaries, Error Handling and List Slicing'
---

# Week 3

## Exercise 1 - Login System MKII

Here we create a new and improved login system, by making use of the different **data structures** we have learnt about, **dictionaries** and **lists.**

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ex1.py" %}
```python
# Store the username and password as key-value pairs 'username : password'
users = {"alex" : "1234", "joe" : "5678", "luke" : "0000"}

# store the bad passwords in a list
bad_passwords = ["password", "pass", "word", "1234"]

# store custom welcome messages for each user in users
welcome_msgs = {"alex" : "Greetings Alex", 
                "joe" : "Howdy Joe", 
                "luke" : "Good day Luke"}

# Add a captcha by getting the user to answer a question
answer = input("What is 4 + 21? ")    # always reads a string
answer = int(answer)    # convert string input to integer

# if captcha answer was wrong, print error message and quit program
if answer != 25:
    print("You are not human!")
    exit()    # stops the script from being run

# Now get user to enter their name
input_name = input("Enter your username: ")
input_name = input_name.lower() # Convert to lowercase

# check if the username exists in our users-password dictionary
if input_name in users.keys():
    # input_name exists so check password matches
    input_password = input("Enter your password:")
    if input_password == users[input_name]:
        # password is correct, print custom welcome message
        print(welcome_msgs[input_name])
        
        # check if the password is in the bad list
        # use lower() to ignore case when checking for bad passwords
        if input_password.lower() in bad_passwords:
            # password is bad so give the option to change it
            change_password = input("Warning: Password sucks, change?(y/n):")
            if change_password == "y":
                # user wants to change, so get a new one
                new_password = input("Enter new password:")
                users[input_name] = new_password  # store for that user
                print("Password changed to:" + new_password)
    else:
        # password invalid
        print("You have entered an incorrect password")
else:
    # input_name is not in the users dictionary
    print("Unknown username")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extensions

The code for the extensions can be inserted into the solution above between the preceding and subsequent lines of code -- see the comments in the code for which lines these are.

## Extension 1 - Incompetent User Warning

We put the integer conversion into a try except block so that we can stop the program from reporting an error when a non-integer answer is entered.

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext1.py" %}
```python
.............
answer = input("What is 4 + 21? ")    # preceding line
# input always returns a string, so we need to convert it to an integer

# attempt to convert the inputted string to an integer
try:
    answer = int(answer)
except ValueError:
    print("You are incompetent! That was not an integer!")
    exit()
    
if(answer != 25):    # subsequent line
.............
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 2 - List Slicing Fun

We take the poem as a string and split it up using the **split\(' '\)**  method, splitting on spaces. Then we get every sixth word in the list using **list slicing**, rejoin the list together and print the result.

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext2.py" %}
```python
poem = "hidden from all to see, trapped in an eternal night, those shadows plain surrounding me, no sunrise in sight"

# split the poem into a list of words
poem_list = poem.split(' ')

# split the list on every 6th word
new_poem_list = poem_list[::6]

# create a new poem from the list of words
new_poem = " "  # space is our separator
new_poem = new_poem.join(new_poem_list)
print(new_poem)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 3 - Forced Palindromes

We ask the user to input a word, and print out a palindrome version of the word, using list slicing by reversing the word and not including the first reversed character

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext3.py" %}
```python
# Get a word from the user
user_input = input("Enter a word:")

# reverse the word and don't include the first reverse character
new_word = user_input + user_input[::-1][1:]
print(new_word)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 4 - Random Captcha



