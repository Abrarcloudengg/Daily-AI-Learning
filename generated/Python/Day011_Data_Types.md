# Data Types

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what data types are and why they are important
- Identify and use basic data types in Python
- Convert between different data types
- Handle complex data types like collections
- Apply type checking and type conversion techniques
- Solve real-world problems using appropriate data types

## Prerequisites

- Basic Python syntax understanding
- Python installed on your system
- Familiarity with variables and basic operations
- Understanding of basic programming concepts

## What is Data Types?

Data types in Python define the kind of value a variable can hold and what operations can be performed on that value. They determine how data is stored, interpreted, and manipulated in memory. Python has built-in data types that automatically handle memory allocation and provide various methods for data manipulation.

Each data type has:
- Specific storage requirements
- Defined range of values
- Set of operations that can be performed
- Methods and attributes associated with it

## Why is it Important?

Understanding data types is crucial because:
- **Memory Management**: Different data types require different amounts of memory
- **Performance**: Using appropriate data types improves program efficiency
- **Error Prevention**: Correct data types prevent runtime errors
- **Data Integrity**: Ensures data is stored and processed correctly
- **Code Readability**: Makes code more understandable and maintainable
- **Functionality**: Determines what operations can be performed
- **Debugging**: Helps identify and fix type-related issues quickly

## Real World Analogy

Think of data types like containers in a kitchen:
- **Integer Container**: Like measuring cups for whole numbers (1, 2, 3)
- **Float Container**: Like measuring cups for precise measurements (1.5 cups)
- **String Container**: Like labeled boxes for text (recipe names)
- **Boolean Container**: Like light switches (ON/OFF, True/False)
- **List Container**: Like a shopping cart holding multiple items
- **Dictionary Container**: Like a recipe book with ingredient-name pairs

Each container serves a specific purpose and can only hold certain types of items effectively.

## Theory

Python has several built-in data types categorized as:

### Immutable Data Types
- **Numbers**: int, float, complex
- **Strings**: str
- **Tuples**: tuple
- **Boolean**: bool

### Mutable Data Types
- **Lists**: list
- **Dictionaries**: dict
- **Sets**: set

### Numeric Types
- **int**: Whole numbers (positive, negative, zero)
- **float**: Decimal numbers
- **complex**: Numbers with real and imaginary parts

### Sequence Types
- **str**: Text sequences
- **list**: Ordered, changeable collections
- **tuple**: Ordered, unchangeable collections

### Mapping Type
- **dict**: Key-value pairs

### Set Types
- **set**: Unordered collections with no duplicates
- **frozenset**: Immutable set

## Syntax

```python
# Basic data type declarations
integer_var = 42
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3, 4]
tuple_var = (1, 2, 3, 4)
dict_var = {"name": "Alice", "age": 30}
set_var = {1, 2, 3, 4}

# Type checking
type(variable_name)

# Type conversion
int(value)
float(value)
str(value)
list(value)
tuple(value)
```

## Flow / Working

```
Variable Declaration → Data Type Assignment → Memory Allocation → 
Operations Performed → Type Checking → Type Conversion (if needed) → 
Output/Return
```

1. **Declaration**: Variable is created with a value
2. **Type Assignment**: Python automatically assigns data type
3. **Memory Allocation**: Memory is allocated based on type
4. **Operations**: Performed according to type rules
5. **Type Checking**: Using type() or isinstance()
6. **Conversion**: If needed, convert to another type
7. **Output**: Return or display results

## Example 1 (Beginner)

```python
# Basic Data Types Demonstration
print("=== Basic Data Types ===")

# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String
name = "Alice Johnson"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Type Conversion Examples
print("\n=== Type Conversion ===")
number_str = "123"
print(f"String number: {number_str}, Type: {type(number_str)}")

# Convert string to integer
number_int = int(number_str)
print(f"Integer number: {number_int}, Type: {type(number_int)}")

# Convert integer to float
number_float = float(number_int)
print(f"Float number: {number_float}, Type: {type(number_float)}")
```

## Example 2 (Intermediate)

