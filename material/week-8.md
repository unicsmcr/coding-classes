# Matplot

### MatplotLib - What and Why?

MatplotLib is a library for creating graphs in python

* Useful for creating data visualisations
* Can make it easy to understand complex data
* Can be combined with other modules like numpy and scipy
* Large number of options available

### Bar Chart

One of the simplest plots we can create with MatplotLib is the bar chart. First we create a list of the names to go below each bar. We then create a list of corresponding values, where each value corresponds to the height of the bar chart. Then we use `plt.bar()`function to create the bar chart. Finally, we tell MatplotLib to show all of the charts that have been created using the `plt.show()` function.

```python
import matplotlib.pyplot as plt

names = ['first', 'second', 'third']
values = [3, 1, 6]

plt.bar(names, values)
plt.show()
```

### Line Graph

Line graphs can be created in a similar way, first a lists of x and corresponding y values are created. Then the plt.plot\(\) function is used to create the graph.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 3, 6]

plt.plot(x, y)
plt.show()
```

### Scatter Graph

Scatter graphs can be created in the same way as lien graphs, except that `plt.scatter()` is used instead of `plt.plot()`.

```python
import matplotlib.pyplot as plt

x = [1, 3, 2, 1.5]
y = [0, 5, 1, 4]

plt.scatter(x, y)
plt.show()
```

### Formatting

The examples we have seen so far generate very basic plots with just the default options and no labeling. MatplotLib provides a number of functions to customise the appearance of appearance of plots.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [1, 3, 6]

plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('This is a graph')
plt.show()
```

