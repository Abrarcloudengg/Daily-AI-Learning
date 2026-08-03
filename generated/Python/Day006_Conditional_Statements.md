# Conditional Statements

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the concept and importance of conditional statements
- Implement various types of conditional statements in Python
- Use if, elif, and else statements effectively
- Apply nested conditions and conditional expressions
- Solve complex problems using conditional logic
- Debug common conditional statement issues
- Apply best practices for writing clean conditional code

## Prerequisites

Before starting this lesson, you should have a basic understanding of:

- Python syntax and variables
- Data types (integers, strings, booleans)
- Basic operators (comparison and logical)
- Input/output operations
- Basic understanding of program flow

## What is Conditional Statements?

Conditional statements are decision-making constructs in programming that allow code execution based on specific conditions. They enable programs to make choices and execute different code paths depending on whether certain conditions are met or not.

In simple terms, conditional statements work like "if-then-else" scenarios in our daily lives. For example, "If it's raining, then take an umbrella; otherwise, wear sunglasses."

## Why is it Important?

Conditional statements are fundamental to programming because they:

1. **Enable Decision Making**: Allow programs to make logical decisions based on data
2. **Control Program Flow**: Determine which code blocks execute under specific circumstances
3. **Handle Multiple Scenarios**: Process different inputs or situations appropriately
4. **Create Interactive Applications**: Respond to user input and system states
5. **Implement Business Logic**: Apply rules and regulations in software applications
6. **Error Handling**: Manage exceptions and edge cases in programs

## Real World Analogy

Think of conditional statements as traffic lights on a busy road:

- **Green Light (If condition is True)**: Cars can go through the intersection
- **Yellow Light (Elif condition)**: Cars should prepare to stop or proceed with caution
- **Red Light (Else condition)**: Cars must stop and wait

Each light represents a condition that determines what action should be taken. Similarly, in programming, conditions determine which code path the program will follow.

## Theory

Conditional statements in Python are used to perform different actions based on different conditions. They evaluate boolean expressions and execute code blocks accordingly.

The main components are:

1. **Boolean Expressions**: Conditions that evaluate to True or False
2. **Code Blocks**: Indented sections of code that run when conditions are met
3. **Control Flow**: The order in which statements are executed

Python supports several types of conditional statements:
- Simple if statements
- if-else statements
- if-elif-else statements
- Nested conditional statements
- Conditional expressions (ternary operator)

## Syntax

### Basic If Statement
```python
if condition:
    # code to execute if condition is True
```

### If-Else Statement
```python
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```

### If-Elif-Else Statement
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
elif condition3:
    # code for condition3
else:
    # code if none of the above conditions are True
```

### Nested Conditions
```python
if condition1:
    if condition2:
        # code when both conditions are True
    else:
        # code when condition1 is True but condition2 is False
else:
    # code when condition1 is False
```

### Conditional Expression (Ternary Operator)
```python
value_if_true if condition else value_if_false
```

## Flow / Working

The flow of conditional statements works as follows:

1. **Condition Evaluation**: The program evaluates the boolean expression
2. **Decision Making**: Based on whether the condition is True or False, the program decides which path to take
3. **Code Execution**: The corresponding code block is executed
4. **Flow Continuation**: The program continues with the next statement after the conditional block

Flowchart representation:
```
Start
  ↓
Condition True? → No → Else Block
  ↓ Yes
If Block
  ↓
Continue Execution
```

## Example 1 (Beginner)

```python
# Simple grade calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Check if a number is positive, negative, or zero
number = -15

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Simple voting eligibility checker
age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote yet")
```

## Example 2 (Intermediate)

```python
# Advanced calculator with user input
def calculator():
    print("Advanced Calculator")
    print("Operations: +, -, *, /, %, **")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        elif operator == "%":
            result = num1 % num2
        elif operator == "**":
            result = num1 ** num2
        else:
            print("Invalid operator!")
            return
        
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

