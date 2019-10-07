---
description: 'Lists, Dictionaries, Error Handling and List Slicing'
---

# Week 3

## Login System MKII - New and Improved!

Now that we're armed with the ability to mathematically manipulate user input, and store data in elegant structures, let's revisit and improve the login system from last time.

{% hint style="info" %}
If you didn't manage to finish the final extension exercise last time, or have lost your code, then feel free to use our [solution](../solutions/solutions.md#extension-3-bad-passwords) 
{% endhint %}

### Captcha

Let's have a go at utilizing typecasting, by asking the user to verify a simple Captcha before allowing them to try to login.  
  
Something like: "What is 4 - 2?" will suffice for now.

### A better database

Store three username-password, key-value pairs in a dictionary, and use this dictionary to directly simplify the logic of username and password checking \(i.e. **don't** store username-password information for each user in distinct variables, even for _if-statement_ purposes\).

{% hint style="info" %}
You'll still want to check that the username is correct before checking the password. It'll be helpful to remember that:

1. You can check which keys \(usernames\) are stored in a dictionary using the .keys\(\) member function
2. You can access values corresponding to a key using square brackets: dictionary\[key\]
{% endhint %}

### More bad passwords

Use a list to store some of what you'd consider "bad passwords" and then check that the usernames password doesn't match any of these - make sure this check _**isn't case sensitive**\)_

### Customized Welcome Messages

Use another dictionary to store different welcome messages, corresponding to different users - print these out to users once they've successfully logged in.



## Extension 1 - Incompetent User Warning

Use error handling to ensure that your login system berates the user if they don't enter an actual number when attempting the Captcha \(rather than just crashing and throwing a ValueError\).

## Extension 2 - List Slicing Fun

Using the join and split function, we're going to find a hidden message in the following poem:

_hidden from all to see, trapped in an eternal night, those shadows plain surrounding me, no sunrise in sight_

To do this, carry out the following:

1. Split the poem into a list of words
2. Use list slicing to create a new list containing items 0, 6, 12 ,18 from the list you created \(i.e. step-size 6\)
3. Use **join\(\)** to print this list out - hopefully revealing a secret message

## Extension exercise 3 - Forced Palindromes

Take an input word from the user, and "palindromify" it - ****Utilize the fact that list slicing can also be similarly applied to strings

For example: "frog" -&gt; "frogorf"

## Extension 4 - Random Captcha 

### Random Numbers

random\(\)

### Random String

ASCII character - typecast integer to character with \(chr\) 65-125  [ASCII Table](http://www.asciitable.com/)

