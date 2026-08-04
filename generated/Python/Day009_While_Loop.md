# While Loop

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand the concept and purpose of while loops
- Write and execute while loops in Python
- Differentiate between while and for loops
- Implement while loops with various conditions and control statements
- Debug common while loop issues
- Apply while loops to solve real-world programming problems
- Use advanced techniques like nested while loops and loop control statements

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax
- Knowledge of variables and data types
- Familiarity with conditional statements (if-else)
- Understanding of basic input/output operations
- Basic knowledge of operators in Python

## What is While Loop?

A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. It's called a "loop" because the code block continues to execute in a cycle until the condition becomes false. The while loop is particularly useful when you don't know in advance how many times the loop needs to execute.

Think of a while loop as a repetitive decision-making process. As long as a certain condition remains true, the program keeps executing the same block of code. Once the condition becomes false, the loop stops and the program continues with the next statement after the loop.

## Why is it Important?

While loops are fundamental in programming because they allow us to:
- Automate repetitive tasks without writing the same code multiple times
- Process data until a specific condition is met
- Create interactive programs that continue running until the user decides to stop
- Implement algorithms that require iterative processing
- Handle unknown quantities of data or operations

They're essential for creating dynamic, responsive programs that can adapt to changing conditions during execution.

## Real World Analogy

Think of a while loop like following a recipe instruction: "Keep stirring the sauce until it thickens." You don't know exactly how long it will take - maybe 2 minutes, maybe 5 minutes. You keep performing the action (stirring) while the condition is true (sauce isn't thick yet). As soon as the sauce reaches the desired thickness, you stop stirring.

Another example is a security guard making rounds: "Keep checking doors until all 20 doors have been verified." The guard doesn't know how many rounds it will take - they continue the process while there are still unverified doors.

## Theory

A while loop evaluates a condition before each iteration. If the condition is true, the loop body executes. After executing the body, the condition is checked again. This process repeats until the condition becomes false.

Key theoretical concepts:
1. **Condition Evaluation**: The condition is checked before each iteration
2. **Loop Body**: The block of code that executes repeatedly
3. **Iteration**: Each execution of the loop body
4. **Termination**: The loop stops when the condition becomes false
5. **Infinite Loop**: When the condition never becomes false, the loop runs forever

The while loop is particularly useful when the number of iterations is not predetermined but depends on a dynamic condition.

## Syntax

The basic syntax of a while loop in Python is:

```python
while condition:
    # code block to execute
    # can be one or multiple statements
```

Key components:
- `while`: The keyword that starts the loop
- `condition`: A Boolean expression that determines if the loop continues
- `:`: Colon that ends the while statement
- Indented block: The code that executes repeatedly

Optional components:
```python
while condition:
    # code block
else:
    # optional else block executes when condition becomes false
```

## Flow / Working

The flow of a while loop works as follows:

1. **Condition Check**: The condition is evaluated first
2. **Decision**: If condition is True, proceed to step 3; if False, exit the loop
3. **Execute Body**: Run all statements in the loop body
4. **Return**: Go back to step 1
5. **Exit**: When condition becomes False, continue with the next statement after the loop

This is a pre-test loop because the condition is checked before each iteration, meaning the loop body might never execute if the initial condition is False.

## Example 1 (Beginner)

Let's start with a simple example that counts from 1 to 5:

```python
# Initialize counter
count = 1

# While loop to print numbers from 1 to 5
while count <= 5:
    print(f"Count is: {count}")
    count = count + 1  # Increment the counter

print("Loop finished!")
```

In this example:
- We initialize a counter variable to 1
- The loop continues while count is less than or equal to 5
- Inside the loop, we print the current count and increment it
- When count becomes 6, the condition is false and the loop ends

## Example 2 (Intermediate)

Let's create a more practical example that calculates the factorial of a number:

