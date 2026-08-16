# Recursion

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand the fundamental concept of recursion and how it works
- Implement recursive functions in Python with proper base cases
- Analyze recursive algorithms and trace their execution flow
- Recognize when recursion is an appropriate problem-solving approach
- Debug common recursion issues like stack overflow and infinite loops
- Apply recursion to solve mathematical and data structure problems
- Convert between iterative and recursive solutions
- Understand tail recursion optimization concepts

## Prerequisites

Before starting this lesson, you should be familiar with:
- Basic Python syntax and data types
- Function definitions and calls
- Control flow statements (if/else, loops)
- Basic understanding of the call stack
- Lists, tuples, and dictionaries
- Basic mathematical operations

## What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. It's based on the mathematical concept of recursive definitions, where something is defined in terms of itself.

Think of recursion like Russian nesting dolls – each doll contains a smaller version of itself, and you keep opening dolls until you reach the smallest one that can't be opened further.

In programming terms, a recursive function has two essential components:
1. **Base Case**: A condition that stops the recursion (like hitting the smallest doll)
2. **Recursive Case**: The function calling itself with modified parameters (like opening the next doll)

## Why is it Important?

Recursion is important because it provides an elegant way to solve problems that have self-similar structures. It's particularly useful for:
- Tree and graph traversals
- Mathematical computations (factorials, Fibonacci)
- Divide-and-conquer algorithms
- Backtracking problems
- Parsing nested data structures

Recursion often leads to cleaner, more readable code compared to iterative solutions, especially for complex hierarchical problems. It's also fundamental to understanding many computer science concepts and algorithms.

## Real World Analogy

Imagine you're looking for a specific book in a library that organizes books by putting them in boxes, and those boxes might contain more boxes. To find your book:

1. Open the current box
2. If you find the book, you're done
3. If you find another box, repeat the process with that box
4. If you find nothing, you've exhausted all possibilities

This mirrors recursion perfectly – each step involves the same process applied to a smaller subset of the original problem.

## Theory

In computer science, recursion is based on the principle of mathematical induction. A recursive function must satisfy:

1. **Base Case**: This is the simplest possible input for which the answer is known without further recursion. Without it, the function would call itself indefinitely.

2. **Recursive Case**: This reduces the problem to a simpler version of itself. Each recursive call should bring the problem closer to the base case.

The execution of a recursive function follows a stack-based model:
- Each function call is pushed onto the call stack
- When a function returns, it's popped from the stack
- The last function called is the first to return (LIFO - Last In, First Out)

Memory usage grows linearly with the depth of recursion, which can lead to stack overflow errors if the recursion depth is too large.

## Syntax

```python
def recursive_function(parameters):
    # Base case
    if base_condition:
        return base_value

    # Recursive case
    # Modify parameters to approach base case
    return recursive_function(modified_parameters)
```

The general pattern includes:
- A function that calls itself
- A clear base case that stops the recursion
- Parameters that change with each recursive call
- A return statement that combines results

## Flow / Working

Let's trace through a simple recursive function:

```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n-1)
```

When calling `factorial(4)`:
1. `factorial(4)` → calls `factorial(3)` and waits
2. `factorial(3)` → calls `factorial(2)` and waits
3. `factorial(2)` → calls `factorial(1)` and waits
4. `factorial(1)` → returns 1 (base case)
5. `factorial(2)` → returns 2 * 1 = 2
6. `factorial(3)` → returns 3 * 2 = 6
7. `factorial(4)` → returns 4 * 6 = 24

This is called the "unwinding" phase where results propagate back up the call stack.

## Example 1 (Beginner)

Let's implement a recursive function to calculate the factorial of a number:

```python
def factorial(n):
    """
    Calculate the factorial of n using recursion
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test the function
print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")
print(f"3! = {factorial(3)}")
```

## Example 2 (Intermediate)

Let's implement a recursive function to traverse and sum all elements in a nested list structure:

```python
def sum_nested_list(data):
    """
    Recursively sum all numbers in a nested list structure
    """
    total = 0

    for item in data:
        if isinstance(item, list):
            # Recursive case: item is a list, recurse into it
            total += sum_nested_list(item)
        else:
            # Base case: item is a number, add it to total
            total += item

    return total

# Test with nested lists
nested_data = [1, [2, 3], [4, [5, 6]], 7]
print(f"Sum of {nested_data} = {sum_nested_list(nested_data)}")

# More complex example
complex_data = [1, [2, [3, [4, 5]]], 6, [7, [8, 9]]]
print(f"Sum of complex data = {sum_nested_list(complex_data)}")
```

