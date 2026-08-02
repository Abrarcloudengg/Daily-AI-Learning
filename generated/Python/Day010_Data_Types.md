# Data Types

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what data types are and their significance in programming
- Identify and work with different built-in data types in Python
- Convert between different data types using type casting
- Handle complex data structures like collections and custom objects
- Apply best practices for efficient data type usage
- Solve real-world problems using appropriate data types
- Prepare for technical interviews involving data types

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax
- Knowledge of variables and assignment operators
- Familiarity with basic programming concepts
- Python installed on your system
- A code editor or IDE ready for practice

## What is Data Types?

Data types in Python define the kind of value that can be stored in a variable. They determine:
- The type of data a variable can hold
- The operations that can be performed on that data
- How much memory space the data will occupy
- How the data is represented internally

Python is dynamically typed, meaning you don't need to explicitly declare data types - they're inferred automatically.

## Why is it Important?

Understanding data types is crucial because they:
- Help prevent runtime errors by ensuring compatibility between operations
- Optimize memory usage and performance
- Enable appropriate methods and functions for specific data kinds
- Improve code readability and maintainability
- Facilitate debugging and error handling
- Support efficient algorithm design and implementation

## Real World Analogy

Think of data types like different containers in a kitchen:
- **Integer** = Measuring cups (for whole numbers)
- **Float** = Kitchen scale (for precise measurements)
- **String** = Labels or recipe cards (for text)
- **Boolean** = Light switches (on/off states)
- **List** = Shopping bags (holding multiple items)
- **Dictionary** = Phone book (key-value pairs)

Each container serves a specific purpose and can only hold certain types of items effectively.

## Theory

Python has several categories of data types:

### Immutable Data Types
- **Numbers**: int, float, complex
- **Strings**: str
- **Tuples**: tuple
- **Frozen Sets**: frozenset
- **Bytes**: bytes

### Mutable Data Types
- **Lists**: list
- **Dictionaries**: dict
- **Sets**: set
- **Byte Arrays**: bytearray

### Built-in Data Types Classification

| Category | Type | Description |
|----------|------|-------------|
| Numeric | int | Integer numbers |
| Numeric | float | Decimal numbers |
| Numeric | complex | Complex numbers |
| Text | str | String sequences |
| Boolean | bool | True/False values |
| Sequence | list | Ordered, mutable collection |
| Sequence | tuple | Ordered, immutable collection |
| Mapping | dict | Key-value pairs |
| Set | set | Unordered unique elements |
| Binary | bytes | Immutable byte sequence |

## Syntax

```python
# Basic syntax for declaring variables with different data types
integer_var = 42
float_var = 3.14
complex_var = 2 + 3j
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
dict_var = {"name": "Alice", "age": 30}
set_var = {1, 2, 3}
```

## Flow / Working

1. **Variable Declaration**: Python automatically assigns a data type based on the assigned value
2. **Memory Allocation**: System allocates appropriate memory based on data type
3. **Type Checking**: Python verifies compatibility during operations
4. **Type Conversion**: Automatic or explicit conversion when needed
5. **Operation Execution**: Appropriate methods execute based on data type
6. **Memory Management**: Garbage collection handles unused variables

## Example 1 (Beginner)

```python
# Basic data types demonstration
print("=== Basic Data Types ===")

# Numbers
age = 25              # integer
height = 5.9          # float
complex_num = 3 + 4j  # complex number

print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Complex: {complex_num} (type: {type(complex_num)})")

# Strings
name = "John Doe"
message = 'Hello, Python!'
multiline = """This is a
multiline string"""

print(f"\nName: {name} (type: {type(name)})")
print(f"Message: {message}")
print(f"Multiline:\n{multiline}")

# Booleans
is_student = True
is_graduated = False

print(f"\nIs Student: {is_student} (type: {type(is_student)})")
print(f"Is Graduated: {is_graduated}")

# None type
empty_value = None
print(f"Empty Value: {empty_value} (type: {type(empty_value)})")
```

## Example 2 (Intermediate)

