# Variables

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what variables are and their purpose in programming
- Declare and assign variables in Python
- Work with different data types in variables
- Identify naming conventions and best practices
- Handle variable scope and lifetime
- Apply advanced variable concepts like unpacking and dynamic typing
- Solve real-world problems using variables

## Prerequisites

- Basic understanding of Python syntax
- Python installed on your system
- Text editor or IDE for coding
- Fundamental knowledge of data types (strings, numbers, booleans)

## What is Variables?

A variable is a named storage location in computer memory that holds data which can be changed during program execution. Think of a variable as a container or a box that can hold different values. In Python, variables are used to store information that can be referenced and manipulated throughout your program.

Variables in Python are dynamically typed, meaning you don't need to declare their type explicitly - Python figures it out based on the value assigned.

## Why is it Important?

Variables are fundamental to programming because they:
- Allow programs to store and manipulate data
- Make code more readable and maintainable
- Enable dynamic behavior in applications
- Reduce code duplication by reusing values
- Facilitate complex calculations and data processing
- Support the creation of interactive and responsive programs

## Real World Analogy

Think of variables like labeled boxes in a warehouse:
- Each box has a unique label (variable name)
- The box can contain different items (values) at different times
- You can access the contents by referring to the label
- The warehouse worker (Python interpreter) knows what's in each box
- Boxes can be rearranged, emptied, or filled with new items

## Theory

In Python, variables work based on the following principles:

1. **Dynamic Typing**: Variables don't have fixed types; their type is determined by the value they hold
2. **Object References**: Variables are references to objects in memory, not the objects themselves
3. **Memory Management**: Python automatically manages memory allocation and deallocation
4. **Scope Rules**: Variables have different scopes (local, global, built-in) that determine where they can be accessed
5. **Mutability**: Some variable types can be changed after creation (mutable), while others cannot (immutable)

## Syntax

```python
# Basic variable assignment
variable_name = value

# Multiple assignment
var1 = var2 = var3 = value

# Multiple variables in one line
var1, var2, var3 = value1, value2, value3

# Type annotation (optional)
variable_name: data_type = value
```

## Flow / Working

1. **Declaration**: Python automatically declares variables when you assign a value
2. **Memory Allocation**: Python allocates memory for the object based on its type
3. **Assignment**: The variable name becomes a reference to the memory location
4. **Usage**: The variable can be used anywhere in its scope
5. **Reassignment**: Variables can be reassigned to different values/types
6. **Garbage Collection**: When variables go out of scope, Python automatically frees the memory

## Example 1 (Beginner)

```python
# Simple variable assignment
name = "Alice"
age = 25
is_student = True

# Printing variables
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)

# Basic arithmetic with variables
x = 10
y = 5
sum_result = x + y
print("Sum:", sum_result)

# String concatenation with variables
greeting = "Hello, " + name + "!"
print(greeting)
```

## Example 2 (Intermediate)

```python
# Multiple assignment
a = b = c = 10
print(f"a: {a}, b: {b}, c: {c}")

# Unpacking sequences
coordinates = (3, 4, 5)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")

# Swapping variables (Pythonic way)
first = 100
second = 200
print(f"Before swap - first: {first}, second: {second}")
first, second = second, first
print(f"After swap - first: {first}, second: {second}")

# Type checking and conversion
user_input = "42"
print(f"Original type: {type(user_input)}")
number = int(user_input)
print(f"Converted type: {type(number)}")

# Working with different scopes
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(local_var)
    print(global_var)  # Can access global variables

my_function()
# print(local_var)  # This would cause an error
```

## Example 3 (Advanced)

```python
# Dynamic typing demonstration
variable = 42
print(f"Variable is {type(variable)} with value {variable}")

variable = "Now I'm a string"
print(f"Variable is {type(variable)} with value {variable}")

variable = [1, 2, 3, 4, 5]
print(f"Variable is {type(variable)} with value {variable}")

# Variable unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Using variables in list comprehensions
multiplier = 2
result = [x * multiplier for x in range(1, 6)]
print(f"Result: {result}")

# Advanced unpacking with dictionaries
person = {"name": "Bob", "age": 30, "city": "New York"}
def display_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

display_person(**person)  # Unpacking dictionary

# Using globals() and locals()
def show_variables():
    local_var = "Local"
    print("Local variables:", locals())
    print("Global variables:", list(globals().keys()))

show_variables()
```

