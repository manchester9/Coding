# Eg:1
# Create the function sumOfDigits that adds individual digits of a number, and returns the sum.
def sum_of_digits(a,b):
	return a + b
print(sum_of_digits(3,4))

# Eg:2
# Write a function to convert a variable name from under_score format to camelCase. 
# Make sure you support an unlimited number of underscores in the input!  You will not have to worry 
# about white space in your input, only alphanumeric characters and underscores.
def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]
print(camelCase("big_bath_monster"))

# Eg:3
# Write a function functionRunner that accepts a function to run and an argument to pass to that function.  
# It should call the passed in function and return the result of the function call.



# Eg:4
# Write a function, flatten, that accepts a two-dimensional array as its argument and returns a flattened one-dimensional copy of the array.  
# The argument array will never be more than 2 levels deep.  Remember to return a copy, meaning you should not modify the original 2D array passed in!



# Eg:5
# Write a function mySlice that mirrors the behavior of JavaScript's .slice() array method. 
# The slice() method returns a copy of a portion of an array into a new array object selected from arguments begin to end (end not included). 
# The original array will not be modified.  However,  unlike the built in method, mySlice will accept the array to operate on as its first parameter, 
# rather than being invoked as a method on that array.  Try and mirror the behavior of the native .slice() method exactly.    
# A few things to keep in mind: the `begin` and `end` arguments are optional, `end` can be a negative number, and mySlice should not modify 
# the original array!





# Eg:6
# Write a function myJoin that mirrors the behavior of JavaScript's .join() array method. 
# However, myJoin will accept the array to operate on as its first parameter, rather than being invoked as a method on that array.  
# Try and mirror the behavior of the native .join() method exactly.   Note that if an element is undefined or null it should be converted to the 
# empty string.  Additionally, if there is no delimiter argument, use a ',' character.




# Eg:7
# Write a function that accepts and array of numbers and returns and array of arrays. 
# The first array in the return array should include all the even numbers from the argument array. The second array in the return array should 
# include all odd numbers.





# Eg:8
# Write a function, changeKeys, which will take an array of musical keys and transpose those keys a specified number of steps.
# In music the chromatic scale has the following notes [A, A#, B, C, C#, D, D#, E, F, F#, G, G#].  A '#' is "sharp" notation.  A#, or A sharp, 
# is in between A and B.  Your function changeKeys() should take an array of notes and a number between 1-9 as the number of steps. 
# The function should return an array with all the notes in the array transposed up that many steps. 





# Eg:9
# Write a function, properNounFilter, which will determine whether the string argument passed in is a proper noun. 
# A word is considered a proper noun if only the first letter is capitalized. If the argument is a proper noun, properNounFilter should 
# return true.  It should return false if the word isn't a proper noun, if the word is mixed case, or if it is all caps.





# Eg:10
# Write the function myPush which mirrors the behavior of JavaScripts .push() array method.  
# myPush should accept the array to operate on as an argument and return the new array with the added element.
# myPush will receive two arguments: the array, and a single value to the added to the end of the array.






# Eg:11
# Create a function, removeZeros, which strips out any zeros from a number, and returns the 'stripped' number. 
# So, what happens if the input is zero? That is a special case! If the input is zero, the function should return NaN, which stands for 
# 'Not a Number'. NaN is a special value that isn't a number, but still is of type 'number'!






# Eg:12
# Write a function, totalPortfolioValue, that will calculate the total value of someone's stock portfolio based on the provided stock values. 
# It will take two array inputs--The stockTicker (current  value of the stocks) and an array that represents a person's current portfolio.
# There's a lot going on here, so let's take a closer look at the inputs.





# Eg:13
# Create the function isPrime(num) which will take the num parameter being passed and return true if the parameter is a prime number, 
# otherwise return false.





# Eg:14
# Write a function that will rotate an array to the right by a certain number of "steps".  
# For example, the array to rotate is: [1,2,3,4,5,6,7] and will be rotated 3 "steps". The final array will look like: [5,6,7,1,2,3,4].  
# Notice the position of each index is shifted to the right by three places. The first argument to the rotate function is the array to rotate; 
# the second argument is a number of​ steps.





