# Lesson 3: Reading journals from food critics

In this lesson, you'll use AI to decide whether the contents of a file are about food and restaurants.

Text data like emails, journal entries, and social media posts often have no predefined structure. Additionally, each person writes in their own style: some use bullet points, while others prefer long paragraphs. For this reason, text data is known as **unstructured data**. 

Let's start by loading some helper functions to use in the notebook:

```python
from helper_functions import get_llm_response, print_llm_response
```

## Working with text data

You'll take look at journal entries in the working directory. The journals are stored as plain text files with extension `.txt'.

Start by opening and reading the Cape Town journal:

```python
f = open("cape_town.txt", "r")
journal_cape_town = f.read()
f.close()
```

Print the contents of the journal:

```python
print(journal_cape_town)
```

As you can see, the file is about restaurants and food.

Next, open the Tokyo journal entry file and read its contents:

```python
f = open("tokyo.txt", "r")
journal_tokyo = f.read() 
f.close()
```

Print the contents of the journal:

```python
print(journal_tokyo)
```

This entry is also about restaurants and food - but notice how different the format of the journal is from the Cape Town example!

## Determining if text files are relevant using LLMs

In this section, you'll write a prompt that instructs an LLM to determine whether a file content is about food and restaurants or some other topic. 

Define the prompt and include the Tokyo journal entry as the input data to check:

```python
prompt = f"""Respond with "Relevant" or "Not relevant": 
the journal describes restaurants and their specialties. 

Journal:
{journal_tokyo}"""
```

Print the LLM response to see if the file is relevant for our purpose or not:

```python
print_llm_response(prompt)
```

## Checking all files using a `for` loop

Using Python and an LLM together allows you to quickly iterate over multiple files and check the relevance of the content for your tasks.

Start by creating a list of all the files you want to check:

```python
# List of the journal files
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]
```

Next, use a `for` loop to open each file and have an LLM check if the content from that file is relevant to food and restaurants.
* *If you need a refresher on `for` loops, please revisit Course 2!*

```python
for file in files:
    # Read journal file for the city
    f = open(file, "r")
    journal = f.read()
    f.close()

    # Create prompt
    prompt = f"""Respond with "Relevant" or "Not relevant": 
    the journal describes restaurants and their specialties. 

    Journal:
    {journal}"""

    # Use LLM to determine if the journal entry is useful
    print(f"{file} -> {get_llm_response(prompt)}")
```

It seems that the Madrid journal entry is not relevant. Let's print its contents to see why the LLM flagged it as "not relevant":

```python
# Here you can check the content from any journal entry
f = open("madrid.txt", "r") 
print(f.read()) 
f.close()
```

The Madrid journal entry doesn't contain information about restaurants to try. Instead, it is a description of the economy of the city.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
    <br><br>
    I am using AI to determine whether different texts are "relevant" or "not relevant" using an LLM. Does this task have a specific name in AI?
</p>

## Extra practice

Experiment with different prompts to check whether files are of interest to you or not. Below is the example suggested in the video - try running it first. Then, try each exercise.

### Exercise 1

Change the prompt to classify the text for different topics, for example "mentions a dessert" or "describes the restaurant design."

```python
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", 
         "sydney.txt", "tokyo.txt"]

for file in files:
    # Read journal file for the city
    f = open(file, "r")
    journal = f.read()
    f.close()

    # TRY CHANGING THIS PROMPT TO ASK DIFFERENT QUESTIONS
    prompt = f"""Respond with "Yes" or "No": 
    the journal describes restaurants and food dishes. 

    Journal:
    {journal}"""

    # Use LLM to determine if the journal entry is useful
    print(f"{file} -> {get_llm_response(prompt)}")
```

### Exercise 2

Using the same code below, change the prompt to classify into more than two categories.

**Example:**
- mentions a **vegetarian** dish
- mentions a **vegan** dish
- mentions both
- mentions neither

```python
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", 
         "sydney.txt", "tokyo.txt"]

for file in files:
    # Read journal file for the city
    f = open(file, "r")
    journal = f.read()
    f.close()

    # TRY CHANGING THIS PROMPT TO ASK DIFFERENT QUESTIONS
    prompt = f"""Respond with "Yes" or "No": 
    the journal describes restaurants and food dishes. 

    Journal:
    {journal}"""

    # Use LLM to determine if the journal entry is useful
    print(f"{file} -> {get_llm_response(prompt)}")
```
