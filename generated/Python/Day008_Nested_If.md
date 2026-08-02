# Nested If

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what nested if statements are and how they work
- Implement nested if structures in Python programs
- Apply nested conditions for complex decision-making scenarios
- Debug common issues with nested if statements
- Write clean and efficient nested conditional logic
- Solve real-world problems using nested if constructs

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax
- Knowledge of simple if-else statements
- Familiarity with comparison operators (<, >, ==, !=, <=, >=)
- Understanding of logical operators (and, or, not)
- Experience with basic data types (int, float, string, boolean)
- Ability to write and run Python programs

## What is Nested If?

Nested if statements refer to the practice of placing one if statement inside another if statement. This creates a hierarchical structure where inner conditions are only evaluated when outer conditions are met. The term "nested" comes from the idea of nesting dolls - each condition sits inside another, creating layers of decision-making logic.

In practical terms, nested if allows us to check multiple conditions sequentially, where each subsequent condition depends on the outcome of previous conditions. This enables more sophisticated control flow in our programs.

## Why is it Important?

Nested if statements are crucial for several reasons:

1. **Complex Decision Making**: Real-world applications often require checking multiple conditions that depend on each other
2. **Code Organization**: Helps organize complex logic in a structured manner
3. **Efficiency**: Prevents unnecessary checks when outer conditions aren't met
4. **Readability**: Makes program logic clearer by grouping related conditions
5. **Error Prevention**: Ensures prerequisites are met before proceeding to deeper checks
6. **Real-world Applications**: Essential for authentication systems, game logic, business rules, etc.

## Real World Analogy

Think of nested if statements like navigating through security checkpoints at an airport:

1. First checkpoint: Do you have a boarding pass? (Outer if)
   - If NO → You can't proceed
   - If YES → Move to next checkpoint
   
2. Second checkpoint: Is your ID valid? (First level nested if)
   - If NO → You can't proceed
   - If YES → Move to next checkpoint
   
3. Third checkpoint: Do you pass security screening? (Second level nested if)
   - If NO → You can't proceed
   - If YES → You're allowed to board

Each checkpoint depends on passing the previous one. You don't get to security screening without a boarding pass and valid ID.

## Theory

Nested if statements create a tree-like structure of conditional execution. The general principle follows these rules:

1. **Sequential Evaluation**: Conditions are checked from outermost to innermost
2. **Conditional Execution**: Inner blocks only execute if all outer conditions are true
3. **Scope Rules**: Variables defined in outer blocks are accessible in inner blocks
4. **Early Exit**: If any condition fails, remaining nested conditions are skipped
5. **Indentation Matters**: Python uses indentation to define code blocks

The complexity grows exponentially with nesting depth, so it's important to maintain readability and avoid excessive nesting levels.

## Syntax

```python
if condition1:
    # Outer block code
    if condition2:
        # First level nested block
        if condition3:
            # Second level nested block
            # Code here executes only if all three conditions are True
        else:
            # Executes if condition3 is False but condition1 and condition2 are True
    else:
        # Executes if condition2 is False but condition1 is True
else:
    # Executes if condition1 is False
```

Key points about syntax:
- Each nested if must be properly indented
- Every if requires a colon (:)
- else and elif clauses are optional but must align with their corresponding if
- Indentation defines the scope of each block

## Flow / Working

The execution flow of nested if statements follows these steps:

1. **Start** with the outermost if condition
2. **Evaluate** the outer condition
3. **If False** → Skip entire nested block and continue after the outer else/elif/end
4. **If True** → Execute the outer block and move to the first nested if
5. **Repeat** evaluation process for each nested level
6. **Execute** the deepest matching block based on all conditions
7. **Exit** back to the main program flow

Visual representation:
```
Main Program
    ↓
Outer IF (Condition 1)
    ├── True → Nested IF (Condition 2)
    │           ├── True → Deep Nested IF (Condition 3)
    │           │           ├── True → Execute deepest block
    │           │           └── False → Execute else of deepest
    │           └── False → Execute else of second level
    └── False → Execute else of outer or continue main program
    ↓
Main Program Continues
```

## Example 1 (Beginner)

Let's create a simple program to determine if someone can vote based on age and citizenship:

```python
# Voting eligibility checker
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ").lower()

if age >= 18:
    print("Age requirement met.")
    if citizenship == "yes":
        print("Citizenship requirement met.")
        print("Congratulations! You are eligible to vote.")
    else:
        print("Sorry, you must be a citizen to vote.")
else:
    print("Sorry, you must be at least 18 years old to vote.")

print("Thank you for checking your voting eligibility!")
```

