---
description: Course Introduction and Thinking Like a Programmer
---

# Week 1

&lt;Pre-Recorded video here&gt;

## 1.1 Introduction

### Why should I care about programming?

#### Completing course work / projects

Many students will find themselves needing to solve problems by programming at some point - be it programming an experimental apparatus using an archaic instruction set, writing a suite of fancy software, or analyzing and predicting trends from some data set.  
  
In all these cases it is important to remember that programming, like most technical skills, is something which gets easier with time and practice - Even if you never use python again, you'll find it much easier to learn a new programming language once you've spent hours getting angry at another one, as they all ultimately rely on the same kinds of thinking.

#### Employability

The ability to code is perhaps the most sought-after technical skill, along side mathematics, in a world where attempts to automate and digitize permeate an increasing number of jobs.

![Compounds growth rates for jobs in 2015-2020 \(source: World Economic Forum\) ](../.gitbook/assets/image%20%284%29.png)

#### Fun!

This is easily the most important reason to learn to code - _coding is fun!_   
  
We live in a digital world, and so having the skills to not just appreciate and understand how software and technology work, but also to manipulate them, or to create your own, unlocks more doors than you imagine.  
  
Maybe you'll create an app which automatically sends messages to your housemates telling them to do the dishes, or you'll code an artificial intelligence which takes over the world - what you do with the skills we aim to provide is up to you.

![A fairly accurate depiction of a hacker having fun \(source: Kilburn out of hours\)](../.gitbook/assets/image.png)



### And _you're_ going to teach me?

_Alright,_ we'll admit that we're not grizzled veterans of pedagogy, and \(hopefully\) lack the tweed coats and wrinkled skin which wisened lecturers don. However, it wasn't that long ago that we were first getting to grips with programming ourselves \(though sometimes it sure feels like it\), and we think we've got a pretty good idea of not just how to code,  but also how to learn to.

## 1.2 Representing Information

### Morse Code

### Binary

### RGB

## 1.3 Abstraction

### Emojis

## 1.4 Algorithms

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





## Note

See Setup page!

