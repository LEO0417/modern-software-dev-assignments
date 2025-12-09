# Lesson 6 - Helping AI make decisions

In this lesson you will see how booleans can be used to create sophisticated programs with branching decisions.

```python
from helper_functions import print_llm_response
```

## Performing tasks depending on their time to completion

Let's say that you have a task list with tasks that LLMs could assist you with. Each element in that list is a dictionary with two keys: the `description` for the task and the `time_to_complete` after the LLM's first pass.

```python
task_list = [
    {
        "description": "Compose a brief email to my boss explaining that I will be late for next week's meeting.",
        "time_to_complete": 3
    },
    {
        "description": "Create an outline for a presentation on the benefits of remote work.",
        "time_to_complete": 60
    },
    {
        "description": "Write a 300-word review of the movie 'The Arrival'.",
        "time_to_complete": 30
    },
    {
        "description": "Create a shopping list for tofu and olive stir fry.",
        "time_to_complete": 5
    }
]
```

So, if you access the first element, you will get the following dictionary:

```python
task = task_list[0]
print(task)
```

Now, let's check whether the first task takes at most 5 minutes to complete after the LLM's first pass.

```python
task["time_to_complete"] <= 5 
```

To complete a task that requires 5 minutes or less after the LLM's first pass, you can use an `if` statement like the one below:

```python
if task["time_to_complete"] <= 5:
    task_to_do = task["description"]
    print_llm_response(task_to_do)
```

Let's see what would happen if you execute that same code for the second task:

```python
task = task_list[1]
if task["time_to_complete"] <= 5:
    task_to_do = task["description"]
    print_llm_response(task_to_do)
```

```python
task["time_to_complete"] <= 5
```

And for the third and fourth tasks:

```python
task = task_list[2]
if task["time_to_complete"] <= 5:
    task_to_do = task["description"]
    print_llm_response(task_to_do)
```

```python
task = task_list[3]
if task["time_to_complete"] <= 5:
    task_to_do = task["description"]
    print_llm_response(task_to_do)
```

## Looping through the task list

There is a more efficient way to avoid repeating the same code over and over again for different elements in a list. You have used the `for` loop in previous lessons. Here, you will use it to iterate through all the tasks, check if they take 5 minutes or less to complete, and ask the LLM to do a first pass at them if that's the case.

```python
for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)        
```

## `if`-`else` blocks

In some cases, you may want to perform another action when the `if` condition is not met. In those cases, you can use `else`. For instance, here Python will let you know that some of the tasks were not completed and will provide you with the `time_to_complete` information for those tasks.

```python
for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do) 
    else:
        print(f"To complete later: {task['time_to_complete']} time to complete.")        
```

## Saving tasks for later using lists

After you executed the previous cell, you saw that some of the tasks were not completed and their time to completion. However, it is better practice to save all the information from those tasks using a new list. Here, you will again use the coding paradigm where you initialize an empty list to save information (the tasks to complete later) using `.append()`.

```python
tasks_for_later = []

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)
    else:
        tasks_for_later.append(task)
```

```python
print(tasks_for_later)
```

Congratulations 🎉🎉🎉, you are very close to completing this course. In the next lesson, you will go through a quick demo about working with files.

## Extra practice

Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

```python
# Modify this code to complete the task 
# if it takes more than 15 minutes

task = task_list[2]

### EDIT THE FOLLOWING CODE ###
if task["time_to_complete"]: #Modify this line
    task_to_do = task["description"]
    print_llm_response(task_to_do)
### --------------- ###
```

```python
# Fix the code here by only using indentation.
# It should print a message if the "Chocolate" ice cream flavor 
# is located in the ice_cream_flavors list.

ice_cream_flavors = [
    "Vanilla", "Strawberry", "Mint Chocolate Chip",
    "Cookies and Cream", "Rocky Road", "Butter Pecan",
    "Pistachio", "Salted Caramel", "Chocolate",
    "Mango"
]

### EDIT THE FOLLOWING CODE ### 
#Hint: Recall that the code within for loops 
# and if statements is indented. The convention
# in Python is to add four spaces for indented code.
for flavor in ice_cream_flavors:
if flavor == "Chocolate":
print(f"The list of flavors contains {flavor}, Andrew's favorite.")
### --------------- ###
```

```python
# Add variables to the f-string to provide the
# task description as well as the time to complete 
# for the tasks that are left for later.

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do) 
    else:
        ### EDIT THE FOLLOWING CODE ###
        # Hint: To add a variable in an f-string
        # you need to use the following syntax: {variable_name}. 
        print(f"To complete later:") 
        ### ---------------  ###
```