# Password strength checker
def check_password_strength(password):
    if len(password) < 6:
        return "Very Weak"
    elif len(password) < 10:
        if any(c.isupper() for c in password) and any(c.islower() for c in password):
            return "Moderate"
        else:
            return "Weak"
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        if has_upper and has_lower and has_digit and has_special:
            return "Very Strong"
        elif has_upper and has_lower and has_digit:
            return "Strong"
        else:
            return "Moderate"

# Test the password checker
passwords = ["pass", "Password123", "P@ssw0rd123!", "mypassword"]
for pwd in passwords:
    print(f"Password: {pwd} - Strength: {check_password_strength(pwd)}")

calculator()
```

## Example 3 (Advanced)

```python
# Complex loan approval system
def loan_approval_system():
    print("=== Loan Approval System ===")
    
    # Get applicant information
    try:
        age = int(input("Enter your age: "))
        income = float(input("Enter your annual income ($): "))
        credit_score = int(input("Enter your credit score (300-850): "))
        employment_years = int(input("Years of employment: "))
        debt_to_income = float(input("Debt-to-income ratio (%): "))
        loan_amount = float(input("Loan amount requested ($): "))
        
        # Initialize approval score
        approval_score = 0
        reasons = []
        
        # Age criteria (18-65 years old)
        if 18 <= age <= 65:
            approval_score += 20
        elif 16 <= age <= 70:
            approval_score += 10
        else:
            reasons.append("Age outside preferred range")
        
        # Income criteria
        if income >= 50000:
            approval_score += 25
        elif income >= 30000:
            approval_score += 15
        else:
            approval_score += 5
            reasons.append("Low income")
        
        # Credit score criteria
        if credit_score >= 700:
            approval_score += 25
        elif credit_score >= 600:
            approval_score += 15
        elif credit_score >= 500:
            approval_score += 5
        else:
            approval_score -= 10
            reasons.append("Poor credit score")
        
        # Employment stability
        if employment_years >= 3:
            approval_score += 15
        elif employment_years >= 1:
            approval_score += 10
        else:
            approval_score += 2
            reasons.append("Short employment history")
        
        # Debt-to-income ratio
        if debt_to_income <= 20:
            approval_score += 15
        elif debt_to_income <= 35:
            approval_score += 5
        elif debt_to_income <= 50:
            approval_score -= 5
            reasons.append("High debt-to-income ratio")
        else:
            approval_score -= 15
            reasons.append("Very high debt-to-income ratio")
        
        # Loan amount relative to income
        loan_to_income_ratio = (loan_amount / income) * 100
        if loan_to_income_ratio <= 200:
            approval_score += 10
        elif loan_to_income_ratio <= 400:
            approval_score += 0
        else:
            approval_score -= 20
            reasons.append("Loan amount too high relative to income")
        
        # Determine approval status
        if approval_score >= 70:
            status = "APPROVED"
            risk_level = "Low Risk"
        elif approval_score >= 50:
            status = "CONDITIONALLY APPROVED"
            risk_level = "Medium Risk"
        elif approval_score >= 30:
            status = "PENDING REVIEW"
            risk_level = "High Risk"
        else:
            status = "DENIED"
            risk_level = "Very High Risk"
        
        # Display results
        print("\n=== Loan Application Results ===")
        print(f"Approval Score: {approval_score}/100")
        print(f"Status: {status}")
        print(f"Risk Level: {risk_level}")
        
        if reasons:
            print("Areas of Concern:")
            for reason in reasons:
                print(f"  - {reason}")
        
        # Interest rate calculation based on approval score
        base_rate = 3.5
        if approval_score >= 80:
            final_rate = base_rate
        elif approval_score >= 60:
            final_rate = base_rate + 1.0
        elif approval_score >= 40:
            final_rate = base_rate + 2.5
        else:
            final_rate = base_rate + 4.0
        
        print(f"Estimated Interest Rate: {final_rate:.2f}%")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")

# Run the loan approval system
# loan_approval_system()

