# Function Arguments

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what function arguments are and how they work
- Differentiate between various types of function arguments
- Use positional, keyword, default, variable-length, and keyword arguments effectively
- Apply advanced argument techniques like unpacking and combining different argument types
- Debug common mistakes related to function arguments
- Follow best practices for writing clean, maintainable functions

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax and data types
- Knowledge of how to define and call functions
- Familiarity with variables and scope
- Experience with basic control structures (if/else, loops)
- Understanding of lists, tuples, and dictionaries

## What is Function Arguments?

Function arguments are values that you pass to a function when you call it. They allow functions to receive input data, making them dynamic and reusable. Think of arguments as the information you give to a function so it can perform its task with specific data.

When you define a function, you specify what arguments it expects. When you call the function, you provide actual values for those arguments. These values are then available inside the function to be used in computations, operations, or other logic.

Arguments make functions flexible because the same function can behave differently based on the input it receives. Without arguments, functions would be limited to working with fixed data, severely limiting their usefulness.

## Why is it Important?

Function arguments are crucial for several reasons:

1. **Reusability**: Functions can be used with different data without rewriting code
2. **Modularity**: Code becomes more organized when functionality is separated into parameterized functions
3. **Maintainability**: Changes to logic only need to happen in one place
4. **Testing**: Functions with arguments are easier to test with different inputs
5. **Flexibility**: The same function can handle various scenarios based on input
6. **Code Clarity**: Arguments make the purpose and dependencies of functions explicit

Understanding function arguments properly is essential for writing professional Python code and is fundamental to all programming paradigms.

## Real World Analogy

Think of function arguments like ingredients in a recipe. A recipe for "bake_cake()" needs specific ingredients to work - flour, eggs, sugar, etc. The recipe itself is the function definition, but without the actual ingredients (arguments), you can't make the cake.

Different ingredients produce different results:
- `bake_cake(flour=2, eggs=3, sugar=1)` makes one type of cake
- `bake_cake(flour=3, eggs=4, sugar=2)` makes a richer cake

The recipe (function) stays the same, but the ingredients (arguments) determine what gets produced. Just like you can't bake a cake without ingredients, you can't execute meaningful functions without arguments (in most cases).

## Theory

Python supports several types of function arguments:

1. **Positional Arguments**: Passed in order based on position in the function definition
2. **Keyword Arguments**: Passed by explicitly naming the parameter
3. **Default Arguments**: Parameters that have predefined values if not provided
4. **Variable-Length Arguments**: Allow functions to accept arbitrary numbers of arguments
   - *args for non-keyword variable arguments
   - **kwargs for keyword variable arguments

Functions can combine these argument types, but they must follow a specific order:
`def function(positional, default=value, *args, **kwargs)`

Python evaluates arguments in this sequence during function calls, which affects how they're processed internally.

## Syntax

```python
# Basic function with positional arguments
def greet(name, message):
    return f"{message}, {name}!"

# Function with default arguments
def greet_default(name, message="Hello"):
    return f"{message}, {name}!"

# Function with variable arguments
def sum_all(*numbers):
    return sum(numbers)

# Function with keyword arguments
def create_profile(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

# Function with both *args and **kwargs
def process_data(required_arg, *args, **kwargs):
    print(f"Required: {required_arg}")
    print(f"Additional args: {args}")
    print(f"Keyword args: {kwargs}")
```

## Flow / Working

When a function is called with arguments, Python follows this process:

1. **Argument Matching**: Python matches provided arguments to function parameters
2. **Positional Processing**: Positional arguments are assigned first, in order
3. **Keyword Assignment**: Keyword arguments are matched by name
4. **Default Values**: Unprovided parameters use their default values
5. **Variable Arguments**: Extra positional arguments go to *args
6. **Keyword Variables**: Extra keyword arguments go to **kwargs
7. **Function Execution**: The function body executes with all arguments in scope
8. **Return Value**: The function returns a value (or None if no return statement)

This flow ensures arguments are processed consistently and predictably, regardless of how they're provided.

## Example 1 (Beginner)