## Output

```
Name: Alice
Age: 25
Is Student: True
Sum: 15
Hello, Alice!

a: 10, b: 10, c: 10
X: 3, Y: 4, Z: 5
Before swap - first: 100, second: 200
After swap - first: 200, second: 100
Original type: <class 'str'>
Converted type: <class 'int'>

I'm local
I'm global

Variable is <class 'int'> with value 42
Variable is <class 'str'> with value Now I'm a string
Variable is <class 'list'> with value [1, 2, 3, 4, 5]
First: 1, Middle: [2, 3, 4], Last: 5
Result: [2, 4, 6, 8, 10]
Bob is 30 years old and lives in New York
Local variables: {'local_var': 'Local'}
Global variables: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'name', 'age', 'is_student', 'x', 'y', 'sum_result', 'greeting', 'a', 'b', 'c', 'coordinates', 'first', 'second', 'user_input', 'number', 'global_var', 'my_function', 'variable', 'numbers', 'multiplier', 'result', 'person', 'display_person', 'show_variables', 'local_var']
```

## Common Mistakes

| Mistake | Explanation | Solution |
|---------|-------------|----------|
| Using undefined variables | Trying to use a variable before assigning it | Always initialize variables before use |
| Incorrect naming | Using reserved keywords or invalid names | Follow Python naming conventions |
| Scope confusion | Accessing local variables outside their scope | Understand variable scope rules |
| Type errors | Performing operations on incompatible types | Check and convert types appropriately |
| Mutable default arguments | Using mutable objects as default parameters | Use None and create new objects inside functions |
| Unpacking mismatch | Number of variables doesn't match values | Ensure correct number of variables and values |

## Best Practices

1. **Use descriptive names**: Choose meaningful variable names that explain their purpose
2. **Follow naming conventions**: Use snake_case for variable names (e.g., `user_name`)
3. **Initialize variables**: Always assign initial values to avoid undefined behavior
4. **Limit scope**: Keep variables in the smallest scope necessary
5. **Use constants for fixed values**: Define constants in uppercase (e.g., `MAX_SIZE = 100`)
6. **Avoid global variables**: Minimize use of global variables to reduce complexity
7. **Use type hints**: Add type annotations for better code documentation
8. **Consistent naming**: Maintain consistency in naming across your codebase

## Pro Tips

1. **Use f-strings for variable interpolation**: `f"Hello {name}"` is more readable than `"Hello " + name`
2. **Leverage tuple unpacking**: `a, b = b, a` for swapping variables
3. **Use walrus operator (Python 3.8+)**: `if (n := len(data)) > 10:` assigns and checks in one line
4. **Understand variable references**: Lists and dictionaries are mutable, so changes affect all references
5. **Use `id()` to check object identity**: `id(variable)` shows the memory address
6. **Use `is` for identity comparison**: `a is b` checks if two variables reference the same object
7. **Use `copy()` for shallow copying**: `new_list = old_list.copy()` creates a new list
8. **Leverage multiple assignment**: `x, y, z = 1, 2, 3` for cleaner initialization

## Interview Questions (10)

1. **What is the difference between a variable and a constant in Python?**
2. **Explain Python's dynamic typing with an example.**
3. **What is variable scope and what are the different types of scope in Python?**
4. **How does Python handle memory management for variables?**
5. **What is the difference between `==` and `is` operators?**
6. **Explain variable unpacking with examples.**
7. **What happens when you assign one variable to another in Python?**
8. **How do you handle mutable default arguments in functions?**
9. **What is the purpose of the `global` and `nonlocal` keywords?**
10. **Explain the concept of variable references and object identity.**

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
a) 2variable
b) variable-name
c) variable_name
d) variable name

