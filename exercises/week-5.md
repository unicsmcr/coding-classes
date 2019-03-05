# Week 5

## 0 Finish last weeks stuff!

There were a lot of exercises last week, try and finish the for/while loop exercises before attempting this weeks material on functions \(don't worry about completing the challenge problems though\).

## 1 Fun with Functions

#### 1.1 Maximal entertainment <a id="Maximal-entertainment"></a>

Create a function which takes in a list and prints out the biggest value in the list \(**don't** use pythons max\(\) function!\)

**Extension**

Instead, **return** the maximum value and print it outside of the function

#### 1.2 Sum thing to do <a id="Sum-thing-to-do"></a>

Create a function which accepts a **list** of numbers and prints the **sum** of all the numbers

**Extension**

Get your function to return the **average** value in the list \(You'll want to use len\(\)\)

**1.3 Developing a range of skills**

Create a function which mimics the function of range\(\), by returning a list of integers from the minimum value to the maximum value - 1 \(i.e. my\_range\(min, max\)\)

**Extension 1**

Use **default arguments** such that if the "min" argument is not given, the function starts counting from zero

**Extension 2** 

Try and implement the range function using recursion \(you can use another function to do the actual list creation, if you like, so long as it uses recursion!\)

## 2 Import-ant Syntax

Import the following two packages, renaming them, such that you can get the following code snippet to run:

* Import "numpy", renamed to "np"
* Import the "pyplot" module from the "matplotlib" package, renamed to "plt"

Then run:

```python
# Scary block of awful code
plt.scatter([0.35 * (2/7) + 0.15, 0.5 - 0.35 * (2/7) ], [2, 2], c='b', marker='s', s=300 )
plt.scatter(0.325, 0.75, c='k', marker='^', s=150);l = np.arange(0.15, 0.51, 0.01)
plt.plot(l ,np.sin(np.linspace(np.pi, 2*np.pi, len(l))), c="r")
plt.axis('off');plt.margins(0.25);plt.title("?sracs eseht tog I woh wonk annaW"[::-1])
plt.show()
```

You'll know when it's working ;\)

