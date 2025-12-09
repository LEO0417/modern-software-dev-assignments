# Lesson 6: APIs to use AI models


In this lesson, you will learn how to use the OpenAI API. You'll also see how the `print_llm_response` and `get_llm_response` functions you have been using work to pass your prompt to the OpenAI API and retrieve the response.

As always, you'll start by loading some functions you need:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
```

Note the `openai` package, which you are using for the first time! The `OpenAI` function here is what enables the connect in Python to the chatbot. Check out the [OpenAI documentation](https://platform.openai.com/docs/api-reference/introduction) if you want to learn more!

**Note:** If you want to install this on your own computer, you would run `!pip install openai`. But it's already installed here for you.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: 
<br><br>
Explain what each line of this function does:
<br><br>
def get_llm_response(prompt):<br>
&nbsp &nbsp &nbsp completion = client.chat.completions.create(<br>
&nbsp &nbsp &nbsp model="gpt-4o-mini",<br>
&nbsp &nbsp &nbspmessages=[<br>
&nbsp &nbsp &nbsp&nbsp{<br>
&nbsp &nbsp &nbsp&nbsp&nbsp"role": "system",<br>
&nbsp &nbsp &nbsp&nbsp&nbsp"content": "You are a helpful but terse AI assistant who gets straight to the point.",<br>
&nbsp &nbsp &nbsp&nbsp&nbsp},<br>
&nbsp &nbsp &nbsp&nbsp{"role": "user", "content": prompt},<br>
&nbsp &nbsp &nbsp&nbsp],<br>
&nbsp &nbsp &nbsptemperature=0.0,<br>
&nbsp &nbsp &nbsp)<br>
&nbsp &nbsp &nbspresponse = completion.choices[0].message.content<br>
&nbspreturn response<br>
</p>

## Setting up the API key

To use the OpenAI API service you need an API key. Run the following code to set up the key in this learning environment:

```python
# Get the OpenAI API key from the .env file
load_dotenv('.env', override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = openai_api_key)
```

## Revisiting ```get_llm_response```

Here is the code you saw in the slides to define the ```get_llm_response``` function:

```python
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response
```

You can now use this function to ask a question to an LLM:

```python
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)
```

## Modifying the system message to change the LLM behavior 

Try changing/adding details in the "content" of the system message to change the LLM response
* For example, "You are a sarcastic AI assistant."
* Be sure to run the function cell each time you change the system message before you prompt the LLM.

```python
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant.", # change this instruction!
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response
```

Now give your prompt to the LLM:

```python
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)
```

Vary the system prompt a few times to see the behavior change!

## Modify the temperature to change the randomness of the output

Try changing the temperature value to make the response of the model more random and different each time
* For example, set the temperature to 1.0 or 0.7 and see what happens
* Be sure to run the function cell each time you change the temperature before you prompt the LLM.

```python
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant.", 
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0, # change this to a value between 0 and 2
    )
    response = completion.choices[0].message.content
    return response
```

Now give your prompt to the LLM

```python
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)
```

Change the temperature to a value greater than 0 and run the prompt cell a few times to see the response change!

## Using LLMs through the `aisetup` package

If you have installed aisetup on your own computer, you'll need to run an extra line of code to get your own API key into the notebook and accessible to the `print_llm_response` and `get_llm_response` functions:

```python
from aisetup import authenticate, print_llm_response, get_llm_response

authenticate("YOUR API KEY HERE")

# Print the LLM response
print_llm_response("What is the capital of France")

# Store the LLM response as a variable and then print
response = get_llm_response("What is the capital of France")
print(response)
```

**Note:** Please follow best practices and **don't** expose your API KEY in any code you write! 

You can try this method instead:

```python
from aisetup import authenticate, print_llm_response, get_llm_response
from dotenv import load_dotenv
import os

load_dotenv('.env', override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
authenticate(openai_api_key)

# Print the LLM response
print_llm_response("What is the capital of France")

# Store the LLM response as a variable and then print
response = print_llm_response("What is the capital of France")
print(response)
```

## Extra practice 

Ask the chatbot for help understanding how the `load_dotenv` code works. Ask for step-by-step instructions on how you can create and setup a `.env` file on your own computer.
