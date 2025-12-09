# Lesson 1: Using files in Python

Hit the play button on the video next to this Jupyter notebook to start the video and follow along as Andrew explains how to work through this lesson.

So far, if you have taken the previous courses in this sequence, 
* You have worked with data that is created and assigned to variables within Jupyter notebooks.
* You have created multi-line strings.
* You have created lists and dictionaries.
* You have automated tasks using `for` loops and `if` statements.


In this lesson, you will read files using Python!

Let's start by loading some functions you'll use in this notebook:

```python
from helper_functions import get_llm_response
from IPython.display import display, Markdown
```

* Write a prompt to create a recipe using `get_llm_response`.

```python
# Write a list of ingredients
ingredients = ['chicken', 'broccoli', 'rice']

# Write the prompt
prompt = f"""
    Create a short recipe that uses the following ingredients:
    {ingredients}
"""

# Get the response from the LLM
response = get_llm_response(prompt)

# Print the LLM response
print(response)
```

## Opening a text file and saving it as a string

You will load data that has already been created and is stored 📁 for you in files.

* Start by loading an email that Daniel sent recently. It is stored in a '.txt' file.

```python
f = open("email.txt", "r")
email = f.read()
f.close()
```

* Print what it is 'inside' the email ✉️.

```python
print(email)
```

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
    <br><br>
    Explain this code line by line:
    <br><br>f = open("email.txt", "r")
    <br>email = f.read()
    <br>f.close()
</p>

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
    <br><br>
    What happens if I don't close a file?
</p>

## Using LLMs to extract bullet points from the email

* Create a prompt to extract bullet points from Daniel's email ✉️.

```python
prompt = f"""Extract bullet points from the following email. 
Include the sender information. 

Email:
{email}"""

print(prompt)
```

* Run the ```get_llm_response``` function to get the response with bullet points.

```python
bullet_points = get_llm_response(prompt)
print(bullet_points)
```

* Print the LLM response in Markdown format.

```python
# Print in Markdown format
display(Markdown(bullet_points))
```

## Extra practice

Try the exercises below to get an LLM to carry out different tasks using the email text you read in from file:

### Exercise 1

Complete the code below to identify all the **countries** mentioned in the email.

```python
# Complete the code below to identify all of the countries mentioned 
# in the email
prompt = f"""WRITE YOUR PROMPT HERE

Email:
{email}
"""

countries = get_llm_response(prompt)
print(countries)
```

### Exercise 2

Write code below to list all of the activities that Daniel did on his trip. You'll need to create a prompt and use either `get_llm_response` or `print_llm_response`.

```python
# Write code below to list all of the activities that Daniel did on 
# his trip. You'll need to create a prompt and use either 
# get_llm_response or print_llm_response
# START YOUR CODE HERE
```
