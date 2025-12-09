# L9: Building LLM prompts with variables

In the next cell, you will import the function `print_llm_response` that uses an LLM with an instruction that you provide as a string and displays the result.

```python
from helper_functions import print_llm_response
```

Basically, you can use that function as if you were asking a chatbot. You just need to provide your instructions as a string. For instance, you can ask "What is the capital of France?" using the following code:

```python
print_llm_response("What is the capital of France?")
```

Let's ask the LLM for the lifestyle description for Otto Matic, whose name is stored in `name`, if he were a `dog_age` years old dog.

```python
name = "Otto Matic"
dog_age = 21/7
```

```python
print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
Describe what life stage that would be for a dog and what that might 
entail in terms of energy level, interests, and behavior.""")
```

<b>You just used AI with your own variables!</b> You used an LLM with instructions that included variables you defined in this notebook.

<b>Congratulations 🎉🎉🎉</b>

## Variable names restrictions

The following variable names also have some problems. Try to fix them yourself or use the help from the chatbot.

```python
driver = "unicorn"
driver's vehicle = "colorful, asymmetric dinosaur car"
favorite planet = "Pluto
```

Now, update the next cell with any changes you made in the previous cell.

```python
print_llm_response(f"""Write me a 300 word children's story about a {driver} racing
a {driver's vehicle} for the {favorite planet} champion cup.""")
```

## Extra practice

Try the exercises below to practice the concepts from this lesson. Read the comments in each cell with the instructions for each exercise.

<b>Feel free to use the chatbot if you need help.</b>

```python
# Fix this code
1favorite-book = "1001 Ways to Wear a Hat"
"2002 Ways to Wear a Scarf" = second_fav_book
print(f"My most favorite book is {1favorite-book}, but I also like {second_fav_book})
```

```python
# Make variables for your favorite game, movie, and food.
# Then use print_llm_response to ask the LLM to recommend you
# a new song to listen to based on your likes.

print_llm_response(f"""

""")
```