```python
# Calculate factorial of a number using while loop
number = 5
factorial = 1
counter = 1

print(f"Calculating factorial of {number}")

while counter <= number:
    factorial = factorial * counter
    print(f"Step {counter}: factorial = {factorial}")
    counter = counter + 1

print(f"Factorial of {number} is {factorial}")
```

This example demonstrates:
- Using multiple variables in the loop
- Performing calculations in each iteration
- Tracking the process with intermediate outputs
- More complex logic within the loop body

## Example 3 (Advanced)

Let's implement a number guessing game with while loop and additional features:

```python
import random

# Number guessing game
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
guessed_correctly = False

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts and not guessed_correctly:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            guessed_correctly = True
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0 and not guessed_correctly:
            print(f"You have {remaining_attempts} attempts left.")

    except ValueError:
        print("Please enter a valid number!")
        attempts -= 1  # Don't count invalid input as an attempt

if not guessed_correctly:
    print(f"Game over! The number was {secret_number}")

print("Thanks for playing!")
```

This advanced example shows:
- Nested conditions within the while loop
- Error handling with try-except
- Multiple exit conditions
- User interaction and input processing
- Game logic implementation

## Output

For Example 1:
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Loop finished!
```

For Example 2:
```
Calculating factorial of 5
Step 1: factorial = 1
Step 2: factorial = 2
Step 3: factorial = 6
Step 4: factorial = 24
Step 5: factorial = 120
Factorial of 5 is 120
```

For Example 3 (sample run):
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100. You have 7 attempts.
Enter your guess: 50
Too low! Try a higher number.
You have 6 attempts left.
Enter your guess: 75
Too high! Try a lower number.
You have 5 attempts left.
Enter your guess: 63
Too low! Try a higher number.
You have 4 attempts left.
Enter your guess: 69
Too high! Try a lower number.
You have 3 attempts left.
Enter your guess: 66
Congratulations! You guessed it in 5 attempts!
Thanks for playing!
```

## Common Mistakes

1. **Infinite Loop**: Forgetting to update the loop variable
   ```python
   # Wrong - infinite loop
   count = 1
   while count <= 5:
       print(count)
       # Forgot to increment count

   # Correct
   count = 1
   while count <= 5:
       print(count)
       count += 1
   ```

2. **Off-by-one Errors**: Incorrect boundary conditions
   ```python
   # Wrong - prints 1,2,3,4
   count = 1
   while count < 5:
       print(count)
       count += 1

   # Correct - prints 1,2,3,4,5
   count = 1
   while count <= 5:
       print(count)
       count += 1
   ```

3. **Wrong Initial Value**: Starting with incorrect initial value
   ```python
   # Wrong - skips 1
   count = 2
   while count <= 5:
       print(count)
       count += 1

   # Correct - starts with 1
   count = 1
   while count <= 5:
       print(count)
       count += 1
   ```

4. **Incorrect Condition Logic**: Using wrong comparison operators
   ```python
   # Wrong - might not execute
   count = 1
   while count > 5:
       print(count)
       count += 1
   ```

## Best Practices

1. **Always Initialize Variables**: Make sure loop variables are properly initialized
2. **Update Loop Variables**: Ensure the loop variable changes in each iteration
3. **Use Meaningful Variable Names**: Make your code readable
   ```python
   # Good
   user_attempts = 0
   max_attempts = 3
   while user_attempts < max_attempts:
       # code here
       user_attempts += 1
   ```

4. **Avoid Complex Conditions**: Keep loop conditions simple and readable
5. **Use Comments for Complex Logic**: Explain what the loop is doing
6. **Consider Using For Loops**: When you know the number of iterations, prefer for loops
7. **Handle User Input Carefully**: Validate input within loops
8. **Use Break Statements Judiciously**: Only when necessary for clarity

## Pro Tips

1. **Use the Walrus Operator (Python 3.8+)**: For cleaner input loops
   ```python
   # Traditional way
   line = input("Enter text: ")
   while line != "quit":
       print(f"You entered: {line}")
       line = input("Enter text: ")

   # With walrus operator
   while (line := input("Enter text: ")) != "quit":
       print(f"You entered: {line}")
   ```

