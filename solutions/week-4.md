---
description: 'Solutions to While, For and Challenges'
---

# Week 4

## Exercise 1 - Finishing Login System

Here we finally finish the login system by making use of while loops to let the user have multiple attempts at entering the password correctly.

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
    remaining_attempts = 3
    
    # if the password is wrong and we have attempts left, ask again
    while (input_password != users[input_name]) and (remaining_attempts > 0):
        # re-enter the captcha
        captcha_answer = input("Wrong password! What is 7 + 36? ")
        captcha_answer = int(captcha_answer)    # convert to integer
        # captcha was wrong, so stop them trying
        if captcha_answer != 43:
            print("You are not human!")
            break
        
        input_password = input("Try again:")
        remaining_attempts = remaining_attempts - 1
    
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
        print("You have run out of password attempts!")
else:
    # input_name is not in the users dictionary
    print("Unknown username")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2.1 - Hip to be Square

Here we print a square of 'X' with a side length entered by the user

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ex2\_1.py" %}
```python
# request a number, entered by the user
size = input("Enter a number: ")
size = int(size)  # Convert to int, assuming the input was an integer

# print size amount of 'X', size times - to produce size x size square
for number in range(size):
    print("X " * size)

# print hollow square
# print top border - a line of X, then print middle - 'X spaces X',
# then bottom border
print("X " * size)
for number in range(size-2)
    print("X " + "  " * (size-2) + "X ")
print("X " * size)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2.1 Extension - Hollow Square

This time we print a hollow square

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext2\_1.py" %}
```python
# request a number, entered by the user
size = input("Enter a number: ")
size = int(size)  # Convert to int, assuming the input was an integer

# print top border - a line of X, then print middle - 'X spaces X',
# then bottom border - a line of X
print("X " * size)
for number in range(size-2)
    print("X " + "  " * (size-2) + "X ")
print("X " * size)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2.2 - Hidden message via For Loop

Split the message into words and put into a list. Then we loop through them all and only add them to the secret message if the word begins with an uppercase character.

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ex2\_2.py" %}
```python
# the secret message
message = "it was The best of times, it was the worst of times, it was the age of wisdom, it was the age of Foolishness, it was the epoch Of Belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it Was The spring of Hope, it was the winter Of despair, we had everything before us, we had nothing before us, we were all Going direct To Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

words = message.split(" ")
secret_message = ""
for word in words:
    if word[0].tolower != word[0]:
        secret_message = secret_message + word + " "

print(secret_message)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2.3 - Pythagorean Triples

Here we print all the Pythagorean Triples which sum to less than 100 using for loops to calculate them. To check that c\*\*2 = a\*\*2 + b\*\*2, we get the square root of a\*\*2 + b\*\*2 which will be a decimal value, and we check that it equals the integer version, e.g. 5.0 == 5. 

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ex2\_3.py" %}
```python
# the stored triples
pythag_triples = []

for a in range(1, 101):
    for b in range(a, 101):
        c = a * a + b * b
        
        # need to check that c is a square number
        # so we check the square root is equal to the int version of sqrt
        if c**0.5 < 100 and c**0.5 == int(c**0.5):
            pythag_triples.append([a, b, int(c**0.5)])
            
print(pythag_triples)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension 1 - Goat Latin

We implement Goat Latin \(adding extra "a"s to the beginning of words in repeating pattern of 1, 2, 3\) by using for loops

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext1.py" %}
```python
# Get the user input first
user_input = input("Enter a sentence: ")

result = ""
num_of_a = 1
words = user_input.split(" ")
for word in words:
    # add num_of_a amount of a's to the beginnning of the word
    result = result + "a" * num_of_a + word + " "
    
    # increment number of a's, but keep value between 1 and 3
    num_of_a = num_of_a + 1    
    if num_of_a > 3:
        num_of_a = 1
    
print(result)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Extension Extra 1 - Advanced Goat Latin

This time, if a word begins with a vowel, append 'ma' to it, otherwise take the first letter, remove it from the beginning and add to the end and then append 'ma' to it. Also add an 'a' to the end of each word per index in the list, e.g. 4 a's for the fourth word.

{% code-tabs %}
{% code-tabs-item title="week3\_solutions\_ext2.py" %}
```python
# the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Get the user input first
user_input = input("Enter a sentence: ")

result = ""
index = 1
words = user_input.split(" ")
for word in words:
    # word begins with a vowel
    if word[0] in vowels:
        result = result + word
    else:
        result = result + word[1:] + word[0]
        
    # now add "ma" followed by index number of 'a'
    result = result + "ma" + "a" * index + " "
    index = index + 1    # increment counter
    
print(result)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

