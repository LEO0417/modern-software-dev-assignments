# Lesson 1: Using functions from a local file

Hit the play button on the video next to this Jupyter notebook to start the video and follow along as Andrew explains how to work through this lesson!

In all of the courses so far, you have used a set of helper functions that were made available to you in the learning environment.

In this lesson, you will see how these functions are stored in Python files and loaded into the notebook for you to use with the `import` command.

## Revisiting the temperature conversion example

Here is the function you saw in the last course for converting temperatures from Fahrenheit to Celsius. Run the next cell to define the function:

```python
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
```

And run the next cell to use the function!

```python
fahrenheit_to_celsius(68)
```

In the cells above, you directly defined the function and then used it. 

Throughout the previous courses, you used functions that you imported from `helper_functions`.

It turns out these were stored in a local file in the same directory as the notebook called `helper_functions.py`.

A related function to the `fahrenheit_to_celsius` function above is also included in the `helper_functions.py` file. It's called `celsius_to_fahrenheit` and does the temperature conversion in the other direction.

```python
celsius_to_fahrenheit(20)
```

This code doesn't work because you haven't made the function available to Python yet. Let's ask the chatbot how to do that:

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: I have the celsius_to_fahrenheit function in the file helper_functions.py. How do I load it into my Jupyter notebook?</p>

Import the `celsius_to_fahrenheit` function from the `helper_functions.py` file:

```python
from helper_functions import celsius_to_fahrenheit
```

You can now use the function!

```python
celsius_to_fahrenheit(20)
```

## Different ways to import functions from a file

Python has a few different ways to import functions from a file. Run the code below to import all functions in a file:

```python
import helper_functions
```

To use this, you must five the name of the file *and* the name of the function, separated by a `.` character:

```python
helper_functions.print_llm_response("What is the capital of France?")
```

Note that you must include the `.` for this to work. For example, if you want to use `get_llm_response` - which is also defined in `helper_functions.py` - and you try the following code, it won't work:

* 🚨 Alert: running the next cell will return an error!

```python
response = get_llm_response("What is the capital of France?")
```

To fix this, you must include the file name and the `.` character as with `print_llm_above`:

```python
response = helper_functions.get_llm_response("What is the capital of France?")
print(response)
```

There is another way to import all of the functions in a file that avoids the `.` notation above. You can use a `*` character and the following command:

```python
from helper_functions import *
```

This imports all the functions in a file and makes them available without `.` notation.

```python
# Try again
response = get_llm_response("Give me three tips to become a good learner.")
```

```python
# It worked!
print(response)
```

**Note:** Using the `from file import *` notation can cause unexpected results in some cases. 

Instead, it is recommended to only load what you need (e.g. `from helper_functions import print_llm_response`), or to import that whole file and use the `.` notation. 