```python
# Simple function with positional arguments
def add_numbers(a, b):
    """Add two numbers together"""
    return a + b

# Calling with positional arguments
result1 = add_numbers(5, 3)
print(f"5 + 3 = {result1}")

# Calling with keyword arguments
result2 = add_numbers(b=7, a=2)
print(f"2 + 7 = {result2}")

# Function with default argument
def greet_person(name, greeting="Hello"):
    """Greet a person with a customizable greeting"""
    return f"{greeting}, {name}!"

print(greet_person("Alice"))
print(greet_person("Bob", "Hi"))
```

## Example 2 (Intermediate)

```python
# Function demonstrating multiple argument types
def student_report(name, grade, *subjects, attendance=100, **details):
    """
    Generate a student report with various information

    Args:
        name (str): Student's name
        grade (int): Current grade level
        *subjects: Variable list of subjects
        attendance (int): Attendance percentage (default 100)
        **details: Additional key-value information
    """
    print(f"Student Report for: {name} (Grade {grade})")
    print(f"Subjects: {', '.join(subjects)}")
    print(f"Attendance: {attendance}%")

    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")

# Using the function with various argument types
student_report(
    "Emma",
    10,
    "Math", "Science", "English",
    attendance=95,
    teacher="Mr. Smith",
    locker_number=24
)
```

## Example 3 (Advanced)

```python
# Advanced example with argument unpacking and complex processing
def advanced_calculator(operation, *numbers, precision=2, **options):
    """
    Perform calculations with advanced options

    Args:
        operation (str): Type of calculation to perform
        *numbers: Numbers to operate on
        precision (int): Decimal places for result
        **options: Additional calculation options
    """
    import math

    # Handle empty numbers
    if not numbers:
        raise ValueError("At least one number required")

    # Perform operation based on string
    if operation == "sum":
        result = sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    elif operation == "power":
        if len(numbers) != 2:
            raise ValueError("Power operation requires exactly 2 numbers")
        result = numbers[0] ** numbers[1]
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # Apply rounding based on precision
    result = round(result, precision)

    # Apply additional options
    if options.get('absolute'):
        result = abs(result)

    if options.get('square_root') and result >= 0:
        result = round(math.sqrt(result), precision)

    return result

# Examples of usage
print(advanced_calculator("sum", 1, 2, 3, 4, 5))
print(advanced_calculator("product", 2, 3, 4, precision=3))
print(advanced_calculator("average", 10, 20, 30, absolute=True))
print(advanced_calculator("power", 2, 8, square_root=True))

# Using argument unpacking
number_list = [1, 2, 3, 4, 5]
print(advanced_calculator("sum", *number_list, precision=1))
```

## Output

```
5 + 3 = 8
2 + 7 = 9
Hello, Alice!
Hi, Bob!
Student Report for: Emma (Grade 10)
Subjects: Math, Science, English
Attendance: 95%
Additional Details:
  teacher: Mr. Smith
  locker_number: 24
15
24
30.0
16.0
15.0
```

## Common Mistakes

1. **Incorrect Argument Order**: Placing keyword arguments before positional ones
   ```python
   # Wrong
   def func(a, b=10, c):
       pass

   # Correct
   def func(a, c, b=10):
       pass
   ```

2. **Mutable Default Arguments**: Using lists or dicts as defaults
   ```python
   # Wrong - shared between calls
   def func(items=[]):
       items.append(1)
       return items

   # Correct
   def func(items=None):
       if items is None:
           items = []
       items.append(1)
       return items
   ```

3. **Missing Required Arguments**: Forgetting to provide required positional args
   ```python
   def func(a, b):
       return a + b

   # This will raise TypeError
   # func(5)  # Missing argument b
   ```

4. **Too Many Arguments**: Passing more positional args than expected
   ```python
   def func(a, b):
       return a + b

   # This will raise TypeError
   # func(1, 2, 3)  # Too many arguments
   ```

## Best Practices

1. **Use Descriptive Parameter Names**: Make function signatures self-documenting
   ```python
   # Good
   def calculate_area(length, width):
       return length * width

   # Avoid
   def calc_area(l, w):
       return l * w
   ```

2. **Limit Number of Parameters**: Functions should ideally have fewer than 5 parameters
   ```python
   # Consider refactoring if you have too many
   def process_user(name, age, email, phone, address, city, state, zip_code):
       # Maybe group related data into objects
       pass
   ```

