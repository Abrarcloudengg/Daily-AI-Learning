# Keyword Arguments

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what keyword arguments are in Python
- Differentiate between positional and keyword arguments
- Use keyword arguments effectively in function calls
- Apply advanced keyword argument techniques including **kwargs
- Avoid common mistakes with keyword arguments
- Implement best practices for function design using keyword arguments

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python functions
- Knowledge of function parameters and arguments
- Experience with basic function calls
- Understanding of variable scope in Python

## What is Keyword Arguments?

Keyword arguments are a way to pass arguments to a function by explicitly specifying the parameter name along with its value. Unlike positional arguments where the order matters, keyword arguments allow you to specify arguments in any order by using the parameter name as a "key" to identify which value goes where.

When you use keyword arguments, Python matches each argument with its corresponding parameter by name rather than by position. This makes function calls more readable and flexible, especially when dealing with functions that have multiple parameters.

## Why is it Important?

Keyword arguments are important for several reasons:

1. **Readability**: They make function calls self-documenting by showing exactly which parameter each value corresponds to
2. **Flexibility**: You can specify arguments in any order, making it easier to skip optional parameters
3. **Maintainability**: Code becomes easier to understand and modify as requirements change
4. **Default Values**: They work seamlessly with default parameter values, allowing you to override only specific parameters
5. **Function Evolution**: As functions grow and parameters are added or reordered, keyword arguments reduce breaking changes

## Real World Analogy

Think of keyword arguments like filling out a form. When you fill out a form, you don't rely on the position of the fields - you look for the label (like "Name:", "Email:", "Phone:") and fill in the appropriate information under that label.

Similarly, when you use keyword arguments in Python, you're explicitly labeling each piece of information you're providing to a function, making it clear what each value represents regardless of order.

## Theory

In Python, when you define a function, you specify parameters. When you call that function, you provide arguments. Arguments can be passed in two ways:

1. **Positional Arguments**: Matched to parameters based on their position in the function call
2. **Keyword Arguments**: Matched to parameters based on their name

Keyword arguments follow the syntax `parameter_name=value`. Python allows mixing positional and keyword arguments, but positional arguments must come before keyword arguments.

Python also supports:
- Default parameter values
- Variable-length argument lists (*args)
- Variable-length keyword argument dictionaries (**kwargs)

## Syntax

The basic syntax for keyword arguments is:

```python
function_name(parameter1=value1, parameter2=value2, ...)
```

For function definitions with default values:

```python
def function_name(param1, param2=default_value, param3=default_value):
    # function body
```

For accepting variable keyword arguments:

```python
def function_name(**kwargs):
    # kwargs is a dictionary of keyword arguments
```

## Flow / Working

1. Function is called with keyword arguments
2. Python matches each keyword argument to its corresponding parameter by name
3. If a parameter doesn't receive a value, Python uses the default value (if provided)
4. If no default value exists and no argument is provided, Python raises a TypeError
5. Function executes with the provided or default values
6. Return value is passed back to the caller

## Example 1 (Beginner)

```python
def greet_person(name, greeting, punctuation):
    return f"{greeting}, {name}{punctuation}"

# Using positional arguments
print(greet_person("Alice", "Hello", "!"))

# Using keyword arguments
print(greet_person(name="Bob", greeting="Hi", punctuation="."))

# Using keyword arguments in different order
print(greet_person(punctuation="?", greeting="Howdy", name="Charlie"))

# Mixing positional and keyword arguments
print(greet_person("David", punctuation="!", greeting="Hey"))
```

## Example 2 (Intermediate)

```python
def create_profile(name, age=25, city="Unknown", occupation="Student"):
    return f"Name: {name}, Age: {age}, City: {city}, Occupation: {occupation}"

# Using only required argument
print(create_profile("Emma"))

# Overriding some defaults
print(create_profile("Frank", age=30, city="New York"))

# Overriding different defaults
print(create_profile("Grace", occupation="Engineer", city="San Francisco"))

# Using all keyword arguments
print(create_profile(name="Henry", age=35, city="Boston", occupation="Doctor"))

# Mixing positional with keyword
print(create_profile("Ivy", 28, occupation="Designer"))
```

## Example 3 (Advanced)

```python
def flexible_function(required_arg, *args, default_arg="default", **kwargs):
    print(f"Required argument: {required_arg}")
    print(f"Additional positional args: {args}")
    print(f"Default argument: {default_arg}")
    print(f"Keyword arguments: {kwargs}")

    # Process kwargs
    for key, value in kwargs.items():
        print(f"Processing {key}: {value}")

# Function call with various argument types
flexible_function(
    "main_value",           # required_arg
    "extra1", "extra2",     # *args
    default_arg="custom",   # keyword argument
    name="John",            # **kwargs
    age=30,                 # **kwargs
    country="USA"           # **kwargs
)
```

