---
description: File I/O and Numpy Array
---

# Week 7

## File I/O

File I/O \(Input/Output\) refers to our ability to create / manipulate files via our Python scripts. Though many packages have specific functions for this purpose, Python itself has a convenient set of functions which we can use to manipulate files.

### Open and Close <a id="Open-and-Close"></a>

Before we can manipulate files, we need to open or create them. To open a file we use the **open\(\)** function and store a "link" to the file in a variable:

* If we want to write to the file: **open\("file\_name", "w"\)**
* If we want to read from the file: **open\("file\_name", "r"\)**
* If we want to append to a file: **open\("file\_name", "a"\)**
* There are more options - see the documentation at [https://docs.python.org/3/library/functions.html\#open](https://docs.python.org/3/library/functions.html#open)

```python
# Create a file for writing, called "my_file.txt"
new_file = open("my_file.txt", "w")
```

{% hint style="info" %}
If a file doesn't exist when we try to open it, then Python will create it
{% endhint %}

Once we're done with using a file, we call **.close\(\)** on the file link to close it

```python
# Close the file
new_file.close()
```

Alternatively, we can use a **with statement** to open a file, do some immediate manipulation, and then have python automatically close it \(i.e. the file link can only be used within the indented statement\):

```python
with open("my_file.txt", "r") as f:
    # Do something to the file here
    print("hi")
```

### Write <a id="Write"></a>

The simplest way to add to our file is by using the **.write\(\)** function _on_ the variable containing the file link:

```python
new_file = open("my_second_file.txt", "w")

# We can write as many times as we want
new_file.write("Stories outlive their authors")
new_file.write("\n") # Start a new line
new_file.write("So too will these python class materials")

new_file.close()
```

The above example will create the following text file in our **working directory** \(typically the same folder as your python script\)**:**

{% code title="my\_second\_file.txt" %}
```text
Stories outlive their authors
So too will these python class materials
```
{% endcode %}

### Read <a id="Read"></a>

Sometimes we'd rather read the profound works of others than create our own. To this end, we can use

* **.read\(n\)** to read the first **n** characters
* **.readline\(\)** to read the first line
* **.readlines\(\)** to read the entire file - stores it as a list, with each line \(string\) as an element

{% hint style="info" %}
These **read** functions step through the parts of the file that have already been read - so calling .readline\(\) twice in succession will read the first two lines of a file
{% endhint %}

Let's put this to use on some of Gandalf's wise advice:

{% code title="wisdom.txt" %}
```
'I wish it need not have happened in my time,' said Frodo.
'So do I', said Gandalf, 'and so do all who live to see such times.'
'But that is not for them to decide.'
'All we have to decide is what to do with the time that is given us.’
```
{% endcode %}

Supposing the "wisdom.txt" file is in our working directory, we can try reading it:

```python
wisdom = open("wisdom.txt", "r") # Open file

first_six = wisdom.read(6) # Get first six characters
first_line = wisdom.readline() # Get REMAINDER of line
whole_file = wisdom.readlines() # Get REMAINDER of file

wisdom.close()
```

If you'd like to play around with the read/write functionality, here's the file used in the above example:

{% file src="../.gitbook/assets/wisdom.txt" caption="Gandalf\'s wise words to Frodo" %}

### Reading with For loops

Most often, we'll just use a for loop to read our file, **line by line**. Essentially, the for loop is performing:

```python
for line in file_link.readlines():
    ...
```

but we don't need to specify the conversion of the file to a list of lines, as this is the default behavior:

```python
wisdom = open("wisdom.txt", "r") # Open file

for line in wisdom:
    # Essentially loops through list wisdom.readlines()
    print(line)
    
wisdom.close()
```

