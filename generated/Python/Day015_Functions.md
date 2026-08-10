# Functions

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what functions are and why they're essential in programming
- Create and call functions with different parameters and return types
- Work with default parameters, variable arguments, and keyword arguments
- Apply function best practices and avoid common mistakes
- Use functions effectively in real-world programming scenarios
- Prepare for technical interviews involving functions

## Prerequisites

Before starting this lesson, you should have a solid understanding of:
- Basic Python syntax and data types
- Variables and operators
- Control flow statements (if-else, loops)
- Basic understanding of data structures (lists, dictionaries)

## What is Functions?

A function is a reusable block of code that performs a specific task. It's like a mini-program within your program that can be called multiple times with different inputs to produce outputs. Functions help organize code, reduce repetition, and make programs more modular and maintainable.

Think of a function as a machine that takes inputs (called parameters), processes them according to a set of instructions, and produces outputs (called return values). Once defined, you can use this machine as many times as needed throughout your program.

## Why is it Important?

Functions are fundamental to good programming for several reasons:

1. **Code Reusability**: Write once, use multiple times
2. **Modularity**: Break complex problems into smaller, manageable pieces
3. **Maintainability**: Changes only need to be made in one place
4. **Readability**: Makes code easier to understand and follow
5. **Testing**: Easier to test individual components
6. **Collaboration**: Team members can work on different functions independently

