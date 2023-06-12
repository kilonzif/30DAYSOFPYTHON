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

### Day 6: Lists in Python
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

### Day 7: Dictionaries in Python 
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



### Day 8: Sets 
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

### Day 9: Tuples 
Understand Tuples and working with Tuples in Python 

https://www.programiz.com/python-programming/tuple
https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples

#### Exercise 
1. Write a Python program to check whether an element exists within a tuple.
2. Write a Python program to convert a list to a tuple.
3. Attempt this Quiz on Tuples in [Python] (https://pynative.com/python-tuple-quiz/) 

### Day 10: Regular Expressions
Understand the basics of Regex and how to apply it in Python 
Study via: https://www.pythoncheatsheet.org/cheatsheet/regular-expressions
https://www.edureka.co/blog/python-regex/
https://programmingwithmosh.com/interviews/interview-questions-in-python-regular-expressions/

#### Exercise 
1. Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls’ comments, neutralizing the threat.
Your task is to write a function that takes a string argument and returns a new string with all vowels removed.
For example, the string “Hello World!” would become “Hll Wrld”.
     Note: For this problem, ‘y’ is NOT considered a vowel.
     
2. Write a Python program to match if two words from a list of words start with the letter 'P'.

3. Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    Expected Output:
    example
    w3resource
    github
    stackoverflow


### Day 11: Object-Oriented Python 
Understand the concept of OOP in Python, covering Classes, Instance Methods, Objects 
https://www.programiz.com/python-programming/object-oriented-programming
 
 #### Exercise 
 1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))


***
2. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.

***
3. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format

### Day 12: OOP Concepts in Python: Inheritance, Polymorphism, Encapsulation & Abstraction

Advanced OOP in Python 
https://www.programiz.com/python-programming/inheritance

#### Exercise 
1.Inheritance: Create a class called Animal with a method speak() that prints "The animal makes a sound." Create two subclasses, Dog and Cat, which inherit from the Animal class. Override the speak() method in each subclass to print "The dog barks" and "The cat meows" respectively. Create instances of both subclasses and call their speak() methods.

*** 
2. #Polymorphism : Create a class called Shape with an abstract method area(). Implement two subclasses, Circle and Rectangle, which inherit from the Shape class. Override the area() method in each subclass to calculate and return the area of a circle and rectangle respectively. Create instances of both subclasses and call their area() methods.

***
3. Encapsulation: Create a class called BankAccount with private attributes account_number and balance. Implement public methods to access and modify these attributes. Use encapsulation to protect the data from direct access outside the class. Create an instance of the BankAccount class and demonstrate how to access and modify the account number and balance using the public methods.

### Day 13: Working with Files (Reading and Writing)

Understand how to navigate the directory and acess files
How to READ, WRITE and manipulate Files --- Excel files, csv files, text files 

#### Exercise
1. Create a new file named "output.txt" and write the sentence "Hello, world!" to it using Python.

***
2. Given a file named "numbers.txt" containing a list of integers separated by spaces, write a Python function to read the file and return the sum of all the numbers.

***
3.Write a Python program that reads a CSV file named "students.csv" with columns "Name" and "Age". Create a new file named "young_students.txt" and write the names of all students who are below 18 years old to this file.

### Day 14: Working with JSON (Reading and Writing)
Understand how to read and write into JSON files using Python. 
https://www.programiz.com/python-programming/json
https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/
https://www.simplilearn.com/tutorials/python-tutorial/json-python

#### Exercise 
1.  Reading a JSON File
Create a JSON file named "data.json" with the following content:
{
  "name": "John Doe",
  "age": 25,
  "city": "New York"
}
Write a Python program that reads the content of the JSON file and prints it on the console.


2. Parsing JSON Data
Create a JSON file named "books.json" with the following content:
[  {    "title": "Python Crash Course",    "author": "Eric Matthes",    "year": 2015  },  {    "title": "Learning Python",    "author": "Mark Lutz",    "year": 2018  },  {    "title": "Fluent Python",    "author": "Luciano Ramalho",    "year": 2015  }]

Write a Python program that reads the content of the JSON file and prints the title and author of each book.


### Day 15: Debugging,Error and Exception Handling 

