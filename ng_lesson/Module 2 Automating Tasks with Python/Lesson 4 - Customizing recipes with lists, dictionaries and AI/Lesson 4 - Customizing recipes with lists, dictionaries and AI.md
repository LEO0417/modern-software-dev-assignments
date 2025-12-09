# Lesson 4 - Customizing recipes with lists, dictionaries and AI

In the previous lesson, you went through how to use dictionaries to complete tasks by priority. In this lesson, you will see how you can use dictionaries to update LLM prompts and create food recipies that match your friends preferences, restrictions and cooking experience. 

```python
from helper_functions import print_llm_response, get_llm_response
```

## Food preference dictionaries

Dictionaries are a useful way to organize multiple variables associated with a single entity, like one of your friends. In the next dictionary, you store the food preferences and cooking experience for Tommy.

```python
food_preferences_tommy = {
        "dietary_restrictions": "vegetarian",
        "favorite_ingredients": ["tofu", "olives"],
        "experience_level": "intermediate",
        "maximum_spice_level": 6
}
```

As you can see there, that dictionary has four keys, wich you can access using `".keys()"`:

```python
print(food_preferences_tommy.keys())
```

And it has values with different data types: lists, strings and integers. 

```python
print(food_preferences_tommy.values())
```

Let's see how you can use these in a prompt to create recipes that take into account your friends dietary preferences.

## Using keys and values within AI prompt

So here's a prompt that uses all the information in the dictionary to create a customized recipe

```python
prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
Provide a two sentence description.
"""
```

Run the cell below to print the prompt.

```python
print(prompt)
```

Now, you can use that prompt with an LLM to suggest a recipe to fit Tommy's preferences:

```python
print_llm_response(prompt)
```

The model followed the instructions. Tommy will be delighted!

## Refining the prompt with available ingredients

You can go a step further and consider the available ingredients at your house. To do so, let's use the following lists:

```python
available_spices = ["cumin", "turmeric", "oregano", "paprika"]
```

You can add these directly to the prompt so that the LLM take those into consideration

```python
prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
Provide a two sentence description.

The recipe should not include spices outside of this list:
Spices: {available_spices}
"""
print(prompt)
```

Now, get the LLM response to that prompt and assign it to a variable:

```python
recipe = get_llm_response(prompt)
```

And print the recipe that considers Tommy's restrictions as well as the available ingredients at your house.

```python
print(recipe)
```

Try changing the prompt to give you step-by-step instructions and try adding a key-value pair to the dictionary that indicates favorite cuisine.

## Looking ahead

Let's take another look at`food_preferences_tommy["dietary_restrictions"]` 

```python
print(food_preferences_tommy["dietary_restrictions"])
```

Here is a different way you could tell Python that Tommy is vegetarian:

```python
food_preferences_tommy["is_vegetarian"] = True
```

```python
print(food_preferences_tommy)
```

Go to next video to see what `True` and `False` are and how they work in Python

## Extra practice

Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

```python
# Update the following dictionary 
# with your own preferences 

### EDIT THE FOLLOWING CODE ###
my_food_preferences = {
        "dietary_restrictions": [], #List with dietary restrictions
        "favorite_ingredients": [], #List with top three favorite ingredients
        "experience_level": "", #Experience level
        "maximum_spice_level": 0 #Spice level in a scale from 1 to 10
}
### --------------- ###

print(my_food_preferences)
```

```python
# Modify the following prompt, 
# without adding more than two sentences,
# so that the provided recipe includes detailed instructions.

### EDIT THE FOLLOWING CODE ###
#Hint: look at the last sentence in this prompt
prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
Provide a two sentence description.
"""
### --------------- ###

print_llm_response(prompt)
```
