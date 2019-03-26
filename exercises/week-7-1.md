---
description: Numpy array basics
---

# Week 7

## 1 Alex's Awry Array Ailment 

In this exercise you'll need to use list slicing and some previously unintroduced numpy functions to achieve a specific goal

Your aim is to create a function which creates a numpy array of dimension \(NxM\) \[These are the parameters of the function\] consisting of alternating 1s and 0s 

**You are not allowed to do this using lists or for-loops, instead use:**

* **np.ones\(n,m\) -** creates a n x m matrix of 1s
* **np.zeros\(n,m\)** - creates a n x m matrix of 0s

## 2 Loading data with numpy

Use **np.genfromtext\(\)** to load the data we've provided for you. For this exercise you'll want to use the "Deaths"data.

In order to get the desired behaviour, you'll need to specify some arguments in **np.genfromtxt\(\)**, as we did in the example \(What's the delimiter?, Is there a column names row?, Are there multiple types of data in each row?\).

{% hint style="info" %}
See [https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html)
{% endhint %}

1. Once you've imported these two data sets successfully, double check that you can access and print items from the numpy arrays in the same was we did with lists \(i.e. using a for loop and \[\] index notation\)
2. Add a column to the array which contains the fraction of deaths attributed to males