2. **Implement Timeout Mechanisms**: Prevent infinite loops in production code
   ```python
   import time
   start_time = time.time()
   timeout = 10  # seconds

   while condition and (time.time() - start_time) < timeout:
       # loop body
       pass
   ```

3. **Use Enumerate When Needed**: Even in while loops for tracking iterations
   ```python
   items = ['apple', 'banana', 'cherry']
   index = 0
   while index < len(items):
       print(f"{index}: {items[index]}")
       index += 1
   ```

4. **Combine with Else Clause**: Useful for search operations
   ```python
   numbers = [1, 3, 5, 7, 9]
   target = 6
   index = 0

   while index < len(numbers):
       if numbers[index] == target:
           print(f"Found {target} at index {index}")
           break
       index += 1
   else:
       print(f"{target} not found in the list")
   ```

## Interview Questions (10)

1. What is the difference between while loop and for loop in Python?
2. How do you prevent infinite loops in while loops?
3. Explain the flow of execution in a while loop.
4. What happens if the condition in a while loop is never true?
5. How can you exit a while loop before the condition becomes false?
6. What is the purpose of the else clause in a while loop?
7. When would you prefer a while loop over a for loop?
8. How do you handle user input validation in a while loop?
9. What are the common causes of infinite loops?
10. Explain how to implement a do-while loop behavior in Python.

## MCQs (10)

1. What is the minimum number of times a while loop can execute?
   a) 0
   b) 1
   c) 2
   d) Infinite
   **Answer: a) 0**

2. When is the condition in a while loop checked?
   a) Only at the beginning
   b) Before each iteration
   c) After each iteration
   d) Only at the end
   **Answer: b) Before each iteration**

3. What will be the output of: `count = 0; while count < 3: print(count); count += 1`
   a) 0 1 2
   b) 1 2 3
   c) 0 1 2 3
   d) 1 2
   **Answer: a) 0 1 2**

4. Which keyword is used to exit a while loop immediately?
   a) exit
   b) stop
   c) break
   d) continue
   **Answer: c) break**

5. What does the else clause in a while loop execute?
   a) When the loop starts
   b) When the condition becomes false
   c) In every iteration
   d) Never executes
   **Answer: b) When the condition becomes false**

6. What causes an infinite loop?
   a) Condition never becomes true
   b) Condition never becomes false
   c) Empty loop body
   d) Using break statement
   **Answer: b) Condition never becomes false**

7. How many times will this loop execute: `x = 5; while x > 10: print(x); x += 1`
   a) 0
   b) 1
   c) 5
   d) Infinite
   **Answer: a) 0**

8. Which statement skips the current iteration and continues with the next?
   a) pass
   b) break
   c) skip
   d) continue
   **Answer: d) continue**

9. What is the output of: `i = 1; while i <= 3: i += 1; print(i)`
   a) 1 2 3
   b) 2 3 4
   c) 2 3
   d) 1 2
   **Answer: b) 2 3 4**

10. In a while loop, what happens if you don't update the loop variable?
    a) Syntax error
    b) Infinite loop
    c) Loop executes once
    d) Loop doesn't execute
    **Answer: b) Infinite loop**

## Practice Questions (10)

1. Write a while loop to print all even numbers between 1 and 20.
2. Create a program that keeps asking for a password until the correct one is entered.
3. Implement a countdown timer from 10 to 0 using a while loop.
4. Write a program to calculate the sum of digits of a given number using while loop.
5. Create a simple calculator that keeps running until the user chooses to exit.
6. Write a program that finds the largest number among user inputs until they enter -1.
7. Implement a program that reverses a given number using while loop.
8. Create a guessing game where the user has to guess a number between 1-50.
9. Write a program to check if a number is prime using while loop.
10. Create a program that keeps track of expenses until the user enters 0.

