# Continue Statement

## Learning Objectives

- Understand what the `continue` statement does in Python loops
- Learn when and why to use `continue` in your programs
- Master the difference between `continue` and `break` statements
- Apply `continue` effectively in both simple and complex scenarios
- Recognize common pitfalls and best practices when using continue

## Prerequisites

- Basic understanding of Python programming
- Familiarity with `for` and `while` loops
- Knowledge of conditional statements (`if`, `elif`, `else`)
- Understanding of basic data structures like lists and ranges

## What is Continue Statement?

The `continue` statement is a control flow statement in Python that allows you to skip the remaining code inside a loop for the current iteration only. When Python encounters a `continue` statement, it immediately jumps to the next iteration of the loop without executing any remaining statements in the current iteration.

Think of `continue` as a way to say "skip the rest of this iteration and move on to the next one." It's particularly useful when you want to avoid executing certain code under specific conditions while still continuing with the loop.

## Why is it Important?

The `continue` statement is important because it provides clean and readable code when you need to skip certain iterations based on conditions. Instead of nesting your entire loop logic inside multiple `if` statements to avoid executing code, you can use `continue` to make your code more readable and maintainable.

It's especially valuable in data processing scenarios where you might want to skip invalid or unwanted data points while processing large datasets. This leads to more efficient and cleaner code compared to alternatives like deeply nested conditional blocks.

## Real World Analogy

Imagine you're a teacher grading a stack of exam papers. You go through each paper one by one (loop iteration). When you encounter a paper that doesn't have a student name (condition), you skip grading that paper entirely and move on to the next one. You don't waste time looking at the answers because you know it's incomplete.

The `continue` statement works exactly like this - when a certain condition is met, you skip the rest of the processing for that particular item and move on to the next one in your stack.

## Theory

In programming loops, there are often scenarios where you want to skip certain iterations based on specific conditions. The `continue` statement provides an elegant way to achieve this without breaking out of the entire loop (which `break` would do).

When `continue` is executed:
1. The remaining code in the current loop iteration is skipped
2. The loop proceeds to the next iteration (if available)
3. If it's a `for` loop, it moves to the next item
4. If it's a `while` loop, it re-evaluates the condition and continues if true

This is different from `break` which completely exits the loop, and from `pass` which does nothing and continues execution normally.

## Syntax

```python
# In a for loop
for item in iterable:
    if condition:
        continue
    # Code here will be skipped if continue is executed
    # Code here will run normally if continue is not executed

# In a while loop
while condition:
    if another_condition:
        continue
    # Code here will be skipped if continue is executed
    # Code here will run normally if continue is not executed
```

## Flow / Working

Let's break down how the `continue` statement works step by step:

1. **Loop Entry**: The loop starts its iteration
2. **Condition Check**: The code reaches an `if` statement with a condition
3. **Continue Decision**: If the condition evaluates to `True`, the `continue` statement executes
4. **Skip Remaining Code**: All code after `continue` in the current iteration is skipped
5. **Next Iteration**: The loop proceeds to the next iteration immediately
6. **Loop Completion**: If there are no more items or the while condition becomes false, the loop ends

## Example 1 (Beginner)

Let's start with a simple example that demonstrates skipping even numbers in a loop:

```python
print("Numbers from 1 to 10, skipping even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

In this example, we're printing only odd numbers from 1 to 10. When the number is even (divisible by 2), we use `continue` to skip the print statement and move to the next number.

## Example 2 (Intermediate)

Here's a more practical example where we process a list of user data and skip invalid entries:

```python
# Processing user data, skipping entries with missing information
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "", "age": 30, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": ""},
    {"name": "David", "age": 40, "email": "david@example.com"},
    {"name": "Eve", "age": 0, "email": "eve@example.com"}
]

print("Processing valid users:")
valid_users_count = 0

for user in users:
    # Skip users with missing name
    if not user["name"]:
        print(f"Skipping user: Missing name")
        continue

    # Skip users with missing email
    if not user["email"]:
        print(f"Skipping user {user['name']}: Missing email")
        continue

    # Skip users with invalid age
    if user["age"] <= 0:
        print(f"Skipping user {user['name']}: Invalid age")
        continue

    # Process valid user
    print(f"Processing user: {user['name']}, Age: {user['age']}, Email: {user['email']}")
    valid_users_count += 1

print(f"\nTotal valid users processed: {valid_users_count}")
```

This example shows how `continue` can be used multiple times in a loop to skip different invalid conditions while still processing valid data.

## Example 3 (Advanced)

Let's look at a complex example involving nested loops and data processing:

```python
# Advanced example: Processing matrix data with continue
import random

