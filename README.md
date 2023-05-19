# 30DAYSOFPYTHON
This is an open-source project guide for learning Python Programming Language .
Fork it and create separate branches/folders for each day. 


Key Resources 
1. https://www.programiz.com/python-programming
2. https://www.pythoncheatsheet.org/cheatsheet/
3. https://www.w3resource.com/python/python-tutorial.php

## Topics Breakdown

### Day 1: Python Basics
Start by installing Python and a text editor. Learn the basics of Python, such as: 
 variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

#### Exercise
Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 


### Day 2: Python Control Flow - IF Statements, Logical and Comparator Operations

Learn how to use control flow statements like if-else statements, Switch-Case Statement,Logical Operators (and, OR), Boolean operators and comparisonooperations such as <, >, !==, ==, etc

#### Exercise
You are building a program to help a user decide what to wear based on the current weather conditions. Write a Python program that prompts the user to enter the current temperature in Fahrenheit and whether it is currently raining or not (as a boolean value), and then suggests an appropriate outfit based on the following criteria:

If the temperature is less than 50 degrees Fahrenheit, suggest wearing a coat, hat, scarf, and gloves.
If the temperature is between 50 and 70 degrees Fahrenheit and it is not raining, suggest wearing a sweater or light jacket.
If the temperature is between 50 and 70 degrees Fahrenheit and it is raining, suggest wearing a rain jacket and boots.
If the temperature is above 70 degrees Fahrenheit and it is not raining, suggest wearing a t-shirt and shorts.
If the temperature is above 70 degrees Fahrenheit and it is raining, suggest wearing a light jacket and rain boots.


### Day 3: Loops and Iteration in Python 
Understand how to apply Loops and iteration in python programs. 
*** While loops:With boolean values, do-while loop too
*** For Loops: Using Indexing,using range(), Using items, looping over sequential data (sets, dictionaries, lists, tuples) 
*** For-Else statements
*** Break and Continue Statements

#### Exercise
    Fibonacci: Write a program that prompts the user to enter a positive integer n, and then prints the first n Fibonacci numbers. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.


### Day 4: Functions In Python 
Understand the concept of functions in Python. A function is a block of organized code that is used to perform a single task. They provide better modularity for your application and reuse-ability.
A function can take arguments and return values:

#### Exercise:
    1.write a function in python that takes a list of numbers and returns the sum of the given numbers. 

    2. write a function in python that takes a list of numbers and returns the second-largest item in the list of the given numbers. 

     3. write a function in python that takes 3 parameters: name, age, and occupation and prints this sentence as output: "My name is {name}, I am {age} years old and I work as a {occupation}". 

### Day 5: Strings and String Manipulations 
Understand how to create strings in python, how to format and how to manipulate. 
https://www.programiz.com/python-programming/methods/string
https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings
https://www.pythoncheatsheet.org/cheatsheet/string-formatting

#### Exercise:

1. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

### Day 5: Lists in Python
Understand LISTS and how to manipulate lists in python. 
Understand CRUD Operations in Lists using Python. 
https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples
https://www.programiz.com/python-programming/list

#### Exercise 
1. Write a Python program to remove duplicates from a list.
2. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

3. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False

### Day 6: Dictionaries in Python 
Understand the concept of dictionaries in Python
Understand CRUD Operations and manipulation of dictionaries 

https://www.programiz.com/python-programming/dictionary
https://www.pythoncheatsheet.org/cheatsheet/dictionaries

#### Exercise 
1. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

2. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

3. Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]



### Day 7: Sets 
Understand what Sets are,& how they work in Python
https://www.programiz.com/python-programming/set

#### Exercises
1.  Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
2.  Write a Python program to return a new set with unique items from both sets by removing duplicates.
   Given:
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
   Expected output:
    {70, 40, 10, 50, 20, 60, 30}

3. Update the first set with items that don’t exist in the second set
Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
Given:
  set1 = {10, 20, 30}
  set2 = {20, 40, 50}
Expected output:
 set1 {10, 30}

### Day 8: Tuples 



### Day 9:  




### Day 10: Regular Expressions


### Day 11: Object-Oriented Python 
 Classes, Inheritance, Objects 


### Day 12: Working with Files (Reading and Writing)

Excel files, csv files, text files 


### Day 13: Working with JSON (Reading and Writing)



### Day 14: Debugging,Error and Exception Handling 




### Day 15: Working with APIs 



### Day 16: Working with SQL Databases and Python 


