## Coding Exercises (5)

1. **Temperature Converter**: Create a program that continuously asks for temperature in Celsius and converts it to Fahrenheit until the user enters 'quit'.

2. **Simple ATM**: Implement an ATM simulation that allows withdrawals and deposits until the user chooses to exit. Keep track of balance.

3. **Pattern Printer**: Write a program that prints a triangle pattern of stars using while loops. The user should be able to specify the height.

4. **Word Counter**: Create a program that counts the number of words in sentences entered by the user until they enter an empty string.

5. **Fibonacci Sequence**: Generate the Fibonacci sequence up to a specified number using while loop.

## Mini Project

**Task Manager Application**

Create a simple command-line task manager that allows users to:
1. Add tasks
2. View all tasks
3. Mark tasks as completed
4. Delete tasks
5. Exit the application

Requirements:
- Use while loop for the main menu
- Store tasks in a list
- Each task should have an ID, description, and completion status
- Provide proper user feedback
- Handle invalid inputs gracefully

```python
tasks = []
task_id = 1

print("=== Task Manager ===")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        description = input("Enter task description: ")
        tasks.append({"id": task_id, "description": description, "completed": False})
        print(f"Task added with ID: {task_id}")
        task_id += 1

    elif choice == "2":
        if not tasks:
            print("No tasks found!")
        else:
            print("\n--- Tasks ---")
            for task in tasks:
                status = "✓" if task["completed"] else "○"
                print(f"{task['id']}. [{status}] {task['description']}")

    elif choice == "3":
        try:
            task_num = int(input("Enter task ID to mark complete: "))
            found = False
            for task in tasks:
                if task["id"] == task_num:
                    task["completed"] = True
                    print(f"Task {task_num} marked as complete!")
                    found = True
                    break
            if not found:
                print("Task not found!")
        except ValueError:
            print("Please enter a valid task ID!")

    elif choice == "4":
        try:
            task_num = int(input("Enter task ID to delete: "))
            for i, task in enumerate(tasks):
                if task["id"] == task_num:
                    tasks.pop(i)
                    print(f"Task {task_num} deleted!")
                    found = True
                    break
            if not found:
                print("Task not found!")
        except ValueError:
            print("Please enter a valid task ID!")

    elif choice == "5":
        print("Thank you for using Task Manager!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
```

## Assignment

**Student Grade Calculator**

Create a comprehensive grade calculator that:
1. Allows teachers to enter student names and their scores
2. Calculates average grades
3. Assigns letter grades based on average
4. Displays class statistics
5. Continues until the teacher chooses to stop

Requirements:
- Use while loops for all repetitive operations
- Store student data in appropriate data structures
- Implement proper input validation
- Calculate and display class average, highest score, and lowest score
- Allow teachers to search for specific students
- Provide a clean, user-friendly interface

Grading Scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

## Summary

A while loop is a fundamental control structure that executes a block of code repeatedly as long as a specified condition remains true. Key points covered:

- While loops check conditions before each iteration
- They're ideal when the number of iterations is unknown
- Proper initialization and updating of loop variables is crucial
- Infinite loops occur when conditions never become false
- Break and continue statements provide additional control
- While loops can be combined with else clauses
- They're essential for interactive programs and data processing

## Key Takeaways

1. While loops execute code repeatedly based on a condition
2. Always ensure loop variables are properly initialized and updated
3. The condition is checked before each iteration
4. Infinite loops are a common mistake to avoid
5. While loops are perfect for unknown iteration counts
6. Break and continue provide fine-grained control
7. Else clauses execute when the condition becomes false naturally
8. Real-world applications include games, calculators, and data processing

## Next Topic Preview

In the next lesson, we'll explore **For Loops** in Python. We'll learn how to iterate over sequences like lists, strings, and ranges, and understand when to use for loops instead of while loops. We'll also cover nested loops, loop control statements, and advanced iteration techniques.
