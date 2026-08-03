# Match Case

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand the concept and purpose of match-case statements in Python
- Implement basic to advanced match-case patterns
- Apply pattern matching for data validation and control flow
- Differentiate between match-case and traditional if-elif statements
- Use advanced pattern matching techniques like wildcards and guards
- Create robust error handling with match-case statements

## Prerequisites

Before starting this lesson, you should be comfortable with:
- Basic Python syntax and data types
- Control flow statements (if-else, loops)
- Functions and basic data structures
- Basic understanding of data validation concepts
- Python 3.10+ installed on your system

## What is Match Case?

Match-case is Python's implementation of pattern matching, introduced in Python 3.10. It provides a more readable and powerful alternative to long chains of if-elif statements by allowing you to match values against patterns rather than just equality checks. Think of it as an enhanced switch-case statement found in other programming languages, but with much more flexibility.

The match-case statement evaluates an expression and compares it against a series of patterns. When a pattern matches, the corresponding code block executes. Each pattern can include various matching criteria, making it extremely versatile for complex data structures.

## Why is it Important?

Match-case statements are important for several reasons:

1. **Readability**: They make complex conditional logic more readable and maintainable
2. **Performance**: Can be more efficient than long if-elif chains
3. **Expressiveness**: Allow for sophisticated pattern matching that's difficult to achieve with traditional conditionals
4. **Data Validation**: Excellent for validating and processing complex data structures
5. **Functional Programming**: Brings functional programming concepts like pattern matching to Python
6. **Error Handling**: Provides cleaner ways to handle different error conditions

## Real World Analogy

Think of match-case like a sorting machine at a postal facility. Letters come in (the data), and the machine examines each one to see which pattern it matches (zip code, size, weight). Based on the match, it routes the letter to the appropriate destination (executes the corresponding code). This is more efficient and accurate than manually checking each letter against a long list of conditions.

## Theory

Pattern matching works by:
1. Evaluating the subject expression
2. Sequentially checking each pattern in the order defined
3. When a pattern matches, executing the corresponding code block
4. Using specific matching rules for different data types
5. Supporting advanced features like wildcards, guards, and destructuring

The match-case system supports various pattern types:
- Literal patterns (exact value matches)
- Variable patterns (capture values for use)
- Wildcard patterns (match anything)
- Or patterns (logical OR between patterns)
- As patterns (binding with additional constraints)
- Sequence patterns (match sequences like lists)
- Mapping patterns (match dictionaries)
- Class patterns (match object attributes)

## Syntax

```python
match subject:
    case pattern1:
        # code block 1
    case pattern2:
        # code block 2
    case pattern3 if condition:
        # guarded pattern
    case _:
        # default case (wildcard)
```

## Flow / Working

1. The match statement evaluates the subject expression
2. It checks each case pattern in sequence from top to bottom
3. When a pattern matches the subject:
   - The corresponding code block executes
   - The match statement exits (no fall-through like switch-case in other languages)
4. If no patterns match and there's a wildcard case (_), it executes
5. If no patterns match and no wildcard exists, nothing happens
6. Each pattern can include guards (if conditions) for additional matching logic

## Example 1 (Beginner)

```python
# Simple grade categorization system
def categorize_grade(score):
    match score:
        case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
            return "A Grade"
        case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
            return "B Grade"
        case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
            return "C Grade"
        case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
            return "D Grade"
        case _:
            return "F Grade or Invalid Score"

# Test the function
print(categorize_grade(95))  # A Grade
print(categorize_grade(75))  # C Grade
print(categorize_grade(45))  # F Grade or Invalid Score
```

## Example 2 (Intermediate)

```python
# HTTP status code handler with pattern matching
def handle_http_status(status):
    match status:
        case 200:
            return "Success: OK"
        case 201:
            return "Success: Created"
        case 204:
            return "Success: No Content"
        case 400:
            return "Client Error: Bad Request"
        case 401:
            return "Client Error: Unauthorized"
        case 403:
            return "Client Error: Forbidden"
        case 404:
            return "Client Error: Not Found"
        case 500:
            return "Server Error: Internal Server Error"
        case 502:
            return "Server Error: Bad Gateway"
        case 503:
            return "Server Error: Service Unavailable"
        case code if 200 <= code < 300:
            return f"Success: Other Success Code {code}"
        case code if 400 <= code < 500:
            return f"Client Error: Other Client Error {code}"
        case code if 500 <= code < 600:
            return f"Server Error: Other Server Error {code}"
        case _:
            return f"Unknown Status Code: {status}"

# Test with various status codes
print(handle_http_status(200))  # Success: OK
print(handle_http_status(404))  # Client Error: Not Found
print(handle_http_status(202))  # Success: Other Success Code 202
print(handle_http_status(999))  # Unknown Status Code: 999
```

