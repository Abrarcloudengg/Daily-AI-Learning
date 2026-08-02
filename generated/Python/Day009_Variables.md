# Variables

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what variables are and their purpose in programming
- Declare and initialize variables in Python
- Work with different data types using variables
- Recognize variable naming conventions and best practices
- Handle variable scope and lifetime
- Apply advanced variable concepts like unpacking and dynamic typing
- Debug common variable-related issues

## Prerequisites

- Basic understanding of Python syntax
- Python installed on your system
- Familiarity with basic data types (integers, strings, floats)
- Understanding of basic programming concepts

## What is Variables?

Variables are named storage locations in computer memory that hold data values. Think of them as containers that can store information which can be changed during program execution. In Python, variables are created when you assign a value to them, and they can hold different types of data like numbers, text, lists, and more complex objects.

Unlike some programming languages, Python variables don't need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable.

## Why is it Important?

Variables are fundamental to programming because they:
- Allow programs to store and manipulate data
- Make code more readable and maintainable
- Enable dynamic behavior in applications
- Reduce code duplication by reusing values
- Facilitate complex calculations and data processing
- Allow programs to remember and use information throughout execution

Without variables, programs would be static and unable to process user input, perform calculations, or maintain state.

## Real World Analogy

Think of variables like labeled boxes in a storage room:
- Each box has a unique label (variable name)
- You can put different items in each box (assign values)
- You can change what's in a box at any time (reassign values)
- You can look inside any box by calling its label (access values)
- Some boxes might be bigger and hold multiple items (data structures)
- You can move boxes around and use their contents in different ways (manipulate data)

## Theory

In Python, variables work based on these principles:

**Dynamic Typing**: Python automatically determines the data type of a variable based on the value assigned to it.

**Object References**: Variables in Python are references to objects in memory, not the objects themselves.

**Memory Management**: Python automatically manages memory allocation and deallocation for variables.

**Scope**: Variables have different scopes (local, global, built-in) that determine where they can be accessed.

**Mutability**: Some data types (like lists) are mutable, meaning you can change their content without changing their identity, while others (like strings) are immutable.

## Syntax

```python
# Basic variable assignment
variable_name = value

# Multiple assignment
var1 = var2 = var3 = value

# Multiple variables assignment
var1, var2, var3 = value1, value2, value3

# Type annotation (optional)
variable_name: data_type = value
```

## Flow / Working

1. **Variable Creation**: When Python encounters an assignment statement, it creates a variable
2. **Memory Allocation**: Python allocates memory to store the value
3. **Object Creation**: If the value is a new object, Python creates it in memory
4. **Reference Assignment**: The variable name becomes a reference to the object
5. **Value Access**: When the variable is used, Python retrieves the referenced object
6. **Garbage Collection**: When no variables reference an object, Python frees the memory

## Example 1 (Beginner)

```python
# Basic variable creation and usage
name = "Alice"
age = 25
height = 5.6
is_student = True

# Printing variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Basic operations with variables
next_year_age = age + 1
print("Age next year:", next_year_age)

# Reassigning variable values
name = "Bob"
print("New name:", name)
```

## Example 2 (Intermediate)

```python
# Multiple assignment techniques
# Assigning same value to multiple variables
x = y = z = 10
print(f"x: {x}, y: {y}, z: {z}")

# Assigning different values to multiple variables
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# Swapping variables (Pythonic way)
a, b = b, a
print(f"After swap - a: {a}, b: {b}")

# Working with different data types
student_info = {
    "name": "Charlie",
    "grades": [85, 92, 78, 96],
    "courses": ("Math", "Science", "English")
}

# Accessing and modifying variables
student_info["age"] = 20
student_info["grades"].append(88)

print("Student Info:")
for key, value in student_info.items():
    print(f"  {key}: {value}")

# Using variables in functions
def calculate_average(grades):
    return sum(grades) / len(grades)

average_grade = calculate_average(student_info["grades"])
print(f"Average Grade: {average_grade:.2f}")
```

