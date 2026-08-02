# Variables

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what variables are and their role in programming
- Declare and initialize variables in Python
- Differentiate between various data types and variable naming conventions
- Apply variable scoping rules and understand memory management
- Use advanced variable concepts like unpacking and type hints
- Debug common variable-related issues
- Write clean, efficient code using proper variable practices

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax
- Python installed on your system
- Knowledge of basic data types (int, float, string, boolean)
- Understanding of basic programming concepts
- Familiarity with Python's print() function

## What is Variables?

A variable is a named storage location in computer memory that holds data which can be changed during program execution. Think of variables as containers that store information for later use in your program. Each variable has:
- A name (identifier)
- A value (the data it holds)
- A data type (what kind of data it can store)
- A memory location

In Python, variables are dynamically typed, meaning you don't need to declare their type explicitly - Python figures it out automatically.

## Why is it Important?

Variables are fundamental to programming because they:
- Enable data storage and manipulation
- Make programs dynamic and interactive
- Allow code reusability and maintainability
- Facilitate complex calculations and logic
- Enable user input processing
- Support data persistence within program execution
- Make code more readable and organized

Without variables, programs would be static and unable to process different inputs or maintain state.

## Real World Analogy

Think of variables like labeled boxes in a warehouse:
- Each box has a unique label (variable name)
- The box can contain different items (values)
- You can change what's inside the box (reassign values)
- You can look inside to see what's there (access values)
- The size of the box determines what it can hold (data type)
- Boxes can be moved around and used in different contexts (scope)

Just like you'd label a box "Winter Clothes" to easily find winter clothing, you name a variable `user_age` to store and access age information.

## Theory

### Variable Fundamentals

In Python, variables work differently than in many other languages:
- **Dynamic Typing**: Variable types are determined at runtime
- **Object References**: Variables are references to objects in memory
- **Mutable vs Immutable**: Some data types can be changed after creation
- **Memory Management**: Python handles memory allocation automatically
- **Garbage Collection**: Unused variables are automatically cleaned up

### Variable Assignment

When you assign a value to a variable:
1. Python creates an object in memory with the value
2. The variable name becomes a reference to that memory location
3. The assignment operator `=` links the name to the object

### Memory Model

```python
x = 10        # Creates integer object, x points to it
y = x         # y now points to the same object as x
x = 20        # Creates new integer object, x now points to it
```

## Syntax

### Basic Variable Declaration
```python
variable_name = value
```

### Multiple Assignment
```python
# Single value to multiple variables
a = b = c = 10

# Multiple values to multiple variables
x, y, z = 1, 2, 3
```

### Variable Naming Rules
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (`age` ≠ `Age`)
- Cannot be Python keywords

### Valid Variable Names
```python
name = "John"
_age = 25
student1 = True
total_amount = 100.50
MAX_SIZE = 1000  # Convention for constants
```

## Flow / Working

1. **Declaration**: Variable name is created in namespace
2. **Assignment**: Value is assigned to the variable
3. **Memory Allocation**: Python creates object and assigns reference
4. **Usage**: Variable can be accessed throughout its scope
5. **Reassignment**: New value can replace old value
6. **Garbage Collection**: When out of scope, memory is freed

## Example 1 (Beginner)

```python
# Basic variable operations
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Variable reassignment
age = 26
print("Updated Age:", age)

# Basic calculations with variables
num1 = 10
num2 = 5
sum_result = num1 + num2
product = num1 * num2

print(f"Sum of {num1} and {num2} is {sum_result}")
print(f"Product is {product}")
```

## Example 2 (Intermediate)

```python
# Variable scope and advanced operations
def demonstrate_scope():
    # Local variable
    local_var = "I'm local"
    print(local_var)
    
    # Global variable access
    global global_counter
    global_counter += 1
    print(f"Global counter: {global_counter}")

# Global variable
global_counter = 0
message = "Hello, World!"

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 100

# Variable unpacking
coordinates = (10, 20, 30)
x_coord, y_coord, z_coord = coordinates

# Type checking
print(f"Type of message: {type(message)}")
print(f"Type of a: {type(a)}")

# String formatting with variables
user_info = f"User: {name}, Age: {age}, Height: {height}"
print(user_info)

# Calling function to show scope
demonstrate_scope()
```