# Eg:15
# Write a function myLastIndexOf that mirrors the behavior of JavaScript's .lastIndexOf() array method. 
# The lastIndexOf() method returns the last index at which a given element can be found in the array, or -1 if it is not present. 
# The array is searched backwards, starting at the optional parameter, fromIndex.  However,  unlike the built in method, myLastIndexOf 
# will accept the array to operate on as its first parameter, rather than being invoked as a method on that array.  Try and mirror the 
# behavior of the native .myLastIndexOf() method exactly.





# Eg:16
# Write a function mySplice that mirrors the behavior of JavaScript's .splice() array method. 
# The splice() method changes the contents of an array by removing existing elements and/or adding new elements.  However,  unlike the built 
# in method, mySplice will accept the array to operate on as its first parameter, rather than being invoked as a method on that array.  
# Unlike slice, splice modifies the original array!  Try and mirror the behavior of the native .slice() method exactly. 
# mySplice can take an unlimited number of arguments. The first is start, the index at which to start changing the array. The second, deleteCount 
# is optional and is the number of elements to take out of the array.  If deleteCount is omitted, all of the elements beginning with start index 
# on through the end of the array will be deleted. Every argument after deleteCount will be an element you should add to the array starting at the 
# start index. 
# Remember, mySplice returns the deleted elements, not the modified array!



# Eg:17
# Write a function that accepts a "shopping cart" array and returns the total bill for all the items. 
# Each item is represented by an array, where the first element is the item name, and the second element is an object with 
# two properties: quantity and price.





# Eg:18
# Write a function that accepts a nested array and returns a well-structured object. The array passed into the function will look like the 
# one below and have only four levels of nested-ness.
# As you can see in the examples below, the structure of the input is an array. Each element of that array is an array. The first element
# of the nested array (eg. animals) should become a property key on the return object.  The second element of the nested array is also an array, 
# where the elements alternate between property names (eg. dogs) and corresponding property values (eg. ['Corgi, 'Sheltie']).






# Eg:19
# Write a function that returns `true` if two objects contain the same data, or are equivalent, and `false` if not.
# In order for the function to return true, ALL the properties that exist in object 1 must exist and be equal to those in object 2. 
# Similarly, ALL the properties in object 2 must exist and be equal to those in object 1.
# Note: You can assume that each object will only have one level, meaning there will be no nested objects.






# Eg:20
# Write a function myMap that accepts an array and a callback function that is used to create a mapped array. Try to mirror the 
# functionality of the native .map() array method as closely as possible.
# Just like the native .map(), our myMap function should not change the array passed in as an argument, but should rather return 
# a mapped copy of that array.






# Eg:21
# Write a function myFilter that accepts an array and a callback function that is used to create a filtered array. 
# Try to mirror the functionality of the native .filter() array method as closely as possible.
# Just like the native .filter(), our myFilter function should not change the array passed in as an argument, but should 
# rather return a filtered copy of that array.





# Eg:22
# Write a function that will use the .reduce() method to find the frequency of strings in an array. Your function, strFrequency, takes 
# an array of strings, some strings occurring multiple times, and returns an object that specifies how many times each string occurred in the array.




# Eg:23
# Write a function that takes a string of text and returns an object containing the count for each character in the string. 
# Note: The input string will only contain lowercase letters. There will not be any whitespace, capital letters, numbers, or special characters.





# Eg:24
# Write a function that uses the native Array .reduce method to sum up an array of numbers, but starting at 50. 




# Write a function that takes a string of text and returns an object containing the count for each character in the string. 
# Note: The input string will only contain lowercase letters. There will not be any whitespace, capital letters, numbers, or special characters



# **********************************************************************************************************************************
# David beazley
# Eg 1: Suppose the file portfolio.dat contains information about some stocks that you purchased. 
# There are three columns showing the name, number of shares, and purchase price.

# A different file, prices.dat, contains a list of current stock prices. The columns in this file are the stock name and price.

# Write a program that reads the stock portfolio in portfolio.dat, the stock prices from prices.dat, and prints out 
# how much the entire portfolio has increased or decreased in value.