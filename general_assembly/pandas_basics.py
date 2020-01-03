# Warmup
# 1.	Write a function that takes & prints all the even numbers between 1 and 10,000.




# 2.	Write a function that returns a list of the numbers between 1 and 10,000 that are divisible by 3.




# 3.	The same as 2, but use Python list comprehensions




# 4.	Write a function get_max that takes a list of numbers and returns the max of those numbers, don't use the built-in max () function. Afterward, try using max() 



# 5.	Write a function is_odd_or_div_by_7 that returns true if a number is odd or divisible by 7 and False otherwise. Then write it using a lambda function.




# 6.	Use is_odd_or_div_by_7 and list comprehensions to write a function get_sublist_of_numbers_odd_or_div_by_7 that takes in a list and returns a sublist of those numbers that are either odd or divisible by 7.



# 7.	Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], write a function get_aggregate_order_counts that takes the list and returns a dictionary with the different dishes 
# as keys and the number of times they appear in the list as the values. For example, it takes ["burger", "fries", "burger", "tenders", "apple pie"] and outputs { "burger": 2, "fries": 1, "tenders": 1, "apple pie": 1 } 



# 8.	Use collections. Counter to achieve the same functionality.



# 9.	Write a function get_most_popular_order_data that takes a list of orders but instead of returning a dictionary with the counts, it just outputs a tuple: the dish that appears the most in the list and 
# the number of times it appears in the list. So the output given the example would be ("burger", 2) 



# ************************************************************************************************************************

# Download dataset: https://www.dropbox.com/s/cbffxkqq0ujru58/rock.csv?dl=0 
# 1.	How many songs are from 1981?


# 2.	How many songs are from before 1984


# 3.	What is the earliest release year in the data? (HINT: You might have to account for/clean up dirty data)


# 4.	What are the top 20 songs by play count (HINT: use built-in sorted() function, documentation here: https://wiki.python.org/moin/HowTo/Sorting)


# 5.	Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?


# 6.	How many different artists appear in the data?

# 7.	How songs does 'Rock'/’rock’ appear in the title of?



# Download csv from https://github.com/suneel0101/lesson-plan
# Nested dictionaries, list comprehensions, lambda functions, collections module, & csv module

# 1.	What are the top 10 highest funded companies?

# 2.	How many companies are from New York?

# 3.	What are the most popular Markets?

# 4.	Plot of companies against region, limiting to 20 most popular regions


# Data dave: https://github.com/datadave (Intermediate python)


# *****************************************************************

# Preliminary exercise
# What is the dataset about






#Basic Manipulation (75)
#Let's read in the data.
#How do we see what columns are available?
#How do we look at just the head or tail of the dataset?
#How do we look at only a few rows?
#How do we only look at certain columns?
#How do we pull out a column and look at it as a series?







# Filtering DataFrames (80)
# How do we look at only those rows that have Status = won
# Exercise: How many accounts have a price greater than $12,000?
# How do we get the maximum value of a certain column?
# Exercise: What is the minimum account price? The mean? The sum? The standard deviation?




# Aggregating data (120)
# What is the total dollar amount pending?
# How do we add columns?
# Let's add a column called Amount that is equal to Quantity * Price
# Exercise: Let's select just those rows where status is pending and sum up those amounts.





# Pivot tables (130)
# Question: What are pivot tables? Why are they useful?
# Let's pivot using one index.
# Let's pivot on multiple indexes
# Let's reverse those indexes
# Let's specify which values we care about
# Let's specify which columns we want broken down
# Let's specify how we want the values to be aggregated (aggfunc)
# Let's fill N/A values
# Let's get subtotals
# (Creative) Exercise: with a partner, use pivot tables to play around with the data. What pivots do you find particularly interesting or useful for this dataset?



# Plots from the dataframe
# Let's see documentation on DataFrame.plot


# Let's pivot and sum up Amount by Account Name
# Reset index so we get a normal pivot table again
# Make a clean bar chart.


