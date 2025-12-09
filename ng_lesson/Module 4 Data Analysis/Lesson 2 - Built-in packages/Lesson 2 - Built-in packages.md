# Lesson 2: Built-in packages

In this lesson, you'll learn how to work with **packages** (sometimes called **modules**) that are built-in to Python.

These packages contain functions that can be made available in your programs using the same `import` statements you learned in the last lesson.

## The `math` package

Imagine that you want to show your neighbor's kid how to double-check his trigonometry homework using Python.

Python contains functions in the ```math``` package that can let you do trigonometry. Let's load the ```cos, sin``` and ```pi``` functions and use them.

You make these functions available with the following code:

```python
# Import from the math package the cos, sin and pi functions
from math import cos, sin, pi
```

The `pi` you just loaded isn't actually a function, it's a single number:

```python
print(pi)
```

You can check the data type using the `type` function:

```python
type(pi)
```

Next, define a list of values for which you want to compute ```cos``` and ```sin```:

```python
values = [0, pi/2, pi, 3/2*pi, 2*pi]
```

Iterate through the list of values using a ```for``` loop and calculate the ```cos``` function for each value:

```python
for value in values:
    print(f"The cosine of {value:.2f} is {cos(value):.2f}")
```

### Try for yourself!

Pause the video and update the code below to calculate the sine instead of cosine!

```python
for value in values:
    print(f"The sine of {value:.2f} is {cos(value):.2f}")
```

The `math` package contains a function called `floor` that rounds values down to the nearest whole number. 

Try the code below to use it 
* 🚨 Alert! This will return an error!

```python
floor(5.7)
```

This code gave an error because you hadn't yet imported the function so that it could be used. Let's do that now:

```python
from math import floor
```

Now you can run the code:

```python
# Try again
floor(5.7)
```

You can ask the chatbot to tell you about more functions in the `math` package, or look up the documentation [here](https://docs.python.org/3/library/math.html).

## Calculating useful statistics with `statistics`

Python also comes with a package for ```statistics```. You can use it to compute common statistics like mean, median, or standard deviation.

To try it out, let's import the ```mean``` and ```stdev``` functions from the `math` package:

```python
from statistics import mean, stdev
```

First, create a list that contains the heights of a group of friend's heights:

```python
my_friends_heights = [160, 172, 155, 180, 165, 170, 158, 182, 175, 168]
```

You can now calculate the ```mean``` value of the list of heights using the `mean` function:

```python
mean(my_friends_heights)
```

You can also calculate the standard deviation of the heights using the ```stdev``` function:

```python
stdev(my_friends_heights)
```

There are other functions in the statistics package that you can import to calculate other statistics, like median, etc. You can read more about the statistics package [here](https://docs.python.org/3/library/statistics.html) - or ask the chatbot!

## Introducting randomness to your programs with `random`

Python also comes with a ```random``` package that generates random numbers and selects random elements from a list. This can be very useful in coding projects! You can read more about `random` [here](https://docs.python.org/3/library/random.html).

You'll write code here to randomly sample from a list of items. To get started, import the ```sample``` function from the ```random``` module:

```python
from random import sample
```

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: 
<br>Explain how to use the function sample from the random module.</p>

Create lists of ingredients and that you'll select from and pass to the LLM for recipe suggestions:

```python
spices = ["cumin", "turmeric", "oregano", "paprika"]
vegetables = ["lettuce", "tomato", "carrot", "broccoli"]
proteins = ["chicken", "tofu", "beef", "fish", "tempeh"]
```

You can use Python to select random ingredients for you from these lists.

The ```sample``` function takes two parameters: the list you want to select from, and the number of items you want to select:

```python
random_spices = sample(spices, 2)
random_vegetables = sample(vegetables, 2)
random_protein = sample(proteins, 1)
```

See what ingredients you selected:

```python
print(random_protein)
```

## Try for yourself! 

Pause the video here, and try running the last two cells again. 
* You'll see that you get different ingredients each time! 
* Check the `random_spices` and `random_vegetables` variables too and see that they also change

## Use an LLM to suggest a recipe for you using those 'randomly selected' ingredients.

Create a prompt that asks an LLM to create a recipe using your randomly selected ingredients:

```python
prompt = f"""Please suggest a recipe that includes the following ingredients.

Spices: {random_spices}
Vegetables: {random_vegetables}
Proteins: {random_protein}
"""
```

Check the prompt to see the ingredients:

```python
print(prompt)
```

Next, import the `get_llm_response` function from `helper_functions.py` to use to generate the recipe:

```python
from helper_functions import get_llm_response
```

Next, pass the prompt to the LLM, store the response in a variable named `recipe`, and then print the result:

```python
recipe = get_llm_response(prompt)

print(recipe)
```

## Extra practice

Try the following exercises to practice what you have learned. If you need help, don't hesitate to ask the 🤖 chatbot!

### Exercise 1

Write code to import the `tan` (tangent) function from `math`, then calculate and print the tan of each value.


```python
# Write code to import the tan (tangent) function from math
from math 

values = [0, pi/2, pi, 3/2*pi, 2*pi]

# Complete the following code to calculate the tan of each value:
for value in values:
    print (f"The tangent of {value:.2f} is    ")
```

### Exercise 2

Write code to calculate the median score in the list of scores below. You'll need to write an import statement as well as use the `median` function on your data.

```python

scores = [28, 14, 15, 25, 21, 26, 30, 8, 36]

# Write code to import the median function from the statistics package
from 

# Calculate the median score
median_score = 
print(median_score)
```

### Challenge exercise!

Write code using Python's built-in random package to print a random number between 1 and 10.

Work with a chatbot, or consult the `random` package's [documentation website](https://docs.python.org/3/library/random.html) when you need help.

```python
# YOUR CODE HERE
```