## Example 3 (Advanced)

```python
# Complex data validation with nested patterns
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Person:
    name: str
    age: int
    email: str
    hobbies: List[str]

@dataclass
class Company:
    name: str
    employees: int
    industry: str

def process_data(data):
    match data:
        # Match specific person with exact attributes
        case Person(name="Alice", age=30, email=email):
            return f"Alice found! Email: {email}"
        
        # Match person with age constraint
        case Person(name=name, age=age) if age >= 18:
            return f"Adult person: {name}, age {age}"
        
        # Match person with specific hobby
        case Person(hobbies=hobbies) if "programming" in hobbies:
            return "Found a programmer!"
        
        # Match company with employee count constraint
        case Company(name=name, employees=count) if count > 100:
            return f"Large company: {name} with {count} employees"
        
        # Match company in specific industry
        case Company(industry="Technology"):
            return "Tech company detected"
        
        # Match any person (wildcard pattern)
        case Person(name=name):
            return f"Person found: {name}"
        
        # Match any company (wildcard pattern)
        case Company(name=name):
            return f"Company found: {name}"
        
        # Match list with specific structure
        case [first, second, *rest]:
            return f"List with at least 2 items. First: {first}, Second: {second}"
        
        # Match dictionary with specific keys
        case {"type": "error", "code": code, "message": msg}:
            return f"Error {code}: {msg}"
        
        # Match tuple with specific values
        case (x, y) if x > 0 and y > 0:
            return f"Positive coordinates: ({x}, {y})"
        
        # Default case
        case _:
            return "Unknown data structure"

# Test with various data types
alice = Person("Alice", 30, "alice@email.com", ["reading", "programming"])
bob = Person("Bob", 17, "bob@email.com", ["gaming"])
tech_company = Company("TechCorp", 150, "Technology")
small_company = Company("LocalShop", 5, "Retail")
error_dict = {"type": "error", "code": 404, "message": "Not Found"}
coordinates = (10, 20)
mixed_list = [1, 2, 3, 4, 5]

print(process_data(alice))          # Alice found! Email: alice@email.com
print(process_data(bob))            # Person found: Bob
print(process_data(tech_company))   # Large company: TechCorp with 150 employees
print(process_data(small_company))  # Company found: LocalShop
print(process_data(error_dict))     # Error 404: Not Found
print(process_data(coordinates))    # Positive coordinates: (10, 20)
print(process_data(mixed_list))     # List with at least 2 items. First: 1, Second: 2
```

## Output

```
A Grade
C Grade
F Grade or Invalid Score
Success: OK
Client Error: Not Found
Success: Other Success Code 202
Unknown Status Code: 999
Alice found! Email: alice@email.com
Person found: Bob
Large company: TechCorp with 150 employees
Company found: LocalShop
Error 404: Not Found
Positive coordinates: (10, 20)
List with at least 2 items. First: 1, Second: 2
```

## Common Mistakes

| Mistake | Description | How to Fix |
|---------|-------------|------------|
| Forgetting the colon | `case 1` instead of `case 1:` | Always include the colon after case |
| Using break statements | Trying to use `break` like in switch-case | Match-case doesn't fall through, so no break needed |
| Incorrect pattern syntax | `case x > 5:` instead of `case x if x > 5:` | Use `if` for guards, not direct comparison |
| Missing wildcard pattern | Not handling unexpected cases | Always include `case _:` for default handling |
| Pattern order issues | Putting specific patterns after general ones | Place specific patterns before general ones |
| Incorrect tuple unpacking | `case (x, y, z):` for a 2-element tuple | Match the exact structure of your data |

## Best Practices

