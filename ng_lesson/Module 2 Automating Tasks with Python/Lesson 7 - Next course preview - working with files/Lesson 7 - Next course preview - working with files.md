# Lesson 7 - Next course preview: working with files

In the next course, you will work with files in Python, exploring some fun applications. This lesson is a quick teaser of the topics you will cover next.

```python
from helper_functions import *
```

In the next cell, you load text from a file that contains a journal entry with descriptions of restaurants and their specialties.

```python
journal = read_journal("journal_entries/cape_town.txt") 
print(journal)
```

As you can see, there is a lot of text, and finding the important information can take some time. You can use LLMs to highlight the important information for you. For instance, the restaurants and their specialties.

```python
prompt = f"""
Given the following journal entry from a food critic, identify the restaurants and their specialties.
For each restaurant, highlight its name and specialties in bold and use different colors for each.
Provide the output as HTML suitable for display in a Jupyter notebook.

Journal entry:
{journal}
"""
html_response = get_llm_response(prompt)
display_html(html_response)
```

You have achieved a fantastic feat! 🎉🎉🎉 You completed this course and are ready to tackle new programming challenges. You have already seen how to work with lists, dictionaries, and booleans, and are familiar with how to use all of them with LLMs. I hope to see you in the next course so that you continue to explore cool examples like the one in this lesson! 🚀👏
