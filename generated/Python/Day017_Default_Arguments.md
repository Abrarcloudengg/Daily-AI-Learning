# Default Arguments

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what default arguments are and how they work
- Implement functions with default parameters effectively
- Identify when to use default arguments for cleaner code
- Avoid common pitfalls and mistakes with mutable defaults
- Apply best practices for function design with defaults
- Debug issues related to default argument behavior

## Prerequisites

Before learning about default arguments, you should have a solid understanding of:
- Basic Python syntax and data types
- Function definitions and calling functions
- Basic understanding of mutable vs immutable objects
- Python variable scope concepts

## What is Default Arguments?

Default arguments are parameters in a function that have predefined values. When a function is called without providing a value for these parameters, the default values are used automatically. This allows functions to be called with fewer arguments than defined, making them more flexible and easier to use.

Default arguments essentially provide sensible fallback values for function parameters, reducing the burden on the caller to specify every single argument when the default behavior is acceptable.

## Why is it Important?

Default arguments are important because they:

1. **Improve Code Readability**: Functions become more intuitive to use when common parameters have sensible defaults
2. **Reduce Code Duplication**: Eliminate the need for multiple function definitions for similar operations
3. **Enhance User Experience**: Make APIs more user-friendly by reducing required parameters
4. **Maintain Backward Compatibility**: Allow addition of new parameters without breaking existing code
5. **Enable Flexible Function Design**: Support both simple and complex use cases with a single function interface

## Real World Analogy

Think of default arguments like setting up a coffee machine with preset options. When you buy coffee from a shop, you can specify exactly what you want (double shot, almond milk, extra sugar), but if you just say "coffee," they'll make it with their standard settings (single shot, regular milk, regular sugar). The standard settings are the "default arguments" - they work for most people, but you can customize when needed.

## Theory

Default arguments are evaluated at function definition time, not at call time. This is a crucial distinction that can lead to unexpected behavior with mutable objects. When Python encounters a function definition with default arguments, it evaluates the default expressions immediately and stores the resulting objects. For immutable objects (like numbers, strings, tuples), this behavior is predictable. For mutable objects (like lists, dictionaries), this can cause problems because the same object is reused across multiple function calls.

Default arguments must appear after all non-default arguments in the parameter list. This ensures that Python can correctly match positional arguments to parameters when the function is called.

## Syntax

```python
def function_name(param1, param2=default_value2, param3=default_value3):
    # function body
    pass

# Calling with all arguments
function_name(value1, value2, value3)

# Calling with some defaults
function_name(value1)  # uses default values for param2 and param3
```

## Flow / Working

1. **Function Definition**: Python evaluates default argument expressions and stores them
2. **Function Call**: Python matches provided arguments to parameters
3. **Missing Arguments**: For parameters without provided values, Python uses the stored default values
4. **Function Execution**: The function executes with the complete set of arguments (provided + defaults)
5. **Return**: Function returns result as usual

## Example 1 (Beginner)

```python
def greet(name, greeting="Hello", punctuation="!"):
    """
    A simple greeting function with default arguments
    """
    return f"{greeting}, {name}{punctuation}"

# Using all defaults
print(greet("Alice"))  # Output: Hello, Alice!

# Overriding some defaults
print(greet("Bob", "Hi"))  # Output: Hi, Bob!

# Overriding all defaults
print(greet("Charlie", "Hey", "?"))  # Output: Hey, Charlie?

# Using keyword arguments to skip middle parameter
print(greet("David", punctuation="."))  # Output: Hello, David.
```

## Example 2 (Intermediate)

```python
def create_profile(name, age=None, hobbies=None, location="Unknown"):
    """
    Create a user profile with default values
    """
    if hobbies is None:
        hobbies = []  # Correct way to handle mutable default

    profile = {
        "name": name,
        "age": age,
        "hobbies": hobbies,
        "location": location
    }

    return profile

# Creating profiles with different combinations
profile1 = create_profile("Alice")
print(profile1)
# Output: {'name': 'Alice', 'age': None, 'hobbies': [], 'location': 'Unknown'}

profile2 = create_profile("Bob", 25, ["reading", "swimming"])
print(profile2)
# Output: {'name': 'Bob', 'age': 25, 'hobbies': ['reading', 'swimming'], 'location': 'Unknown'}

profile3 = create_profile("Charlie", location="New York")
print(profile3)
# Output: {'name': 'Charlie', 'age': None, 'hobbies': [], 'location': 'New York'}
```

## Example 3 (Advanced)