```python
# Collections and advanced operations
print("=== Collections and Type Operations ===")

# Lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

print(f"Fruits List: {fruits} (length: {len(fruits)})")
print(f"First fruit: {fruits[0]}")
fruits.append("grape")
print(f"After adding grape: {fruits}")

# Tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)

print(f"\nCoordinates: {coordinates} (immutable)")
print(f"Red component: {rgb_color[0]}")

# Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript"]
}

print(f"\nPerson Dictionary: {person}")
print(f"Person's name: {person['name']}")
person["email"] = "alice@example.com"
print(f"Updated person: {person}")

# Sets
unique_numbers = {1, 2, 3, 3, 4, 4, 5}  # duplicates removed
print(f"\nUnique Numbers Set: {unique_numbers}")

# Type checking and conversion
num_str = "123"
converted_num = int(num_str)
print(f"\nConverted '{num_str}' to {converted_num} (type: {type(converted_num)})")

# String formatting with different types
formatted_message = f"Age: {age}, Height: {height:.2f}, Name: {name}"
print(f"\nFormatted message: {formatted_message}")
```

## Example 3 (Advanced)

```python
# Advanced data types and custom implementations
print("=== Advanced Data Types ===")

import datetime
import decimal
from collections import namedtuple, defaultdict, Counter

# Custom data types using classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return self.__str__()

# Using namedtuple for structured data
Point = namedtuple('Point', ['x', 'y'])
point1 = Point(10, 20)
print(f"Named Tuple Point: {point1}, X: {point1.x}, Y: {point1.y}")

# Default dictionary with default values
word_count = defaultdict(int)
words = ["python", "java", "python", "javascript", "python"]
for word in words:
    word_count[word] += 1
print(f"\nWord Count: {dict(word_count)}")

# Counter for frequency analysis
text = "hello world hello python"
char_frequency = Counter(text)
print(f"\nCharacter Frequency: {char_frequency}")

# Decimal for precise calculations
price1 = decimal.Decimal('19.99')
price2 = decimal.Decimal('5.50')
total = price1 + price2
print(f"\nPrecise Calculation: {price1} + {price2} = {total}")

# Datetime objects
now = datetime.datetime.now()
future_date = now + datetime.timedelta(days=30)
print(f"\nCurrent time: {now}")
print(f"Future date: {future_date}")

# Custom object with type annotations (Python 3.5+)
def create_person(name: str, age: int) -> Person:
    return Person(name, age)

person_obj = create_person("Bob", 28)
print(f"\nCustom Person Object: {person_obj}")
print(f"Object type: {type(person_obj)}")

# Type introspection
print(f"\n--- Type Introspection ---")
data_types = [42, 3.14, "hello", [1,2,3], {"a": 1}, (1,2), {1,2,3}]
for item in data_types:
    print(f"{str(item):15} -> {type(item).__name__:10} -> Size: {item.__sizeof__()} bytes")
```

## Output

```
=== Basic Data Types ===
Age: 25 (type: <class 'int'>)
Height: 5.9 (type: <class 'float'>)
Complex: (3+4j) (type: <class 'complex'>)

Name: John Doe (type: <class 'str'>)
Message: Hello, Python!
Multiline:
This is a
multiline string

Is Student: True (type: <class 'bool'>)
Is Graduated: False
Empty Value: None (type: <class 'NoneType'>)

=== Collections and Type Operations ===
Fruits List: ['apple', 'banana', 'orange'] (length: 3)
First fruit: apple
After adding grape: ['apple', 'banana', 'orange', 'grape']

Coordinates: (10, 20) (immutable)
Red component: 255

Person Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York', 'skills': ['Python', 'JavaScript']}
Person's name: Alice
Updated person: {'name': 'Alice', 'age': 30, 'city': 'New York', 'skills': ['Python', 'JavaScript'], 'email': 'alice@example.com'}

Unique Numbers Set: {1, 2, 3, 4, 5}

Converted '123' to 123 (type: <class 'int'>)

Formatted message: Age: 25, Height: 5.90, Name: John Doe

=== Advanced Data Types ===
Named Tuple Point: Point(x=10, y=20), X: 10, Y: 20

Word Count: {'python': 3, 'java': 1, 'javascript': 1}

Character Frequency: Counter({'l': 5, 'o': 3, 'h': 2, ' ': 2, 'e': 1, 'w': 1, 'r': 1, 'd': 1, 'p': 1, 'y': 1, 't': 1, 'n': 1})

Precise Calculation: 19.99 + 5.50 = 25.49

Current time: 2024-01-15 14:30:45.123456
Future date: 2024-02-14 14:30:45.123456

Custom Person Object: Person(name='Bob', age=28)
Object type: <class '__main__.Person'>

--- Type Introspection ---
42              -> int        -> Size: 28 bytes
3.14            -> float      -> Size: 24 bytes
hello           -> str        -> Size: 54 bytes
[1, 2, 3]       -> list       -> Size: 80 bytes
{'a': 1}        -> dict       -> Size: 216 bytes
(1, 2)          -> tuple      -> Size: 48 bytes
{1, 2, 3}       -> set        -> Size: 216 bytes
```

