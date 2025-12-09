# L8 : Variables

In computer programming, <b>variables</b> are used to store, process, and manipulate data. So, let's say you wanted to store `28` in the variable `age`, this is what you would do:

```python
age = 28
```

So if you used `print()` with `age` as an argument, you would get the value that you assigned to that variable.

```python
print(age)
```

With `age = 28` you are telling Python to create a variable named `age` and use it to store the value `28`. However, you can change the value assigned to any variable you previously created. For instance, you can assign a value of `5` to `age` using the following code:

```python
age = 5
```

So if you display `age`, you will get `5` instead of `28`.

```python
print(age)
```

## Variables store numbers, strings and other type of data

Variables can be used to store floating point numbers, integers, strings, and other types of data. For instance, you can create a variable `name` and assign it the string `"Otto"`, or a variable `gnome_height` and assign it the floating point number `12.7`.

```python
name = "Otto"
gnome_height = 12.7
```

You can use variables within f-strings to make your output more readable. For example, you can print the value assigned to `age` along with the string `"Age: "` so that anyone reading the display will understand what the value represents.

Here’s how you can do it:

```python
print(f"Age: {age}")
```

As another example, let's use f-strings to display the values assigned to `name` and `gnome_height`.

```python
print(f"Name: {name}")
print(f"Gnome height: {gnome_height}")
```

<b>Important:</b> Variables are case-sensitive, so `Gnome_height` and `gnome_height` are not the same. To see this, you can run the next cell where you will get an error message.

```python
print(f"Gnome height: {Gnome_height}")
```

## Variables help you store values that constantly change 

Take a game where the score starts at zero. In the next cell, you create a variable `score`, assign it the value of `0`, and display the current score.

```python
score = 0 # now score is 0
print(score)
```

When the score increases by 50 points, you can update the variable by using its previous value and adding `50`.

```python
score = score + 50 # now score is 0 + 50 which is 50
print(score)
```

In a similar way, when the score increases by 100 points, the variable `score` can be updated by adding `100` to the previous value stored in `score`.

```python
score = score + 100 # now score is 100 + 50 which is 150
print(score)
```

And, after scoring an extra 300 points, the variable `score` is updated by adding `300` to the previous value stored in `score`.

```python
score = score + 300 # now score is 150 + 300 which is 450
print(score)
```

So at the end, the variable `score` stores the most updated score value. 

You can print the final score using an f-string as shown in the cell below:

```python
print(f"Your final score was: {score}") # prints 450
```

## Variable names restrictions

To demonstrate an important fact about variable names in Python, try to run the code below.

```python
my score = 450 
```

Now, ask the chatbot why that code didn't work. You can use the prompt suggested here.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: Why doesn't this code work? my score = 450
</p>

## Variables allow you to code efficiently!

Recall the dog age example that you saw in previous lessons. Assuming that Otto is 49 years old, you can display his dog age by using `print(49 / 7)`.

```python
print(49 / 7)
```

Using f-strings so that it is clear what you are displaying, you would use code similar to the one in the cell below.

```python
print(f"Otto's age in dog years is {49 / 7}")
```

Alternatively, now that you have seen how variables work, you can compute Otto's dog age and assign it to the variable `dog_age`.

```python
dog_age = 49 / 7
```

You can see how this would be an advantage if you consider the following scenario. Let's say you want to display an f-string with Otto's dog age multiple times. Without using variables, you would need to compute his dog age as many times as you refer to it.

```python
print(f"""Otto's dog age is {49/7}. So a dog that's about
{49/7} would be the same age as Otto. Any dog born about {49/7}
years ago would be in the same stage of life as Otto.""")
```

If Otto became a year older, you would need to change the values in each of the curly braces to `50/7`. Instead, if you used an f-string with the `dog_age` variable as the one below:

```python
print(f"""Otto's dog age is {dog_age}. So a dog that's about
{dog_age} would be the same age as Otto. Any dog born about {dog_age}
years ago would be in the same stage of life as Otto.""")
```

You will only need to update `dog_age` with Otto's new equivalent dog age:

```python
dog_age = 50/7
```

And use the same f-string that you used before without editing. By defining a variable once, you can use it in multiple places, which makes computer programs much more efficient.

```python
print(f"""Otto's dog age is {dog_age}. So a dog that's about
{dog_age} would be the same age as Otto. Any dog born about {dog_age}
years ago would be in the same stage of life as Otto.""")
```

As another example, you can replace the name "Otto" with the variable `name` in curly braces.

```python
print(f"""{name}'s dog age is {dog_age}. So a dog that's about
{dog_age} would be the same age as {name}. Any dog born about {dog_age}
years ago would be in the same stage of life as {name}.""")
```

This way, you can change Otto's name to his first and last name:

```python
name = "Otto Matic"
```

And use the f-string where the change is reflected in all places where the variable `name` appears.

```python
print(f"""{name}'s dog age is {dog_age}. So a dog that's about
{dog_age} would be the same age as {name}. Any dog born about {dog_age}
years ago would be in the same stage of life as {name}.""")
```

## Extra practice

Try the exercises below to practice the concepts from this lesson. Read the comments in each cell with the instructions for each exercise.

<b>Feel free to use the chatbot if you need help.</b>

```python
# Create a variable called 'my_name' and assign it the value of your name as a string.
# Then print out a greeting using the variable, like "Hello, Andrew!"
my_name = 
print()
```

```python
# Enter your favorite number below and store it in a variable called 'fav_num'. 
# Print out a message telling you what your favorite number plus 10 is.
fav_num = 
print(f"Your favorite number plus 10 is {}")
```

```python
# Create two variables, 'countries_visited' and 'countries_to_visit' and assign them the number of
# countries you've been to and the number of countries you hope to visit. Then complete the print statement.



print(f"""I have visited {} countries. I plan to visit {} more countries, 
      and when I'm done I will have visited {} countries.""")
```