## Output

```
Hello, Alice!
Hi, Bob.
Howdy, Charlie?
Hey, David!

Name: Emma, Age: 25, City: Unknown, Occupation: Student
Name: Frank, Age: 30, City: New York, Occupation: Student
Name: Grace, Age: 25, City: San Francisco, Occupation: Engineer
Name: Henry, Age: 35, City: Boston, Occupation: Doctor
Name: Ivy, Age: 28, City: Unknown, Occupation: Designer

Required argument: main_value
Additional positional args: ('extra1', 'extra2')
Default argument: custom
Keyword arguments: {'name': 'John', 'age': 30, 'country': 'USA'}
Processing name: John
Processing age: 30
Processing country: USA
```

## Common Mistakes

1. **Mixing positional arguments after keyword arguments**:
   ```python
   # Wrong
   greet_person(name="Alice", "Hello")  # SyntaxError
   ```

2. **Providing duplicate arguments**:
   ```python
   # Wrong
   greet_person("Alice", name="Bob")  # TypeError
   ```

3. **Misspelling parameter names**:
   ```python
   # Wrong
   greet_person(nmae="Alice")  # TypeError
   ```

4. **Forgetting that keyword arguments must come after positional arguments**:
   ```python
   # Wrong
   greet_person(greeting="Hi", "Alice")  # SyntaxError
   ```

5. **Using reserved words as parameter names without attention**:
   ```python
   def func(class, def):  # These are Python keywords
       pass
   ```

## Best Practices

1. **Use descriptive parameter names** that make keyword arguments self-explanatory
2. **Place required parameters before optional ones** in function definitions
3. **Use default values for optional parameters** to make functions more flexible
4. **Be consistent with parameter ordering** across related functions
5. **Document your functions** clearly, especially when using keyword arguments
6. **Consider using keyword-only arguments** (Python 3+) for critical parameters
7. **Avoid changing parameter order** in public APIs as it breaks existing code
8. **Use **kwargs judiciously** - only when you truly need variable keyword arguments

## Pro Tips

1. **Keyword-only arguments** (Python 3+):
   ```python
   def secure_function(arg1, *, arg2, arg3):
       # arg2 and arg3 must be passed as keywords
       pass
   ```

2. **Unpacking dictionaries as keyword arguments**:
   ```python
   params = {"name": "Alice", "age": 30}
   create_profile(**params)  # Equivalent to create_profile(name="Alice", age=30)
   ```

3. **Combining args and kwargs**:
   ```python
   def wrapper_function(*args, **kwargs):
       # Can accept any combination of arguments
       return original_function(*args, **kwargs)
   ```

4. **Preserving function signatures**:
   ```python
   def decorator(func):
       def wrapper(*args, **kwargs):
           # Do something
           return func(*args, **kwargs)
       return wrapper
   ```

## Interview Questions (10)

1. What is the difference between positional and keyword arguments in Python?
2. Can you mix positional and keyword arguments in a function call? If so, what are the rules?
3. How do default parameter values work with keyword arguments?
4. What is the purpose of **kwargs in function definitions?
5. Explain what happens when you pass a keyword argument that doesn't match any parameter.
6. How can you enforce that certain arguments must be passed as keywords?
7. What are some advantages of using keyword arguments over positional arguments?
8. How do you unpack a dictionary as keyword arguments when calling a function?
9. What happens if you provide both a positional and keyword argument for the same parameter?
10. When would you use keyword-only arguments in your function design?

## MCQs (10)

1. **What is the correct syntax for a keyword argument?**
   a) `function(value)`
   b) `function(parameter=value)`
   c) `function(value:parameter)`
   d) `function(value->parameter)`

2. **Which of the following is NOT true about keyword arguments?**
   a) They must come after positional arguments
   b) They can be specified in any order
   c) They must always be used
   d) They make code more readable

3. **What happens with this code: `func(a=1, b=2, a=3)`?**
   a) It works fine
   b) It raises SyntaxError
   c) It uses the last value (3)
   d) It uses the first value (1)

4. **In `def func(a, b=10)`, what is `b` called?**
   a) Keyword argument
   b) Positional argument
   c) Default parameter
   d) Required parameter

5. **What does **kwargs represent in a function definition?**
   a) A tuple of extra arguments
   b) A dictionary of keyword arguments
   c) A list of positional arguments
   d) A set of unique arguments

6. **Which is correct Python syntax?**
   a) `func(a=1, 2)`
   b) `func(1, a=2)`
   c) `func(1, 2, a=3, 1)`
   d) `func(a=1, b=2, 1)`

