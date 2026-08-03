# Operators

## Learning Objectives
- Understand different types of operators in Python
- Learn how to use arithmetic, comparison, logical, and assignment operators
- Master bitwise and membership operators
- Apply operators in complex expressions and real-world scenarios
- Recognize operator precedence and associativity rules

## Prerequisites
- Basic understanding of Python syntax
- Knowledge of variables and data types
- Familiarity with basic programming concepts

## What is Operators?

Operators in Python are special symbols that perform operations on variables and values. They are fundamental building blocks that enable mathematical calculations, logical comparisons, and data manipulation. Operators take one or more operands (values or variables) and return a result based on the operation performed.

## Why is it Important?

Operators are essential because they:
- Enable mathematical and logical operations in programs
- Simplify complex calculations and comparisons
- Form the foundation for expressions and conditions
- Allow efficient data manipulation and decision-making
- Are crucial for algorithm implementation and problem-solving

## Real World Analogy

Think of operators like tools in a toolbox:
- Arithmetic operators (+, -, *, /) are like basic tools (hammer, screwdriver)
- Comparison operators (==, >, <) are like measuring instruments (ruler, scale)
- Logical operators (and, or, not) are like decision-making processes
- Assignment operators (=, +=, -=) are like storage containers that hold and modify values

## Theory

Python operators can be categorized into several types:

### 1. Arithmetic Operators
Perform mathematical operations on numeric values.

### 2. Comparison/Relational Operators
Compare values and return boolean results.

### 3. Logical Operators
Combine boolean expressions.

### 4. Assignment Operators
Assign values to variables.

### 5. Bitwise Operators
Work on binary representations of integers.

### 6. Membership Operators
Test if a value exists in a sequence.

### 7. Identity Operators
Compare the identity of two objects.

## Syntax

```python
# Arithmetic: operand1 operator operand2
result = a + b

# Comparison: operand1 operator operand2
is_equal = a == b

# Logical: operand1 operator operand2
result = condition1 and condition2

# Assignment: variable operator= value
x += 5  # equivalent to x = x + 5
```

## Flow / Working

1. Operators receive operands as input
2. Perform the specified operation
3. Return the result based on operator type
4. Results can be stored in variables or used directly
5. Operator precedence determines evaluation order
6. Parentheses can override default precedence

## Example 1 (Beginner)

```python
# Basic arithmetic operations
print("=== Arithmetic Operators ===")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# Comparison operations
print("\n=== Comparison Operators ===")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Assignment operations
print("\n=== Assignment Operators ===")
x = 5
print(f"Initial x = {x}")
x += 3  # x = x + 3
print(f"After x += 3: {x}")
x *= 2  # x = x * 2
print(f"After x *= 2: {x}")
```

## Example 2 (Intermediate)

```python
# Logical and bitwise operations
print("=== Logical Operators ===")
age = 25
has_license = True
is_student = False

# AND operator - both conditions must be True
can_drive = age >= 18 and has_license
print(f"Can drive (age >= 18 and has_license): {can_drive}")

# OR operator - at least one condition must be True
discount_eligible = age < 18 or is_student
print(f"Discount eligible (age < 18 or is_student): {discount_eligible}")

# NOT operator - negates the boolean value
print(f"Not a student: {not is_student}")

print("\n=== Membership Operators ===")
fruits = ["apple", "banana", "orange", "grape"]
print(f"fruits list: {fruits}")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'mango' not in fruits: {'mango' not in fruits}")

print("\n=== Identity Operators ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list2: {list1 == list2}")

print("\n=== Bitwise Operators ===")
x = 12  # Binary: 1100
y = 10  # Binary: 1010

print(f"x = {x} (binary: {bin(x)})")
print(f"y = {y} (binary: {bin(y)})")
print(f"Bitwise AND (x & y): {x & y} (binary: {bin(x & y)})")
print(f"Bitwise OR (x | y): {x | y} (binary: {bin(x | y)})")
print(f"Bitwise XOR (x ^ y): {x ^ y} (binary: {bin(x ^ y)})")
print(f"Bitwise NOT (~x): {~x} (binary: {bin(~x & 0xFF)})")
print(f"Left shift (x << 2): {x << 2} (binary: {bin(x << 2)})")
print(f"Right shift (x >> 2): {x >> 2} (binary: {bin(x >> 2)})")
```

## Example 3 (Advanced)

```python
# Complex expressions and operator precedence
print("=== Operator Precedence ===")

# Without parentheses
result1 = 2 + 3 * 4 ** 2
print(f"2 + 3 * 4 ** 2 = {result1}")

# With parentheses to show order
result2 = 2 + 3 * (4 ** 2)
print(f"2 + 3 * (4 ** 2) = {result2}")

# Complex logical expression
age = 30
income = 50000
credit_score = 700
is_employed = True

loan_approved = (age >= 21 and income >= 30000) and (credit_score >= 650 or is_employed)
print(f"\nLoan approval criteria: (age >= 21 and income >= 30000) and (credit_score >= 650 or is_employed)")
print(f"Loan approved: {loan_approved}")

# Chained comparisons
x = 15
chained_result = 10 < x < 20
print(f"\nChained comparison 10 < {x} < 20: {chained_result}")

# Ternary operator (conditional expression)
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"\nScore: {score}, Grade: {grade}")

# Walrus operator (Python 3.8+)
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(f"\nList has {n} elements, which is more than 3")

# Operator overloading example
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2  # Uses overloaded + operator
print(f"\nVector addition: {v1} + {v2} = {v3}")
```