This example demonstrates:
- Two-level nesting
- User input processing
- Clear conditional logic flow
- Informative output messages

## Example 2 (Intermediate)

Let's build a more complex grading system that considers multiple factors:

```python
# Advanced student grading system
student_name = input("Enter student name: ")
attendance_percentage = float(input("Enter attendance percentage: "))
assignment_score = float(input("Enter assignment score (0-100): "))
exam_score = float(input("Enter exam score (0-100): "))

print(f"\n--- Grade Report for {student_name} ---")

# Check attendance first
if attendance_percentage >= 75:
    print("✓ Attendance requirement met")
    
    # Check assignment performance
    if assignment_score >= 60:
        print("✓ Assignment requirement met")
        
        # Calculate final grade based on exam
        if exam_score >= 90:
            grade = "A"
            status = "Excellent work!"
        elif exam_score >= 80:
            grade = "B"
            status = "Good job!"
        elif exam_score >= 70:
            grade = "C"
            status = "Satisfactory performance."
        elif exam_score >= 60:
            grade = "D"
            status = "Passing grade, but needs improvement."
        else:
            grade = "F"
            status = "Failed - needs significant improvement."
            
        print(f"Final Grade: {grade}")
        print(f"Status: {status}")
        
    else:
        print("✗ Assignment score too low")
        print("Grade: F (Incomplete requirements)")
        
else:
    print("✗ Attendance below 75%")
    print("Grade: F (Attendance requirement not met)")

print("--- End of Report ---")
```

This intermediate example shows:
- Three-level nesting
- Multiple input validations
- Combined conditional logic
- Detailed feedback system
- Proper formatting and user experience

## Example 3 (Advanced)

Let's create a comprehensive banking system with multiple account types and transaction rules:

```python
# Advanced Banking System with Nested Conditions
class BankAccount:
    def __init__(self, account_type, balance, account_age_months):
        self.account_type = account_type.lower()
        self.balance = balance
        self.account_age = account_age_months
        self.transaction_fee = 0
    
    def process_transaction(self, transaction_type, amount):
        print(f"\nProcessing {transaction_type.upper()} transaction...")
        print(f"Amount: ${amount:.2f}")
        
        # Check if transaction type is valid
        if transaction_type.lower() in ['deposit', 'withdrawal']:
            
            # Handle deposits
            if transaction_type.lower() == 'deposit':
                if amount > 0:
                    if amount >= 10000:  # Large deposit check
                        print("Large deposit detected. May require additional verification.")
                        verification = input("Proceed with verification? (yes/no): ").lower()
                        if verification == 'yes':
                            self.balance += amount
                            print(f"Deposit successful! New balance: ${self.balance:.2f}")
                        else:
                            print("Transaction cancelled by user.")
                    else:
                        self.balance += amount
                        print(f"Deposit successful! New balance: ${self.balance:.2f}")
                else:
                    print("Error: Deposit amount must be positive.")
            
            # Handle withdrawals
            else:  # withdrawal
                if amount > 0:
                    # Check sufficient funds
                    if self.balance >= amount:
                        
                        # Account-specific withdrawal rules
                        if self.account_type == 'checking':
                            
                            # Checking account rules
                            if self.account_age >= 6:  # Account older than 6 months
                                if amount <= 500:  # Small withdrawal
                                    self.balance -= amount
                                    print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
                                else:  # Large withdrawal
                                    if self.balance >= (amount + 10):  # Can cover fee
                                        self.balance -= (amount + 10)
                                        print(f"Withdrawal successful! $10 fee applied.")
                                        print(f"New balance: ${self.balance:.2f}")
                                    else:
                                        print("Insufficient funds for transaction fee.")
                            else:  # New account restrictions
                                if amount <= 300:
                                    self.balance -= amount
                                    print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
                                else:
                                    print("New accounts limited to $300 withdrawals.")
                                    
                        elif self.account_type == 'savings':
                            
                            # Savings account rules
                            if self.account_age >= 12:  # Mature savings account
                                monthly_withdrawals = int(input("How many withdrawals this month? "))
                                if monthly_withdrawals < 6:  # Within limit
                                    self.balance -= amount
                                    print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
                                else:
                                    if self.balance >= (amount + 5):  # Can cover excess fee
                                        self.balance -= (amount + 5)
                                        print("Excess withdrawal fee ($5) applied.")
                                        print(f"New balance: ${self.balance:.2f}")
                                    else:
                                        print("Insufficient funds for excess fee.")
                            else:  # New savings account
                                print("New savings accounts cannot make withdrawals.")
                                
                        else:
                            print("Invalid account type for withdrawal.")
                            
                    else:
                        print("Insufficient funds for withdrawal.")
                else:
                    print("Withdrawal amount must be positive.")
                    
        else:
            print("Invalid transaction type. Use 'deposit' or 'withdrawal'.")

# Example usage
account = BankAccount('checking', 1500.00, 8)
account.process_transaction('withdrawal', 600)

# Another example with savings account
savings_account = BankAccount('savings', 5000.00, 15)
savings_account.process_transaction('withdrawal', 1000)
```

