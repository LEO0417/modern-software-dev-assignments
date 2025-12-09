# Lesson 1 - Completing a task list with AI

In this course, you'll learn how to automate tasks using Python. This means you'll be able to have Python **do repetitive things** and **make decisions** for you. One important skill you'll develop is the ability to store multiple pieces of data together. This lesson will introduce you to **lists**, a powerful tool for this purpose.

To get started, let's load some functions that you'll use in this lesson.

```python
from helper_functions import print_llm_response, get_llm_response
```

### What are lists?
In the last course, you learned about variables. Each variable holds a single piece of data.

For example:

```python
name = "Tommy"
```

Let's say I want to write a poem for all my friends... all three of them. Run the cell below, then change the name above to Isabel and rerun the cell.

```python
prompt = f"""
Write a four line birthday poem for my friend {name}. 
The poem should be inspired by the first letter of my friend's name.
"""
print_llm_response(prompt)
```

Changing the value held by a variable requires lots of updates to the variables. A better way to handle this is by using a list. 

Lists are a data type in Python that can hold multiple pieces of data. This reduces the need for repetitive variable assignments since you can include all the pieces of data together.

## Creating  a list

Below, you will create a list that holds the names `"Tommy"`, `"Isabel"` and `"Daniel"`.

```python
friends_list = ["Tommy", "Isabel", "Daniel"]
```

```python
print(friends_list)
```

`friends_list` is a single variable of type `list` that holds multiple values.

```python
type(friends_list)
```

You can check how many values are stored in the list by using `len()`:

```python
len(friends_list)
```

So this list has three elements.

You can use lists as you used variables before within LLM prompts. Below, you are including the `friends_list` in the prompt to write four-line birthday poems for `'Tommy'`, `'Isabel'` and `'Daniel'`.

```python
prompt = f"""
Write a set of four line birthday poems for my friends {friends_list}. 
The poems should be insipred by the first letter of each friend's name.
"""
print(prompt)
```

Now, you can use that prompt with the LLM:

```python
print_llm_response(prompt)
```

## Accessing individual elements of a list

You can access individual elements from a list. Let's ask the chatbot how to do that.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: How do I access a specific element of this list:
friends_list = ["Tommy", "Isabel", "Daniel"]
</p>

For instance, to access the first element, you would use the following code:

```python
first_friend = friends_list[0]
print(first_friend)  # Output: Tommy
```

To access the second element, you would use the following code:

```python
print(friends_list[1]) # Output: Isabel
```

Note that for accessing the first element you used the index 0, and for accessing the second element you used 1.

So, if you do the following, you'll get an error.

```python
print(friends_list[3]) # Gives an error
```

But, if you run the following code, you will be able to access the last element from that list. 

```python
print(friends_list[2])
```

## Adding another element to the list

```python
print(friends_list)
```

If you want to add some data to an list, you will use `list.append(new_data)`. So, to add `"Otto"` to your `friends_list`, you can run the following code:

```python
# add single element to list
friends_list.append("Otto")
```

```python
print(friends_list)
```

Try for yourself - modify code to add another friend, or yourself

```python
# Modify the code below to add another friend:
friends_list.append()
```

## Deleting elements

Tommy moved to Bora Bora, so we can't be friends anymore. Let's remove Tommy from `friends_list` by using `.remove()`:

```python
#using remove
friends_list.remove("Tommy")
```

```python
print(friends_list)
```

## Lists with other data types

Lists can hold any type of data. For instance, here is a list of numbers

```python
list_ages = [42, 28, 30]
```

```python
print(list_ages)
```

Lists can also hold long strings. Here's a list of tasks that might make up a todo list

```python
#list of tasks in priority order. Multi-line lists are allowed in python!
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]
```

If you were wondering how to use lists with AI, take this example. Each element in the previous list is a string that you can pass to `print_llm_response()`. If you want an LLM to do each of these tasks for you, here's what you would do:

Set a variable called `task` to each element in the list in turn, then pass it to `print_llm_response()`.

```python
task = list_of_tasks[0]
print_llm_response(task)
```

```python
task = list_of_tasks[1]
print_llm_response(task)
```

```python
task = list_of_tasks[2]
print_llm_response(task)
```

You worked through all the elements in the list, but there is still a lot of repetition here. You had to specify each element separately. There is actually a much better way to do this using something called a for loop. Let's go to the next video to see it in action.


## Extra practice

Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

```python
# Create a list with the titles 
# of five of your favorite movies

### WRITE CODE HERE ###
movie_list = 
### --------------- ###
```

```python
# Display the fourth element of 
# the following list using print()

prime_numbers = [2, 3, 5, 7, 11]

### WRITE CODE HERE ###

### --------------- ###
```

```python
# Fix the bug in the following code

prime_numbers = [2, 3, 5, 7, 11]

### FIX THIS CODE ###
print(prime_numbers(3)) #access and print() the fourth element
### --------------- ###
```

```python
# Add one name to friends_list using append

friends_list = ["Tommy", "Isabel", "Daniel", "Otto"]

### WRITE CODE HERE ###

### --------------- ###

print(friends_list)
```

```python
# In the following code, remove the country 
# that is not in South America

countries_in_south_america = ["Colombia", "Peru", 
                              "Brasil", "Japan",
                              "Argentina"]

### WRITE CODE HERE ###

### --------------- ###

print(countries_in_south_america)
```
