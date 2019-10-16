---
description: 'While, For and Challenges!'
---

# Week 5

## 1 While Loops - Finishing our Login System!

### 1.1 Have mercy on the user

Using a while loop allow the user to keep entering their password until they get it right \(do this without breaking all the functionality you implemented in the past - feel free to use our solutions\).

### 1.2 That was too much mercy

Limit the number of attempts the user gets by using a counter, as we discussed in the slides.

### 1.3 More secure than Hillary's inbox

We don't want Russian hackers breaking through! Use the Captcha code from last time, and force the user to enter a Captcha after every failed password attempt.

## 2 For loops

### 2.1 Hip to be Square

Take a number N from the user, and print an NxN square using characters 'X'

#### 2.1 Extension

Print a "hollow" square \(i.e. only the edges are "X"\)

### **2.2 Hidden message with for loop**

Use **.split\(" "\) \[**see [extensions](../material/week-3/extensions.md#Split)\] and print out all words in the following phrase which start with a capital letter:

_it was The best of times, it was the worst of times, it was the age of wisdom, it was the age of Foolishness, it was the epoch Of Belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it Was The spring of Hope, it was the winter Of despair, we had everything before us, we had nothing before us, we were all Going direct To Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only._

### 2.3 Pythagorean triples - Three times the fun!

Pythagorean triples are sets of three integers which satisfy Pythagoras' theorem:

* a\*\*2 + b\*\*2 = c\*\*2

For example, the first Pythagorean triple is \(3, 4, 5\).

Find all Pythagorean triples where c &lt; 100 and print these out \(ignoring duplicates in a and b\), formatted as:  \[3, 4, 5\] , \[a2, b2, c2\] , \[a3, b3, c3\] ...

## Extension 1 - Goat Latin 

Implement goat Latin \(a made up version of english \[this is a facebook interview question!\]\), such that a user can input a normal english sentence, and your program returns the goatified version:

* E.g.: "word1 word2 word3 word4 word5..." -&gt; "aword1 aaword2 aaaword3 aword4 aaword5..."

Instead of adding unlimited extra 'a's with increasing word index, add one, then two, then three, and then one again, etc.

### **Extension 1 Extra**

1. If a word begins with a vowel, append "ma" to the end of the word.
   * "apple" becomes "applema"
2. If a word begins with a consonant \(i.e. not a vowel\), remove the first letter and append it to the end, then add "ma".
   * "goat" becomes "oatgma"
3. Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
   * Example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

**Note:** You may find the following list useful:  vowels = \['a', 'e', 'i', 'o', 'u'\]

## Challenges

These challenges are tricky and require lots of clever steps! Don't feel disparaged if you don't manage to finish them - they are fairly mathematical, and it takes a lot of practice to develop the patterns of thought which computer scientists use to tackle such glorified logic puzzles.

However, we **strongly** recommend that you ask friends, or even us \(contact us via the Facebook HackSoc group\) before you look at the worked solutions - sometimes people are closer to the solution than they realise and all they need is a few helpful hints \(google "rubber duck debugging" ;\) \)

### Challenge 1 \(Modulu\) - Fizz Buzz <a id="Challenge-1-(Modulu)---Fizz-Buzz"></a>

This is a classic problem which you'll probably encounter many times if you learn other programming languages in future.

#### Problem Statement <a id="Problem-Statement"></a>

Given an integer N \(provided by the user\), print out all the integers from 0 to N. However, you must replace numbers as follows:

* If a number is a multiple of 3, then print **Fizz** instead of the number
* If a number is a multiple of 5, then print **Buzz** instead of the number
* If a number is a multiple of 3 **and** 5, then print **Fizz Buzz**

#### Extension <a id="Extension"></a>

* Instead of using the built-in % operator from python, implement it yourself using another while loop - Can't trust the python developers!
* Make sure that your program can handle **edge cases** - This is extremely important for real programmes

### Challenge 2 \(While + List Slicing\) - Pascal's Triangle <a id="Challenge-2-(While-+-List-Slicing)---Pascal&apos;s-Triangle"></a>

Here you will create a piece of code which generates Pascal's triangle

#### Base Problem Statement <a id="Base-Problem-Statement"></a>

Given an integer N \(provided by the user\), using a while loop print out Pascal's Triangle in the format: 1, 121, 1331, 14641,... row\_N  
\[Try doing this without creating more than one list per loop step for more difficulty\]

#### Extra Challenge <a id="Extra-Challenge"></a>

* Use _Nested Lists_! Store each row as a list inside of a larger list, e.g.: \[\[1\], \[121\], \[1331\],... \[row\_N\]\]
* After you've created your pascal's triangle list, print it out so it looks like an actual triangle:

  ```text
    1  
  1 2 1 ...
  ```

\(Note: strings can be multiplied, e.g. "Hiiiiiiii" = "H" + "i" \* 8\)