1. **Always include a wildcard case** (`case _:`) to handle unexpected inputs
2. **Order patterns from specific to general** to ensure correct matching
3. **Use descriptive variable names** in patterns for better readability
4. **Combine patterns with guards** for more precise matching when needed
5. **Keep patterns simple** - complex patterns can be hard to maintain
6. **Use type hints** to make pattern matching more predictable
7. **Test edge cases** thoroughly since pattern matching can be complex
8. **Document complex patterns** with comments for future maintainability
9. **Prefer match-case over long if-elif chains** when dealing with multiple discrete values
10. **Use pattern matching for structural data rather than just value checking**

## Pro Tips

1. **Nested pattern matching**: You can match nested data structures like `case {"user": {"id": id_val, "name": name_val}}:`
2. **Pattern capture**: Capture matched values for use in the code block: `case Person(name=n, age=a):`
3. **Wildcards with constraints**: `case _ if condition:` for default cases with additional logic
4. **Sequence patterns**: Match lists/tuples with specific lengths or elements
5. **Mapping patterns**: Match dictionary keys and values efficiently
6. **Class patterns**: Match object attributes directly without accessing them manually
7. **Or patterns**: Combine multiple patterns with `|` for cleaner code
8. **As patterns**: Bind matched values with additional constraints using `as` keyword
9. **Guard conditions**: Add `if` conditions to patterns for more sophisticated matching
10. **Performance consideration**: Match-case can be faster than long if-elif chains for many conditions

## Interview Questions (10)

1. What is the main difference between match-case and traditional if-elif statements?
2. How do you handle the default case in match-case statements?
3. Can you explain what pattern matching means in the context of Python?
4. What happens if multiple patterns could match the same value?
5. How do you implement conditional matching in match-case statements?
6. What data structures can be effectively pattern matched in Python?
7. Can match-case statements fall through like switch-case in other languages?
8. How would you match a dictionary with specific key-value pairs?
9. What is the purpose of the wildcard pattern `_` in match-case?
10. How can you capture matched values for use within the case block?

## MCQs (10)

1. **Which Python version introduced match-case statements?**
   a) 3.8
   b) 3.9
   c) 3.10
   d) 3.11

2. **What happens when no patterns match and there's no wildcard case?**
   a) Error is raised
   b) Default case executes
   c) Nothing happens
   d) Program crashes

3. **How do you combine multiple patterns in a single case?**
   a) Using &&
   b) Using ||
   c) Using |
   d) Using and

4. **What is the correct syntax for a guarded pattern?**
   a) `case value if condition:`
   b) `case value | condition:`
   c) `case value && condition:`
   d) `case value where condition:`

5. **Which pattern matches any value?**
   a) `*`
   b) `?`
   c) `_`
   d) `...`

6. **In what order should patterns be placed?**
   a) Random order
   b) General to specific
   c) Specific to general
   d) Alphabetical order

7. **What happens after a pattern matches?**
   a) Continue checking other patterns
   b) Fall through to next case
   c) Execute and exit the match statement
   d) Loop back to first pattern

8. **How do you match a list with exactly 3 elements?**
   a) `case [a, b, c]:`
   b) `case [a, b, c, *]:`
   c) `case [a, b, c, ...]:`
   d) `case list(3):`

9. **What is the purpose of the `|` operator in patterns?**
   a) Logical OR
   b) Pattern combination
   c) List concatenation
   d) Both a and b

10. **How do you access captured values from a matched pattern?**
    a) Through global variables
    b) They're automatically available in the case block
    c) Through a special match object
    d) Through function parameters

## Practice Questions (10)

1. Create a match-case function that categorizes a day of the week as weekday or weekend
2. Write a pattern matcher for HTTP methods (GET, POST, PUT, DELETE) with appropriate responses
3. Implement a calculator function using match-case that handles basic arithmetic operations
4. Create a function that matches different types of geometric shapes and calculates their area
5. Write a pattern matcher for different file extensions (.txt, .jpg, .pdf) with actions
6. Implement a function that matches nested list structures to extract specific data
7. Create a match-case system for processing different types of user input commands
8. Write a pattern matcher for JSON-like data structures with validation
9. Implement a function that matches complex nested dictionaries
10. Create a match-case handler for different types of network protocols

## Coding Exercises (5)

### Exercise 1: Weather Condition Handler
Create a function that takes weather conditions and returns appropriate advice using match-case.

### Exercise 2: Command Processor
Implement a command-line interface processor that matches different commands and executes corresponding actions.

### Exercise 3: Data Validator
Create a pattern matcher that validates different types of user input data (email, phone, address).

