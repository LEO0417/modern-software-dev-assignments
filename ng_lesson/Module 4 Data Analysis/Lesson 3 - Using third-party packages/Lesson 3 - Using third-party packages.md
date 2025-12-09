# Lesson 3: Using third-party packages

In this lesson, you'll try out some third-party Python packages that let you explore and visualize data!

## Loading and exploring data with ```pandas```

One of the most popular Python third-party packages is called ```pandas```. 

It helps you with loading and exploring structured data, like the kind stored in spreadsheets and ```.csv``` files. Check out the [Pandas documentation](https://pandas.pydata.org/) if you want to learn more!

To use the ```pandas``` package, you first need to load it:

```python
import pandas as pd
```

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: 
<br><br>
What does "as" in the following code do?<br><br>
import pandas as pd
</p>

So `import pandas as pd` creates a shortcut that you can use to avoid typing pandas. 

**Note:** you'll need to use the `.` notation when using the function in pandas - go back to the "Using functions from a local file" lesson in this course if you need a refresher!

Next, you'll load a CSV file of used car sales prices using pandas:

```python
# Dataset adapted from here https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
data = pd.read_csv('car_data.csv')

print(data)
```

How do you show only cars that sold for more than $10,000? Let's ask the chatbot!

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: 
<br><br>
I have loaded some data using this code:
<br><br>data = pd.read_csv('car_data.csv')
<br>print(data)<br><br>
The data looks like this when I print it: <br>
Model    Price  Year  Kilometer <br>
0    Honda Amaze 1.2 VX i-VTEC  5050.00  2017      87150 <br>
1              Honda Brio V MT  3510.00  2014      39276 <br>
2      Honda WR-V VX MT Petrol  8199.99  2018      27963 <br>
3            Honda CR-V 2.4 AT  8600.00  2013      67000 <br>
4              Honda Brio S MT  4400.00  2016      50374 <br><br>
Show only the cars with a price greater than or equal to 10000. <br>
</p>

Next, run the code the LLM wrote to filter the data by price:

```python
# Code to show only the cars with a price >= 10000
print(data[data["Price"]>=10000])
```

You can also filter by other columns in the data, for example the year:

```python
# Show all the cars from the 2015 
print(data[data["Year"]==2015])
```

Pandas includes built-in tools to calculate interesting statistics, like the median selling value for the cars from 2015. Here's the code:

```python
filtered_data = data[data["Year"]==2015]
print(filtered_data["Price"].median())
```

## Plotting data with ```matplotlib```

This is a popular package used by data scientists and developers to visualize data. You can check out the [Matplotlib documentation](https://matplotlib.org/) if you want to learn more!

To use matplotlib, you first have to import it with the following command:

```python
# Note the .pyplot
import matplotlib.pyplot as plt
```

Don't worry about remembering this command, you can always find it by asking a chatbot or searching online. Again, the `as` form of the import command is being used to set up an alias - so now you can type `plt` instead of `matplotlib.pyplot` saving you lots of typing!

Let's start by using ```matplotlib.pyplot``` to plot the selling price of a car against how many miles it has driven:

```python
plt.scatter(data["Kilometer"], data["Price"])

plt.title('Car Price vs. Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

plt.show()
```

Matplotlib has many settings that can help you customize your charts. You can ask a chatbot to help you write the code to modify these settings:

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
<br><br>
I have the following plot in matplotlib:
<br><br>
plt.scatter(data["Kilometer"], data["Price"])
<br>plt.title('Car Price vs. Kilometers Driven')<br>
plt.xlabel('Kilometers Driven')<br>
plt.ylabel('Price (in USD)')<br>
plt.show()<br><br>
Please add a grid, change the scatter plot color to red, and increase the title font size.
</p>



Let's try the code the chatbot suggested:

```python
plt.scatter(data["Kilometer"], data["Price"], color='red')
plt.title('Car Price vs. Kilometers Driven', fontsize=16)
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

# Add the grid
plt.grid(True)

# Display the plot
plt.show()
```

## Extra practice

Use the 🤖 chatbot to help you try the following exercises!

### Exercise 1

Write code to create a filtered table of all the Honda Accords in the dataset.

**Hint:** You can always copy and paste the code from the earlier parts of this notebook and ask the chatbot to modify it!

```python
# WRITE YOUR CODE HERE

```

### Exercise 2

Write code to display a scatter plot of sales price vs year.

```python
# WRITE YOUR CODE HERE

```

### Challenge exercise!

Ask the LLM to help you create a pie chart of the data showing how many cars were sold each year.

**Hint:** Be sure you tell the chatbot what your data variable is called! It may pick a different name by default.

```python
# WRITE YOUR CODE HERE

```
