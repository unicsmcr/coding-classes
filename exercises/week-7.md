---
description: Plotting a dataset
---

# Week 9

### Hatching a Plot <a id="Hatching-a-Plot"></a>

{% file src="../.gitbook/assets/alcohol\_prices.csv" caption="Alcohol Price Data" %}

{% file src="../.gitbook/assets/deaths.csv" caption="Deaths Data" %}

{% file src="../.gitbook/assets/drugs\_prescribed \(1\).csv" caption="Drug Prescription Data" %}

{% file src="../.gitbook/assets/household\_expenditure \(1\).csv" caption="Household Expenditure" %}

#### Part 1: Loading data with numpy <a id="Part-1:-Loading-data-with-numpy"></a>

Use **np.genfromtext\(\)** to load the data we've provided for you. For this exercise you'll want to use the "Deaths" and "Household\_expenditure" data.

In order to get the desired behaviour, you'll need to specify some arguments in **np.genfromtxt\(\)**, as we did in the example \(What's the delimiter?, Is there a column names row?, Are there multiple types of data in each row?\).

* Once you've imported these two data sets succesfully, double check that you can access and print items from the numpy arrays in the same was we did with lists \(i.e. using a for loop and \[\] index notation\)

#### Part 2: Plotting with Matplotlib <a id="Part-2:-Plotting-with-Matplotlib"></a>

You'll want to start by importing matplotlib.pyplot as plt, because no one wants to write so much stuff everytime they use the module. Then

* Using for loops, create lists containing the years, total spending and percentage spending from the Household expenditure array
* Plot the total spending and percentage spending against years, in two seperate plots
* Make your plots look nice by setting labels and titles using plt.title\("my title"\), plt.xlabel\("x axis label"\)

**Extension:**

* Plot both the percentange and total spending on the same plot, first normalizing \(i.e. rescaling\) the data, so only the trend information is seen.
* Using the label="my label" argument in the plotting step, create a legend \(you'll need to call plt.legend\(\) before plt.show\(\)\)

#### Part 3: Bar Charts <a id="Part-3:-Bar-Charts"></a>

Using the **plt.barh\(bin\_labels, bin\_frequencies\)** function, create a barchart visualizing the relative frequencies of alchol-related deaths in 2015 \(i.e. the data imported from the Deaths.csv\)

* You'll need to use the first column of the data as the axis labels

### A fitting challenge <a id="A-fitting-challenge"></a>

Choosing an interesting dataset \(e.g. Alcohol-related expenditure\), try to fit a polynomial function to the data using **np.polyfit** \(see: [https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html\)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html%29), and based on the best fitting polynomial, extrapolate the trend for the next five years - plot this prediction and see whether it makes sense!