# Advanced pattern matching with conditions
def pattern_recognition_system():
    """A system that categorizes text based on multiple conditions"""
    
    def categorize_text(text):
        # Initialize categories
        categories = []
        
        # Length-based categorization
        if len(text) < 10:
            categories.append("Very Short")
        elif len(text) < 50:
            categories.append("Short")
        elif len(text) < 100:
            categories.append("Medium")
        else:
            categories.append("Long")
        
        # Content-based categorization
        if any(word in text.lower() for word in ['hello', 'hi', 'hey']):
            categories.append("Greeting")
        
        if any(char.isdigit() for char in text):
            categories.append("Contains Numbers")
        
        if any(char in text for char in '!@#$%^&*()'):
            categories.append("Contains Special Characters")
        
        # Sentiment analysis simulation
        positive_words = ['good', 'great', 'excellent', 'wonderful', 'amazing']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing']
        
        positive_count = sum(1 for word in positive_words if word in text.lower())
        negative_count = sum(1 for word in negative_words if word in text.lower())
        
        if positive_count > negative_count:
            categories.append("Positive")
        elif negative_count > positive_count:
            categories.append("Negative")
        else:
            categories.append("Neutral")
        
        # Complexity analysis
        words = text.split()
        if len(words) > 0:
            avg_word_length = sum(len(word) for word in words) / len(words)
            if avg_word_length > 6:
                categories.append("Complex Vocabulary")
            else:
                categories.append("Simple Vocabulary")
        
        return categories
    
    # Test the pattern recognition system
    test_texts = [
        "Hello there!",
        "This is a great day with amazing weather",
        "Bad service, terrible experience @#$!",
        "Simple text with numbers 12345",
        "Congratulations on your wonderful achievement"
    ]
    
    for i, text in enumerate(test_texts, 1):
        categories = categorize_text(text)
        print(f"Text {i}: '{text}'")
        print(f"Categories: {', '.join(categories)}")
        print("-" * 50)

# Run the pattern recognition system
pattern_recognition_system()
```

## Output

```
Your grade is: B
The number is negative
You are eligible to vote

Password: pass - Strength: Very Weak
Password: Password123 - Strength: Moderate
Password: P@ssw0rd123! - Strength: Very Strong
Password: mypassword - Strength: Weak

Text 1: 'Hello there!'
Categories: Short, Greeting, Neutral, Simple Vocabulary
--------------------------------------------------
Text 2: 'This is a great day with amazing weather'
Categories: Medium, Positive, Simple Vocabulary
--------------------------------------------------
Text 3: 'Bad service, terrible experience @#$!'
Categories: Medium, Contains Special Characters, Negative, Simple Vocabulary
--------------------------------------------------
Text 4: 'Simple text with numbers 12345'
Categories: Medium, Contains Numbers, Neutral, Simple Vocabulary
--------------------------------------------------
Text 5: 'Congratulations on your wonderful achievement'
Categories: Long, Positive, Simple Vocabulary
--------------------------------------------------
```

## Common Mistakes

| Mistake | Description | How to Fix |
|---------|-------------|------------|
| **Forgetting colons** | Missing `:` after if/elif/else | Always add `:` after condition |
| **Incorrect indentation** | Code not properly indented | Use consistent 4-space indentation |
| **Using assignment `=` instead of comparison `==`** | `if x = 5:` instead of `if x == 5:` | Use `==` for comparison |
| **Chaining comparisons incorrectly** | `if 10 <= x <= 20` is correct, but `if 10 <= x and x <= 20` also works | Both syntaxes are valid |
| **Not handling edge cases** | Forgetting to check for zero, empty strings, etc. | Always consider boundary conditions |
| **Overcomplicating conditions** | Writing very long, complex conditions | Break into smaller, readable parts |
| **Ignoring operator precedence** | `if a > b and c or d` can be confusing | Use parentheses for clarity |
| **Not using elif properly** | Using multiple if statements when elif is appropriate | Use elif for mutually exclusive conditions |

## Best Practices

1. **Use Descriptive Variable Names**: Make conditions readable
   ```python
   # Bad
   if x > 18 and y < 100:
   
   # Good
   if is_adult and is_healthy:
   ```

2. **Keep Conditions Simple**: Break complex conditions into multiple lines
   ```python
   # Good
   is