Functions also enable the DRY (Don't Repeat Yourself) principle, which is a cornerstone of clean, efficient code.

## Real World Analogy

Think of a function like a coffee machine in an office. The machine (function) takes inputs (water, coffee beans, milk), follows a specific process (heating, grinding, brewing), and produces an output (a cup of coffee).

Anyone in the office can use the machine by providing the required inputs, and they'll get the same quality coffee each time. If the machine needs maintenance, only the machine itself needs to be fixed, not every person's coffee-making process.

Similarly, a function takes inputs (parameters), processes them according to its instructions, and produces outputs. Multiple parts of your program can "use" the function, and if you need to change how it works, you only modify the function itself.

## Theory

Functions in Python are first-class objects, meaning they can be assigned to variables, passed as arguments to other functions, and returned as values from functions. This makes Python functions very powerful and flexible.

A function consists of:
- **Function Definition**: The code that specifies what the function does
- **Parameters**: Variables that receive values when the function is called
- **Function Body**: The statements that define what the function does
- **Return Statement**: Specifies what value the function should output
- **Function Call**: The act of executing the function with specific arguments

Functions can have:
- No parameters or multiple parameters
- Default parameter values
- Variable number of arguments
- Keyword arguments
- Return single values or multiple values

## Syntax

```python
# Basic function syntax
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional

# Function with no parameters
def greet():
    return "Hello, World!"

# Function with parameters
def add_numbers(a, b):
    return a + b

# Function with default parameters
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function with variable arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def create_profile(**kwargs):
    return kwargs

# Function with return statement
def multiply(x, y):
    result = x * y
    return result
```

## Flow / Working

1. **Function Definition**: Python reads and stores the function definition in memory
2. **Function Call**: When the function is called, Python jumps to the function definition
3. **Parameter Assignment**: Arguments from the call are assigned to parameters
4. **Execution**: The function body executes line by line
5. **Return**: The function returns a value (or None if no return statement)
6. **Resume**: Execution continues from where the function was called

## Example 1 (Beginner)

```python
# Simple function to calculate area of a rectangle
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

# Function to greet a user
def greet_user(name):
    """Greet a user by name"""
    greeting = f"Hello, {name}! Welcome to our program."
    return greeting

# Function with no return value
def print_welcome():
    """Print a welcome message"""
    print("Welcome to our program!")
    print("We're glad you're here!")

# Using the functions
print_welcome()
print(greet_user("Alice"))
area = calculate_area(5, 3)
print(f"The area is: {area}")
```

## Example 2 (Intermediate)

```python
# Function with default parameters
def create_user_profile(name, age=18, city="Unknown", active=True):
    """Create a user profile with default values"""
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }
    return profile

# Function with variable arguments
def calculate_statistics(*numbers):
    """Calculate statistics for a variable number of numbers"""
    if not numbers:
        return {"count": 0, "sum": 0, "average": 0}

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return {
        "count": count,
        "sum": total,
        "average": average,
        "min": min(numbers),
        "max": max(numbers)
    }

# Function with keyword arguments
def format_message(template, **values):
    """Format a message template with provided values"""
    try:
        return template.format(**values)
    except KeyError as e:
        return f"Missing value for placeholder: {e}"

# Function that returns multiple values
def divide_with_remainder(dividend, divisor):
    """Divide two numbers and return quotient and remainder"""
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Using the functions
user1 = create_user_profile("John")
user2 = create_user_profile("Jane", 25, "New York", False)

print("User Profiles:")
print(user1)
print(user2)

stats = calculate_statistics(10, 20, 30, 40, 50)
print("\nStatistics:")
for key, value in stats.items():
    print(f"{key}: {value}")

message = format_message(
    "Hello {name}, you are {age} years old and live in {city}.",
    name="Alice",
    age=30,
    city="Paris"
)
print(f"\nFormatted message: {message}")

quotient, remainder = divide_with_remainder(17, 5)
print(f"\n17 divided by 5: quotient={quotient}, remainder={remainder}")
```

## Example 3 (Advanced)

```python
# Higher-order function: function that takes another function as argument
def apply_operation(numbers, operation):
    """Apply an operation to each number in a list"""
    return [operation(num) for num in numbers]

# Function that returns another function
def create_multiplier(factor):
    """Create a function that multiplies by a given factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Decorator function
def log_function_calls(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Recursive function
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Function with type hints (Python 3.5+)
def process_data(data: list, threshold: int = 10) -> dict:
    """Process a list of numbers and return statistics"""
    filtered_data = [x for x in data if x >= threshold]
    return {
        "original_count": len(data),
        "filtered_count": len(filtered_data),
        "filtered_sum": sum(filtered_data),
        "filtered_average": sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }

# Using the advanced functions
numbers = [1, 2, 3, 4, 5]

# Using higher-order function
squared = apply_operation(numbers, lambda x: x**2)
doubled = apply_operation(numbers, lambda x: x*2)
print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

# Using function that returns another function
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"\nDouble of 5: {double(5)}")
print(f"Triple of 4: {triple(4)}")

# Using decorator
@log_function_calls
def add(a, b):
    return a + b

result = add(3, 5)

# Using recursive function
print(f"\nFibonacci sequence (first 10 numbers):")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Using function with type hints
data = [5, 12, 8, 15, 3, 20, 7, 25]
stats = process_data(data, threshold=10)
print(f"\nData processing results:")
for key, value in stats.items():
    print(f"{key}: {value}")
```

## Output

```
Welcome to our program!
We're glad you're here!
Hello, Alice! Welcome to our program.
The area is: 15

User Profiles:
{'name': 'John', 'age': 18, 'city': 'Unknown', 'active': True}
{'name': 'Jane', 'age': 25, 'city': 'New York', 'active': False}

Statistics:
count: 5
sum: 150
average: 30.0
min: 10
max: 50

Formatted message: Hello Alice, you are 30 years old and live in Paris.

17 divided by 5: quotient=3, remainder=2

Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]
Doubled: [2, 4, 6, 8, 10]

Double of 5: 10
Triple of 4: 12

Calling add with args=(3, 5), kwargs={}
add returned: 8

Fibonacci sequence (first 10 numbers):
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34

Data processing results:
original_count: 8
filtered_count: 4
filtered_sum: 72
filtered_average: 18.0
```

## Common Mistakes

1. **Forgetting the colon after function definition**:
   ```python
   # Wrong
   def my_function()
       pass

   # Correct
   def my_function():
       pass
   ```

2. **Incorrect indentation**:
   ```python
   # Wrong
   def my_function():
   result = "Hello"  # Not indented
       return result

   # Correct
   def my_function():
       result = "Hello"
       return result
   ```

3. **Modifying mutable default arguments**:
   ```python
   # Wrong - dangerous!
   def add_item(item, target_list=[]):
       target_list.append(item)
       return target_list

   # Correct
   def add_item(item, target_list=None):
       if target_list is None:
           target_list = []
       target_list.append(item)
       return target_list
   ```

4. **Returning inside loops unnecessarily**:
   ```python
   # Wrong - exits after first iteration
   def find_even(numbers):
       for num in numbers:
           if num % 2 == 0:
               return num  # Only returns first even number

   # Correct if you want all even numbers
   def find_even(numbers):
       evens = []
       for num in numbers:
           if num % 2 == 0:
               evens.append(num)
       return evens
   ```

5. **Not handling function return values**:
   ```python
   # Wrong - ignoring return value
   def calculate_sum(a, b):
       return a + b

   calculate_sum(5, 3)  # Result is lost

   # Correct
   result = calculate_sum(5, 3)
   print(result)
   ```

## Best Practices

1. **Use descriptive function names**: Choose names that clearly describe what the function does
2. **Keep functions focused**: Each function should have a single, well-defined purpose
3. **Use docstrings**: Document your functions with clear explanations of parameters and return values
4. **Limit function length**: Aim for functions that fit on one screen
5. **Use type hints**: In Python 3.5+, use type hints for better code documentation and IDE support
6. **Handle errors gracefully**: Use try/except blocks when appropriate
7. **Avoid global variables**: Pass needed data as parameters instead
8. **Return early**: Use early returns to avoid deep nesting
9. **Use default arguments wisely**: Be careful with mutable default arguments
10. **Test your functions**: Write tests to ensure functions work as expected

## Pro Tips

1. **Use *args and **kwargs for flexible function signatures**:
   ```python
   def flexible_function(required_param, *args, **kwargs):
       print(f"Required: {required_param}")
       print(f"Extra args: {args}")
       print(f"Keyword args: {kwargs}")
   ```

2. **Leverage lambda functions for simple operations**:
   ```python
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x**2, numbers))
   ```

3. **Use function annotations for better documentation**:
   ```python
   def greet(name: str, age: int) -> str:
       return f"Hello {name}, you are {age} years old"
   ```

4. **Create function factories**:
   ```python
   def make_multiplier(n):
       return lambda x: x * n

   double = make_multiplier(2)
   triple = make_multiplier(3)
   ```

5. **Use decorators for cross-cutting concerns**:
   ```python
   def timer(func):
       import time
       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           end = time.time()
           print(f"{func.__name__} took {end - start:.4f} seconds")
           return result
       return wrapper
   ```

6. **Unpack return values for multiple returns**:
   ```python
   def get_name_age():
       return "Alice", 30

   name, age = get_name_age()  # Unpacking
   ```

## Interview Questions (10)

1. What is the difference between a parameter and an argument?
2. Explain the concept of function scope in Python.
3. What are lambda functions and when would you use them?
4. How do you handle variable numbers of arguments in a function?
5. What is a decorator and how does it work?
6. Explain the difference between *args and **kwargs.
7. What is the purpose of the return statement in a function?
8. How do default parameter values work in Python?
9. What are first-class functions and how does Python support them?
10. Explain recursion and provide an example of when it's useful.

## MCQs (10)

1. What keyword is used to define a function in Python?
   a) function
   b) def
   c) func
   d) define