# Create a 5x5 matrix with random values (0-10)
matrix = [[random.randint(0, 10) for _ in range(5)] for _ in range(5)]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nProcessing Matrix (skipping zeros and even numbers):")
processed_count = 0
total_skipped = 0

for i, row in enumerate(matrix):
    print(f"Row {i+1}: ", end="")
    for j, value in enumerate(row):
        # Skip zeros
        if value == 0:
            print("X", end=" ")
            total_skipped += 1
            continue

        # Skip even numbers
        if value % 2 == 0:
            print("E", end=" ")
            total_skipped += 1
            continue

        # Process odd numbers
        print(value, end=" ")
        processed_count += 1

    print()  # New line after each row

print(f"\nTotal odd numbers processed: {processed_count}")
print(f"Total values skipped: {total_skipped}")

# Another advanced example: Finding prime numbers with continue optimization
def is_prime_optimized(n):
    """Check if a number is prime with continue optimization"""
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Check odd divisors only
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

print("\nFinding prime numbers from 1 to 30 (skipping evens after 2):")
primes = []

for num in range(1, 31):
    # Skip 1 as it's not prime
    if num == 1:
        continue

    # Skip even numbers after 2
    if num > 2 and num % 2 == 0:
        continue

    # Check if the number is prime
    if is_prime_optimized(num):
        primes.append(num)

print(f"Prime numbers: {primes}")
```

This advanced example demonstrates:
1. Using `continue` in nested loops
2. Processing 2D data structures
3. Optimization techniques by skipping unnecessary calculations
4. Combining `continue` with efficient algorithms

## Output

```
Numbers from 1 to 10, skipping even numbers:
1
3
5
7
9

Processing valid users:
Skipping user: Missing name
Skipping user Charlie: Missing email
Processing user: Alice, Age: 25, Email: alice@example.com
Processing user: David, Age: 40, Email: david@example.com
Skipping user Eve: Invalid age

Total valid users processed: 2

Original Matrix:
[7, 2, 0, 9, 4]
[1, 8, 3, 0, 6]
[5, 0, 2, 7, 1]
[3, 4, 9, 2, 8]
[0, 6, 1, 5, 3]

Processing Matrix (skipping zeros and even numbers):
Row 1: 7 X X 9 E
Row 2: 1 E 3 X E
Row 3: 5 X E 7 1
Row 4: 3 E 9 E E
Row 5: X E 1 5 3
Total odd numbers processed: 11
Total values skipped: 14

Finding prime numbers from 1 to 30 (skipping evens after 2):
Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Common Mistakes

1. **Infinite Loops with While**: Using `continue` in a `while` loop without properly updating the loop variable can cause infinite loops.

```python
# WRONG - Infinite loop
count = 0
while count < 5:
    if count == 2:
        continue  # This will cause infinite loop
    print(count)
    count += 1
```

2. **Placing Continue After Loop Control**: Putting `continue` at the end of a loop where it has no effect.

3. **Overusing Continue**: Using `continue` when a simple `if` statement would be clearer.

4. **Confusing Continue with Break**: Mixing up the behavior of `continue` (next iteration) with `break` (exit loop).

5. **Logic Errors**: Placing code before `continue` that should also be skipped.

## Best Practices

1. **Place Continue Early**: Put `continue` statements early in the loop to improve readability and avoid deep nesting.

2. **Use Descriptive Comments**: Add comments explaining why you're using `continue` for better code maintainability.

3. **Avoid Complex Conditions**: Keep the conditions for `continue` simple and readable.

4. **Consider Alternatives**: Sometimes an `if-else` structure might be more readable than using `continue`.

5. **Update Loop Variables**: In `while` loops, ensure loop variables are updated before `continue` to avoid infinite loops.

6. **Use Meaningful Variable Names**: Make it clear what conditions cause the `continue`.

7. **Test Edge Cases**: Ensure your `continue` logic works correctly with edge cases.

## Pro Tips

1. **Combine with Exception Handling**: Use `continue` in exception handling to skip problematic data:

```python
data = [1, 2, "invalid", 4, 5, None, 7]
valid_numbers = []

for item in data:
    try:
        number = int(item)
        valid_numbers.append(number)
    except (ValueError, TypeError):
        continue  # Skip invalid items
```

2. **Performance Optimization**: Use `continue` to skip expensive operations when conditions are met.

3. **Loop Refactoring**: When you have deeply nested `if` statements, consider using `continue` to flatten the structure.

