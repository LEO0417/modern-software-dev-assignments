# Lesson 2: Loading and using your own data

In this notebook, you will get a chance to work with one of your own text files (.txt).
If you don't have any, you can create one by copying and pasting text into Notepad, MS Word, or Google Docs and saving it as a .txt file.

## Reading files in the working directory

To access data you have stored in files and folders on your computer, you need to tell Python where to find them. By default, Python will always look first for files in the folder your Jupyter notebook is in.

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
    <br><br>
    What is the folder called where Python looks first for files, and which folder is that by default?
</p>

* Load some functions to use in this notebook (note there are some new ones here, and they will be explained as you use them):

```python
from helper_functions import upload_txt_file, list_files_in_directory, print_llm_response
```

* Use the 'list_files_in_directory' function to list out the files in the current working directory:

```python
list_files_in_directory()
```

The function lists all of the files that are in the same folder as the Jupyter notebook for this lesson. 

Jupyter notebooks have a **.ipynb** extension and Python files have a **.py** extension.

The Python file here is the ```helper_function.py``` file, which it is loaded with some pre-defined functions. You will learn more about this file and how it works in Course 4.

There are also two plain text files, `email.txt` and `recipe.txt`. Let's take a look at those files:

```python
# Open the email.txt file and print its contents
f = open("email.txt", "r")
email = f.read()
f.close()

print(email)
```

```python
# Open the recipe.txt file and print its contents
f = open("recipe.txt", "r")
recipe = f.read()
f.close()

print(recipe)
```

## Uploading and reading your own text files

You can upload a text file to this folder using the button that appears after running the next cell.

Here are some notes about the file you can upload...
* It can be any plain text file with a .txt extension.
* Make sure the file size doesn't exceed 3 KB (about 3000 characters)
* You can create a plain text file by copying and pasting text into a text editor on your computer like Notepad (windows) or TextEdit (mac). 
* You can also use a Google Doc and download it as a plain text '.txt' file.
* **Don't upload anything confidential!** 

Run the next cell to open the upload file button:


```python
upload_txt_file() 
```

* See that your file is now in the same folder with the other files you listed above:

```python
# Print the list of the files inside this folder
list_files_in_directory()
```

* Open and print your own file content.

```python
# Change the file name on the next line to the one you uploaded. 
# Make sure you keep the double quotation marks around the file name!
f = open("your_file.txt", "r")
your_file_content = f.read() 
f.close()
```

```python
print(your_file_content)
```

## Use AI to summarize your file contents

* Ask an LLM to create a summary of your file content

```python
prompt = f"""Summarize the content from the following text
in at most two sentences. 

Text:
{your_file_content}"""
```

* Print out the prompt - notice that it now contains the content of your file:

```python
print(prompt)
```

* Print out the response from the LLM

```python
print_llm_response(prompt)
```

## Extra Practice

Try the exercises below to practice some of the techniques you learned in this lesson.

### Exercise 1

Modify the prompt below to ask the LLM a different question about your text data.

```python
# Modify the prompt below to ask the LLM a different question about 
# your data
prompt = f"""ADD YOUR INSTRUCTION HERE. 

Text:
{your_file_content}"""

print_llm_response(prompt)
```

### Exercise 2

Modify the prompt to use the data that you loaded in from `recipe.txt`.

**Hint:** look back throughout the notebook for the variable you stored the recipe data in.

```python
# Modify the prompt to use the data that you loaded in from recipe.txt
# Hint: look back throughout the notebook for the variable you stored 
# the recipe data in.
prompt = f"""Identify all of the cooking techniques used in the 
following recipe:

Recipe:
{your_file_content}"""

print_llm_response(prompt)
```