https://learnbyexample.gitbooks.io/python-basics/content/Exception_Handling_and_Debugging.html
https://www.tutorialspoint.com/python/python_exceptions.htm
https://www.geeksforgeeks.org/python-exception-handling/
https://pp4e-book.github.io/chapters/ch9_error_handling.html

#### Exercises 
Exercise 1: Handling a ZeroDivisionError
Write a Python program that takes two numbers as input from the user.
Implement exception handling to handle the scenario where the second number is zero (ZeroDivisionError).
Display an appropriate error message if the second number is zero, and ask the user to enter a non-zero number.

Exercise 2: Handling a FileNotFoundError
Write a Python program that asks the user to enter a file name.
Implement exception handling to handle the scenario where the specified file does not exist (FileNotFoundError).
Display an appropriate error message if the file is not found and ask the user to enter a valid file name.

Exercise 3: Handling a ValueError
Write a Python program that asks the user to enter an integer.
Implement exception handling to handle the scenario where the input cannot be converted to an integer (ValueError).
Display an appropriate error message if the input is not a valid integer and ask the user to enter a valid integer.

### Day 16: Working with SQL Databases and Python 
Everything about SQL - SQLite Installation,How to create SQL Tables, and Queries
     * Use SQL to store data and retrieve it later on.
     * Use SQLite to build relational databases on your computer.
     * Perform CRUD operations on relational databases using SQL.

https://datatofish.com/create-database-python-using-sqlite3/ 
https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/
https://www.sqlitetutorial.net/sqlite-python/creating-database/

#### Exercises 
1. In your VSCode or editor of your choice, create an SQLite database with 2 tables, students and teachers with accompanied attributes and perform the following operations: 
     1. Insert data into the tables using SQL 
     2. SELECT data by a particular id eg 'where id=2'
     3. SELECT ALL (*) the table data 
     4. Update a row data 
     5. Delete a particular table row data
     6. Drop a Table


### Day 17: ORM and Python 

Applying the concept of OOP with Python Data
* Create Python objects using SQL database records.
* Create SQL database records using Python objects.
#### Exercise
1. Exercise 1: Create Python objects using SQL database records

      Create a new Python file and import the sqlite3 library.
      Create a connection to the database.
      Create a cursor object.
      Execute a query to get all the records from the users table.
      Create a new Python object for each record in the users table.
      Print the name and email address of each user.

2. Exercise 2: Create SQL database records using Python objects

Create a new Python file and import the sqlite3 library.
Create a connection to the database.
Create a cursor object.
Create a new Python object for a user.
Use the execute() method to insert the user object into the users table.
Commit the changes to the database.


### Day 19: SQLALchemy and Python 
Using ORM and SQL concepts, implement the CRUD operations using SQLAlchemy library 
https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
https://youtu.be/AKQ3XEDI9Mw
https://www.youtube.com/watch?v=dIV8NHzboxU&amp;index=2

#### Exercise
1# Using a use-case of your choice, apply the concepts of ORM and SQLAlchemy to demonstrate these functionalities ~ Create, Read, Update, and Delete with SQLAlchemy.


### Day 20: Working with SQL Relations SQLALCHEMY and Python 
Understand how to implement CRUD operations using Python and SQLAlchemy covering relationships
 1:1 relationships in sqlalchemy (CRUD)  
 1:*  relationships in sqlalchemy (CRUD) 
 *:*  relationships in sqlalchemy (CRUD) 



#### Exercise 

1. One-to-many relationship

In this exercise, we will create a one-to-many relationship between a Customer table and an Order table. The Customer table will have a id column that is the primary key, and the Order table will have a customer_id column that is a foreign key to the Customer table. Once you have the tables created, populate them with data such that using JOINs, you can query the data to see how the relationships work. For example, we can get all of the orders for a particular customer by using the join keyword. 


2. One-to-one relationship between a User table and a Profile table

In this exercise, we will create a one-to-one relationship between a User table and a Profile table. The User table will have a id column that is the primary key, and the Profile table will have a user_id column that is a foreign key to the User table.Once you have created and populated the tables with data, write a query that finds the profile for a particular user by using the join keyword, eg at id 1. 

3.   Many-to-many relationship