```python
import time
from datetime import datetime

def log_message(message, level="INFO", timestamp=None, format_string="{timestamp} [{level}] {message}"):
    """
    Advanced logging function with default arguments
    """
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_log = format_string.format(
        timestamp=timestamp,
        level=level,
        message=message
    )

    return formatted_log

# Using with all defaults
print(log_message("Application started"))
# Output: 2023-10-15 14:30:45 [INFO] Application started

# Customizing level
print(log_message("User login failed", level="ERROR"))
# Output: 2023-10-15 14:30:45 [ERROR] User login failed

# Customizing format
custom_format = "[{level}] {message}"
print(log_message("Debug info", level="DEBUG", format_string=custom_format))
# Output: [DEBUG] Debug info

# Using with custom timestamp
print(log_message("Manual entry", timestamp="2023-01-01 00:00:00"))
# Output: 2023-01-01 00:00:00 [INFO] Manual entry
```

## Output

```
Hello, Alice!
Hi, Bob!
Hey, Charlie?
Hello, David.
{'name': 'Alice', 'age': None, 'hobbies': [], 'location': 'Unknown'}
{'name': 'Bob', 'age': 25, 'hobbies': ['reading', 'swimming'], 'location': 'Unknown'}
{'name': 'Charlie', 'age': None, 'hobbies': [], 'location': 'New York'}
2023-10-15 14:30:45 [INFO] Application started
2023-10-15 14:30:45 [ERROR] User login failed
[DEBUG] Debug info
2023-01-01 00:00:00 [INFO] Manual entry
```

## Common Mistakes

| Mistake | Description | Correct Approach |
|---------|-------------|------------------|
| Mutable defaults | Using `def func(lst=[]):` | Use `def func(lst=None):` and set `lst = []` inside function |
| Position after defaults | Placing non-default after default | Put all non-defaults before defaults |
| Complex expressions | Using expensive operations as defaults | Use `None` and compute inside function |
| Changing defaults | Modifying mutable defaults affects future calls | Never modify mutable defaults directly |

## Best Practices

1. **Use Immutable Defaults**: Stick to numbers, strings, None, or tuples as defaults
2. **Handle Mutable Objects Properly**: Use `None` for mutable defaults and initialize inside the function
3. **Order Parameters Correctly**: Place default parameters after non-default parameters
4. **Use Meaningful Defaults**: Choose defaults that make sense for most use cases
5. **Document Defaults Clearly**: Explain what each default does in docstrings
6. **Avoid Complex Expressions**: Don't use function calls or complex expressions as defaults
7. **Consider Keyword-Only Arguments**: For complex functions, consider using keyword-only parameters after *args

## Pro Tips

1. **Debugging Default Issues**: If you suspect a default argument issue, print the function's `__defaults__` attribute
2. **Performance Optimization**: Default arguments are evaluated once, so they can be used for caching expensive operations (though rarely recommended)
3. **Configuration Functions**: Default arguments are perfect for configuration functions where most users need standard settings
4. **API Evolution**: Add new parameters with defaults to maintain backward compatibility
5. **Validation**: Always validate default values, especially when they come from external sources

## Interview Questions (10)

1. What happens when you use a mutable object as a default argument?
2. Explain why default arguments are evaluated at definition time, not call time.
3. How would you implement a function that accepts a list but has a default empty list?
4. What is the correct order of parameters when mixing default and non-default arguments?
5. Can you change the value of a default argument after the function is defined?
6. How do you skip a middle parameter and use its default value?
7. What are some alternatives to using mutable default arguments?
8. When would you use `**kwargs` with default arguments?
9. How do default arguments interact with *args and **kwargs?
10. What happens if you pass a keyword argument that doesn't exist?

## MCQs (10)

1. What is the output of `def f(x=[]): x.append(1); return x; print(f(), f())`?
   a) [1] [1]  b) [1] [1, 1]  c) [1, 1] [1, 1]  d) [1] [2]

2. Which parameter order is correct?
   a) `def func(a=1, b)`  b) `def func(b, a=1)`  c) Both  d) Neither

3. What is used as a default for mutable objects?
   a) `[]`  b) `[None]`  c) `None`  d) `""`

4. Default arguments are evaluated:
   a) At call time  b) At definition time  c) Every time  d) Never

5. How do you skip a parameter and use its default?
   a) Leave it blank  b) Use `None`  c) Use keyword arguments  d) Can't skip

6. What's the result of `def f(x, y=2, z=3): return x+y+z; f(1, z=5)`?
   a) 6  b) 8  c) 9  d) Error