## Example 3 (Advanced)

```python
# Advanced variable concepts

# Variable unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Coordinates: x={x}, y={y}, z={z}")

# Unpacking with * operator
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Global and local variables
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")

# Using vars() and dir() to inspect variables
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("David", 30)
print("Person attributes:", vars(person))

# Dynamic variable creation
variable_names = ['var1', 'var2', 'var3']
for i, name in enumerate(variable_names, 1):
    globals()[name] = i * 10

print(f"Dynamic variables: var1={var1}, var2={var2}, var3={var3}")

# Type checking and conversion
user_input = "123"
if user_input.isdigit():
    number = int(user_input)
    print(f"Converted to integer: {number}")
else:
    print("Invalid input for conversion")
```

## Output

```
Name: Alice
Age: 25
Height: 5.6
Is Student: True
Age next year: 26
New name: Bob

x: 10, y: 10, z: 10
a: 1, b: 2, c: 3
After swap - a: 2, b: 1
Student Info:
  name: Charlie
  grades: [85, 92, 78, 96, 88]
  courses: ('Math', 'Science', 'English')
  age: 20
Average Grade: 87.80

Coordinates: x=10, y=20, z=30
First: 1, Middle: [2, 3, 4], Last: 5
Inside function - Local: I'm local
Inside function - Global: Modified global
Outside function - Global: Modified global
Person attributes: {'name': 'David', 'age': 30}
Dynamic variables: var1=10, var2=20, var3=30
Converted to integer: 123
```

## Common Mistakes

| Mistake | Description | Solution |
|---------|-------------|----------|
| `NameError` | Using variable before assignment | Always initialize variables before use |
| Invalid names | Using keywords or special characters | Follow naming conventions |
| Type errors | Performing operations on incompatible types | Check and convert data types |
| Scope issues | Accessing local variables outside scope | Understand variable scope rules |
| Mutable default | Using mutable objects as default arguments | Use None and create new objects |
| Unpacking errors | Mismatch in number of variables and values | Ensure equal count in unpacking |
| Shadowing | Local variables hiding global ones | Use different names or explicit global keyword |

## Best Practices

1. **Use descriptive names**: `user_age` instead of `ua`
2. **Follow naming conventions**: Use `snake_case` for variables
3. **Initialize variables**: Always give initial values
4. **Use type hints**: Improve code readability and IDE support
5. **Limit scope**: Keep variables in the smallest scope necessary
6. **Avoid global variables**: Prefer function parameters and return values
7. **Use constants for fixed values**: `MAX_USERS = 100`
8. **Group related variables**: Use classes or dictionaries
9. **Document complex variables**: Add comments for clarity
10. **Consistent naming**: Maintain naming patterns throughout your code

## Pro Tips

1. **Use f-strings for variable formatting**: `f"Hello {name}"` is more efficient than concatenation
2. **Leverage tuple unpacking**: `a, b = b, a` for swapping without temporary variables
3. **Use walrus operator (Python 3.8+)**: `if (n := len(data)) > 10:` assigns and checks in one line
4. **Understand variable references**: Lists and dictionaries are mutable, so copying requires care
5. **Use `is` for identity checks**: `if x is None:` instead of `if x == None:`
6. **Leverage multiple assignment**: `x, y, z = 0, 0, 0` for initialization
7. **Use `locals()` and `globals()`**: For debugging and dynamic variable access
8. **Consider memory usage**: Large data structures should be managed carefully
9. **Use `del` to remove variables**: Free memory when variables are no longer needed
10. **Profile variable usage**: Use tools like `memory_profiler` for optimization

## Interview Questions (10)

1. What is the difference between mutable and immutable variables in Python?
2. How does variable assignment work in Python compared to other languages?
3. Explain the concept of variable scope in Python.
4. What happens when you assign one variable to another in Python?
5. How do you handle variable naming conflicts in Python?
6. What is the difference between `==` and `is` when comparing variables?
7. How does Python manage memory for variables?
8. Explain the concept of variable unpacking with examples.
9. What are the best practices for variable naming in Python?
10. How do you debug variable-related issues in Python?