In this exercise, we will create a many-to-many relationship between a Book table and an Author table. The Book table will have a id column that is the primary key, and the Author table will have a id column that is the primary key. We will also create a BookAuthor table that will store the relationship between books and authors. Once you have all the 3 tables populated, write a query that gets all of the books that were written by a particular author ege  'J.R.R. Tolkien' by using the join keyword. 


### Day 21: Web Scraping Basics
Introduction to web scraping in Python, using libraries such as BeautifulSoup and requests.

#### Exercise
1. Write a Python program that uses web scraping to extract the title and price of a product from an online shopping website. Print the extracted information.

2. Write a Python program that scrapes the headlines and summaries of the latest news articles from a news website. Print the extracted information.

3. Write a Python program that scrapes the names, prices, and ratings of the top-rated products in a specific category on an e-commerce website. Print the extracted information.


### Day 22: Advanced Web Scraping Techniques
Learn advanced techniques in web scraping, such as handling pagination, handling dynamic content using Selenium, and using proxies and user agents.

#### Exercise
1. Write a Python program that scrapes the names, prices, and ratings of all products in a specific category on an e-commerce website, handling pagination. Print the extracted information.

2. Write a Python program that scrapes the names, prices, and ratings of all products in a specific category on an e-commerce website, handling dynamic content using Selenium. Print the extracted information.

3. Write a Python program that scrapes the names, prices, and ratings of all products in a specific category on an e-commerce website, using proxies and rotating user agents to bypass IP blocking. Print the extracted information.


### Day 23: Data Structures in Python
Learn about different data structures in Python, such as lists, tuples, dictionaries, sets, stacks, queues, and linked lists. Understand their properties, use cases, and operations.

#### Exercise
1. Implement a stack data structure in Python using a list. Include push, pop, and peek operations.

2. Implement a queue data structure in Python using a list. Include enqueue, dequeue, and peek operations.

3. Implement a linked list data structure in Python. Include methods to insert a node, delete a node, and print the linked list.

### Day 24: Python Algorithms: Searching 

In today's lesson, we'll dive into essential algorithms used for sorting and searching data in Python. Understanding these algorithms will empower you to efficiently organize and retrieve data from various data structures.

Topics to be covered:

1. *Introduction to algorithms: Understand the fundamental concepts of algorithms, including time complexity, space complexity, and algorithmic efficiency.
2. *Linear search: Learn about the linear search algorithm and its applications. We'll cover its implementation and analyze its time complexity.
3. *Binary search: Dive into the binary search algorithm, which is significantly faster than linear search for sorted data. We'll explore its implementation and analyze its time complexity.
4. *Optimizing search algorithms: Learn about advanced search algorithms like interpolation search and exponential search, which optimize the searching process for specific scenarios.
#### Exercise
1. Implement a binary search algorithm in Python to search for a specific number in a sorted list.

2. Implement a breadth-first search algorithm in Python to traverse a graph and print its nodes in breadth-first order.

### Day 25: Python Algorithms: Sorting 
1. *Sorting algorithms: Explore various sorting algorithms such as bubble sort, selection sort, insertion sort, merge sort, quicksort, and heapsort. Understand their implementation details, time complexities, and best-case and worst-case scenarios.
2. *Advanced sorting techniques: Discover advanced sorting techniques such as radix sort, bucket sort, and counting sort. Understand their applications and analyze their time complexities.

#### Exercise
1. Implement a bubble sort algorithm in Python to sort a list of numbers in ascending order.

### Day 26: Advanced Python Algorithms
In this lesson, we will explore advanced algorithms and data structures in Python. We will cover the following topics:

*Sorting Algorithms: Dive deeper into sorting algorithms such as QuickSort, MergeSort, and HeapSort. Understand their principles, analyze their time and space complexity, and implement them in Python.

*Graph Algorithms: Learn about graph theory and explore popular graph algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's algorithm, and Bellman-Ford algorithm. Implement these algorithms to solve graph-related problems.

*Dynamic Programming: Understand the concept of dynamic programming and its applications in solving complex problems. Learn how to break down a problem into smaller subproblems and use memoization or bottom-up approaches to optimize computations.

*Tree Algorithms: Explore algorithms related to trees, such as Tree Traversal (pre-order, in-order, post-order), Binary Search Trees (BST), and AVL Trees. Implement these algorithms to perform operations on trees efficiently.