## Example 3 (Advanced)

```python
# Advanced variable concepts
from typing import List, Dict, Optional

# Type hints (Python 3.5+)
def process_data(numbers: List[int], multiplier: int = 2) -> Dict[str, int]:
    """Process a list of numbers with type hints"""
    result = {
        'original_sum': sum(numbers),
        'multiplied_sum': sum(num * multiplier for num in numbers),
        'count': len(numbers)
    }
    return result

# Variable annotations (Python 3.6+)
name: str = "Advanced Python"
items: List[int] = [1, 2, 3, 4, 5]
metadata: Dict[str, str] = {"version": "1.0", "author": "Python"}

# Walrus operator (Python 3.8+) - assignment expression
if (n := len(items)) > 3:
    print(f"List has {n} items, which is more than 3")

# Variable unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Dictionary unpacking
person = {"name": "Bob", "age": 30}
greeting = "Hello {name}, you are {age} years old".format(**person)
print(greeting)

# Advanced multiple assignment
a, b = b, a  # Swap variables without temp variable
print(f"Swapped: a={a}, b={b}")

# Using variables in list comprehensions
squared_values = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squared even numbers: {squared_values}")

# Processing with type hints
data_result = process_data([1, 2, 3, 4, 5], 3)
print(f"Processed data: {data_result}")
```

## Output

```
Name: Alice
Age: 25
Height: 5.6
Is Student: True
Updated Age: 26
Sum of 10 and 5 is 15
Product is 50
I'm local
Global counter: 1
Type of message: <class 'str'>
Type of a: <class 'int'>
User: Alice, Age: 26, Height: 5.6
First: 1, Middle: [2, 3, 4], Last: 5
Hello Bob, you are 30 years old
Swapped: a=100, b=100
Squared even numbers: [0, 4, 16, 36, 64]
Processed data: {'original_sum': 15, 'multiplied_sum': 45, 'count': 5}
```

## Common Mistakes

| Mistake | Example | Correct Approach |
|---------|---------|------------------|
| Using undefined variables | `print(x)` (without defining x) | `x = 10; print(x)` |
| Invalid variable names | `1variable = 5` | `variable1 = 5` |
| Confusing = and == | `if x = 5:` | `if x == 5:` |
| Variable name typos | `usernmae = "John"` | `username = "John"` |
| Reusing variable names | `list = [1,2,3]` (shadows built-in) | `my_list = [1,2,3]` |
| Scope issues | Using local var outside function | Return or make global |
| Mutable default arguments | `def func(lst=[]):` | `def func(lst=None):` |
| Unpacking mismatch | `a, b = [1,2,3]` | `a, b, c = [1,2,3]` |

## Best Practices

1. **Use descriptive names**: `total_price` instead of `tp`
2. **Follow naming conventions**: 
   - `snake_case` for variables
   - `UPPER_CASE` for constants
3. **Initialize variables before use**
4. **Avoid single letter names** except for loop counters
5. **Use type hints** for better code documentation
6. **Keep variable scope minimal**
7. **Use meaningful prefixes** for related variables
8. **Avoid shadowing built-in names**
9. **Use constants for magic numbers**
10. **Group related variables logically**

## Pro Tips

1. **Use f-strings for variable interpolation**:
   ```python
   name, age = "Alice", 25
   print(f"Hello {name}, you are {age} years old")
   ```

2. **Variable unpacking for multiple returns**:
   ```python
   def get_name_age():
       return "Bob", 30
   name, age = get_name_age()
   ```