```python
# Complex Data Types and Operations
print("=== Complex Data Types ===")

# List operations
fruits = ["apple", "banana", "orange"]
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
fruits.append("grape")
print(f"After adding grape: {fruits}")

# Dictionary operations
student = {
    "name": "Bob",
    "age": 20,
    "grades": [85, 92, 78, 96],
    "is_enrolled": True
}
print(f"\nStudent info: {student}")
print(f"Student name: {student['name']}")
print(f"Average grade: {sum(student['grades']) / len(student['grades'])}")

# Tuple operations (immutable)
coordinates = (10, 20)
print(f"\nCoordinates: {coordinates}")
print(f"X coordinate: {coordinates[0]}")

# Set operations
unique_numbers = {1, 2, 3, 2, 4, 3, 5}  # Duplicates removed
print(f"\nUnique numbers: {unique_numbers}")

# Type checking with isinstance()
print(f"\n=== Type Checking ===")
print(f"Is 'fruits' a list? {isinstance(fruits, list)}")
print(f"Is 'student' a dict? {isinstance(student, dict)}")
print(f"Is 'coordinates' a tuple? {isinstance(coordinates, tuple)}")
```

## Example 3 (Advanced)

```python
# Advanced Data Types and Type Handling
print("=== Advanced Data Types ===")

# Complex numbers
complex_num = 3 + 4j
print(f"Complex number: {complex_num}")
print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")

# Nested data structures
company = {
    "name": "TechCorp",
    "employees": [
        {"name": "Alice", "department": "Engineering", "salary": 75000},
        {"name": "Bob", "department": "Marketing", "salary": 65000},
        {"name": "Charlie", "department": "Engineering", "salary": 80000}
    ],
    "departments": {"Engineering", "Marketing", "HR"},
    "founded": (2020, 1, 15)  # Year, Month, Day
}

print(f"\nCompany: {company['name']}")
print("Employees:")
for emp in company["employees"]:
    print(f"  - {emp['name']} ({emp['department']}): ${emp['salary']}")

# Type introspection and dynamic type handling
def process_data(data):
    """Process data based on its type"""
    if isinstance(data, int):
        return f"Integer: {data * 2}"
    elif isinstance(data, float):
        return f"Float: {round(data, 2)}"
    elif isinstance(data, str):
        return f"String: {data.upper()}"
    elif isinstance(data, list):
        return f"List with {len(data)} items"
    elif isinstance(data, dict):
        return f"Dictionary with {len(data)} keys"
    else:
        return f"Unknown type: {type(data)}"

# Test with different data types
test_values = [42, 3.14159, "hello world", [1, 2, 3], {"key": "value"}]
print("\n=== Dynamic Type Processing ===")
for value in test_values:
    print(process_data(value))

# Custom class with type annotations (Python 3.5+)
from typing import List, Dict, Optional

class DataProcessor:
    def __init__(self):
        self.processed_data: List[Dict[str, str]] = []
    
    def add_record(self, name: str, value: str) -> None:
        self.processed_data.append({"name": name, "value": value})
    
    def get_records(self) -> List[Dict[str, str]]:
        return self.processed_data

# Using the class
processor = DataProcessor()
processor.add_record("temperature", "25.5")
processor.add_record("humidity", "60%")
print(f"\nProcessed data: {processor.get_records()}")
```

## Output

```
=== Basic Data Types ===
Age: 25, Type: <class 'int'>
Height: 5.9, Type: <class 'float'>
Name: Alice Johnson, Type: <class 'str'>
Is Student: True, Type: <class 'bool'>

=== Type Conversion ===
String number: 123, Type: <class 'str'>
Integer number: 123, Type: <class 'int'>
Float number: 123.0, Type: <class 'float'>

=== Complex Data Types ===
Fruits list: ['apple', 'banana', 'orange']
First fruit: apple
After adding grape: ['apple', 'banana', 'grape']

Student info: {'name': 'Bob', 'age': 20, 'grades': [85, 92, 78, 96], 'is_enrolled': True}
Student name: Bob
Average grade: 87.75

Coordinates: (10, 20)
X coordinate: 10

Unique numbers: {1, 2, 3, 4, 5}

=== Type Checking ===
Is 'fruits' a list? True
Is 'student' a dict? True
Is 'coordinates' a tuple? True

=== Advanced Data Types ===
Complex number: (3+4j)
Real part: 3.0, Imaginary part: 4.0

Company: TechCorp
Employees:
  - Alice (Engineering): $75000
  - Bob (Marketing): $65000
  - Charlie (Engineering): $80000

=== Dynamic Type Processing ===
Integer: 84
Float: 3.14
String: HELLO WORLD
List with 3 items
Dictionary with 1 keys

Processed data: [{'name': 'temperature', 'value': '25.5'}, {'name': 'humidity', 'value': '60%'}]
```