## MCQs (10)

1. **What is the output of the following code?**
   ```python
   x = 10
   y = x
   x = 20
   print(y)
   ```
   a) 10
   b) 20
   c) Error
   d) None

2. **Which of the following is a valid variable name in Python?**
   a) 2var
   b) var-name
   c) var_name
   d) class

3. **What does the following code do?**
   ```python
   a, b = b, a
   ```
   a) Adds a and b
   b) Swaps values of a and b
   c) Multiplies a and b
   d) Compares a and b

4. **Which keyword is used to declare a global variable inside a function?**
   a) global
   b) nonlocal
   c) external
   d) public

5. **What is the data type of the variable after this assignment?**
   ```python
   x = [1, 2, 3]
   ```
   a) int
   b) list
   c) tuple
   d) string

6. **How do you delete a variable in Python?**
   a) delete variable_name
   b) del variable_name
   c) remove variable_name
   d) variable_name = None

7. **What is the result of this code?**
   ```python
   x = "Hello"
   y = "Hello"
   print(x is y)
   ```
   a) True
   b) False
   c) Error
   d) None

8. **Which of the following is NOT a valid way to assign multiple variables?**
   a) x, y, z = 1, 2, 3
   b) x = y = z = 1
   c) x, y = 1, 2, 3
   d) x, y, z = [1, 2, 3]

9. **What does the `id()` function return?**
   a) Variable name
   b) Variable value
   c) Memory address
   d) Variable type

10. **Which of the following is a mutable data type?**
    a) int
    b) str
    c) tuple
    d) list

## Practice Questions (10)

1. Create variables to store a person's information (name, age, email) and print them.
2. Write a program that swaps two numbers using variables.
3. Create a list of 5 numbers and use variables to store and manipulate them.
4. Write a function that takes user input and stores it in appropriately named variables.
5. Create variables with different data types and demonstrate type checking.
6. Implement a simple calculator using variables to store operands and results.
7. Create a dictionary using variables as keys and values.
8. Write a program that demonstrates local and global variable scope.
9. Use variable unpacking to process a list of coordinates.
10. Create constants for mathematical values (π, e) and use them in calculations.

## Coding Exercises (5)

1. **Temperature Converter**: Create variables for Celsius and Fahrenheit temperatures. Write functions to convert between them using these variables.

2. **Bank Account Simulator**: Create variables to represent account balance, transactions, and account holder information. Implement deposit and withdrawal functions.

3. **Student Grade Calculator**: Use variables to store student names, grades for multiple subjects, and calculate averages. Store results in appropriate variables.

4. **Shopping Cart**: Create variables to represent items, prices, quantities, and total cost. Implement functions to add items and calculate totals.

5. **Text Analyzer**: Create variables to store text input, word count, character count, and other statistics. Process the text and store results in variables.

## Mini Project

**Personal Finance Tracker**

Create a comprehensive personal finance tracker that uses variables to manage:
- Income sources and amounts
- Expense categories and amounts
- Budget limits for different categories
- Savings goals and progress
- Financial summaries and reports

Features:
1. Variables for different income streams
2. Variables for expense tracking by category
3. Variables for budget limits and remaining amounts
4. Variables for savings goals and current progress
5. Variables for monthly and yearly summaries
6. Use variable unpacking for transaction processing
7. Implement proper variable scope management
8. Use constants for fixed values like tax rates

```python
# Personal Finance Tracker - Starter Code
class FinanceTracker:
    def __init__(self):
        self.income_sources = {}
        self.expenses = {}
        self.budget_limits = {}
        self.savings_goals = {}
        self.TAX_RATE = 0.2  # Constant
    
    def add_income(self, source, amount):
        self.income_sources[source] = amount
    
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
    
    def set_budget(self, category, limit):
        self.budget_limits[category