This advanced example demonstrates:
- Multi-level complex nesting (up to 5+ levels)
- Object-oriented approach with class methods
- Real-world business logic implementation
- Interactive user input within nested conditions
- Error handling and validation at multiple levels
- Dynamic fee calculations based on conditions

## Output

### Example 1 Output:
```
Enter your age: 20
Are you a citizen? (yes/no): yes
Age requirement met.
Citizenship requirement met.
Congratulations! You are eligible to vote.
Thank you for checking your voting eligibility!
```

### Example 2 Output:
```
Enter student name: John Smith
Enter attendance percentage: 85
Enter assignment score (0-100): 75
Enter exam score (0-100): 88

--- Grade Report for John Smith ---
✓ Attendance requirement met
✓ Assignment requirement met
Final Grade: B
Status: Good job!
--- End of Report ---
```

### Example 3 Output:
```
Processing WITHDRAWAL transaction...
Amount: $600.00
Withdrawal successful! $10 fee applied.
New balance: $890.00
```

## Common Mistakes

| Mistake | Description | How to Fix |
|---------|-------------|------------|
| Improper indentation | Incorrect spacing causing wrong code blocks | Use consistent 4-space indentation |
| Missing colons | Forgetting `:` after if statements | Always add colon after condition |
| Logic errors | Conditions in wrong order | Plan logic flow before coding |
| Infinite nesting | Too many nested levels | Refactor using functions or loops |
| Forgotten else cases | Not handling all possible outcomes | Add appropriate else clauses |
| Variable scope issues | Using undefined variables in nested blocks | Define variables in correct scope |
| Redundant conditions | Checking same condition multiple times | Optimize condition placement |

## Best Practices

1. **Limit Nesting Depth**: Keep nesting to maximum 3-4 levels for readability
2. **Use Early Returns**: Exit early when conditions fail to reduce nesting
3. **Descriptive Variable Names**: Make conditions self-documenting
4. **Comment Complex Logic**: Explain why certain nested conditions exist
5. **Consistent Formatting**: Maintain uniform indentation and spacing
6. **Validate Inputs Early**: Check prerequisites before deep nesting
7. **Extract Functions**: Break complex nested logic into separate functions
8. **Test Edge Cases**: Verify behavior with boundary values
9. **Use Logical Operators**: Combine conditions when appropriate to reduce nesting
10. **Document Assumptions**: Note dependencies between nested conditions

## Pro Tips

1. **Guard Clauses**: Use early returns to reduce nesting:
   ```python
   if not condition1:
       return  # or handle error
   # Continue with nested logic
   ```

2. **Combine Conditions**: Use `and` operator when possible:
   ```python
   # Instead of nesting
   if condition1:
       if condition2:
           # do something
   
   # Better approach
   if condition1 and condition2:
       # do something
   ```

3. **Dictionary Mapping**: Replace some nested ifs with dictionaries:
   ```python
   grade_map = {
       'A': lambda score: score >= 90,
       'B': lambda score: score >= 80,
       # ...
   }
   ```

4. **Ternary Operators**: Simplify simple nested conditions:
   ```python
   result = "pass" if score >= 60 else "fail"
   ```

5. **State Pattern**: For very complex nested logic, consider design patterns

## Interview Questions (10)

1. **What is a nested if statement and when would you use it?**
2. **How does the execution flow work in nested if statements?**
3. **What are the potential drawbacks of deeply nested if statements?**
4. **How can you reduce the complexity of nested if statements?**
5. **Explain the difference between nested if and if-elif-else chains.**
6. **What happens to variable scope in nested if blocks?**
7. **How do you handle error conditions in nested if structures?**
8. **Can you convert a nested if into a single if with logical operators? When would you do this?**
9. **What are guard clauses and how do they relate to nested if statements?**
10. **Describe a real-world scenario where nested if statements would be the appropriate solution.**

## MCQs (10)

1. **How many levels of nesting are typically recommended for good code readability?**
   a) 1-2 levels  
   b) 3-4 levels  
   c) 5-6 levels  
   d) No limit  

2. **What happens when an outer if condition evaluates to False in a nested structure?**
   a) All inner conditions still execute  
   b) Only the immediate nested if executes  
   c) All nested conditions are skipped  
