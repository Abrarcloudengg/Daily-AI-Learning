# Day 3: Input and Output in Python

## Explanation

Input and output operations are fundamental to any programming language. In Python, we use `input()` to receive data from users and `print()` to display information. These functions allow our programs to interact with users, making them dynamic and useful.

The `input()` function always returns a string, so we need to convert it to the appropriate data type when necessary. The `print()` function can display multiple values and offers formatting options for better presentation.

## Syntax

### Input Function
```python
variable = input("Prompt message: ")
variable = int(input("Enter a number: "))  # Converting to integer
variable = float(input("Enter a decimal: "))  # Converting to float
```

### Print Function
```python
print(value)
print(value1, value2, value3)
print("Text with", variable)
print(f"Formatted string with {variable}")
print("Text {}".format(variable))
```

## Example Code

```python
# Basic input and output
name = input("What is your name? ")
print("Hello,", name + "!")

# Getting numerical input
age = int(input("How old are you? "))
years_to_hundred = 100 - age
print(f"You will be 100 years old in {years_to_hundred} years.")

# Multiple inputs
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
sum_result = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {sum_result}")

# Formatted output
product = first_number * second_number
print("Product: {:.2f}".format(product))  # Rounded to 2 decimal places

# Multiple values in print
print("Name:", name, "| Age:", age, "| Sum:", sum_result)
```

## Output

```
What is your name? Alice
Hello, Alice!
How old are you? 25
You will be 100 years old in 75 years.
Enter first number: 10.5
Enter second number: 3.2
The sum of 10.5 and 3.2 is 13.7
Product: 33.60
Name: Alice | Age: 25 | Sum: 13.7
```

## Common Mistakes

1. **Forgetting to convert input types:**
   ```python
   # Wrong - this will cause an error when doing math
   number = input("Enter a number: ")
   result = number + 10  # Error! Can't add string and int
   
   # Correct
   number = int(input("Enter a number: "))
   result = number + 10
   ```

2. **Not handling invalid input:**
   ```python
   # Wrong - will crash if user enters "abc"
   age = int(input("Enter your age: "))
   
   # Better approach
   try:
       age = int(input("Enter your age: "))
   except ValueError:
       print("Please enter a valid number")
   ```

3. **Using too many print statements:**
   ```python
   # Inefficient
   print("Name:")
   print(name)
   print("Age:")
   print(age)
   
   # Better
   print(f"Name: {name}\nAge: {age}")
   ```

4. **Forgetting comma in print function:**
   ```python
   # Wrong
   print("Hello" name)
   
   # Correct
   print("Hello", name)
   # or
   print("Hello " + name)
   ```

## Interview Questions

1. **What is the difference between `input()` in Python 2 and Python 3?**
   - In Python 2, `input()` evaluates the input as Python code, while `raw_input()` returns a string
   - In Python 3, `input()` always returns a string

2. **How do you handle invalid input from users?**
   - Use try-except blocks to catch ValueError exceptions
   - Implement input validation loops

3. **What are different ways to format output in Python?**
   - String concatenation with +
   - Comma separation in print()
   - .format() method
   - f-strings (formatted string literals)

4. **How do you read multiple values from a single input line?**
   ```python
   # Using split()
   x, y, z = input("Enter three numbers: ").split()
   ```

5. **What happens if you don't convert input data types?**
   - All input is treated as strings, causing issues with mathematical operations

## Practice Questions

1. Write a program that asks for a user's first name and last name, then prints their full name.

2. Create a simple calculator that takes two numbers and an operator (+, -, *, /) and displays the result.

3. Write a program that converts temperature from Celsius to Fahrenheit using the formula: F = (C × 9/5) + 32

4. Create a program that asks for the length and width of a rectangle and calculates its area and perimeter.

5. Write a program that takes a person's age and tells them how many days, hours, and minutes they've been alive (approximately).

## Assignment

**Student Grade Calculator**

Create a program that:
1. Asks for a student's name
2. Takes input for 5 subject marks (out of 100)
3. Calculates the total marks and percentage
4. Determines the grade based on:
   - 90-100%: A+
   - 80-89%: A
   - 70-79%: B
   - 60-69%: C
   - 50-59%: D
   - Below 50%: F
5. Displays a formatted report card with:
   - Student name
   - All subject marks
   - Total marks obtained
   - Percentage
   - Grade
   - Pass/Fail status (Pass if percentage >= 50%)

**Sample Output:**
```
Enter student name: John Smith
Enter marks for Math: 85
Enter marks for Science: 92
Enter marks for English: 78
Enter marks for History: 88
Enter marks for Geography: 90

-------- REPORT CARD --------
Student Name: John Smith
Math: 85
Science: 92
English: 78
History: 88
Geography: 90
Total Marks: 433/500
Percentage: 86.6%
Grade: A
Status: PASS
-----------------------------
```