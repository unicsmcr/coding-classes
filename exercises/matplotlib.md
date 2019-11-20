---
description: Plotting graphs from data
---

# Matplotlib

#### Part 1: Creating a line graph <a id="Part-1:-Loading-data-with-numpy"></a>

You'll want to start by importing **matplotlib.pyplot** as **plt** because no one wants to write so much stuff everytime they use the module.

Use **plt.plot\(\)** to plot the data we've provided for you below.

You would need to store the data to be able to access it. After plotting the graph, add a title to it and labels to each axis to make the graph and table more readable.

**Data for this exercise:**

Months:

             \["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"\]

Temperatures:

             \[4.1, 2.4, 3.8, 8.4, 12.1, 14.8, 17.3, 15.3, 12.4, 9.6, 7.3, 5.8\]

**Extension:**

* Once you've finished the above assignment try to make the graph look better by adding individual marker for each data point on the graph change their colour \(You might have to do some research for this one!\)

#### Part 2: Plotting with Matplotlib <a id="Part-2:-Plotting-with-Matplotlib"></a>

Use **plt.scatter\(\)** to plot the data we've provided for you about the sales of ice cream against the temperature outside. Add labels to each axis and a title to the graph.

**Data for this exercise:**

Sales\(in thousands of pounds\):

              ****\[73, 57, 81, 94, 110, 124, 134, 139, 124, 103, 81, 80\]

Temperatures:

              \[4.1, 2.4, 3.8, 8.4, 12.1, 14.8, 17.3, 15.3, 12.4, 9.6, 7.3, 5.8\]

#### Part 3: Bar Charts <a id="Part-3:-Bar-Charts"></a>

Using the **plt.bar\(\)** function, create a barchart visualizing the choice of pets of UK household in 2018. This exercise should be slightly tougher to complete as **plt.bar\(\)** has a more dissimilar syntax to the previous two functions used.

**Data for this exercise:**

Pet types:

              \["Any", "Dog", "Cat", "Rabbit", "Bird", "Hamster", "Turtle", "Lizard", "Snake"\]

Percentage owned per type:

              \[40, 25, 17, 1, 1, 1, 0.7, 0.6, 0.4\]

### Extension to all tasks <a id="A-fitting-challenge"></a>

Modify all the previous tasks to get their data from their respective text file down below. Read in the data from the file and store it before performing the same plotting functions. \(The graphs should remain the same after changing the approach to reading the data!\)

{% file src="../.gitbook/assets/task1.txt" caption="Task1\_data" %}

{% file src="../.gitbook/assets/task2.txt" caption="Task2\_data" %}

{% file src="../.gitbook/assets/task3.txt" caption="Task3\_data" %}



