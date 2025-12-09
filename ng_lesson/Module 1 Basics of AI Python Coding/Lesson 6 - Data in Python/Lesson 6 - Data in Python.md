# Lesson 6: Data in Python

There are different types of data in Python. Here, you will see how text and numbers are used in Python.

## Strings

Strings are used to store and manipulate text. As you see here, strings are written inside of quotes and can contain letters, numbers, punctuation marks, and other special characters. Run the following cells to print these four different strings. 

```python
print("Hello, World")
```

```python
print("My favorite drink is Earl Grey tea.")
```

```python
print("¯\_(ツ)_/¯")
```

```python
print("2.99")
```

## Multiline strings

If you use triple quotation marks, you can store a multiline string. These strings can span more than one line. When you run the following cell, you will see how the spaces in the second line are actually read as characters for the string.

```python
print("""Hello, World!
      It's great to be here!""")
```

Trying to define a multiline string using single quotes will lead to errors.

```python
print("Hello, World!
      It's great to be here!")
```

## The type() function

In Python, you can check the type of any data that you are using. To check the data type, you can use the `type()` function. When you run the next cell, you will retrieve the type for the string `"Andrew"`.

```python
type("Andrew")
```

Python returned `str`, which is short for string. Let's check the type for a multiline string:

```python
type("""
Numbers, text, and truth,
Strings, ints, and floats in our code,
Data shapes our path
""")
```

This also returns `str`, since it is also a string. Let's try a number within quotation marks:

```python
type("2.99")
```

This is also a string, even though it looks like a number. By using quotation marks you're telling Python to treat it as text, rather than a number. What about a number without quotes?

```python
type(100)
```

This time you get `int`, which is short for integer. Integers are the positive and negative whole numbers, like 42, 100, -9, and 0. Since there are no quotes around the number Python assumes this is numerical data, and since there is no decimal place on this number, it interprets it as an integer. Now, let's try a number that does have decimal places:

```python
type(2.99)
```

The function type gives `float`, which is the data type used to store floating point numbers. Floating point numbers are positive and negative numbers that include a decimal place, like 3.14, 2.99, and -0.003. 

## Python as a calculator!

Python works great for quick arithmetic operations. For instance, if you had a lemonade stand, and wanted to compute the total number of sales you made through the last 12 months, you can use Python like this:

```python
print(28+35+43+50+65+70+68+66+75+80+95)
```

As another example, you can perform more advanced math, like computing the compound interest after 10 years at a rate of 5%. To do that, you can compute 1.05 to the power of 10. Not sure how to do it in Python? You can use the Chatbot!

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: How do I compute 1.05 to the power of 10?
</p>

```python
print("Complete with chatbot code")
```

### Order of operations

The order of operations in Python is the same as in arithmetic. First, you compute parentheses, then exponents, then you multiply and divide (from left to right), and finally, you add and subtract (from left to right). 

So, if you are trying to convert from Fahrenheit to Celsius, the following cell will give you an incorrect answer:

```python
print(75 - 32 * 5 / 9)
```

Whereas the computation in this cell is correct.

```python
print((75 - 32) * 5 / 9)
```

### Try for yourself!
Try printing text with mixed numbers and letters, or just symbols, then check the type. Try multiline strings using the triple quotes. If you make any mistakes, as the chatbot for help. 

```python
print()
```

```python
type()
```

Fix the errors in the following code cells.

```python
# Fix the error in the following code
print(There are 366 days in a leap year")
```

```python
# Fix the error in the following code
print("There are 366 
days in a leap year")
```

A foot was defined as exactly 0.3048 meters in 1959. Convert 6 feet to meters.

```python
# Write code to convert 6 feet to meters
print("Convert 6 feet to meters")
```