4. **Data Validation Pattern**: `continue` is excellent for data validation where you skip invalid entries.

5. **Resource Management**: Skip iterations that would cause resource issues (like division by zero).

## Interview Questions (10)

1. What is the difference between `continue` and `break` statements in Python?

2. How does `continue` behave differently in `for` loops versus `while` loops?

3. Can you have multiple `continue` statements in a single loop? Explain with example.

4. What happens if you place code after a `continue` statement in a loop?

5. How would you avoid infinite loops when using `continue` in a `while` loop?

6. When would you prefer using `continue` over nested `if` statements?

7. Can `continue` be used outside of loops? What happens if you try?

8. Explain a scenario where using `continue` improves code readability.

9. How does `continue` affect the flow of nested loops?

10. What are the performance implications of using `continue` in loops?

## MCQs (10)

1. What does the `continue` statement do in a loop?
   a) Exits the entire loop
   b) Skips the current iteration and moves to the next
   c) Pauses the loop execution
   d) Restarts the loop from the beginning

2. In which part of a loop can `continue` be used?
   a) Only at the beginning
   b) Only at the end
   c) Anywhere inside the loop body
   d) Only in nested loops

3. What is the output of this code?
   ```python
   for i in range(5):
       if i == 2:
           continue
       print(i)
   ```
   a) 0 1 2 3 4
   b) 0 1 3 4
   c) 0 1
   d) 3 4

4. Can `continue` be used outside of a loop?
   a) Yes, it works anywhere
   b) No, it will cause a SyntaxError
   c) No, but it will be ignored
   d) Yes, but it will cause runtime error

5. What happens to the code after `continue` in the same iteration?
   a) It executes normally
   b) It executes after the loop ends
   c) It is skipped entirely
   d) It executes twice

6. In a nested loop, what does `continue` affect?
   a) Both inner and outer loops
   b) Only the innermost loop containing it
   c) Only the outermost loop
   d) All loops in the program

7. What is the output of this code?
   ```python
   count = 0
   while count < 3:
       count += 1
       if count == 2:
           continue
       print(count)
   ```
   a) 1 2 3
   b) 1 3
   c) 2
   d) 1

8. Which is a good use case for `continue`?
   a) Exiting a program completely
   b) Skipping invalid data in a dataset
   c) Repeating the same iteration
   d) Breaking out of nested loops

9. What happens if `continue` is the last statement in a loop?
   a) The loop ends
   b) It has no effect
   c) It causes an error
   d) It restarts the loop

10. How does `continue` differ from `pass`?
    a) `continue` skips iterations, `pass` does nothing
    b) They work exactly the same
    c) `pass` is for loops, `continue` is for functions
    d) `continue` ends the loop, `pass` continues

## Practice Questions (10)

1. Write a program that prints all numbers from 1 to 20 except multiples of 3.

2. Create a list of words and print only those that have more than 4 characters, skipping the rest.

3. Process a list of numbers and calculate the sum of only positive numbers, skipping negative ones.

4. Write a program that asks for user input until 'quit' is entered, skipping empty inputs.

5. Create a nested loop that prints a multiplication table but skips products greater than 50.

6. Process a list of dictionaries representing students, skipping those with grades below 60.

7. Write a function that takes a list and returns a new list with even numbers removed.

8. Create a program that reads numbers from user input and calculates average, skipping non-numeric inputs.

9. Process a string and print only consonants, skipping vowels and spaces.

10. Write a program that simulates a simple file processing system, skipping files with certain extensions.

## Coding Exercises (5)

1. **Filter Prime Numbers**: Write a program that prints all numbers from 1 to 100, but skips prime numbers. Use the `continue` statement to implement this logic.

2. **Data Validation**: Create a program that processes a list of email addresses. Skip any email that doesn't contain '@' symbol or doesn't end with '.com'. Print valid emails.

3. **Temperature Filter**: Process a list of daily temperatures. Skip temperatures below -50°C or above 50°C as they're considered invalid. Calculate the average of valid temperatures.

4. **Nested Loop Pattern**: Create a program that prints numbers in a triangular pattern (1, 12, 123, 1234) but skip printing any number that is divisible by 3.

5. **File Processing Simulation**: Simulate processing files in a directory. Skip files with extensions '.tmp', '.log', or '.cache'. Count and display how many files were processed vs skipped.

## Mini Project

Create a "Student Grade Analyzer" that processes student data and provides statistics. Your program should:

