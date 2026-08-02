# Day 2: Python Data Types

## Explanation

Data types are classifications that specify which kind of value a variable can hold. Python has several built-in data types that help us store and manipulate different kinds of information. Understanding data types is crucial for writing effective Python programs.

Python has two main categories of data types:
- **Built-in Data Types**: Predefined by Python (int, float, str, bool, etc.)
- **Derived Data Types**: Created from built-in types (list, tuple, dict, set, etc.)

## Syntax

Python is dynamically typed, meaning you don't need to explicitly declare the data type. Python automatically determines the type based on the value assigned.

```python
variable_name = value
```

## Example Code

```python
# Numeric Data Types
age = 25              # int (integer)
height = 5.9          # float
complex_num = 3 + 4j  # complex

# Text Data Type
name = "Alice"        # str (string)
grade = 'A'           # str (single character)

# Boolean Data Type
is_student = True     # bool
is_graduate = False   # bool

# None Type
result = None         # NoneType

# Displaying types
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Name: {name} (Type: {type(name)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")
print(f"Result: {result} (Type: {type(result)})")

# Type conversion examples
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(f"\nType Conversion:")
print(f"String '123' to int: {num_int} (Type: {type(num_int)})")
print(f"String '123' to float: {num_float} (Type: {type(num_float)})")
```

## Output

```
Age: 25 (Type: <class 'int'>)
Height: 5.9 (Type: <class 'float'>)
Name: Alice (Type: <class 'str'>)
Is Student: True (Type: <class 'bool'>)
Result: None (Type: <class 'NoneType'>)

Type Conversion:
String '123' to int: 123 (Type: <class 'int'>)
String '123' to float: 123.0 (Type: <class 'float'>)
```

## Common Mistakes

1. **Type Confusion**: Mixing strings and numbers in operations
   ```python
   # Wrong
   age = "25"
   next_year = age + 1  # This will cause an error
   
   # Correct
   age = "25"
   next_year = int(age) + 1  # Convert string to int first
   ```

2. **Incorrect Boolean Values**: Using lowercase or incorrect values
   ```python
   # Wrong
   is_valid = true  # Should be True
   is_complete = false  # Should be False
   
   # Correct
   is_valid = True
   is_complete = False
   ```

3. **String Concatenation with Numbers**: Forgetting to convert numbers to strings
   ```python
   # Wrong
   age = 25
   message = "I am " + age + " years old"  # Error!
   
   # Correct
   message = "I am " + str(age) + " years old"
   # Or better yet, use f-strings
   message = f"I am {age} years old"
   ```

## Interview Questions

1. **What are the different data types in Python?**
2. **Explain the difference between int and float data types.**
3. **What is the difference between list and tuple?**
4. **How do you check the data type of a variable in Python?**
5. **What is type casting? Give examples of implicit and explicit type casting.**
6. **What is the difference between None and empty string ""?**
7. **Explain mutable and immutable data types with examples.**

## Practice Questions

1. Create variables of different data types and print their values and types.
2. Convert a string "45.67" to a float and then to an integer.
3. Write a program that takes user input and determines its data type.
4. Create a boolean variable and demonstrate its use in an if statement.
5. Show the difference between `None` and `0` with examples.

## Assignment

**Personal Information Manager**

Create a Python program that stores and displays personal information using appropriate data types:

**Requirements:**
1. Store the following information using correct data types:
   - Full Name (string)
   - Age (integer)
   - Height in meters (float)
   - Is Student (boolean)
   - Grades in three subjects (list of integers)
   - Contact information (dictionary with phone and email)

2. Display all information in a formatted way
3. Calculate and display the average grade
4. Check if the person is eligible for a scholarship (average grade > 80 and is_student = True)

**Sample Output:**
```
=== Personal Information ===
Name: John Smith
Age: 20 years
Height: 1.75 meters
Student Status: True
Grades: [85, 92, 78]
Average Grade: 85.0
Scholarship Eligible: True

Contact Information:
Phone: 123-456-7890
Email: john@email.com
```

**Bonus Challenge:** Add type validation to ensure correct data types are entered.