## Output

```
=== Arithmetic Operators ===
a = 10, b = 3
Addition (a + b): 13
Subtraction (a - b): 7
Multiplication (a * b): 30
Division (a / b): 3.3333333333333335
Floor Division (a // b): 3
Modulus (a % b): 1
Exponentiation (a ** b): 1000

=== Comparison Operators ===
a == b: False
a != b: True
a > b: True
a < b: False
a >= b: True
a <= b: False

=== Assignment Operators ===
Initial x = 5
After x += 3: 8
After x *= 2: 16

=== Logical Operators ===
Can drive (age >= 18 and has_license): True
Discount eligible (age < 18 or is_student): False
Not a student: True

=== Membership Operators ===
fruits list: ['apple', 'banana', 'orange', 'grape']
'banana' in fruits: True
'mango' not in fruits: True

=== Identity Operators ===
list1: [1, 2, 3]
list2: [1, 2, 3]
list3: [1, 2, 3]
list1 is list2: False
list1 is list3: True
list1 == list2: True

=== Bitwise Operators ===
x = 12 (binary: 0b1100)
y = 10 (binary: 0b1010)
Bitwise AND (x & y): 8 (binary: 0b1000)
Bitwise OR (x | y): 14 (binary: 0b1110)
Bitwise XOR (x ^ y): 6 (binary: 0b110)
Bitwise NOT (~x): -13 (binary: 0b11110011)
Left shift (x << 2): 48 (binary: 0b110000)
Right shift (x >> 2): 3 (binary: 0b11)

=== Operator Precedence ===
2 + 3 * 4 ** 2 = 50
2 + 3 * (4 ** 2) = 50

Loan approval criteria: (age >= 21 and income >= 30000) and (credit_score >= 650 or is_employed)
Loan approved: True

Chained comparison 10 < 15 < 20: True

Score: 85, Grade: Pass

List has 5 elements, which is more than 3

Vector addition: Vector(2, 3) + Vector(1, 4) = Vector(3, 7)
```

## Common Mistakes

| Mistake | Explanation | Correct Approach |
|---------|-------------|------------------|
| `==` vs `=` | Using assignment instead of comparison | Use `==` for comparison |
| Order of operations | Forgetting operator precedence | Use parentheses to clarify |
| `is` vs `==` | Confusing identity with equality | Use `==` for value comparison |
| Integer division | Expecting float from `/` in Python 2 | Use `//` for floor division |
| Bitwise vs Logical | Using `&` instead of `and` for booleans | Use logical operators for booleans |
| Modulo with negative numbers | Misunderstanding negative modulo | Test behavior with negative numbers |

## Best Practices

1. **Use parentheses for clarity**: Even when not required, parentheses make code readable
2. **Choose appropriate operators**: Use `is` for None checks, `==` for value comparison
3. **Understand operator precedence**: Know when parentheses are needed
4. **Use descriptive variable names**: Makes operator expressions self-documenting
5. **Avoid complex chained operations**: Break complex expressions into simpler parts
6. **Use walrus operator judiciously**: Only when it improves readability
7. **Be explicit with boolean operations**: Don't rely on truthiness unnecessarily

## Pro Tips

1. **Short-circuit evaluation**: `and`/`or` operators don't evaluate second operand if first determines result
2. **Chained comparisons**: `10 < x < 20` is equivalent to `10 < x and x < 20`
3. **Ternary operator**: `value_if_true if condition else value_if_false`
4. **Walrus operator**: Assign and evaluate in same expression (Python 3.8+)
5. **Bitwise for powers of 2**: `x << n` is faster than `x * (2**n)`
6. **Membership testing**: `in` operator works with any iterable
7. **Identity vs Equality**: `is` checks object identity, `==` checks value equality

## Interview Questions (10)

1. Explain the difference between `==` and `is` operators in Python.
2. What is operator precedence and how does it affect expression evaluation?
3. How do logical operators use short-circuit evaluation?
4. What are the differences between `/`, `//`, and `%` division operators?
5. Explain the use cases for bitwise operators in Python.
6. How does Python's membership operator work with different data types?
7. What is the ternary operator and how is it used in Python?
8. Describe the walrus operator and when to use it.
9. How do identity operators differ from equality operators?
10. What are the rules for operator overloading in Python?

## MCQs (10)

1. **What is the result of `5 ** 2`?**
   a) 10
   b) 25
   c) 7
   d) 3

2. **Which operator is used for integer division?**
   a) /
   b) //
   c) %
   d) **

3. **What does the `not` operator return?**
   a) The opposite boolean value
   b) The same boolean value
   c) None
   d) 0

4. **Which operator checks if an item exists in a sequence?**
   a) is
   b) in
   c) ==
   d) &

5. **What is the result of `10 % 3`?**
   a) 3
   b) 1
   c) 3.33
   d) 0

6. **Which has higher precedence: `+` or `*`?**
   a) +
   b) *
   c) Same precedence
   d) Depends on operands

7. **What does `x //= 3` do?**
   a) Divides x by 3
   b) Performs floor division and assigns result to x
   c) Multiplies x by 3
   d) Returns remainder of x/3

8. **Which operator is used for bitwise AND?**
   a) &
   b) &&
   c) and
   d) |

9. **What is the result of `True and False`?**
   a) True
   b) False
   c) None
   d) Error

10. **What does