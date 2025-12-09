# Lesson 4: Running your first program

Now it's your turn to try running Python code! 

Hit the play button on the video next to this Jupyter notebook to start the video and follow along as Andrew explains how to work through this lesson.

### 1. Hello, World!

Below is the code for the "Hello, World!" program that you saw the chatbot write in the previous video. 

To run the code, click anywhere into the cell (the box with the code inside), and then type `Shift` + `Enter` (`Shift` + `Return` on a Mac) to execute.

```python
print("Hello, World!")
```

**Congratulations!** You have just joined the millions of people who have started their computer programming adventure by running this simple code!

### 2. Hello, you!

Let's create python code to say hello to you, instead of the world. Here are the steps to follow along with Andrew in the video:
1. Open the chatbot
2. Type in this prompt (substituting your name for mine)

            Modify the code below to have it say hello to me.
            
            print("Hello, World!")
            
            My name is Andrew
   
4. Paste the output code in the cell below using `Ctrl`+`V` (`Command`+`C` on a Mac)
6. Press `Shift + Enter` to submit your prompt

Once the chatbot has returned the code to you, you can copy and paste it into the cell below. Only copy the code in the black box - don't copy any conversation text that the chatbot writes.

```python
# PASTE CODE FROM CHATBOT ON THE NEXT LINE IN THIS CELL

```

You should see Python print out "Hello," followed by your name above.

One other thing to notice here - when you run a code cell, the little square brackets to the left of the cell will change to a number.

### 3. Say hello to someone you love!

Copy and paste (or just type out directly) the "Hello, World!" code in the cell below. Then modify the text between the quotation to say hello to your best friend, or favorite pet, or anyone else you love!

```python
# ADD YOUR CODE ON THE NEXT LINE

```

### 4. Comments in code
You may be wondering what the text is in the cells above that starts with the `#` hash or pound symbol. This is a comment line. It tells Python that it can ignore anything that follows on that line after the `#` symbol. Comments are used to help other humans understand what your code does.

Try running the next cell by pressing `Shift`+`Enter` - what do you think will happen?

```python
# THIS IS A COMMENT - PYTHON WILL IGNORE THIS LINE
```

The cell above runs just like the code you ran before - you saw the `*` appear to the left of the cell, and then change to a number. But this time nothing appeared on the screen.`

A comment line is a valid piece of Python code. It tells Python to ignore what follows. Here, Python followed that command exactly, running the code, ignoring the text, and because the code had no output to return to you, it seemed like "nothing happened."

Click into the cell below and click `Shift`+`Enter` to run the code - make sure to ask yourself what you think will happen first, and then see if you were right.

```python
print("This is a print statement!")
```

Now click into the cell again and type a `#` at the start of the line. What do you think this change will result in? Run the cell by pressing `Shift` + `Enter` to check!

You can have multiple comment lines in your code, including one after another, and dispersed throughout your code:

```python
# This is an example of code with multiple
# comments, including this one which
# spans multiple lines
print("Hello, Andrew!")
# Follow up with an additional print command
print("How is your day going?")
```

### 5. Making mistakes is no big deal!

Run the code in the next cell to see an example of how Python responds to code with an error in it.

```python
print("Hello, Andrew!)
```

You can ask the chatbot to help you fix this code:
1. Open the chatbot
2. Enter the following prompt:

       What is wrong with this code, and how do I fix it?

       print("Hello, Andrew!)

Fix the code in the next cell based on the chatbot's recommendation and run the cell using `Shift`+`Enter` to see if the fix worked!

```python
# Edit the code on the next line to correct the error 
print("Hello, Andrew!)
```

### Practice for yourself!

You can practice what you've learned in this lesson by trying out the code exercises below. For each one, follow the instructions in the comment line, then write your code on the next line below the comment. Once you are done, run your code by typing `Shift` + `Enter`. You can do this as many times as you like.

```python
# Write code that displays your favorite color
```

```python
# Write code that answers the question "How are you feeling today?"
```

```python
# Alter your code from the previous cell so that it will cause an error when you run it
```

```python
# Ask an LLM to help you fix the error in the code in the previous cell (or fix yourself) and
# then type the corrected code on the next line:
```