### Exercise 4: Game State Manager
Write a match-case system that handles different game states (menu, playing, paused, game over).

### Exercise 5: API Response Handler
Implement a pattern matcher that processes different types of API responses based on status codes and content.

## Mini Project

### Traffic Light Control System

Create a comprehensive traffic light control system using match-case statements:

```python
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import time

class LightColor(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

@dataclass
class TrafficLight:
    current_color: LightColor
    time_remaining: int
    pedestrian_waiting: bool = False

def process_traffic_light(light: TrafficLight, emergency: bool = False):
    match light, emergency:
        # Emergency vehicle priority
        case _, True:
            return "Emergency override: Turn all lights to red except main road green"
        
        # Normal operation with pedestrian waiting
        case TrafficLight(current_color=LightColor.RED, time_remaining=t) if t <= 5 and light.pedestrian_waiting:
            return "Prepare to change: Red -> Green for pedestrians"
        
        case TrafficLight(current_color=LightColor.GREEN, time_remaining=0):
            return "Green time expired: Prepare to change to Yellow"
        
        case TrafficLight(current_color=LightColor.YELLOW, time_remaining=0):
            return "Yellow time expired: Change to Red"
        
        case TrafficLight(current_color=LightColor.RED, time_remaining=0):
            return "Red time expired: Change to Green"
        
        # Normal counting down
        case TrafficLight(current_color=color, time_remaining=t) if t > 0:
            return f"Normal operation: {color.value.capitalize()} for {t} more seconds"
        
        # Invalid states
        case TrafficLight(current_color=LightColor.GREEN, time_remaining=t) if t < 0:
            return "Error: Invalid green time value"
        
        case _:
            return "Unknown traffic light state"

# Test the system
light1 = TrafficLight(LightColor.GREEN, 30)
light2 = TrafficLight(LightColor.RED, 0, True)
light3 = TrafficLight(LightColor.YELLOW, 5)

print(process_traffic_light(light1))  # Normal operation: Green for 30 more seconds
print(process_traffic_light(light2, True))  # Emergency override: Turn all lights to red except main road green
print(process_traffic_light(light3))  # Normal operation: Yellow for 5 more seconds
```

## Assignment

Create a comprehensive e-commerce order processing system using match-case statements. The system should handle:

1. Different order statuses (pending, confirmed, shipped, delivered, cancelled)
2. Various payment methods (credit card, PayPal, bank transfer)
3. Different shipping methods (standard, express, overnight)
4. Customer types (regular, premium, VIP)
5. Order validation based on inventory and customer credit
6. Error handling for invalid orders or payment failures

Requirements:
- Use at least 5 different pattern matching techniques
- Include proper error handling with match-case
- Handle nested data structures (order details, customer info)
- Provide appropriate responses for each scenario
- Include a testing suite with at least 10 test cases

## Summary

Match-case statements in Python provide a powerful and readable way to implement pattern matching logic. They offer significant advantages over traditional if-elif chains, especially when dealing with complex data structures and multiple discrete values. Key concepts include:

- Pattern matching evaluates expressions against patterns rather than simple equality
- Patterns are checked sequentially from top to bottom
- Wildcard patterns (`_`) handle default cases
- Guard conditions add additional matching logic
- Complex nested patterns can match sophisticated data structures
- No fall-through behavior unlike switch-case in other languages

## Key Takeaways

1. Match-case statements provide cleaner alternatives to long if-elif chains
2. Pattern matching works by evaluating patterns against data structures
3. Always include wildcard patterns for robust error handling
4. Order matters - place specific patterns before general ones
5. Pattern matching supports complex data structures like dictionaries and objects
6. Guard conditions with `if` provide additional matching flexibility
7. Match-case statements are available in Python 3.10+
8. No break statements needed - execution exits after first match
9. Multiple patterns can be combined using the `|` operator
10. Captured values from patterns are immediately available in case blocks

## Next Topic Preview

In the next lesson, we'll explore **Decorators** in Python - a powerful feature that allows you to modify or enhance functions and classes without permanently modifying their code. We'll cover:
- What decorators are and how they work
- Creating custom decorators
- Built-in decorators like @property and @staticmethod
- Decorator patterns and best practices
- Advanced decorator techniques with parameters

This will build upon your understanding of functions and provide powerful tools for code organization and reuse.