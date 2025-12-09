# Lesson 10: Functions - Actions on Data

First, start by running the command below. This imports some functions, including the `print_llm_response` function you used before, from the `helper_functions` Python file.

```python
from helper_functions import *
```

In previous lessons, you have used the `print()` function to display values directly to the screen and the `print_llm_response()` function to use an LLM following the instruction you provide as a string. Below, you will print `"¯\_(ツ)_/¯"` and ask the LLM about the capital of France.

```python
print("¯\_(ツ)_/¯")
```

```python
print_llm_response("What is the capital of France?")
```

You have also used the `type` function, which gives you the type used in Python for a value or variable you provide. For instance, the type of 17 is `int` (for integer).

```python
type(17)
```

In this lesson, you will see more function examples and explore more deeply how functions work.

## Functions to count, to round, and to do much more

There are many functions in Python that you can use straight out of the box. For instance, the `len()` function counts the characters in a string. So when you run the code below, you will display (using `print()`) the result of counting (with `len()`) the number of characters in the string `"Hello World!"`.

```python
print( len("Hello World!") ) 
```

As another example, you can use `round()` to take a floating point number and round it to the nearest integer. Below, you use `print()` to display the result of rounding (with `round()`) the number `42.17`.

```python
print(round(42.17))
```

You can save the result from a function using variables in a very similar way to what you have already explored in previous lessons. Below, you save the result from `len("Hello World!")` to the variable `string_length`.

```python
string_length = len("Hello World!")
print(string_length)
```

There are many functions in Python, and you don't have to memorize them all. If you ever need a function to perform a specific task, you can ask the chatbot. Try it now with the suggested prompt here or try your own.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: How can I find the length of a string?
</p>

## Using functions in AI programs

Functions can be used alongside variables in AI programs. In the previous lesson, you saw how to create custom instructions (or prompts) for an LLM using variables. In the cell below, you will use variables and the `round()` function to create a prompt that you will use for an LLM with the `get_llm_response()` function. The `get_llm_response()` function is very similar to `print_llm_response()` (which you used before); the main difference is that you get a string as a result instead of just displaying the LLM response. This way, you can store the LLM response in the variable `response`.

```python
name = "Tommy"
potatoes = 4.75
prompt = f"""Write a couplet about my friend {name} who has about {round(potatoes)} potatoes"""
response = get_llm_response(prompt)
print(response)
```

## Extra practice

Try the exercises below to practice the concepts from this lesson. Read the comments in each cell with the instructions for each exercise.

<b>Feel free to use the chatbot if you need help.</b>

```python
# Enter one of your favorite numbers. Multiply the result by 10 and save it to a variable called 'lucky_number'.
# Print a message saying "Your lucky number is [lucky_number]!"

lucky_number = 
print(f"Your lucky number is {}!")
```

```python
# Use print_llm_response() to print a poem with the specified number of lines. Use the 
# prompt variable to save your prompt before calling print_llm_response()

number_of_lines = 
prompt = 
print_llm_response()
```

```python
# Repeat exercise 2, this time using the function get_llm_response(), then print() to print it. This function asks 
# the LLM for a response, just like print_llm_response, but does not print it. You'll need to save the response to
# a variable, then print it out separately.

number_of_lines = 
prompt = 
response = 
print()
```