## Common Mistakes

1. **Type Mismatch Errors**
   ```python
   # Wrong: Adding string and integer
   result = "5" + 3  # TypeError
   
   # Correct:
   result = int("5") + 3  # 8
   ```

2. **Mutable Default Arguments**
   ```python
   # Wrong:
   def add_item(item, target_list=[]):
       target_list.append(item)
       return target_list
   
   # Correct:
   def add_item(item, target_list=None):
       if target_list is None:
           target_list = []
       target_list.append(item)
       return target_list
   ```

3. **Incorrect Dictionary Key Access**
   ```python
   # Wrong:
   my_dict = {"name": "John"}
   value = my_dict["age"]  # KeyError
   
   # Correct:
   value = my_dict.get("age", "Unknown")  # Safe access
   ```

4. **Modifying Immutable Objects**
   ```python
   # Wrong:
   my_tuple = (1, 2, 3)
   my_tuple[0] = 5  # TypeError
   
   # Correct:
   my_list = list(my_tuple)
   my_list[0] = 5
   new_tuple = tuple(my_list)
   ```

5. **Floating Point Precision Issues**
   ```python
   # Wrong:
   result = 0.1 + 0.2  # 0.30000000000000004
   
   # Correct:
   from decimal import Decimal
   result = Decimal('0.1') + Decimal('0.2')  # 0.3
   ```

## Best Practices

1. **Use Type Hints for Clarity**
   ```python
   def calculate_area(length: float, width: float) -> float:
       return length * width
   ```

2. **Choose Appropriate Data Structures**
   - Use `list` for ordered, mutable sequences
   - Use `tuple` for immutable sequences
   - Use `set` for unique elements
   - Use `dict` for key-value mappings

3. **Validate Input Types**
   ```python
   def process_number(value):
       if not isinstance(value, (int, float)):
           raise TypeError("Expected numeric value")
       return value * 2
   ```

4. **Use Built-in Functions for Type Checking**
   ```python
   # Instead of type(var) == int
   if isinstance(var, int):
       # process integer
   ```

5. **Prefer Immutable Types When Possible**
   ```python
   # Use tuples instead of lists for fixed data
   coordinates = (x, y, z)  # Better than [x, y, z]
   ```

6. **Handle Type Conversions Safely**
   ```python
   def safe_int_conversion(value):
       try:
           return int(value)
       except (ValueError, TypeError):
           return None
   ```

7. **Use Enum for Constants**
   ```python
   from enum import Enum
   
   class Status(Enum):
       PENDING = 1
       APPROVED = 2
       REJECTED = 3
   ```

## Pro Tips

1. **Check Memory Usage**
   ```python
   import sys
   print(sys.getsizeof(your_variable))  # Check memory footprint
   ```

2. **Deep vs Shallow Copy**
   ```python
   import copy
   
   original = [[1, 2], [3, 4]]
   shallow = copy.copy(original)      # References same objects
   deep = copy.deepcopy(original)     # Completely independent copy
   ```

3. **Use `__slots__` for Memory Optimization**
   ```python
   class OptimizedClass:
       __slots__ = ['name', 'age']  # Reduces memory overhead
       
       def __init__(self, name, age):
           self.name = name
           self.age = age