2. What does a function return if no return statement is used?
   a) 0
   b) None
   c) False
   d) Empty string

3. How do you define a function with default parameter values?
   a) def func(param=default)
   b) def func(param:default)
   c) def func(default=param)
   d) def func(param=default_value)

4. What is the output of: `def f(x, y=2): return x+y; print(f(3))`?
   a) 3
   b) 5
   c) 2
   d) Error

5. Which of the following is used to pass variable number of arguments?
   a) *args
   b) **args
   c) &args
   d) %args

6. What does **kwargs represent in a function definition?
   a) List of arguments
   b) Dictionary of keyword arguments
   c) Tuple of arguments
   d) Set of arguments

7. In Python, functions are:
   a) First-class objects
   b) Second-class objects
   c) Not objects
   d) Static objects

8. What is the purpose of a docstring in a function?
   a) To comment code
   b) To provide function documentation
   c) To define variables
   d) To import modules

9. How do you unpack a function that returns multiple values?
   a) a, b = func()
   b) (a, b) = func()
   c) a = func()[0], b = func()[1]
   d) Both a and b

10. What is a lambda function?
    a) A function with no name
    b) A function defined with lambda keyword
    c) An anonymous function
    d) All of the above

## Practice Questions (10)

1. Write a function that takes a list of numbers and returns the sum of even numbers.
2. Create a function that checks if a string is a palindrome.
3. Write a function that calculates the factorial of a number using recursion.
4. Create a function that takes two lists and returns a dictionary with keys from the first list and values from the second.
5. Write a function that removes duplicates from a list while preserving order.
6. Create a function that finds the second largest number in a list.
7. Write a function that converts temperature between Celsius and Fahrenheit.
8. Create a function that generates a Fibonacci sequence up to n terms.
9. Write a function that validates an email address format.
10. Create a function that flattens a nested list of arbitrary depth.

## Coding Exercises (5)

1. **Temperature Converter**: Create a function that converts between Celsius, Fahrenheit, and Kelvin with appropriate error handling.