#### Exercise:
Choose one of the advanced algorithms discussed in this lesson and implement it in Python. Test the algorithm with different inputs and analyze its performance. Compare its time and space complexity with other algorithms for the same problem.

### Day 27: Advanced Concepts in Python Libraries
In this lesson, we will explore advanced concepts and features in popular Python libraries. We will cover the following topics:

*NumPy: Dive deeper into the NumPy library and learn advanced techniques for array manipulation, broadcasting, and vectorization. Understand how to optimize code using NumPy's functions and features.

*Pandas: Explore advanced data manipulation techniques in Pandas, such as handling missing data, merging and joining datasets, and pivoting data. Learn how to apply advanced operations to analyze and transform data efficiently.

*Matplotlib: Discover advanced plotting techniques in Matplotlib, including subplots, customizing plot styles, and creating interactive visualizations. Understand how to create complex plots and combine multiple visual elements.

*Scikit-learn: Learn advanced machine learning concepts and techniques using Scikit-learn. Explore feature selection, model evaluation, hyperparameter tuning, and ensemble methods to improve the performance of your machine learning models.

#### Exercise:
1. Choose a dataset of your choice and apply advanced data manipulation, analysis, and visualization techniques using libraries such as Pandas, NumPy, and Matplotlib. Perform exploratory data analysis, apply advanced statistical operations, and create insightful visualizations to gain deeper insights from the data.

### Day 28: Advanced Concepts in Python - Concurrency and Parallelism
Explore concurrency and parallelism in Python. Understand how to write concurrent and parallel programs to improve performance and handle multiple tasks simultaneously.

Topics:

Threads
Thread synchronization
Locks and semaphores
Race conditions
Global Interpreter Lock (GIL)
Processes and multiprocessing
Parallel processing
Asynchronous programming
Exercise:

Write a Python program to download multiple files using multi-threading. 

### Day 29: Python for Machine Learning
Learn about the different types of machine learning algorithms and we can use python programming language to implement it.

#### Exercise
1a. Implement a simple machine learning algorithm, such as a linear regression model or a decision tree.
b.Evaluate the performance of a machine learning model.


### Day 30: Python for Web Development - Flask and Django

Learning Objectives for Python Web Development using Flask and Django:
1. Understand the basics of web development and the role of Python in creating web applications.
2. Learn the fundamentals of Flask and Django frameworks.
3. Build and deploy a simple web application using Flask and Django.
4. Gain familiarity with routing, templates, forms, and database integration in Flask and Django.
5. Explore advanced features such as user authentication, RESTful APIs, and testing in Flask and Django.
6. Understand the differences between Flask and Django and choose the appropriate framework for different projects.

#### Important Learning Resources for Beginners:
##### Flask:
*Official Flask Documentation: The official documentation provides a comprehensive guide to Flask, including installation instructions, tutorials, and examples. (https://flask.palletsprojects.com/)
* Flask Mega-Tutorial by Miguel Grinberg: This online tutorial covers Flask from the basics to more advanced topics, guiding you through the development of a blog application. (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

##### Django:
*Official Django Documentation: The official documentation offers extensive information on Django, including installation instructions, tutorials, and a detailed explanation of its various components. (https://docs.djangoproject.com/)
*Django for Beginners by William S. Vincent: This book is a beginner-friendly guide to Django, covering everything from setting up a project to building a complete web application. (https://djangoforbeginners.com/)

##### Online Courses:
*Udemy: "Python Flask for Beginners" by Jose Salvatierra. This course provides a hands-on approach to learning Flask, covering all the essential concepts and building practical projects. (https://www.udemy.com/course/python-flask-for-beginners/)
*Coursera: "Web Applications for Everybody" by Charles Severance. This specialization offers an introduction to web development using Python and Django, with a focus on database integration and deployment. (https://www.coursera.org/specializations/web-applications)

##### YouTube Tutorials:
*Corey Schafer's Flask Tutorial: This comprehensive video series covers Flask from start to finish, explaining the concepts and demonstrating their implementation through practical examples. (https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
*CodeWithHarry Django Playlist: Harry's Django tutorial series is beginner-friendly and covers various aspects of Django development, including forms, authentication, and deployment. (https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL)