7. **What is the output of: `def f(a, b=5): return a+b; print(f(3))`?**
   a) 3
   b) 5
   c) 8
   d) Error

8. **How do you unpack a dictionary as keyword arguments?**
   a) `func(*dict)`
   b) `func(**dict)`
   c) `func(&dict)`
   d) `func(#dict)`

9. **In Python 3, how do you force keyword-only arguments?**
   a) Use *
   b) Use &
   c) Use #
   d) Use !

10. **What's the result of `func(1, **{'b': 2})` if `func(a, b)`?**
    a) Error
    b) func(1, 2)
    c) func(b=2, 1)
    d) func(1, b=2)

## Practice Questions (10)

1. Write a function that takes name, age, and city as parameters and creates a formatted string. Use default values for age and city.

2. Create a function that accepts any number of keyword arguments and prints them in sorted order by key.

3. Design a function that calculates the area of different shapes based on keyword arguments (shape type, dimensions).

4. Implement a function that sends an email with parameters for recipient, subject, body, and optional cc/bcc.

5. Write a configuration function that accepts various settings as keyword arguments and validates them.

6. Create a function that merges multiple dictionaries passed as keyword arguments.

7. Design a logging function that accepts message, level, timestamp, and additional metadata as keyword arguments.

8. Implement a function that creates HTML tags with various attributes passed as keyword arguments.

9. Write a function that processes user registration data with validation using keyword arguments.

10. Create a function that formats different types of dates based on keyword arguments specifying the format.

## Coding Exercises (5)

1. **Email Formatter**: Create a function that formats email headers using keyword arguments for to, from, subject, date, etc.

2. **API Request Builder**: Implement a function that builds HTTP request parameters from keyword arguments.

3. **Database Query Constructor**: Write a function that builds SQL WHERE clauses from keyword arguments.

4. **Configuration Manager**: Create a class that manages application settings using keyword arguments.

5. **Report Generator**: Implement a function that generates reports with various formatting options passed as keyword arguments.

## Mini Project

Create a flexible calculator function that accepts operations and numbers as keyword arguments:

```python
def advanced_calculator(operation="add", precision=2, **numbers):
    """
    Advanced calculator that performs operations on multiple numbers

    Args:
        operation: String representing the operation (add, multiply, average)
        precision: Number of decimal places for result
        **numbers: Named numbers to operate on

    Returns:
        Calculated result rounded to precision
    """
    if not numbers:
        return 0

    values = list(numbers.values())

    if operation == "add":
        result = sum(values)
    elif operation == "multiply":
        result = 1
        for val in values:
            result *= val
    elif operation == "average":
        result = sum(values) / len(values)
    else:
        raise ValueError("Unsupported operation")

    return round(result, precision)

# Example usage:
print(advanced_calculator(operation="add", precision=2, a=10, b=20, c=30))
print(advanced_calculator(operation="multiply", precision=3, x=2, y=3, z=4))
print(advanced_calculator(operation="average", precision=1, score1=85, score2=90, score3=78))
```

## Assignment

Create a comprehensive address book system using keyword arguments:

1. Implement a contact creation function that accepts name, phone, email, address, and other optional details
2. Create a search function that finds contacts by various criteria using keyword arguments
3. Design an update function that modifies contact information using keyword arguments
4. Build a display function that formats contact information in various ways
5. Add validation and error handling for the keyword arguments

Your implementation should demonstrate advanced use of keyword arguments including default values, **kwargs, and proper error handling.

## Summary

Keyword arguments in Python provide a powerful and flexible way to pass arguments to functions. They enhance code readability, maintainability, and flexibility by allowing you to specify arguments by name rather than position. Key concepts include:

- Basic syntax and usage
- Mixing with positional arguments
- Default parameter values
- Variable keyword arguments (**kwargs)
- Advanced features like keyword-only arguments
- Best practices and common pitfalls

Understanding keyword arguments is essential for writing professional Python code and is fundamental to many advanced Python features and design patterns.

## Key Takeaways

1. Keyword arguments use the syntax `parameter_name=value`
2. They can be specified in any order and mixed with positional arguments
3. Default values make parameters optional
4. **kwargs allows functions to accept any number of keyword arguments
5. Code readability improves significantly with proper use of keyword arguments
6. Always follow the rule: positional arguments before keyword arguments
7. Keyword-only arguments provide additional control in Python 3+
8. Unpacking with ** can pass dictionary items as keyword arguments

## Next Topic Preview

In the next lesson, we'll explore **Decorators** - a powerful Python feature that allows you to modify or enhance functions and classes without permanently modifying their code. We'll learn how decorators use keyword arguments and function introspection to create flexible and reusable code patterns.