# ************* Part 2 ******************
# Preliminary Exercise
# Take 2 minutes to download this dataset and examine it.
# Take 4 minutes to talk with a partner about the dataset and what kinds of insights you might extract from the data.
# Share with the class.
# Exercises (125)
# Read in the dataset from the url
# Solo: How many songs were released in 1981
# What is the earliest release year in the data (Hint: there might be dirty data...)
# Data munging (135)
# Using .apply() to clean up the year.
# Let's create a new column that contains the clean year

# lambda functions (150)
# Sometimes the data manipulation we'll want to do on a column will be pretty simple, so we can apply it in place. Say for example we wanted to lowercase an entire column



# >>> df["lowercase_title"] = df["Song Clean"].apply(lambda val: val.lower())

# lambda function exercises
# Create a new column called "contains_Rock" and the value should be True if the title contains the word "Rock" and False otherwise
# Create a new column called "contains_rock" and the value should be True if the title contains "rock" regardless of case (so it could contain "Rock", "ROCK", "roCK", etc) and False otherwise
# Using value_counts (175)
# Pull up the pandas value_counts documentation. We'll answer the following: What are the top 20 songs by play count?

# >>> df["ARTIST CLEAN"].value_counts()[:20]
# Using groupby (180)
# Pull up the Pandas groupby documentation. We'll look at play count grouped by artist.

# >>> df.groupby("ARTIST CLEAN")["PlayCount"].mean()


# ************* Part 3 ******************
# Preliminary Exercises
# Solo: Read in the data. What is this data about? What are some questions you want to answer about the data?
# What is the max funding total?
# Partner: Anything interesting/strange about the column names?
# Class altogether: Let's rename the column names accordingly.
# Using .describe() to get some descriptive statistics
# Pull up the pandas DataFrame describe documentation.






# Exercises (200)
# Construct a pivot table that indexes on region and shows the total funding amounts by region
# What is the average number of funding rounds for companies in NYC? How does that compare to SF?
# What are the top 3 markets with the highest average funding total per company?
# How many companies have Games as a category? What's their average funding total? Using a pivot table, what's the average funding total of those companies that have Games as a category, broken down by Region?
# What is the most popular category of company?
# Practice on revenue schedules data
# Notes: df.dtypes; Parsing datetimes






# How much money won YTD? lost?
# What's the close rate by Account Owner?
# What's the total number of accounts broken down by Account Owner
# What's the average opportunity amount per closed account broken down by Account Owner
# Create a pivot table indexing on Account Name that shows the total amount in each stage, YTD and then separately since the beginning of the data set
# What plots would be useful?
# Practice on leads data
# What pivot tables would you care about? Create them.
# What are the top original referrer domains of leads that have converted in 2015?

def print_evens():
    for i in xrange(1, 10001):
        if not i % 2:
            print(i)
            
print_evens

def even():
    for i in range(5):
        print(i)
        
even


# **********************************************************
# @TODO: Create a list of groceries
groceries = ['Tomatoes', 'Onions', 'Carrots', 'Milk', 'Salt', 'Pickle', 'Cheese']

# @TODO: Find the first two items on the list
groceries[0:3]

# @TODO: Find the last five items on the list
groceries[-5:]

# @TODO: Find every other item on the list, starting from the second item
groceries[2::2]

# @TODO: Add an element to the end of the list
groceries.append('Brinjal')
groceries

# @TODO: Changes a specified element within the list at the given index
groceries[0] = 'Tea'

# @TODO: Calculate how many items you have in the list
len(groceries)

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
groceries.index('Carrot')

# @TODO: Remove an element from the list based on the given element name
groceries.pop('Tea')

# @TODO: Remove an element from the list based on the given index
groceries.pop(groceries[0])

# @TODO: Remove the last element of the list
groceries.pop(groceries[-1])

print("You continue on your journey purchasing groceries...")

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 170
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)
dict = {'JP Morgan Chase': 327, 'Bank of America': 302, 'Citigroup': 170}

# @TODO: Change the market cap for 'Citigroup'
dict['Citigroup'] = 520

# @TODO: Add a new bank and market cap pair
dict['Roland'] = 420

# @TODO: Remove a bank from the dictionary
dict.pop('Roland', None)


for key in dict:
    print(dict[key])

for key in dict:
    print(f'Value: {dict[key]}')
    
for key, value in dict.items():
    print(f'key = {key} AND value = {dict[key]}')