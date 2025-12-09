# Lesson 3 - Prioritizing tasks with dictionaries and AI

In this lesson, you will explore dictionaries, a data structure that helps you store key-value pairs. The main difference with list, is that dictionaries assign a key to each values instead of an index. Let's start by importing some functions.

```python
from helper_functions import print_llm_response, get_llm_response
```

If you wanted to store ice cream flavor descriptions using lists, you would have something like this:

```python
ice_cream_flavors = [
    "Vanilla: Classic and creamy with a rich, smooth flavor from real vanilla beans.",
    "Chocolate: Deep and indulgent, made with rich cocoa for a satisfying chocolate experience.",
    "Strawberry: Sweet and fruity, bursting with the fresh taste of ripe strawberries.",
    "Mint Chocolate Chip: Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough: Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel: Sweet and salty with a smooth caramel swirl and a hint of sea salt.",
    "Pistachio: Nutty and creamy, featuring the distinct taste of real pistachios.",
    "Cookies and Cream: Vanilla ice cream packed with chunks of chocolate sandwich cookies.",
    "Mango: Tropical and tangy, made with juicy mangoes for a refreshing treat.",
    "Rocky Road: Chocolate ice cream mixed with marshmallows, nuts, and chocolate chunks."
]
```

If you wanted to look up the description for a particular flavor, you would have to memorize its index.

## Building intuition and definitions

Dictionaries in Python are very similar to the dictionaries you would find in a library. Each value in a dictionary is associated with a key, just as you will find definitions associated to words in a hardcover dictionary. Let's take as an example the following dictionary with ice cream flavors.

```python
ice_cream_flavors = {
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt."
}   
```

The `ice_cream_flavors` dictionary has keys:

```python
print(ice_cream_flavors.keys())
```

and values:

```python
print(ice_cream_flavors.values())
```

## Accessing elements

Dictionaries don't index their elements as list do, so you cannot access values in the way you would using lists. If you run the cell below, you will get an error message since the index 0 is not a key in the `ice_cream_flavors` dictionary. 

```python
#Wrong way of accessing elements (treating dict as a list)
print(ice_cream_flavors[0])
```

Let's ask the chatbot how to access items in this dictionary.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: How do I access a single item in this dictionary? <br>
ice_cream_flavors = {<br>
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",<br>
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",<br>
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt."<br>
} <br>
</p> 

So, to access the values in the dictionary you need to use its keys. For instance, for `Cookie Dough`, you can run the following code:

```python
cookie_dough_description = ice_cream_flavors["Cookie Dough"]
print(cookie_dough_description)
```

## Adding and updating elements in a dictionary

Let's take another look at the `ice_cream_flavors` dictionary

```python
print(ice_cream_flavors)
```

Now, to add a new item for the `"Rocky Road"` flavor, you will need to assign its definition to `ice_cream_flavors["Rocky Road"]` as follows:

```python
ice_cream_flavors["Rocky Road"] = "Chocolate ice cream mixd witother ngredients."
```

Note that you are using the same syntax that selects a single item, but this time use a key that didn't exist before and assign it a value. Let's check the dictionary after this update:

```python
print(ice_cream_flavors)
```

You can update existing dictionary items in a similar way. Let's fix the typos from the `"Rocky Road"` description.

```python
ice_cream_flavors["Rocky Road"] = "Chocolate ice cream mixed with other ingredients."
```

```python
print(ice_cream_flavors)
```

## Different types of elements

Let's say that you store data about your friends. For Isabel you have the following dictionary.

```python
isabel_facts = {
    "age": 28,
    "Favorite color": "red"
}
print(isabel_facts)
```

You can store information within that dictionary using lists. For instance, the names for each of her cats.

```python
isabel_facts["Cat names"] = ["Charlie", "Smokey", "Tabitha"]
```

```python
print(isabel_facts)
```

Or her favorite snacks:

```python
isabel_facts["Favorite Snacks"] = ["pineapple cake","candy"]
```

```python
print(isabel_facts)
```

## Using dictionaries to complete high priority tasks using AI

In the previous lessons you completed the tasks from a list --like the one below-- using AI.

```python
#task example, large list not ordered by priority. Want to prioritize
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation.",
    "Create an outline for a presentation on the benefits of remote work."
]
```

In reality, not all tasks would have the same priority. In fact, for this example, you have tasks with high, medium and low priorities as defined by the following lists:

```python
#instead of that unorganized large list, divide tasks by priority
high_priority_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Create an outline for a presentation on the benefits of remote work."
]

medium_priority_tasks = [
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation."
]

low_priority_tasks = [
    "Write a 300-word review of the movie 'The Arrival'."
]
```

You can use dictionaries to store all the tasks with their priorities in a single data object. Run the following cell to create that dictionary and display its contents:

```python
#create dictionary with all tasks
#dictionaries can contain lists!
prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks
}
```

```python
print(prioritized_tasks)
```

With this data structure, it is easy for you to focus only on the high priority tasks and complete them using a for loop and LLMs:

```python
print(prioritized_tasks["high_priority"])
```

```python
#complete high priority tasks 
for task in prioritized_tasks["high_priority"]:
    print_llm_response(task)
```

In the next lesson we will continue exploring dictionaries. You will see how to use values to create prompts to use with LLMs.

## Extra practice

Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

```python
# Update the description for the 
# Rocky Road flavor using get_llm_response()

flavor = "Rocky Road" 
prompt = f"Provide a brief description for the {flavor} ice cream flavor"

### EDIT THE FOLLOWING CODE ###
ice_cream_flavors["Rocky Road"] = 
### --------------- ###
```

```python
# Complete the medium priority tasks
# by modifying the following code

### EDIT THE FOLLOWING CODE ###
for task in prioritized_tasks["high_priority"]:
    print_llm_response(task)
### --------------- ###
```