7. Which is NOT a best practice for default arguments?
   a) Use immutable defaults  b) Place defaults after non-defaults
   c) Use complex expressions as defaults  d) Document defaults

8. What happens with `def f(a=[]): a.append(len(a)); return a; print(f(), f())`?
   a) [0] [0]  b) [0] [1]  c) [0] [0,1]  d) [1] [2]

9. How do you properly handle a default dictionary parameter?
   a) `d={}`  b) `d=dict()`  c) `d=None` then `d={}` inside function  d) All work

10. What's the output of `def f(x, y=None): y = y or []; return len(y); f(1)`?
    a) 0  b) 1  c) Error  d) None

## Practice Questions (10)

1. Write a function that calculates the area of a rectangle with default width=1 and height=1.
2. Create a function that joins strings with a default separator of space.
3. Implement a function that sends emails with default subject "No Subject" and body "".
4. Write a function that creates a shopping list with a default empty list, avoiding the mutable default pitfall.
5. Create a configuration function that sets up a database connection with default host, port, username, and password.
6. Implement a function that formats dates with default format and timezone.
7. Write a function that manages a task list with default priority levels.
8. Create a function that builds URLs with default protocol, domain, and path.
9. Implement a function that calculates discounts with default percentages for different customer tiers.
10. Write a function that generates reports with default format, sorting options, and filters.

## Coding Exercises (5)

1. **Email Formatter**: Create a function that formats emails with default subject, greeting, and signature.

2. **File Reader**: Implement a file reader that opens files with default encoding "utf-8" and read mode.

3. **Calculator**: Build a calculator function with default precision and rounding options.

4. **Data Validator**: Create a data validation function with default validation rules.

5. **API Client**: Implement an API client with default headers, timeout, and authentication method.

## Mini Project

**Task Management System with Default Settings**

Create a comprehensive task management system where users can:
- Create tasks with default priority levels (Low, Medium, High)
- Assign default due dates (e.g., end of week)
- Set default categories and tags
- Apply default notification settings
- Use default completion criteria

Include features like:
```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description="", priority="Medium",
                   due_date=None, category="General", tags=None,
                   notify=True, reminder_days=1):
        if tags is None:
            tags = []
        if due_date is None:
            from datetime import datetime, timedelta
            due_date = datetime.now() + timedelta(days=7)

        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "category": category,
            "tags": tags,
            "notify": notify,
            "reminder_days": reminder_days,
            "completed": False
        }
        self.tasks.append(task)
        return task

    def get_tasks_by_priority(self, priority="Medium"):
        return [task for task in self.tasks if task["priority"] == priority]

    def get_upcoming_tasks(self, days=7):
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() + timedelta(days=days)
        return [task for task in self.tasks
                if not task["completed"] and task["due_date"] <= cutoff_date]

# Usage example
tm = TaskManager()
tm.create_task("Learn Python")
tm.create_task("Buy groceries", priority="High", category="Personal")
print(tm.get_tasks_by_priority())
```

## Assignment

**Configuration Management System**

Create a configuration management system for a web application that:
1. Uses default settings for database, cache, logging, and security
2. Allows overriding any setting at runtime
3. Supports environment-specific configurations
4. Handles nested configuration objects properly
5. Provides validation for configuration values
6. Includes a factory function that returns configured objects with defaults

Requirements:
- Implement default configurations as dictionaries
- Create functions to merge user configs with defaults
- Handle nested dictionary merging correctly
- Validate required configuration values
- Support configuration inheritance (dev, staging, prod)
- Provide utility functions for common config operations

## Summary

Default arguments are a powerful Python feature that makes functions more flexible and user-friendly. Key points covered:
- Default arguments provide fallback values for function parameters
- They must appear after non-default parameters
- Mutable defaults require special handling to avoid unexpected behavior
- Proper use improves code readability and reduces duplication
- Common pitfalls include mutable default objects and parameter ordering issues
- Best practices involve using immutable defaults and careful documentation

## Key Takeaways

1. Default arguments make functions more flexible and easier to use
2. Always use None for mutable defaults and initialize inside the function
3. Default arguments are evaluated once at function definition time
4. Parameter order matters: defaults must come after non-defaults
5. Well-designed defaults improve user experience without sacrificing functionality
6. Understanding evaluation timing prevents common bugs
7. Proper documentation of defaults helps other developers use your functions

## Next Topic Preview

In the next lesson, we'll explore **Variable Length Arguments (*args and **kwargs)**, which allow functions to accept any number of positional or keyword arguments. This builds on our understanding of default arguments and provides even more flexibility in function design.