3. **What does the `id()` function return?**
a) Variable value
b) Variable name
c) Memory address
d) Variable type

4. **Which operator is used for identity comparison?**
a) ==
b) =
c) is
d) !=

5. **What is the scope of a variable defined inside a function?**
a) Global
b) Local
c) Built-in
d) Module

6. **What is the output of this code?**
```python
a, b = 5, 10
a, b = b, a
print(a, b)
```
a) 5 10
b) 10 5
c) Error
d) 5 5

7. **Which keyword is used to modify a global variable inside a function?**
a) local
b) global
c) nonlocal
d) external

8. **What happens when you delete a variable using `del`?**
a) Variable value becomes None
b) Variable name is removed from namespace
c) Memory is immediately freed
d) All of the above

9. **Which of the following creates a tuple?**
a) x = (5)
b) x = 5,
c) x = (5,)
d) Both b and c

10. **What is the result of `type(42)`?**
a) int
b) <class 'int'>
c) 42
d) "int"

## Practice Questions (10)

1. Create variables to store your name, age, and whether you're a student. Print them in a formatted string.
2. Write a program that swaps the values of two variables without using a temporary variable.
3. Create a list of numbers and use unpacking to assign the first element to one variable and the rest to another.
4. Write a function that takes a dictionary and unpacks it as keyword arguments to another function.
5. Create a program that demonstrates the difference between local and global variables.
6. Write code that shows how mutable objects behave when assigned to multiple variables.
7. Create a program that uses the walrus operator to simplify a while loop.
8. Write a function that accepts variable arguments using *args and **kwargs.
9. Create a program that shows the difference between shallow and deep copying.
10. Write code that demonstrates variable scope with nested functions.

## Coding Exercises (5)

### Exercise 1: Temperature Converter
Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using variables to store the values.

### Exercise 2: Student Grade Calculator
Write a program that calculates a student's average grade from multiple subjects using variables to store grades and results.

### Exercise 3: Bank Account Simulation
Create a simple bank account system where you can deposit, withdraw, and check balance using variables to track the account state.

### Exercise 4: Word Counter
Write a program that counts the frequency of words in a text using variables to store the text and word counts.

### Exercise 5: Shopping Cart
Create a shopping cart system that calculates total cost, applies discounts, and tracks inventory using variables.

## Mini Project

### Personal Finance Tracker

Create a comprehensive personal finance tracker that uses variables to manage income, expenses, and savings.

```python
class FinanceTracker:
    def __init__(self):
        self.income = 0.0
        self.expenses = 0.0
        self.savings = 0.0
        self.transactions = []
    
    def add_income(self, amount, source):
        self.income += amount
        self.transactions.append(f"Income: +${amount} from {source}")
        self.update_savings()
    
    def add_expense(self, amount, category):
        self.expenses += amount
        self.transactions.append(f"Expense: -${amount} for {category}")
        self.update_savings()
    
    def update_savings(self):
        self.savings = self.income - self.expenses
    
    def get_summary(self):
        return {
            "total_income": self.income,
            "total_expenses": self.expenses,
            "current_savings": self.savings,
            "transaction_count": len(self.transactions)
        }
    
    def display_report(self):
        summary = self.get_summary()
        print("=== FINANCE REPORT ===")
        print(f"Total Income: ${summary['total_income']:.2f}")
        print(f"Total Expenses: ${summary['total_expenses']:.2f}")
        print(f"Current Savings: ${summary['current_savings']:.2f}")
        print(f"Number of Transactions: {summary['transaction_count']}")

# Usage example
tracker = FinanceTracker()
tracker.add_income(3000, "Salary")
tracker.add_expense(800, "Rent")
tracker.add_expense(200, "Groceries")
tracker.display_report()
```

## Assignment

Create a complete inventory management system for a small retail store. Your system should:

1. Use variables to store product information (name, price, quantity)
2. Implement functions to add, remove, and update products
3. Track total inventory