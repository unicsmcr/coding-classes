---
description: Solutions to File I/O and Consolidatio
---

# Week 7

## Exercise 1 - Basic File I/O

Here we create a file, and add some random lines to it. Then we read and print out the file contents.

{% code-tabs %}
{% code-tabs-item title="week6\_solutions\_ex1.py" %}
```python
# create a file
my_file = open("musings.txt", "w+")

# write some things to the file
my_file.write("These are some of my thoughts\n")
my_file.write("The solutions are so great\n")
my_file.write("Thanks for these interesting exercises alex\n")

# close the file, so that we can then read from it
my_file.close()

# open the file for reading
my_file = open("musings.txt", "r")

# now read each line in the file, and print it out
for line in my_file:
    print(line)
    
# close access to the file again
my_file.close()
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 2 - Wherefore art thou paragraph

Here we define a function to read N paragraphs from a file, and print them.

{% code-tabs %}
{% code-tabs-item title="week6\_solutions\_ex2.py" %}
```python
def read_shakespeare(num_of_paragraphs):
    # open the file, read all the lines and store them
    shakespeare_file = open("shakespeare.txt", "r")
    lines = shakespeare_file.readlines()

    current_paragraph = 1
    line_num = 0

    # keep printing, until we are at the paragraph we want to stop at
    while current_paragraph <= num_of_paragraphs:
        current_line = lines[line_num]

        # remove whitespace from line, as paragraph lines have spaces before
        # the number, check if its the next paragraph
        if current_line.strip() == str(current_paragraph + 1):
            # we have reached the next paragraph
            current_paragraph = current_paragraph + 1
            if current_paragraph > num_of_paragraphs:
                break   # don't print the line if we exceed paragraph 

        # print the line, rstrip removes newline character at the end of the line
        print(lines[line_num].rstrip())
        line_num = line_num + 1

read_shakespeare(3)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Exercise 3 - Caesar's Cipher Consolidates Cool Class

{% code-tabs %}
{% code-tabs-item title="week6\_solutions\_ex3.py" %}
```python
def decipher(file_name, decode_word, frequency):
    cipher_file = open(file_name, "r")
    cipher = cipher_file.readline()
    cipher_offset = 0

    decode_diff = []
    for index in range(len(decode_word) - 1):
        ascii_diff = ord(decode_word[index+1]) - ord(decode_word[index])
        if(ascii_diff < 0):
            ascii_diff = ascii_diff % 26
        decode_diff.append(ascii_diff)

    words = cipher.split(" ")
    word_count = {}

    # print(decode_diff)

    for word in words:
        if len(word) == len(decode_word) and word in word_count:
            word_count[word] = word_count[word] + 1
        elif len(word) == len(decode_word):
            word_count[word] = 1

    # print(word_count)

    for key in word_count:
        if word_count[key] == frequency:
            # now check letter positions
            correct_positions = True
            for index in range(len(key)-1):
                # check ascii position changes between key and decode_word
                ascii_diff = ord(key[index+1]) - ord(key[index])
                if(ascii_diff < 0):
                    ascii_diff = ascii_diff % 26
                correct_positions = correct_positions & (ascii_diff == decode_diff[index])

            # we have found the word
            if correct_positions:
                print("here")
                cipher_offset = ord(decode_word[0]) - ord(key[0])
                if cipher_offset < 0:
                    cipher_offset = cipher_offset % 26
                break

    decryted_words = []
    for word in words:
        new_word = ""
        for char in word:
            new_char = chr(97 + ((ord(char) - 97 + cipher_offset) % 26))
            new_word = new_word + new_char

        decryted_words.append(new_word)

    plaintext = " ".join(decryted_words)
    print(plaintext)

decipher("mary.txt", 'the', 4)
decipher("charles.txt", 'of', 12)
decipher("agatha.txt", 'train', 2)
```
{% endcode-tabs-item %}
{% endcode-tabs %}