## Example 3 (Advanced)

Let's implement a recursive solution for the classic "Tower of Hanoi" problem:

```python
def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solve Tower of Hanoi puzzle recursively

    n: number of disks
    source: starting rod
    destination: target rod
    auxiliary: helper rod
    """
    # Base case: only one disk
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    # Move n-1 disks from source to auxiliary
    moves1 = tower_of_hanoi(n-1, source, auxiliary, destination)

    # Move the largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    moves2 = 1

    # Move n-1 disks from auxiliary to destination
    moves3 = tower_of_hanoi(n-1, auxiliary, destination, source)

    return moves1 + moves2 + moves3

# Solve Tower of Hanoi with 3 disks
print("Solution for 3 disks:")
total_moves = tower_of_hanoi(3, 'A', 'C', 'B')
print(f"Total moves: {total_moves}")
```

## Output

```
5! = 120
0! = 1
3! = 6
Sum of [1, [2, 3], [4, [5, 6]], 7] = 28
Sum of complex data = 45
Solution for 3 disks:
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Total moves: 7
```

## Common Mistakes

1. **Missing or incorrect base case**: This leads to infinite recursion and stack overflow
2. **Not making progress toward base case**: Recursive calls don't change parameters properly
3. **Forgetting return statements**: Results aren't passed back up the call stack
4. **Using recursion for problems better solved iteratively**: Can cause unnecessary overhead
5. **Not considering stack overflow**: Deep recursion can exhaust system memory
6. **Incorrect parameter passing**: Logic errors in how parameters change between calls

## Best Practices

1. **Always define clear base cases**: Ensure your recursion has a definitive stopping point
2. **Make the problem smaller with each call**: Each recursive call should bring you closer to the base case
3. **Use meaningful parameter names**: This helps in understanding the recursive logic
4. **Consider iterative solutions**: For simple cases, iteration might be more efficient
5. **Document your recursive functions**: Include comments explaining the base and recursive cases
6. **Test with edge cases**: Verify behavior with 0, 1, and negative inputs
7. **Monitor recursion depth**: Be aware of potential stack overflow issues

## Pro Tips

1. **Trace with small examples**: Use simple inputs to understand the call flow
2. **Use print statements during debugging**: Visualize what's happening at each recursive call
3. **Consider memoization**: For repeated calculations, store results to avoid redundant work
4. **Think about data structure mapping**: Recursion works naturally with trees, graphs, and nested structures
5. **Use helper functions**: Sometimes a helper with additional parameters makes recursion cleaner
6. **Understand tail recursion**: When the recursive call is the last operation, it can be optimized
7. **Combine with other techniques**: Recursion often works well with divide-and-conquer strategies

## Interview Questions (10)

1. Explain the difference between recursion and iteration with examples
2. What is tail recursion and how does it differ from regular recursion?
3. How would you implement a recursive binary search algorithm?
4. Write a recursive function to reverse a string
5. Explain how the call stack works with recursive functions
6. What are the time and space complexities of recursive algorithms?
7. How would you convert a recursive solution to an iterative one?
8. Implement a recursive function to check if a string is a palindrome
9. Write a recursive function to compute Fibonacci numbers and discuss its efficiency
10. How do you handle potential stack overflow errors in recursive functions?

## MCQs (10)

| Question | Options | Correct Answer | Explanation |
|----------|---------|----------------|-------------|
| What is the base case in recursion? | A) The function calling itself | B) The condition that stops recursion | C) The recursive algorithm | D) The main function | B | Base case stops the recursion |
| What happens without a base case? | A) Function executes normally | B) Infinite loop | C) Stack overflow error | D) Faster execution | C | No stopping condition causes stack overflow |
| In factorial recursion, what is the base case? | A) n > 1 | B) n <= 1 | C) n = 0 | D) n < 0 | B | Factorial of 0 or 1 is 1 |
| What does LIFO stand for in recursion context? | A) Last In, First Out | B) Last Input, First Output | C) Long Input, Fast Output | D) Linear In, Fast Out | A | Call stack is LIFO structure |
| Which data structure best represents recursion execution? | A) Queue | B) Array | C) Stack | D) Linked List | C | Call stack represents execution |
| What is tail recursion? | A) Recursion at function start | B) Recursion at function end | C) Infinite recursion | D) Multiple recursive calls | B | Last operation is recursive call |
| How does memory usage grow in recursion? | A) Constant | B) Linear with depth | C) Exponential | D) Logarithmic | B | Each call uses stack space |
| What is the Fibonacci base case? | A) fib(0) and fib(1) | B) fib(1) and fib(2) | C) fib(2) and fib(3) | D) fib(n) and fib(n-1) | A | Standard Fibonacci base cases |
| When should you avoid recursion? | A) For simple iterations | B) For tree traversals | C) For mathematical sequences | D) For divide and conquer | A | Simple iterations are more efficient |
| What is the time complexity of naive recursive Fibonacci? | A) O(n) | B) O(log n) | C) O(2^n) | D) O(n^2) | C | Exponential due to repeated calculations |

