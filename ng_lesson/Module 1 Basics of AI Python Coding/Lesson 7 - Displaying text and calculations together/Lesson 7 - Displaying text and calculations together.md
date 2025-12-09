# Lesson 7: Displaying text and calculations together

You have seen that strings are used to store text and integers and floats are used to store numbers. 

<b>Strings</b>:

- `"Hello, world"`

- `"My favorite drink is Earl Grey tea"`

<b>Integers and floats</b>:

- `42`

- `3.14`

You have also seen that you can display data with `print()`:

- `print("Hello, World!")`

And you can use Python as a calculator:

- `print(3 * 4.5)`

In this lesson, you will see how to mix computations and strings together to display results in a readable way using Python's f-strings.

## Mixing strings with computations or data: f-Strings

If you wanted to display the equivalent degrees Celsius to a temperature in degrees Fahrenheit, you would do something like this:

```python
print(((75 - 32) * 5 / 9))
```

Now, if you wanted to display that degrees conversion using a string that included the computation, you could try:

```python
print("The temperature 75F in degrees Celsius is ((75 - 32) * 5 / 9)C")
```

But that doesn't work. It gives you back the formula, but it doesn't actually convert from degrees Fahrenheit to Celsius. 

To print the result of the computation within that string rather than just the formula, you can use what is called an <b>f-string</b> in Python which looks like this:

```python
print(f"The temperature 75F in degrees celsius is {(75 - 32) * 5 / 9}C")
```

There, I have written `f` (for formatted) before the quotation marks that denote a string, and I included the computation within curly braces `{(75 - 32) * 5 / 9}`. The `f` character tells Python that the subsequent string has data or computations within any pair of curly braces.

## Determining how data is displayed in f-strings

Let's go through another example. You can print Isabel's age as follows:


```python
print("Isabel is 28 years old.")
```

In some countries, there exists the concept of dog age. Since people live longer than dogs on average, someone's dog age is supposed to be one-seventh of their real human age. So, if you wanted to compute and display Isabel's dog age in a readable way, you wouldn't use a regular string like the one below.

```python
print("Isabel is 28/7 dog years old.")
```

Instead, you would use an f-string that includes the dog age equivalency computation as in the temperature conversion example.

```python
print(f"Isabel is {28/7} dog years old.")
```

Now, you see that the last print statement did work, but it displayed the number with one decimal place. What if you wanted to display a whole number, which is much more natural when speaking about ages? You can use the chatbot to answer that question. Feel free to copy and paste the prompt provided below or use your own, using it as a guideline:

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: Modify this code to print the answer without any characters after the decimal place: print(f"Isabel's dog age is {28/7}.")  
</p>


If you used that prompt, or another similar one, you would have gotten the code provided below. 

```python
print(f"Isabel is {28/7:.0f} dog years old.")
```

In `f"{28/7:.0f}"`, the `:.0f` part tells Python to display the result of `28/7` without any decimal places. You don’t need to worry too much about the details, but the `f` in `:.0f` indicates that the number is a floating-point number and should be formatted accordingly. This means it will be rounded to the nearest whole number and displayed without any decimal part.

<b>You just used AI to help you code!</b> You provided it with a piece of code that works in one way (displaying a number with decimal places) and asked it to modify it to work in a different way (displaying a number without decimal places). 

<b>Congratulations 🎉🎉🎉</b>

## Multi-line f-strings

So far, you have worked with strings that have a relatively small length. For lengthy strings, you will use multi-line strings, which are easier to read in a code editor.

The following multi-line f-string includes a description of how Americans use measurements in units that are not in the metric system. It displays the equivalent milliliters (ml) for 8 fluid ounces of milk and the equivalent fluid ounces to 100 ml of water.

```python
print(f"""
    Most countries use the metric system for recipe measurement, 
    but American bakers use a different system. For example, they use 
    fluid ounces to measure liquids instead of milliliters (ml).
    
    So you need to convert recipe units to your local measuring system!
    
    For example, 8 fluid ounces of milk is {8 * 29.5735} ml.
    And 100ml of water is {100 / 29.5735} fluid ounces.
""")
```

As you see there, you have to use triple quotes `"""` instead of single quotes `"` for multi-line strings, and you have multiple lines with text and computations; but besides that, everything works pretty much the same way.

You may have noticed that the way you are using f-strings right now is not that easy to read. All those numbers inside the curly braces don't let you see at a glance what the output is going to be, and if you have lots of calculations, it can be distracting.

In the next lesson, you'll see how to make your code easier to read, more flexible and reusable at the same time.

## Extra practice

Try the exercises below to practice the concepts from this lesson. Read the comments in each cell with the instructions for each exercise.

<b>Feel free to use the chatbot if you need help.</b>

```python
# Modify the code to print your age
print(f"I am {} years old.")
```

```python
# Fix this code
print(f"There are {365/7 weeks in a year")
```

```python
# Complete the code
print(f"The area of a square with side 5 cm is {} cm squared.")
```

```python
# Modify the code to display one decimal place
print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903} meters squared!")
```
