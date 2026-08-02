# Day 4: Input and Output in Python

## Explanation

Input and Output (I/O) operations are fundamental to any programming language. In Python, we use `input()` to receive data from users and `print()` to display information. These functions allow our programs to interact with users, making them dynamic and interactive rather than static.

The `input()` function always returns a string, so we often need to convert it to other data types like integers or floats. The `print()` function can display multiple values and offers formatting options to make output more readable.

## Syntax

### Input Function
```python
variable = input("prompt message")
variable = int(input("prompt message"))  # for integers
variable = float(input("prompt message"))  # for decimal numbers
```

### Print Function
```python
print(value)
print(value1, value2, value3)
print("formatted string", variable)
print("text", variable, sep="separator", end="ending")
```

## Example Code

```python
# Basic input and output
name = input("What is your name? ")
print("Hello, " + name + "!")

# Input with type conversion
age = int(input("How old are you? "))
years_to_hundred = 100 - age
print("You will be 100 years old in", years_to_hundred, "years.")

# Multiple inputs
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
sum_result = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {sum_result}")

# Print formatting with separator and end parameters
print("Apple", "Banana", "Cherry", sep=" - ", end=" | ")
print("These are fruits")

# Using format() method
subject = "Python"
level = "beginner"
print("I am learning {} and I am a {}.".format(subject, level))
```

## Output

```
What is your name? Alice
Hello, Alice!
How old are you? 25
You will be 100 years old in 75 years.
Enter first number: 10.5
Enter second number: 20.3
The sum of 10.5 and 20.3 is 30.8
Apple - Banana - Cherry | These are fruits
I am learning Python and I am a beginner.
```

## Common Mistakes

1. **Forgetting type conversion**: 
   ```python
   # Wrong - this will cause errors in calculations
   age = input("Enter your age: ")  # Returns string
   next_year = age + 1  # Error: can't add string and integer
   
   # Correct
   age = int(input("Enter your age: "))
   next_year = age + 1
   ```

2. **Not handling invalid input**:
   ```python
   # This will crash if user enters "abc"
   number = int(input("Enter a number: "))
   
   # Better approach (will learn exception handling later)
   try:
       number = int(input("Enter a number: "))
   except ValueError:
       print("Please enter a valid number")
   ```

3. **Using + for concatenating strings and numbers**:
   ```python
   # Wrong
   age = 25
   print("I am " + age + " years old")  # Error!
   
   # Correct
   print("I am " + str(age) + " years old")
   # Or better yet:
   print(f"I am {age} years old")
   ```

4. **Forgetting newlines with print()**:
   ```python
   # These print on separate lines (default behavior)
   print("First line")
   print("Second line")
   
   # To print on same line:
   print("First part", end=" ")
   print("Second part")
   ```

## Interview Questions

1. **What is the difference between input() in Python 2 and Python 3?**
   - In Python 2, `input()` evaluates the input as Python code, while `raw_input()` returns a string
   - In Python 3, `input()` always returns a string (like Python 2's `raw_input()`)

2. **How do you handle invalid input in Python?**
   - Use try-except blocks to catch ValueError exceptions
   - Validate input before processing
   - Provide clear error messages to users

3. **What are different ways to format output in Python?**
   - String concatenation with +
   - Comma separation in print()
   - f-strings (f"Hello {name}")
   - .format() method
   - % formatting (older style)

4. **How do you take multiple inputs in a single line?**
   ```python
   # Using split()
   x, y, z = input("Enter three numbers: ").split()
   # Or with type conversion
   x, y, z = map(int, input("Enter three numbers: ").split())
   ```

## Practice Questions

1. Write a program that asks for a user's first name and last name, then prints their full name.

2. Create a simple calculator that takes two numbers and an operator (+, -, *, /) and displays the result.

3. Write a program that converts temperature from Celsius to Fahrenheit using the formula: F = (C × 9/5) + 32

4. Create a program that asks for the radius of a circle and calculates its area and circumference.

5. Write a program that takes a person's age and tells them how many days, hours, and minutes they've been alive (approximately).

## Assignment

**Student Grade Calculator**

Create a program that:
1. Asks for a student's name
2. Takes input for 5 subject marks (out of 100)
3. Calculates the total marks and percentage
4. Assigns a grade based on the percentage:
   - 90-100%: A+
   - 80-89%: A
   - 70-79%: B
   - 60-69%: C
   - 50-59%: D
   - Below 50%: F
5. Displays a formatted report card with all the information

**Sample Output:**
```
Enter student name: John Smith
Enter marks for Math: 85
Enter marks for Science: 92
Enter marks for English: 78
Enter marks for History: 88
Enter marks for Geography: 90

--------- REPORT CARD ---------
Student Name: John Smith
Math: 85
Science: 92
English: 78
History: 88
Geography: 90
Total Marks: 433/500
Percentage: 86.6%
Grade: A
-------------------------------
```

**Bonus Challenge**: Add input validation to ensure marks are between 0 and 100.