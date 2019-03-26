---
description: Course Introduction and Thinking Like a Programmer
---

# Week 1

## 1.1 Introduction

### Why should I care about programming?

#### Completing course work / projects

Many students will find themselves needing to solve problems by programming at some point - be it programming an experimental apparatus using an archaic instruction set, writing a suite of fancy software, or analyzing and predicting trends from some data set.  
  
In all these cases it is important to remember that programming, like most technical skills, is something which gets easier with time and practice - Even if you never use python again, you'll find it much easier to learn a new programming language once you've spent hours getting angry at another one, as they all ultimately rely on the same kinds of thinking.

#### Employability

The ability to code is perhaps the most sought-after technical skill, along side mathematics, in a world where attempts to automate and digitize permeate an increasing number of jobs.

![Compounds growth rates for jobs in 2015-2020 \(source: World Economic Forum\) ](../.gitbook/assets/image%20%287%29.png)

#### Fun!

This is easily the most important reason to learn to code - _coding is fun!_   
  
We live in a digital world, and so having the skills to not just appreciate and understand how software and technology work, but also to manipulate them, or to create your own, unlocks more doors than you imagine.  
  
Maybe you'll create an app which automatically sends messages to your housemates telling them to do the dishes, or you'll code an artificial intelligence which takes over the world - what you do with the skills we aim to provide is up to you.

![A totally accurate depiction of a hacker having fun \(source: Kilburn after hours\)](../.gitbook/assets/image.png)



### And _you're_ going to teach me?

_Alright,_ we'll admit that we're not grizzled veterans of pedagogy, and \(hopefully\) lack the tweed coats and wrinkled skin which wisened lecturers don. However, it wasn't that long ago that we were first getting to grips with programming ourselves \(though sometimes it sure feels like it\), and we think we've got a pretty good idea of not just how to code,  but also how to learn to.

## 1.2 Representing Information

### Binary

Computers store information as binary values, consisting only of **1**s and **0**s. The reasons for this ultimately come down to the fact that is more practical to build electronics which represent only two distinct states, and are thus able to encode binary values.

Binary numbers define a "**base 2**" counting system, where as the one we are used to is "**base 10**" \(known as **Decimal**\) - For example, in base 10, the number 126 is represented by:

$$
126=(1\times100)+(2\times10)+(6\times1)
$$

 Where each column represents the powers of 10; i.e.

$$
126=(1\times10^2)+(2\times10^1)+(6\times10^0)
$$

In binary, numbers are represented similarly, except that the base is now 2 rather than 10. So the number 13 would be written as

$$
13 = (1\times2^3)+(1\times2^2)+(0\times2^1)+(1\times2^0)
$$

Which means that the binary representation of 13 in binary is simply 1101, where each column represents the coefficient for the powers of 2, similar to the way things work in base 10.

This may seem abstract or unnecessary, but the point of showing you binary is simply to prove to you that it is possible to represent any number using only 1s and 0s. Combined with the fact that **we can represent anything in terms of numbers**, this means computers can stores all kinds of information using only 1s and 0s at the electronic level.

Luckily for us, most programmers rarely work at such a low "**machine-level**", so don't worry about the details!

### ASCII

A key example of how we can represent every-day information in terms of numbers is provided by the ASCII character encoding standard. The ASCII standard defines a **mapping** from numbers to characters, including not just the alphabet, but also many common symbols like &, \# !, etc.

The ASCII standard allows us to convert English words to numbers, which can in turn be stored and manipulated by computers, using their binary representation. For example, the word "Hello":

| Alphabetical | ASCII | Binary |
| :--- | :--- | :--- |
| Hello | 72 101 108 108 111 | 1001000 1100101 1101100 1101100 1101111 |

### RGB

There are many kinds of information we might want to represent on our computers besides **strings of characters** \(i.e. words and sentences\). One obvious example is images, which ultimately consist of many thousands of individual "pixels" which have a specific color.

One simple way to encode colors is to decompose them into three primary colors, typically: **Red, Green and Blue**, and to figure out how much of each color you'd have to "mix" together to get the desired color \(known as additive mixing\). 

The RBG standard encodes this information using three numbers between 0-255 which represent the "amount" of each color present in the decomposition. For example:

![An example of an RGB decomposition for a specific shade of pink ](../.gitbook/assets/image%20%2812%29.png)

Some of you may be old enough to remember back in the good old days before HDMI, when SCART cables were still commonly used - these actually had red, green and blue signal channels. Furthermore, pixels on most modern displays actually consist of distinct Red, Green and Blue pixels, each of which changes brightness to give the appearance of millions of different colors.

![Left: SCART cable - these had actual RGB channels \| Right: TV up close - pixels consist of RGB](../.gitbook/assets/image%20%284%29.png)



## 1.3 Abstraction

**Abstraction** is a concept in computer science where some low-level implementation \(such as how data is ultimately stored in binary\) is simplified or taken for granted, so we can use that implementation at a higher level \(such as representing letters, that we can then use in our programs\).