2. **Text Analyzer**: Write a function that takes a string and returns statistics including word count, character count, most frequent word, and average word length.

3. **Bank Account System**: Create functions for deposit, withdraw, and check balance operations with proper validation and error handling.

4. **Data Filter**: Write a function that filters a list of dictionaries based on multiple criteria provided as keyword arguments.

5. **File Processor**: Create a function that reads a text file, processes its content (counts words, lines, characters), and writes statistics to another file.

## Mini Project

**Contact Management System**

Create a comprehensive contact management system using functions:

```python
def add_contact(contacts, name, phone, email):
    """Add a new contact to the system"""
    if name in contacts:
        return f"Contact {name} already exists"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "created": __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return f"Contact {name} added successfully"

def search_contact(contacts, name):
    """Search for a contact by name"""
    return contacts.get(name, f"Contact {name} not found")

def update_contact(contacts, name, **updates):
    """Update contact information"""
    if name not in contacts:
        return f"Contact {name} not found"

    contacts[name].update(updates)
    return f"Contact {name} updated successfully"

def delete_contact(contacts, name):
    """Delete a contact"""
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted successfully"
    return f"Contact {name} not found"

def list_contacts(contacts):
    """List all contacts"""
    if not contacts:
        return "No contacts found"

    result = "Contact List:\n"
    for name, info in contacts.items():
        result += f"Name: {name}\n"
        result += f"  Phone: {info['phone']}\n"
        result += f"  Email: {info['email']}\n"
        result += f"  Added: {info['created']}\n\n"
    return result

def find_contacts_by_email_domain(contacts, domain):
    """Find contacts by email domain"""
    matches = {}
    for name, info in contacts.items():
        if info['email'].endswith(domain):
            matches[name] = info
    return matches

# Main program
def main():
    contacts = {}

    # Add some contacts
    print(add_contact(contacts, "Alice Johnson", "555-1234", "alice@email.com"))
    print(add_contact(contacts, "Bob Smith", "555-5678", "bob@gmail.com"))
    print(add_contact(contacts, "Carol Davis", "555-9012", "carol@email.com"))

    # Search for a contact
    print("\nSearching for Alice:")
    print(search_contact(contacts, "Alice Johnson"))

    # Update a contact
    print("\nUpdating Bob's phone:")
    print(update_contact(contacts, "Bob Smith", phone="555-9999"))

    # List all contacts
    print("\nAll contacts:")
    print(list_contacts(contacts))

    # Find contacts by email domain
    print("\nContacts with email.com domain:")
    email_contacts = find_contacts_by_email_domain(contacts, "email.com")
    for name, info in email_contacts.items():
        print(f"  {name}: {info['email']}")

if __name__ == "__main__":
    main()
```

## Assignment

Create a complete grade management system with the following requirements:

1. Create functions to add students with their grades
2. Implement functions to calculate average grades for individual students and the entire class
3. Write functions to find the highest and lowest grades
4. Create a function to generate grade reports with letter grades (A-F)
5. Implement a function to save/load data from a file
6. Add error handling for invalid inputs
7. Include a function to display statistics (grade distribution, etc.)
8. Provide a menu-driven interface for user interaction

Your solution should demonstrate:
- Function design and organization
- Proper error handling
- Use of appropriate data structures
- File I/O operations
- User-friendly interface

## Summary

Functions are essential building blocks in Python programming that allow you to create reusable, organized, and maintainable code. In this lesson, we covered:

- Basic function syntax and structure
- Parameters and return values
- Default parameters and variable arguments
- Advanced concepts like higher-order functions and decorators
- Best practices for writing effective functions
- Common mistakes to avoid

Functions help you follow the DRY principle, make your code more readable, and enable better collaboration in team environments. Mastering functions is crucial for writing professional Python code.

## Key Takeaways

1. Functions are reusable blocks of code that perform specific tasks
2. They help organize code, reduce repetition, and improve maintainability
3. Functions can have parameters, default values, and variable arguments
4. Python supports advanced features like higher-order functions and decorators
5. Proper function design follows principles like single responsibility and clear naming
6. Always handle errors appropriately and document your functions well
7. Functions are first-class objects in Python, enabling powerful programming patterns

## Next Topic Preview

In the next lesson, we'll explore **Object-Oriented Programming (OOP) in Python**. We'll learn about classes, objects, inheritance, encapsulation, and polymorphism - fundamental concepts that will take your Python programming to the next level. We'll see how OOP builds upon what we've learned about functions to create even more powerful and organized code structures.
