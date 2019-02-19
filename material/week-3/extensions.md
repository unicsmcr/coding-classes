---
description: 'List Slicing, Robust typecasting via Error Handling'
---

# Extensions

## Useful Tip: Tab completion in Spyder

When typing out the names of variables which you've declared above, you can **press the tab key** to autocomplete \(or show a list of possible completions, from which you can then pick\)

In practice, such tricks make writing large pieces of code much faster \(tab completion also works with most syntax like print\(\)\) - especially if you're using informative, but long, variable names.

## More List Stuff

#### List Slicing <a id="List-Slicing"></a>

Sometimes we want to access sub-sections of our list, without needing to manually get every item contained in that section. To this end we can use colons when accessing arrays.

* This works like **my\_list\[begin:end:step\_size\]**

{% hint style="info" %}
**NOTE:** you don't need to specify all three of these values - python will use default values:

* begin = start of list
* end = end of list
* step\_size = 1
{% endhint %}

\*\*\*\*

```text
sentence = ["What", "A", "Great", ",", "Guy","Never","Said", "Anything","Bad"]

# Emulate the media
out_of_context = sentence[4:8:1] # Get part of the list
print(out_of_context)
```

#### Min and Max <a id="Min-and-Max"></a>

**min\(\)** and **max\(\)** do what you'd expect - So long as you have numbers in the list; string comparison is a bit less straightforward

```text
my_numbers = [5,-2,71,-438,9]

print(max(my_numbers)) # 71
print(min(my_numbers)) # -438
```

#### Sort <a id="Sort"></a>

Under the hood, min\(\) and max\(\) work by sorting the list first. We can do this manually by using **.sort\(\)**In \[24\]:  


```text
# Example of sorting
# NOTE: don't mix strings and numbers if you want to sort!
my_list = [4, 7, -20, 32, 9.3] 
my_list.sort() # This sorts the list

print(my_list) # [-20, 4, 7, 9.3, 32]
```

#### Split <a id="Split"></a>

**split\(\)** is a function which allows us to break up strings into sub-strings stored in a list

```text
# Example of split()
my_sentence = "I am too lazy to make sentences into lists"
my_list = my_sentence.split(" ") # Split up string by empty spaces
v
print(my_list)
```

#### Join <a id="Join"></a>

**join\(\)** is essentially the opposite of split, and allows us to nicely format our lists when we want to print them

```text
# Example of join()
# NOTE: all items in the list must be strings - unless you do something clever! ;)
my_list = ["I'm", "12", "now", "mum", "I", "can", "do", "what", "I", "want"]
my_sentence = " ".join(my_list) # Join items in list with an empty space

print(my_sentence)
```

## Basic Error Handling

If we try to something which python can't, then we'll get an error. The jargon for this is that : "python throws an error", and we can "catch" these to stop our programs from crashing.

The syntax for is referred to as a "try, except":

```text
try:
    # do stuff here which might throw an error
    weird_function_does_bad_stuff()
except: # this code runs if an error was thrown above
    print("Oops - I encountered an error!")
```