## Practice Questions (10)

1. Write a recursive function to calculate the sum of digits in a number
2. Implement a recursive function to find the greatest common divisor (GCD) of two numbers
3. Create a recursive function to check if a number is prime
4. Write a recursive function to generate all possible permutations of a string
5. Implement a recursive solution for the power function (x^n)
6. Create a recursive function to flatten a nested list
7. Write a recursive function to perform binary search on a sorted array
8. Implement a recursive function to count the number of nodes in a binary tree
9. Create a recursive function to solve the "N-Queens" problem
10. Write a recursive function to generate Pascal's triangle up to n rows

## Coding Exercises (5)

### Exercise 1: Sum of Digits
```python
def sum_digits(n):
    """Calculate sum of digits in a number recursively"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(12345))  # Should output 15
```

### Exercise 2: GCD using Euclidean Algorithm
```python
def gcd(a, b):
    """Calculate GCD using recursion"""
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Should output 6
```

### Exercise 3: String Permutations
```python
def permutations(s):
    """Generate all permutations of a string"""
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(char + perm)

    return result

print(permutations("abc"))  # Should output ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

### Exercise 4: Power Function
```python
def power(base, exp):
    """Calculate base^exp recursively"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)

print(power(2, 5))  # Should output 32
```

### Exercise 5: Binary Tree Node Count
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root):
    """Count nodes in binary tree recursively"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(count_nodes(root))  # Should output 4
```

## Mini Project

### Recursive Maze Solver

Create a recursive maze solver that finds a path from start to end:

```python
def solve_maze(maze, start, end, path=[]):
    """
    Solve maze using recursive backtracking
    """
    # Add current position to path
    path = path + [start]

    # Base case: reached the end
    if start == end:
        return path

    # Get possible moves
    row, col = start
    moves = []

    # Check up, down, left, right
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  # right, left, down, up
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if (0 <= new_row < len(maze) and
            0 <= new_col < len(maze[0]) and
            maze[new_row][new_col] == 0 and
            (new_row, new_col) not in path):
            moves.append((new_row, new_col))

    # Try each possible move
    for move in moves:
        result = solve_maze(maze, move, end, path)
        if result:
            return result

    # No solution found from this path
    return None

# Test the maze solver
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)
solution = solve_maze(maze, start, end)

if solution:
    print("Path found:", solution)
    # Visualize the path
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) in solution:
                print("*", end=" ")
            elif maze[r][c] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No path found")
```

## Assignment

Create a recursive implementation of a file system navigator that:
1. Traverses directories recursively
2. Counts total files and directories
3. Calculates total size of files
4. Finds files with specific extensions
5. Shows directory structure with proper indentation

Your solution should work with the actual file system and handle errors gracefully. Include docstrings and comprehensive testing.

## Summary

Recursion is a powerful programming technique where functions call themselves to solve problems by breaking them into smaller subproblems. The key components are:
- Base case: stops the recursion
- Recursive case: moves closer to the base case
- Proper parameter management to ensure progress

We explored recursion from basic concepts to advanced applications, including factorial calculation, nested data processing, and complex problem solving like Tower of Hanoi. Recursion provides elegant solutions for hierarchical and self-similar problems, but requires careful consideration of performance and stack limitations.

## Key Takeaways

1. Recursion solves problems by breaking them into similar smaller subproblems
2. Every recursive function must have a base case to prevent infinite recursion
3. The call stack manages the execution of recursive functions
4. Recursion naturally fits tree-like and nested data structures
5. Tail recursion can be optimized but Python doesn't optimize it automatically
6. Always consider iterative alternatives for performance-critical code
7. Debugging recursive functions requires tracing through the call stack
8. Memoization can dramatically improve recursive algorithm performance
9. Recursion depth should be monitored to prevent stack overflow errors
10. Recursive thinking is fundamental to computer science problem solving

## Next Topic Preview

In the next lesson, we'll explore **Decorators** in Python - a powerful feature that allows you to modify or extend the behavior of functions and classes without permanently modifying their code. We'll cover function decorators, class decorators, decorator factories, and practical applications like logging, timing, and authentication.
