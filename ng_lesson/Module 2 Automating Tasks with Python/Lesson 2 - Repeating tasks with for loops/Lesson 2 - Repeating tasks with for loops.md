# Lesson 2 - Repeating tasks with for loops

This lesson will introduce you to a very important concept in programming: the `for` loop. A `for` loop is a special code pattern found in many languages that allows you to repeatedly perform actions on all the items in a list in an automated way. Let's take a look by starting with loading some functions.

```python
from helper_functions import print_llm_response, get_llm_response
```

## From previous lesson

At the end of last lesson you saw this list of tasks

```python
#from previous lesson:
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]
print(list_of_tasks)
```

You passed them one by one to the LLM, repeatedly updated the task variable, then re-executed the function call with this code:

```python
task = list_of_tasks[0]
print_llm_response(task)
```

If you wanted to complete all the tasks in your list, you would have to re-write the same code multiple times. Alternatively, you can use a `for` loop.

## Iterating through task lists with AI

When you run the cell below you will see how the for loop iterates through the elements in `list_of_tasks`.

```python
for task in list_of_tasks:
    print(task)
```

Here's the code that automatically passes all items in list to `print_llm_response`

```python
for task in list_of_tasks:
    print_llm_response(task)
```

Let's break this down.

The `for task in list` pattern works as follows:

- `task` is assigned the first item in the list. In this case, it's the string `"Compose a brief email to my boss explaining that I will be late for tomorrow's meeting."`
- The next indented line is called a block and contains an action to carry out on `task`. In this example, the string gets passed to the LLM, and the result appears on the screen.
- Then the loop starts again. Now, `task` is assigned the string "Write a birthday poem for Otto, celebrating his 28th birthday." It's the same variable, but with a different value.
- `get_llm_response` runs again, and so on.

Be sure to call out the `:` at the end of the line. Indentation is crucial; if it’s not correct, you'll get an error.

```python
for task in list_of_tasks:
print_llm_response(task)
```

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: Explain indentation error and help me fix it in this for loop: <br>
for task in list_of_tasks:<br>
print_llm_response(task)
</p>

## Iteratively updating AI prompts using lists

You can even use lists with for loops to iteratively update more complex prompts with the list items. For instance, let's say that you have a list of ice-cream flavors:

```python
#ice cream flavor example
ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]
```

You can use a for loop to iterate through the flavors and create a captivating description for each of them.

```python
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    print_llm_response(prompt)
```

Now that you know how to use lists, you can even save the promortional descriptions to another list using `.append()`:

```python
#saving results to a list
promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    description = get_llm_response(prompt)
    promotional_descriptions.append(description)
```

After you run that code, you should be able to access the promotional descriptions for each of your ice-cream flavors.

```python
print(promotional_descriptions)
```

## Extra practice

Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

```python
# Fix the following code.
# It should print the flavors in
# ice_cream_flavors one by one.

ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

### EDIT THE FOLLOWING CODE ###
for flavor in ice_cream_flavors;
    print(ice_cream_flavors)
### --------------- ###
```

```python
# Translate the flavors in ice_cream_flavors to Spanish
ice_cream_flavors = ["Vanilla", "Strawberry"]

for flavor in ice_cream_flavors:
    ### EDIT THE FOLLOWING CODE ###
    #Hint: you only need to add one or two sentences to the prompt
    prompt = f"""For the ice cream flavor listed below, 
    
    """
    ### --------------- ###
    print_llm_response(prompt)
```

```python
# Write code to get a list with 
# words without typos

words_with_typos = ["Aple", "Wether", "Newpaper"]
words_without_typos = []

for word in words_with_typos:
    prompt = f"""Fix the spelling mistake in the following word: {word}
    Provide only the word.
    """
    correct_word = get_llm_response(prompt)
    ### WRITE CODE HERE  ###
    #Hint: Append the correct_word to the words_without_typos list 
    ### --------------- ###

print(words_without_typos)
```