### Emojis

Emojis provide a great example of abstraction - let's take a favorite of mine, the "[pile of poo](https://www.iemoji.com/view/emoji/55/smileys-people/pile-of-poo)" emoji:💩.

Similar to the way in which common characters are encoded in the ASCII scheme, a more complex standard known as Unicode is used to represent other objects typically sent in messages - including emojis. For example, in the UTF-8 standard, the 💩 is given by "U+14F4A9". 

Computers compatible with this encoding standard will know that it corresponds to a given set of RGB values, describing a 256x256 pixel image:

![You say &quot;pile of poo&quot;, I say 256x256 RGB values](../.gitbook/assets/image%20%281%29.png)

This is an excellent example of abstraction, because rather than sending your friends a set of 65536 RGB vectors, you just send them ":poop-emoji:" and rely on the fact that someone else has taught your computer to convert that to an image of a smiling piece of feces.  


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p>
          <br />
        </p>
        <p></p>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>## 1.4 Algorithms

![Algorithms take the inputs specified by a problem and output the solution](../.gitbook/assets/image%20%2817%29.png)

Without going into any detail here, it is important to note that the essence of what many programmers do is **problem solving** - more specifically, designing **algorithms** which take the inputs defining a problem \(in a specified representation\) and output the solution \(in a specified representation\).

For example, I might develop an algorithm which tells me what day it will be tomorrow, based on what day it currently is. This would work something like:

```text
If today is Monday => Tomorrow is Tuesday
If today is Tuesday => Tomorrow is Wednesday
...
If today is Sunday => Tomorrow is Monday
```

Where we have chosen a representation in which the days of the week are given by their names in English. Instead, we might be producing an algorithm for a group of efficient Germans, who tell us the day in German, and want the output as a number between 1 and 7 \(to save valuable syllables from being spoken\):

```text
If today is Montag => Tomorrow is 2
If today is Dienstag => Tomorrow is 3
...
If today is Sonntag => Tomorrow is 1
```

**Note**: This highlights an important detail about creating algorithms - Although in both these cases the algorithm works in essentially the same way, the data we feed to it and the data we want it to give us are different, and so the algorithms are distinct. In essence:

$$
Algorithm = Some \ Function + Form \ of \ Data
$$

## 1.5 Pseudocode

### Making a jam sandwich

Suppose you're trying to tell a robot how to go about making a jam sandwich, you might start by giving it instructions along the lines of:

```text
Get the jam
Put two pieces of bread on a plate
Put jam on the bread
Put the pieces of bread on top of eachother
```

And that would probably be more than sufficient, if not slightly patronizing, if you were talking to a competent human. However, what we'll be learning is how to tell computers what to do, and computers are _truly_ _incompetent_ - no common sense whatsoever!

So let's try again, and be really explicit this time:

```text
Get jam jar from cupboard
Place jam jar on kitchen counter and unscrew lid
Take a knife from the draw
...
```

This is better, but still not even close to specific enough - computers need to be told _exactly_ what they need to do at \(preferably\) the highest-level which they can understand \(which is very low, by human standards\). So let's suppose our robot has some sensors which can measure distance, and that it knows about angles and movement.  
  
Then we can start by opening the cupboard which contains the jam:

```text
Using left hand, peform <grip> on handle at x,y,z = (17cm, 21cm, 80cm)
Move left hand in a 60 degree arc in the x-y plane about x,y = (8cm, 21cm)
Using left hand, perform <release>
```

Ok, we did it, we managed to tell the robot how to open the cupboard - Yes... I can hear you saying "Maybe I'll just get a subway instead", but don't worry, we can use **abstraction** to make our lives easier.

Notice that in the example above the robot understands an instruction called &lt;grip&gt;, presumably because the manufacturer thought it would come in handy. We can also create our own complicated instructions by abstracting away whole sets of consecutive moves into so-called **functions,** which we've been denoting using &lt;&gt;.

For example, suppose we went through the horrible effort of teaching the robot how to google an object's name, recognize it and then move it to another object,  referring to this instruction as **&lt;pick up x and place at y&gt;,** then we could avoid bothering about coordinates and angles entirely, except for the one time where we define the function:

```text
function <pick up x and place at y>
    objectImage = <google image search x>
    objectCoordinate = <find closest matching obect to objectImage>
    Using left hand, perform <grip> on objectCoordinate
    ...
```

If we repeated this process of building layer upon layer of abstraction, then we might eventually end up with a single function called **&lt;make jam sandwich&gt;,** which we could now tell the robot to carry out as many times as we liked \(though it's not clear what happens when we run out of jam or bread!\)

In much the same way, most programmers rarely have to dig down to the "nitty gritty" to solve real world problems, as they can instead rely on all the **functions** which other people have implemented in **libraries** or **packages,** when solving related problems before -  we'll come back to this later.

