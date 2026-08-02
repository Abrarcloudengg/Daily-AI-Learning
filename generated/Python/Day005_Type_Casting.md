# Day 5: Type Casting in Python

## Explanation

Type casting (also known as type conversion) is the process of converting a value from one data type to another. Python provides built-in functions to perform type casting between different data types like integers, floats, strings, and booleans. There are two types of type casting:

1. **Implicit Type Casting**: Python automatically converts one data type to another
2. **Explicit Type Casting**: Programmer manually converts data types using built-in functions

## Syntax

```python
# Basic type casting functions
int()     # Converts to integer
float()   # Converts to float
str()     # Converts to string
bool()    # Converts to boolean
list()    # Converts to list
tuple()   # Converts to tuple
set()     # Converts to set
dict()    # Converts to dictionary
```

## Example Code

```python
# Type casting examples

# String to Integer
num_str = "123"
num_int = int(num_str)
print(f"String '{num_str}' to Integer: {num_int}")
print(f"Type: {type(num_int)}")

# String to Float
float_str = "45.67"
float_num = float(float_str)
print(f"String '{float_str}' to Float: {float_num}")
print(f"Type: {type(float_num)}")

# Integer to String
number = 42
number_str = str(number)
print(f"Integer {number} to String: '{number_str}'")
print(f"Type: {type(number_str)}")

# Float to Integer (truncates decimal part)
decimal_num = 9.87
int_num = int(decimal_num)
print(f"Float {decimal_num} to Integer: {int_num}")
print(f"Type: {type(int_num)}")

# Boolean conversions
print(f"Boolean of 0: {bool(0)}")
print(f"Boolean of 1: {bool(1)}")
print(f"Boolean of empty string: {bool('')}")
print(f"Boolean of 'hello': {bool('hello')}")

# Implicit type casting example
a = 5      # integer
b = 3.2    # float
c = a + b  # Python automatically converts int to float
print(f"Implicit casting: {a} + {b} = {c}")
print(f"Result type: {type(c)}")
```

## Output

```
String '123' to Integer: 123
Type: <class 'int'>
String '45.67' to Float: 45.67
Type: <class 'float'>
Integer 42 to String: '42'
Type: <class 'str'>
Float 9.87 to Integer: 9
Type: <class 'int'>
Boolean of 0: False
Boolean of 1: True
Boolean of empty string: False
Boolean of 'hello': True
Implicit casting: 5 + 3.2 = 8.2
Result type: <class 'float'>
```

## Common Mistakes

1. **Invalid String Conversion**:
   ```python
   # Wrong - This will raise ValueError
   num = int("hello")  # Cannot convert non-numeric string to int
   ```

2. **Incorrect Float String Format**:
   ```python
   # Wrong - This will raise ValueError
   num = float("3.4.5")  # Invalid float format
   ```

3. **Casting None**:
   ```python
   # Wrong - This will raise TypeError
   num = int(None)  # Cannot convert None to int
   ```

4. **Assuming Division Always Returns Integer**:
   ```python
   # Be careful - division always returns float in Python 3
   result = 10 / 2  # Returns 5.0, not 5
   ```

## Interview Questions

1. **What is the difference between implicit and explicit type casting?**
2. **What happens when you convert a float to an integer using `int()`?**
3. **How does `bool()` function work with different data types?**
4. **What is the result of `int("5.5")` and why?**
5. **Explain what happens in this code: `str(0)` vs `bool(0)`**
6. **What are the rules for converting strings to numbers?**
7. **How does Python handle type casting in arithmetic operations?**

## Practice Questions

1. Convert the string "123.45" to a float, then to an integer
2. Convert the boolean value `True` to an integer, then to a string
3. Take user input (which is always string) and convert it to appropriate numeric type
4. Convert a list `[1, 2, 3]` to a tuple, then to a set
5. What is the boolean value of an empty list `[]`?
6. Convert the integer 0 to boolean, then back to integer
7. Try converting "abc" to integer and handle the exception

## Assignment

**Grade Calculator with Type Casting**

Create a program that:
1. Takes student marks for 5 subjects as input (strings)
2. Converts them to appropriate numeric types
3. Calculates the total and percentage
4. Displays grades based on percentage
5. Handle invalid input gracefully

**Requirements:**
- Use proper type casting for input conversion
- Handle ValueError exceptions for invalid input
- Calculate percentage and assign grades:
  - 90-100: A+
  - 80-89: A
  - 70-79: B
  - 60-69: C
  - 50-59: D
  - Below 50: F
- Display formatted output with student information

**Sample Output:**
```
Enter marks for 5 subjects:
Math: 85
Science: 92
English: 78
History: 88
Geography: 90

Student Report:
Total Marks: 433
Percentage: 86.6%
Grade: A
```