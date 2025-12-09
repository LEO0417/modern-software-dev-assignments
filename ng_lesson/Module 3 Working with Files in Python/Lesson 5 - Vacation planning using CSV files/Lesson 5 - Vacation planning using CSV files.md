# Lesson 5: Vacation planning using CSV files

In this lesson you'll learn to read in and work with data stored in CSV format. Data of this type looks like a table with rows and columns, and is referred to by programmers as **structured data**.

As always, begin by loading the helper functions you'll use:

```python
# Imports
from helper_functions import get_llm_response, print_llm_response, display_table
from IPython.display import Markdown
import csv
```

Note that `import csv` here is new. Don't worry about the details for now, but this line of code will be used later to read in CSV data. You'll learn more about this code in Course 4.

## Loading data from a CSV file

You'll use the file ```itinerary.csv```, which has information about arrival and departure dates for each destination in a trip around the world.

Here is the code to load the file - the first part is the same as you've been using up to this point:

```python
f = open("itinerary.csv", 'r')
```

The next part, where you read the data in from the file, is different because you are now reading in a CSV file:

```python
csv_reader = csv.DictReader(f)
itinerary = []
for row in csv_reader:
    print(row)
    itinerary.append(row)
```

Now close the file:

```python
f.close()
```

You can print the itinerary to view it's content and use the `type` function to check the datatype:

```python
print(itinerary)
```

```python
type(itinerary)
```

Now take a look at the first item
* Remember the first item in a list has index 0

```python
# Print item 0 
print(itinerary[0])
```

This is a dictionary. You can access a particular value by passing in the key - let's look at the `Country` value in the first row of the itinerary:

```python
print(itinerary[0]["Country"])
```

## Try for yourself!

Pause the video and explore other rows in the itinerary list, or individual items in any destination. Modify the code below to explore this world tour!

```python
print(itinerary[0])
print(itinerary[0]["Country"])
```

<p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
    <br><br>
    Explain this code line by line:
    <br><br>f = open("itinerary.csv", 'r')
    <br>csv_reader = csv.DictReader(f)
    <br>itinerary = []
    <br>for row in csv_reader:
    <br>itinerary.append(row)
    <br><br>f.close()
</p>

## Structured Data

Let's visualize this itinerary in a more readable way.

* Use the ```display_table``` helper function:

```python
display_table(itinerary)
```

Next, write code to filter the table based on some criterion - in this case if the country is Japan - and then add the information for that stop to a new list called `filtered_data`:

```python
# Create an empty list to store the filtered data
filtered_data = []

# Filter by country
for trip_stop in itinerary:
    # For example: get the destinations located in "Japan"
    if trip_stop["Country"] == "Japan":
        filtered_data.append(trip_stop)
```

```python
display_table(filtered_data)
```

Note that the `filtered_data` variable only contains one row.

## Using AI to suggest trip activities

Retrieve the first destination and then ask an LLM for suggestions of activities to do in that location during the dates of the visit:

```python
# Select the first destination from the itinerary list (Hint: index=0)
trip_stop = itinerary[0]
print(trip_stop)
```

Create variables to store all the individual items from ```trip_stop```:

```python
city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]
```

Write a prompt to get activity suggestions for your trip destination:

```python
prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}. 
Please create a detailed daily itinerary."""

print(prompt)
```

Use Markdown to display the LLM response nicely in the Jupyter notebook:

```python
# Store the LLM response
response = get_llm_response(prompt)

# Print in Markdown format
display(Markdown(response))
```

## Extra Practice

In these exercises, you'll create an itinerary for another stop on the trip! 

### Exercise 1

First, create a filtered dataset for Brazil. You'll need to update the `if` statement to select the right country. 

```python
# Create an empty list to store the filtered data
filtered_data = []

# Filter by country
for trip_stop in itinerary:
    # For example: get the destinations located in "Brazil"
    # Complete code on next line:
    if trip_stop["Country"] == "":
        filtered_data.append(trip_stop)

print(filtered_data)
```

### Exercise 2

Next, update the variables to pass in the prompt to the LLM. You'll need to modify the code on the next line to select the first item from `filtered_data` rather than the whole `itinerary`.

```python
trip_stop = itinerary[0]

city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

print(f" The city is: {city}")
print(f" The country is: {country}")
print(" The arrival date is: {arrival}")
print(" The departure date is: {departure}")
```

Now, you can run the prompt to get a new itinerary!

```python
prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}. 
Please create a detailed daily itinerary."""

print_llm_response(prompt)
```

### Challenge exercise!

Complete the code below so that it will **print out the country of every destination** in the `itinerary.csv` file. Ask the chatbot for help if you need it!

```python
f = open("itinerary.csv", "r")
csv_reader = csv.DictReader(f)
itinerary = []
for row in csv_reader:
    print(row)
    itinerary.append(row)
f.close()

# Complete the next two lines to print the country:
for trip_stop in :
    print()
```