## Common Mistakes

| Mistake | Description | How to Avoid |
|---------|-------------|--------------|
| **Type Mismatch** | Adding string to integer | Use type conversion: `int()` or `str()` |
| **Index Errors** | Accessing non-existent list index | Check length with `len()` first |
| **Key Errors** | Accessing non-existent dictionary key | Use `.get()` method or check with `in` |
| **Immutable Modification** | Trying to change tuple values | Convert to list, modify, convert back |
| **Float Precision** | Comparing floats directly | Use `math.isclose()` for comparison |
| **String Concatenation** | Mixing strings and numbers without conversion | Always convert to string first |
| **List vs String** | Forgetting that strings are immutable | Use string methods that return new strings |
| **Shallow Copy Issues** | Modifying nested lists unexpectedly | Use `copy.deepcopy()` for nested structures |

## Best Practices

1. **Explicit Type Conversion**: Always convert types explicitly rather than relying on implicit conversion
2. **Type Checking**: Use `isinstance()` instead of `type()` for type checking
3. **Naming Conventions**: Use descriptive variable names that indicate data types
4. **Documentation**: Document expected data types in function docstrings
5. **Validation**: Validate data types when accepting user input
6. **Memory Efficiency**: Choose appropriate data types for memory constraints
7. **Consistency**: Maintain consistent data types within collections
8. **Error Handling**: Handle type-related exceptions gracefully
9. **Performance**: Use tuples for immutable sequences, lists for mutable ones
10. **Readability**: Use type hints for better code documentation

## Pro Tips

1. **Type Hints**: Use type hints for better code documentation and IDE support:
   ```python
   def calculate_area(length: float, width: float) -> float:
       return length * width
   ```

2. **F-string Debugging**: Use `!r` in f-strings for debugging:
   ```python
   value = "hello"
   print(f"{value!r}")  # Shows 'hello' with quotes
   ```

3. **Collections Module**: Leverage specialized data types:
   ```python
   from collections import defaultdict, Counter
   ```

4. **Memory View**: For large data processing, use memoryview for zero-copy slicing:
   ```python
   data = bytearray(b"Hello World")
   view = memoryview(data)
   ```

5. **Type Checking Libraries**: Use libraries like `mypy` for static type checking

6. **Data Classes**: For simple data containers, use `@dataclass`:
   ```python
   from dataclasses import dataclass
   @dataclass
   class Point:
       x: float
       y: float
   ```

7. **Generator Expressions**: For memory-efficient processing of large datasets

## Interview Questions (10)

1. What are the main categories of data types in Python?
2. Explain the difference between mutable and immutable data types.
3. How does Python handle memory allocation for different data types?
4. What is the difference between `type()` and `isinstance()`?
5. How do you handle type conversion errors in Python?
6. Explain the concept of duck typing in Python.
7. What are the performance implications of different data types?
8. How do you check if a variable is of a specific data type?
9. What happens when you modify a mutable object that's referenced by multiple variables?
10. Explain the difference between shallow copy and deep copy.

## MCQs (10)

1. **Which of the following is a mutable data type?**
   a) int
   b) str
   c) list
   d) tuple
   **Answer: c**

2. **What does the `type()` function return?**
   a) String representation of type
   b) Boolean value
   c) Type object
   d) None
   **Answer: c**

3. **Which data type is used to store key-value pairs?**
   a) list
   b) tuple
   c) dict
   d) set
   **Answer: c**

4. **What is the result of `isinstance(5, int)`?**
   a) "True"
   b) True
   c) False
   d) Error
   **Answer: b**

5. **Which of these cannot be used as a dictionary key?**
   a) string
   b) integer
   c) tuple
   d) list
   **Answer: d**

6. **What happens when you try to modify a tuple?**
   a) It gets modified
   b) TypeError is raised
   c) New tuple is created
   d) None of the above
   **Answer: b**

7. **Which function converts a string to integer?**
   a) str()
   b) int()
   c) float()
   d)