---
description: File I/O and Consolidation
---

# Week 6

## Note

As this is the last week of "Python Basics", there is a large consolidation exercise \(number 3\) which we highly recommend you try and do prior to next week's session - Solutions will be released by Thursday evening!

## 1 Basic File I/O

#### Create <a id="Create"></a>

#### Create a file called musings.txt and write some some of your thoughts into it <a id="Create"></a>

#### Read <a id="Read"></a>



## 2 Wherefore art thou paragraph

{% file src="../.gitbook/assets/shakespeare.txt" caption="Shakespeare Text File" %}

Read the shakespeare.txt file: 

* Create a function which returns the first **N** paragraphs from the file
* Make use of the fact that the line preceding each paragraph contains the corresponding paragraph number

There are two approaches to this problem:

1. Use .readlines\(\) and treat this as a list manipulation problem
2. Use loops and .readline\(\) to "walk through" the file, and format it as you go

**The second approach is more instructive!**

{% hint style="info" %}
1. Use a while loop to carry out .readline\(\) until you reach the end of a paragraph  
2. Create a function which returns one paragraph, and put it inside another function which calls it N times
{% endhint %}

## 3 Caesar's Cipher Consolidates Cool Class

Hold on to your hats, because this is a big one! To complete this exercise you'll need to use almost everything we've learned so far, so make sure you're sitting comfortably \(preferably with a caffeinated beverage at hand\) and let's go!

{% hint style="warning" %}
This is quite a tricky exercise, but I strongly suggest you give it a go, as we'll be moving onto specialized topics next week, and an understanding of the python "basics" will be key.
{% endhint %}

The goal of this exercise to to create a function which will decipher files, given a decode word, and it's frequency. To succeed you should find the source of each of the encrypted messages \(the file names offer a slight clue\)

More specifically, you will be provided with a word in normal English, and the number of times it is used in the paragraph, and must use this to find out the shift of the alphabet that has been applied.

{% hint style="info" %}
You'll want to count the frequency of each encrypted word, and find the one that matches the decode word - dictionaries might be a helpful way of doing this ;\)
{% endhint %}

The type of cipher being used is the simple Caesar Cipher, which works by shifting the alphabet:

{% embed url="https://cryptii.com/pipes/caesar-cipher" %}

The files containing the encrypted messages, and there corresponding decode word, are given below:

For Mary, the decode word is "the" and the frequency is 4

{% file src="../.gitbook/assets/mary.txt" caption="Mary.txt -  Decode \"the\" x 4" %}

For Charles, the decode word is "of" and the frequency is 12

{% file src="../.gitbook/assets/charles.txt" caption="Charles.txt - Decode \"of\" x 12" %}

For Agatha, the decode word is "train", and the frequency is 2

{% file src="../.gitbook/assets/agatha.txt" caption="Agatha.txt - Decode \"train\" x 2" %}

### Challenge

For Jane, you are given that "is" and "in" occur the same number of times within the text

{% file src="../.gitbook/assets/jane.txt" caption="Jane.txt - Decode \#\"is\" = \#\"in\"" %}

{% hint style="danger" %}
Be careful with punctuation in both of the following approaches!
{% endhint %}

### **Decode Approach 1 - Alphabet List** 

Use the alphabet list provided below, and the **.index\(\)** function, to find the shift being applied in the cipher:

{% hint style="info" %}
You'll find the **.index\(element\)** function useful - when called on a list, it returns the first index at which a matching element was found

Here's a list of the alphabet as well: 

alphabet = \['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\]
{% endhint %}

### **Decode Approach 2 - ASCII Conversion**

Using the typecasts which convert characters \(strings of length 1\) to ASCII numbers, and vice versa, find the shift being applied by the cipher.

{% hint style="info" %}
Typecasts:

* **Character -&gt; \(ASCII\) Integer:**  ord\(\)
* **\(ASCII\) Integer:** chr\(\)
{% endhint %}

\*\*\*\*

