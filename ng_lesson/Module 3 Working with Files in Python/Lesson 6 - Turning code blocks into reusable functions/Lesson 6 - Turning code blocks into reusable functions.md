# Lesson 6: Turning code blocks into reusable functions

Through this and the previous courses, you have been using several different **functions**. 

In this lesson, you'll learn how to create your own, and see how they can help you avoid writing lines of code over and over again.

Let's start by importing the helper functions you'll use:

```python
from helper_functions import print_llm_response
from IPython.display import Markdown, display
```

## Revisiting functions you've already used

Here are some of the functions you've encountered so far in these courses.

The `print` function displays data to the screen:

```python
print("Hello World!")
```

The `len` function returns the number of items, or elements, in a list:

```python
# Create a list of friends
friends_list = ["Tommy", "Isabel", "Daniel", "Otto"]

# Return the number of friends in the list
len(friends_list)
```

And you've been using a special helper function called `print_llm_response` to pass prompts to an LLM and display the response to screen:

```python
# The 'print_llm_response' function is in the helper_functions.py file
print_llm_response("What is the capital of France")
```

## Defining your own functions

Defining functions can help you avoid typing the same code over and over. 

For example, to read in the text from different food journals, you'd need to repeat the following code:

```python
# read in the Cape Town journal
f = open("cape_town.txt", "r")
journal_cape_town = f.read()
f.close()
print(journal_cape_town)
```

```python
# read in the Paris journal
f = open("paris.txt", "r")
journal_paris = f.read()
f.close()
print(journal_paris)
```

If you need to load multiple files, you'll have to repeat these three lines for each file.

To avoid this, you can instead define a **function** to read in a file and store the contents to a variable:

```python
def print_journal(file):
    f = open(file, "r")
    journal = f.read()
    f.close()
    print(journal)
```

Now that you have created this function, you can reuse it to read in different files:

```python
# Read in the Sydney journal
print_journal("sydney.txt")
```

You can define a function that **returns** a variable, rather than printing to screen:

```python
def read_journal(file):
    f = open(file, "r")
    journal = f.read()
    f.close()
    # print(journal)
    return journal
```

Use the `read_journal` function to store the contents of the Tokyo journal in a variable:

```python
journal_tokyo = read_journal("tokyo.txt")
```

Print out the Tokyo journal content:

```python
print(journal_tokyo)
```

Print out the length of the journal - the value is the number of individual characters in the string variable `journal_tokyo`:

```python
print(len(journal_tokyo))
```

## Parameters in functions

Previously, you saw how to use Python to carry out calculations that convert degrees Fahrenheit to degrees Celsius:

```python
# Value of temperature in Fahrenheit
fahrenheit = 72
# Calculation for getting the temperature in Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the results
print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
```

If you want to convert another temperature, you have to write the code again, replacing the value for the ```fahrenheit``` variable with the new temperature to convert:

```python
# Value of temperature in Fahrenheit
fahrenheit = 68
# Calculation for getting the temperature in Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the results
print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
```

You can do this as many times as you need

```python
# Value of temperature in Fahrenheit
fahrenheit = 76
# Calculation for getting the temperature in Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the results
print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
```

Again, this is a lot of typing! You can avoid this by writing a function for converting Fahrenheit to Celsius. Here is the code:

```python
def fahrenheit_to_celsius(fahrenheit):
    # Calculation for getting the temperature in celsius
    celsius = (fahrenheit - 32) * 5 / 9
    # Print the results
    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
```

Now, instead of changing the value of the ```fahrenheit``` variable directly each time, you'll pass the desired value to the function as a ***parameter***. A parameter is a variable that is used in functions to pass in information to the function - in this case the temperature in Fahrenheit that you want to covert to Celsius.

Let's use the ```fahrenheit_to_celsius``` function and pass in a temperature as the input parameter!

```python
fahrenheit_to_celsius(71)
```

```python
fahrenheit_to_celsius(70)
```

```python
fahrenheit_to_celsius(212)
```

## Returning values

To be able to save the result from the temperature conversion function, you need to include a ```return``` statement.

Here is a modification of the `fahrenheit_to_celsius` function that returns the converted temperature as a variable:

```python
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    # print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
    
    # Return the calculated value (not to print it, as before)
    return celsius
```

So when you run this function, the result is stored in a variable:

```python
# The value of temperature in Fahrenheit is 45
fahrenheit = 45
celsius = fahrenheit_to_celsius(fahrenheit)
```

You can now print the result:

```python
print(celsius)
```

Note that this function returns a number, in this case a `float`:

```python
type(celsius)
```

## Extra practice

Try the exercises below to practice what you have learned in this lesson!

### Exercise 1

Complete the code below to create a function that converts Celsius to Fahrenheit and displays the result to the screen.

**Hint:** Use the code from Fahrenheit to Celsius to help you!


```python

def celsius_to_fahrenheit():
    # WRITE YOUR CODE HERE

celsius_to_fahrenheit(0)   # Should print 32
celsius_to_fahrenheit(100) # Should print 212
celsius_to_fahrenheit(13)  # Should print 55.4
```

### Exercise 2

Write a function below that converts a length in **meters** to a length in **feet**, then returns the result.

Ask the chatbot if you're not certain of the equation!


```python

def meters_to_feet:
    # WRITE YOUR CODE HERE

print(meters_to_feet(10)) # Should print 32.8084
print(meters_to_feet(0.7)) # Should print 2.29659
```

### Challenge exercise!

Write a function that takes in a **filename** as a parameter, uses an LLM to create a three bullet point summary, and returns the bullets as a string.

Use the chatbot for help when you need it!

```python
from helper_functions import get_llm_response

def create_bullet_points(file):
    # Complete code below to read in the file and store the contents as a string
    f = open(file, "r")
    file_contents = # YOUR CODE HERE

    # Write a prompt and pass to an LLM
    prompt = f"""YOUR PROMPT HERE
    """
    bullets = get_llm_response() # Don't forget to add your prompt!

    # Return the bullet points
    return bullets

# This line of code runs your function for istanbul.txt and returns the output
output_bullets = create_bullet_points("istanbul.txt")

# Print the fucntion output
print(output_bullets)
```