3. **Use Default Values Wisely**: Only use immutable defaults
   ```python
   def log_message(message, timestamp=None):
       if timestamp is None:
           import datetime
           timestamp = datetime.datetime.now()
       print(f"[{timestamp}] {message}")
   ```

4. **Document Arguments**: Use docstrings to explain parameter purposes
   ```python
   def transfer_funds(from_account, to_account, amount, currency="USD"):
       """
       Transfer funds between accounts

       Args:
           from_account (str): Source account identifier
           to_account (str): Destination account identifier
           amount (float): Amount to transfer
           currency (str): Currency code (default: USD)
       """
       pass
   ```

## Pro Tips

1. **Argument Unpacking**: Use * and ** to unpack sequences and dictionaries
   ```python
   def greet(first, last):
       return f"Hello, {first} {last}!"

   name_parts = ["John", "Doe"]
   print(greet(*name_parts))  # Unpacks list as arguments

   person = {"first": "Jane", "last": "Smith"}
   print(greet(**person))  # Unpacks dict as keyword arguments
   ```

2. **Enforce Keyword-Only Arguments**: Use * to force certain arguments to be keyword-only
   ```python
   def create_connection(host, port, *, timeout=30, retries=3):
       # host and port can be positional or keyword
       # timeout and retries must be keyword arguments
       pass

   # Valid calls
   create_connection("localhost", 8080, timeout=60)
   create_connection("localhost", 8080, timeout=60, retries=5)

   # Invalid - would raise TypeError
   # create_connection("localhost", 8080, 60, 5)
   ```

3. **Use functools.partial for Partial Application**:
   ```python
   from functools import partial

   def multiply(x, y, z):
       return x * y * z

   # Create specialized versions
   double = partial(multiply, 2, 1)  # Always multiplies by 2
   triple = partial(multiply, 3, 1)  # Always multiplies by 3

   print(double(5))  # 10
   print(triple(4))  # 12
   ```

## Interview Questions (10)

1. What is the difference between *args and **kwargs in Python?
2. Explain the order of arguments in a Python function signature.
3. How do default arguments work and what are common pitfalls?
4. What happens when you use mutable objects as default arguments?
5. How can you enforce that certain arguments must be passed as keywords?
6. Explain argument unpacking with examples of * and ** operators.
7. What is the difference between positional and keyword arguments?
8. How does Python handle function arguments internally?
9. Can you have both *args and **kwargs in the same function? If so, how?
10. What are some best practices for designing function interfaces with arguments?

## MCQs (10)

1. What will be the output of: `def func(a, b=2): return a+b; print(func(3))`
   a) 3
   b) 5
   c) Error
   d) 2

2. Which is the correct order of arguments in Python function definition?
   a) *args, positional, default, **kwargs
   b) positional, default, *args, **kwargs
   c) default, positional, *args, **kwargs
   d) **kwargs, *args, positional, default

3. What does *args allow a function to do?
   a) Accept keyword arguments only
   b) Accept any number of positional arguments
   c) Accept default arguments
   d) Accept no arguments

4. How do you pass a dictionary as keyword arguments to a function?
   a) Using *
   b) Using **
   c) Directly passing the dictionary
   d) Using ***

5. What happens with mutable default arguments?
   a) New object created each time
   b) Same object reused across calls
   c) Error occurs
   d) Function fails to execute

6. In `def func(a, *, b=10):`, what does * indicate?
   a) Variable arguments
   b) End of arguments
   c) Keyword-only arguments follow
   d) No arguments allowed

7. Which will cause an error?
   a) def func(a=5, b): pass
   b) def func(a, b=5): pass
   c) def func(*args): pass
   d) def func(**kwargs): pass

8. What is the result of: `def f(x, y=1, *args): return len(args); f(1, 2, 3, 4)`
   a) 1
   b) 2
   c) 3
   d) 4

9. How do you unpack a list to pass as separate arguments?
   a) list[]
   b) *list
   c) **list
   d) &list

10. What does **kwargs collect?
    a) Positional arguments
    b) Keyword arguments
    c) Default arguments
    d) All arguments

## Practice Questions (10)