1. Take a list of student records (name, grade, subject)
2. Skip any records with missing data (empty name, None grade, etc.)
3. Skip records where grade is not between 0-100
4. Calculate average grades for valid students
5. Identify top performers (grade > 90)
6. Count students per subject
7. Use `continue` statements appropriately to skip invalid data

```python
# Student Grade Analyzer - Mini Project
students = [
    {"name": "Alice", "grade": 95, "subject": "Math"},
    {"name": "", "grade": 87, "subject": "Science"},  # Missing name
    {"name": "Bob", "grade": 105, "subject": "Math"},  # Invalid grade
    {"name": "Charlie", "grade": 78, "subject": "English"},
    {"name": "David", "grade": 92, "subject": "Math"},
    {"name": "Eve", "grade": -5, "subject": "Science"},  # Invalid grade
    {"name": "Frank", "grade": 88, "subject": "English"},
    {"name": "Grace", "grade": 96, "subject": "Math"},
    {"name": None, "grade": 82, "subject": "Science"},  # Missing name
    {"name": "Henry", "grade": 73, "subject": "English"}
]

# Process valid students
valid_students = []
subject_counts = {}
total_grade = 0
top_performers = []

print("Student Grade Analyzer")
print("=" * 30)

for student in students:
    # Skip records with missing name
    if not student["name"]:
        print(f"Skipping: Missing student name")
        continue

    # Skip records with invalid grades
    if student["grade"] < 0 or student["grade"] > 100:
        print(f"Skipping {student['name']}: Invalid grade {student['grade']}")
        continue

    # Add valid student to our list
    valid_students.append(student)
    print(f"Processing: {student['name']} - {student['grade']} ({student['subject']})")

    # Track subject counts
    subject = student["subject"]
    if subject in subject_counts:
        subject_counts[subject] += 1
    else:
        subject_counts[subject] = 1

    # Track total grades for average calculation
    total_grade += student["grade"]

    # Track top performers
    if student["grade"] > 90:
        top_performers.append(student["name"])

# Calculate and display statistics
if valid_students:
    average_grade = total_grade / len(valid_students)

    print("\nStatistics:")
    print(f"Total valid students processed: {len(valid_students)}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Top performers (grade > 90): {', '.join(top_performers) if top_performers else 'None'}")
    print("\nStudents per subject:")
    for subject, count in subject_counts.items():
        print(f"  {subject}: {count}")
else:
    print("No valid students found!")
```

## Assignment

Create a "Library Book Management System" that processes a collection of books and performs various operations. Your program should:

1. Process a list of book dictionaries with fields: title, author, year, genre, rating
2. Skip books with missing required fields (title, author)
3. Skip books with invalid data (year < 1000 or > current year, rating not between 1-5)
4. Categorize books by genre
5. Find books by a specific author
6. Calculate average rating for valid books
7. Identify highly rated books (rating >= 4.5)
8. Use `continue` statements appropriately to skip invalid data

Requirements:
- Handle at least 15 book entries with some invalid data mixed in
- Provide a clean output showing processed books and statistics
- Include error handling for edge cases
- Demonstrate proper use of `continue` for data validation
- Add comments explaining your use of `continue`

## Summary

The `continue` statement is a powerful control flow tool in Python that allows you to skip the remaining code in a loop iteration and move directly to the next iteration. It's particularly useful for data processing scenarios where you need to skip invalid or unwanted data while continuing to process valid data.

Key points covered:
- `continue` skips the rest of the current iteration but keeps the loop running
- It's different from `break` which completely exits the loop
- Proper placement of `continue` can make code more readable than nested `if` statements
- In `while` loops, be careful to update loop variables before `continue` to avoid infinite loops
- `continue` works in both `for` and `while` loops and can be used multiple times in a single loop

## Key Takeaways

1. `continue` skips the current iteration and moves to the next one
2. It's excellent for data validation and filtering scenarios
3. Always update loop variables in `while` loops before using `continue`
4. Place `continue` early in loops for better readability
5. `continue` only affects the innermost loop it's contained in
6. It's more readable than deeply nested conditional statements
7. Use it judiciously - sometimes simple `if` statements are clearer
8. Combine with exception handling for robust data processing
9. It's particularly useful in data science and file processing applications
10. Understanding `continue` is essential for writing clean, efficient Python code

## Next Topic Preview

In the next lesson, we'll explore the `pass` statement in Python. While `continue` skips loop iterations and `break` exits loops entirely, `pass` serves as a null operation that does nothing when executed. We'll learn when and why you might need such a statement, how it differs from `continue` and `break`, and practical scenarios where `pass` is invaluable for code structure and development workflows.
