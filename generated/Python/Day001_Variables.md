# Day 1: Python Variables

## What are Variables?

Variables are containers that store data values in Python. Think of them as labeled boxes where you can keep information. Each variable has a name (the label) and holds a value (the content inside the box).

## Variable Syntax

```python
variable_name = value
```

### Rules for Variable Names:
- Must start with a letter or underscore (_)
- Can contain letters, numbers, and underscores
- Cannot contain spaces or special characters
- Case-sensitive (age, Age, and AGE are different variables)

## Example Code

```python
# Creating variables
name = "Alice"
age = 25
height = 5.8
is_student = True

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Changing variable values
age = 26
print("New Age:", age)

# Multiple assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Same value to multiple variables
a = b = c = 100
print("a:", a, "b:", b, "c:", c)
```

## Output

```
Name: Alice
Age: 25
Height: 5.8
Is Student: True
New Age: 26
x: 10 y: 20 z: 30
a: 100 b: 100 c: 100
```

## Common Mistakes

1. **Using reserved keywords**: `if = 5` (Invalid - if is a reserved keyword)
2. **Starting with numbers**: `1variable = 10` (Invalid)
3. **Using spaces**: `my variable = 10` (Invalid)
4. **Forgetting case sensitivity**: `Name = "John"` and `name = "John"` are different
5. **Not assigning before using**: `print(undefined_variable)` (NameError)

## Interview Questions

1. **What is a variable in Python?**
2. **How do you assign a value to a variable?**
3. **Are variable names case-sensitive in Python?**
4. **What are the rules for naming variables in Python?**
5. **Can you change the value of a variable after assigning it?**

## Practice Questions

1. Create a variable called `city` and assign it the name of your favorite city.
2. Create three variables (num1, num2, num3) and assign them different integer values.
3. Create a boolean variable called `is_sunny` and set it to True.
4. Create two variables with the same value in one line.
5. Swap the values of two variables without using a third variable.

## Assignment

Create a Python program that:
1. Stores your name, age, and favorite color in variables
2. Prints these values with appropriate labels
3. Changes your age variable to next year's age
4. Prints the updated age
5. Create variables for your first name and last name separately, then combine them into a full name variable

**Bonus Challenge**: Research and try using different data types (string, integer, float, boolean) in your variables.