1. Write a function that accepts any number of integers and returns their average.
2. Create a function that takes a person's details (name, age, city) with city having a default value.
3. Implement a calculator function that can perform addition, subtraction, multiplication, and division using *args.
4. Write a function that accepts a dictionary of student grades and calculates the average grade.
5. Create a function that formats a person's full name with optional title and suffix parameters.
6. Design a function that can merge multiple dictionaries passed as arguments.
7. Write a function that validates user input with required and optional parameters.
8. Implement a logging function that accepts a message and optional timestamp and level parameters.
9. Create a function that generates HTML tags with content and optional attributes.
10. Design a configuration function that accepts base settings and override settings via **kwargs.

## Coding Exercises (5)

1. **Temperature Converter**: Create a function that converts temperatures between Celsius, Fahrenheit, and Kelvin. Accept the temperature value, source unit, target unit, and optional precision parameter.

2. **Shopping Cart Calculator**: Implement a function that calculates total cost including tax and discounts. Accept item prices as *args, tax rate as a keyword argument with default 0.08, and discount as optional keyword argument.

3. **Data Validator**: Write a function that validates different types of data (email, phone, age) based on validation rules passed as **kwargs. Accept the data value and validation type as required arguments.

4. **Report Generator**: Create a function that generates formatted reports. Accept report title, data items as *args, formatting options as keyword arguments (header_style, footer_text, page_size), and additional metadata as **kwargs.

5. **Configuration Manager**: Implement a function that merges configuration settings from multiple sources. Accept base_config as first argument, override_configs as *args, and environment-specific overrides as **kwargs.

## Mini Project

**Personal Finance Tracker**

Create a comprehensive personal finance tracking system with the following functions:

1. `add_transaction(amount, category, date=None, *, description="", tags=None, **metadata)` - Add financial transactions with flexible metadata
2. `generate_report(month, year, *categories, include_totals=True, format="text")` - Generate monthly spending reports
3. `set_budget(category, limit, period="monthly", **notifications)` - Set spending budgets with notification preferences
4. `analyze_spending(*accounts, start_date=None, end_date=None, breakdown="category")` - Analyze spending patterns across accounts
5. `export_data(format, *data_sources, compress=False, **export_options)` - Export financial data in various formats

The system should demonstrate advanced argument handling including default values, variable arguments, keyword-only arguments, and **kwargs for extensibility.

## Assignment

Create a library management system with the following requirements:

1. Implement a `register_member` function that accepts member details with appropriate defaults
2. Create a `checkout_book` function that handles book lending with due dates and renewal options
3. Design a `search_catalog` function that searches books by multiple criteria using *args and **kwargs
4. Build a `generate_statistics` function that produces library usage reports with customizable parameters
5. Develop a `manage_reservations` function that handles book reservations with priority and notification systems

Your implementation should showcase proper use of all argument types learned in this lesson, include comprehensive error handling, and follow best practices for function design.

## Summary

Function arguments are essential components that make Python functions powerful and flexible. We've explored:

- Basic positional and keyword arguments for simple function calls
- Default arguments for providing sensible fallbacks
- Variable-length arguments (*args and **kwargs) for handling arbitrary inputs
- Advanced techniques like argument unpacking and keyword-only parameters
- Best practices for designing clean, maintainable function interfaces

Understanding these concepts enables you to write more robust, reusable Python code and tackle complex programming challenges with confidence.

## Key Takeaways

1. Function arguments enable functions to be dynamic and reusable with different inputs
2. Python supports multiple argument types: positional, keyword, default, and variable-length
3. Arguments must follow a specific order in function definitions: positional, default, *args, **kwargs
4. Default arguments should use immutable values to avoid unexpected behavior
5. *args collects extra positional arguments into a tuple
6. **kwargs collects extra keyword arguments into a dictionary
7. Argument unpacking with * and ** provides flexibility in function calls
8. Proper argument design leads to cleaner, more maintainable code
9. Advanced features like keyword-only arguments enhance API design
10. Following best practices prevents common pitfalls and improves code quality

## Next Topic Preview

In the next lesson, we'll explore **Lambda Functions and Functional Programming** in Python. We'll cover anonymous functions, higher-order functions, map/filter/reduce operations, and how to apply functional programming concepts to solve problems elegantly. This builds directly on our understanding of function arguments by showing how functions can be treated as first-class objects in Python.