3. **Use walrus operator for cleaner code**:
   ```python
   # Instead of:
   data = input("Enter data: ")
   if len(data) > 10:
       print(f"Long input: {data}")
   
   # Use:
   if (data := input("Enter data: ")) and len(data) > 10:
       print(f"Long input: {data}")
   ```

4. **Leverage multiple assignment for swapping**:
   ```python
   a, b = b, a  # No temp variable needed
   ```

5. **Use variable unpacking with * for flexible assignments**:
   ```python
   first, *rest, last = [1, 2, 3, 4, 5]
   ```

6. **Utilize variable annotations for better IDE support**:
   ```python
   from typing import List
   numbers: List[int] = [1, 2, 3, 4, 5]
   ```

## Interview Questions (10)

1. **What is the difference between variables in Python and other languages?**
2. **Explain Python's variable assignment mechanism.**
3. **What is variable scope in Python?**
4. **How does Python handle memory management for variables?**
5. **What are the differences between mutable and immutable variables?**
6. **Explain the concept of variable unpacking in Python.**
7. **What are type hints and how do they improve code quality?**
8. **How does Python's garbage collection work with variables?**
9. **What is the difference between `=` and `==` in variable context?**
10. **Explain the walrus operator and its use cases.**

## MCQs (10)

1. **What does the following code output?**
   ```python
   x = [1, 2, 3]
   y = x
   y.append(4)
   print(x)
   ```
   a) [1, 2, 3]  
   b) [1, 2, 3, 4]  
   c) [4]  
   d) Error

2. **Which is a valid variable name in Python?**
   a) 2variable  
   b) variable-name  
   c) _variable  
   d) class

3. **What is the output of: `a, b = 5, 10; a, b = b, a; print(a, b)`**
   a) 5 10  
   b) 10 5  
   c) Error  
   d) 5 5

4. **In Python, variables are:**
   a) Statically typed  
   b) Dynamically typed  
   c) Strongly typed only  
   d) Weakly typed only

5. **What does `global` keyword do?**
   a) Makes variable local  
   b) Makes variable accessible globally  
   c) Deletes variable  
   d) None of the above

6. **The walrus operator `:=` was introduced in:**
   a) Python 3.5  
   b) Python 3.7  
   c) Python 3.8  
   d) Python 3.9

7. **What is the result of: `x = y = 10; y = 20; print(x)`**
   a) 10  
   b) 20  
   c) Error  
   d) None

8. **Which data type is mutable?**
   a) int  
   b) str  
   c) list  
   d) tuple

9. **What does `*` do in unpacking?**
   a) Multiplies values  
   b) Collects remaining values  
   c) Deletes values  
   d) None of the above

10. **Type hints are:**
    a) Enforced at runtime  
    b) Checked at compile time  
    c) For documentation and IDE support  
    d) Mandatory in Python

## Practice Questions (10)

1. Create variables for a student's name, age, and grades, then display them.
2. Write a program that swaps two variables without using a temporary variable.
3. Create a function that returns multiple values and unpack them into variables.
4. Demonstrate variable scope with global and local variables.
5. Use variable unpacking to separate first, middle, and last elements of a list.
6. Implement a program using type hints for better code documentation.
7. Use the walrus operator to simplify input validation code.
8. Create constants for mathematical values (π, e) and use them in calculations.
9. Write a program that shows the difference between mutable and immutable variables.
10. Implement a function that uses variable-length argument unpacking.

## Coding Exercises (5)

1. **Temperature Converter**: Create variables for Celsius and Fahrenheit temperatures, write conversion functions, and store results in variables.

2. **Bank Account**: Design variables to store account holder information, balance, and transaction history. Implement deposit and withdrawal functions.

3. **Student Grade Calculator**: Use variables to store student scores, calculate averages, and determine letter grades using appropriate variable naming.

4. **Shopping Cart**: Create variables for items, prices, quantities, and totals. Implement functions to add items and calculate final amounts.

5. **Data Analysis Tool**: Use variables with type hints to store dataset information, implement statistical calculations, and return results in structured variables.

## Mini Project

**Personal Finance Tracker**

