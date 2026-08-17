# Scope (Local and Global)

## Learning Objectives

- Understand the concept of variable scope in Python
- Differentiate between local and global scope
- Learn how to access and modify variables across different scopes
- Master the `global` and `nonlocal` keywords
- Apply scope rules to write clean, efficient code
- Avoid common scope-related errors

## Prerequisites

- Basic understanding of Python variables and data types
- Knowledge of Python functions
- Familiarity with basic Python syntax
- Understanding of variable assignment

## What is Scope (Local and Global)?

Scope in Python refers to the region of code where a variable is accessible. Think of scope as the visibility boundary of variables - where they can be "seen" and used within your program.

**Global scope**: Variables declared outside of any function that can be accessed from anywhere in the program.

**Local scope**: Variables declared inside a function that can only be accessed within that function.

Scope determines where in your code a variable can be referenced. Variables in Python don't exist everywhere - they have boundaries defined by where they're created.

## Why is it Important?

Understanding scope is crucial for several reasons:

1. **Avoiding naming conflicts**: Prevents accidentally overwriting variables
2. **Memory management**: Local variables are automatically cleaned up when functions finish
3. **Code organization**: Helps structure programs logically
4. **Debugging**: Makes it easier to track variable values and changes
5. **Security**: Local variables can't be accidentally modified from outside functions
6. **Performance**: Local variable access is faster than global access

Proper scope management leads to more predictable, maintainable, and efficient code.

## Real World Analogy

Think of scope like rooms in a house:

- **Global scope** = The entire house - everyone can access common areas like the living room
- **Local scope** = Individual bedrooms - only the person in that room can access their private items

If you want to access something in someone else's room (local scope), you need special permission (the `global` keyword). Similarly, items in the living room (global scope) can be accessed by anyone, but modifying them requires explicit declaration.

## Theory

Python follows the **LEGB Rule** for scope resolution:

1. **L**ocal - Inside the current function
2. **E**nclosing - Inside enclosing functions (nested functions)
3. **G**lobal - At the module level
4. **B**uilt-in - Predefined names in Python

When Python looks for a variable:
- It first checks the local scope
- Then enclosing scopes (if any)
- Then the global scope
- Finally the built-in scope

If the variable isn't found in any scope, Python raises a `NameError`.

## Syntax

```python
# Global variable
global_variable = "I'm global"

def my_function():
    # Local variable
    local_variable = "I'm local"
    print(local_variable)
    print(global_variable)  # Can access global variables

# Using global keyword
def modify_global():
    global global_variable
    global_variable = "Modified globally"

# Using nonlocal keyword (for nested functions)
def outer_function():
    enclosing_var = "I'm enclosing"

    def inner_function():
        nonlocal enclosing_var
        enclosing_var = "Modified in inner function"
```

## Flow / Working

1. **Variable Creation**: Python creates scope when entering functions or modules
2. **Variable Lookup**: When accessing a variable, Python searches LEGB order
3. **Assignment**: Creates new local variable unless `global` or `nonlocal` is used
4. **Function Execution**: Local variables exist only during function execution
5. **Cleanup**: Local variables are destroyed when function exits
6. **Global Access**: Global variables persist throughout program execution

## Example 1 (Beginner)

```python
# Global variable
message = "Hello from global scope"

def greet():
    # Local variable
    message = "Hello from local scope"
    print(message)

def display_global():
    # Accessing global variable
    print(message)

# Main code
print("Global message:", message)
greet()
display_global()
print("Global message after function calls:", message)
```

## Example 2 (Intermediate)

```python
# Global counter
counter = 0

def increment():
    # This creates a new local variable, not modifying global
    counter = counter + 1  # This will cause UnboundLocalError
    return counter

def increment_correct():
    global counter  # Declare we want to modify the global variable
    counter = counter + 1
    return counter

def demonstrate_scopes():
    # Local variable
    x = "local x"

    def inner():
        # Enclosing scope variable
        y = "local y"
        print("Inner function - x:", x)
        print("Inner function - y:", y)

        # Access built-in function
        print("Built-in len function:", len("test"))

    inner()
    print("Outer function - x:", x)
    # print(y)  # This would cause NameError - y is not accessible here

# Demonstration
print("Initial counter:", counter)
# increment()  # Uncommenting this would raise UnboundLocalError
print("After increment_correct():", increment_correct())
print("Counter value:", counter)
demonstrate_scopes()
```

## Example 3 (Advanced)

```python
# Advanced scope demonstration with nested functions
def outer_function(x):
    """Outer function with enclosing scope"""
    enclosing_var = x * 2

    def middle_function(y):
        """Middle function with nested scope"""
        nonlocal enclosing_var  # Refers to enclosing scope

        def inner_function(z):
            """Innermost function"""
            global global_result  # Refers to global scope
            global_result = enclosing_var + y + z
            enclosing_var = enclosing_var + 10  # Modifies enclosing scope
            return global_result

        result = inner_function(5)
        print(f"Middle function sees enclosing_var as: {enclosing_var}")
        return result

    print(f"Before middle function, enclosing_var: {enclosing_var}")
    final_result = middle_function(10)
    print(f"After middle function, enclosing_var: {enclosing_var}")
    return final_result

# Global variable to store result
global_result = 0

# Main execution
print("Initial global_result:", global_result)
result = outer_function(3)
print("Final global_result:", global_result)
print("Function returned:", result)

# Demonstrate closure behavior
def create_multiplier(factor):
    """Creates a function that multiplies by factor"""
    def multiplier(number):
        return number * factor  # factor is captured in closure
    return multiplier

# Create specific multipliers
double = create_multiplier(2)
triple = create_multiplier(3)

print("Double of 5:", double(5))
print("Triple of 4:", triple(4))
print("Factor is preserved in closure:", double.__closure__[0].cell_contents)
```

## Output

```
Global message: Hello from global scope
Hello from local scope
Hello from global scope
Global message after function calls: Hello from global scope
Initial counter: 0
After increment_correct(): 1
Counter value: 1
Inner function - x: local x
Inner function - y: local y
Built-in len function: 4
Outer function - x: local x
Before middle function, enclosing_var: 6
Middle function sees enclosing_var as: 16
After middle function, enclosing_var: 16
Final global_result: 31
Function returned: 31
Double of 5: 10
Triple of 4: 12
Factor is preserved in closure: 2
```

## Common Mistakes

| Mistake | Correct Approach | Explanation |
|---------|------------------|-------------|
| `counter = counter + 1` in function | `global counter` then increment | Local variables can't reference themselves before assignment |
| Modifying global lists without `global` | Usually works for mutable objects | Mutable globals can be modified without `global` but not reassigned |
| Accessing local variables outside scope | Return values or use global variables | Local scope is limited to function execution |
| Nested function modifying enclosing scope | Use `nonlocal` keyword | Required to modify (not just read) enclosing variables |
| Assuming all outer variables are global | Understand LEGB rule | Enclosing scope is different from global scope |

## Best Practices

1. **Minimize global variables**: Use function parameters and return values instead
2. **Use descriptive names**: Makes scope boundaries clear
3. **Explicit is better than implicit**: Always declare `global` or `nonlocal` when needed
4. **Keep functions pure**: Avoid modifying global state when possible
5. **Limit scope of variables**: Declare variables in the narrowest scope possible
6. **Use constants for global values**: Uppercase names for global constants
7. **Document scope intentions**: Comment when using global/nonlocal keywords
8. **Avoid deep nesting**: Flatten nested scopes when possible for clarity

## Pro Tips

1. **Closures for state**: Use nested functions to create functions with "memory"
2. **Debugging scopes**: Use `locals()` and `globals()` to inspect current scopes
3. **Performance consideration**: Local variable access is faster than global
4. **Scope in comprehensions**: List comprehensions have their own local scope in Python 3
5. **Lambda scope**: Lambdas follow same scope rules as regular functions
6. **Class scope**: Class definitions create their own scope rules
7. **Exception handling**: Exception variables have their own scope in except blocks
8. **Import scope**: Imported modules become global variables in the importing module

## Interview Questions (10)

1. Explain the difference between local and global scope in Python.
2. What is the LEGB rule and how does it apply to variable lookup?
3. When do you need to use the `global` keyword?
4. How does the `nonlocal` keyword differ from `global`?
5. What happens if you try to modify a global variable inside a function without declaring it global?
6. Explain what a closure is and how it relates to scope.
7. How does Python handle variable scope in nested functions?
8. What is the difference between accessing and modifying a global variable inside a function?
9. Can you modify a list that's a global variable inside a function without using `global`?
10. How does scope work in list comprehensions?

## MCQs (10)

1. What is the output of:
```python
x = 10
def func():
    x = 20
    print(x)
func()
print(x)
```
   a) 20, 20  b) 10, 10  c) 20, 10  d) 10, 20

2. Which keyword is used to modify a global variable inside a function?
   a) `local`  b) `global`  c) `nonlocal`  d) `external`

3. In which order does Python search for variables?
   a) Global, Local, Enclosing, Built-in  b) Local, Enclosing, Global, Built-in
   c) Built-in, Global, Enclosing, Local  d) Local, Global, Enclosing, Built-in

4. What happens when you assign a value to a variable inside a function?
   a) It always modifies the global variable
   b) It creates a new local variable
   c) It causes an error
   d) It depends on the variable name

5. What is the scope of variables in a list comprehension?
   a) Global  b) Local to the enclosing function  c) Their own local scope  d) Built-in

6. Which statement about `nonlocal` is true?
   a) It can reference global variables  b) It references enclosing scope variables
   c) It creates new local variables  d) It's used for built-in variables

7. What exception is raised when a local variable is referenced before assignment?
   a) `NameError`  b) `ValueError`  c) `UnboundLocalError`  d) `ReferenceError`

8. Can you access a global variable inside a function without any special keyword?
   a) Yes, always  b) No, never  c) Only if not assigned locally  d) Only in nested functions

9. What does `globals()` function return?
   a) All local variables  b) All global variables as a dictionary
   c) Built-in functions  d) Module names

10. How many scopes can a variable potentially belong to in Python?
    a) 1  b) 2  c) 3  d) 4

## Practice Questions (10)

1. Create a function that counts how many times it's been called using a global variable.
2. Write a program that demonstrates accessing global variables from nested functions.
3. Implement a function that creates a counter using closures.
4. Create a scenario where `nonlocal` is necessary and demonstrate its use.
5. Show the difference between mutable and immutable global variables in function modification.
6. Write code that demonstrates the scope of exception variables in try-except blocks.
7. Create a nested function example showing all four levels of LEGB.
8. Implement a configuration manager that uses global scope appropriately.
9. Demonstrate how to preserve state using function attributes instead of global variables.
10. Show how class variables differ from global variables in terms of scope.

## Coding Exercises (5)

1. **Temperature Converter with History**:
```python
# Create global list to store conversion history
conversion_history = []

def celsius_to_fahrenheit(celsius):
    global conversion_history
    fahrenheit = (celsius * 9/5) + 32
    conversion_history.append(f"{celsius}°C = {fahrenheit}°F")
    return fahrenheit

def get_history():
    global conversion_history
    return conversion_history.copy()  # Return copy to prevent external modification

# Test the functions
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print("History:", get_history())
```

2. **Bank Account with Nested Functions**:
```python
def create_account(initial_balance):
    balance = initial_balance  # Enclosing scope

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return "Insufficient funds"

    def get_balance():
        return balance

    # Return functions as a dictionary (closure)
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance
    }

# Test the account
account = create_account(1000)
print("Initial balance:", account['balance']())
print("After deposit:", account['deposit'](500))
print("After withdrawal:", account['withdraw'](200))
```

3. **Configuration Manager**:
```python
# Global configuration
config = {
    'debug': False,
    'max_connections': 100,
    'timeout': 30
}

def update_config(key, value):
    global config
    if key in config:
        old_value = config[key]
        config[key] = value
        print(f"Updated {key}: {old_value} -> {value}")
    else:
        print(f"Unknown config key: {key}")

def get_config(key=None):
    global config
    if key is None:
        return config.copy()
    return config.get(key, "Key not found")

# Test configuration
print("Current config:", get_config())
update_config('debug', True)
print("Debug mode:", get_config('debug'))
```

4. **Scope Chain Demonstration**:
```python
global_var = "I'm global"

def level1():
    level1_var = "Level 1"

    def level2():
        level2_var = "Level 2"

        def level3():
            level3_var = "Level 3"
            # Access all levels
            print(f"Accessing: {global_var}")
            print(f"Accessing: {level1_var}")
            print(f"Accessing: {level2_var}")
            print(f"Accessing: {level3_var}")

            # Built-in function access
            print(f"Built-in function len(): {len(level3_var)}")

        level3()

    level2()

level1()
```

5. **Closure-Based Counter**:
```python
def create_counter():
    count = 0  # Enclosing scope

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    # Return the counter functions
    return increment, decrement, get_count

# Test the counter
inc, dec, get = create_counter()
print("Initial:", get())
print("After increment:", inc())
print("After increment:", inc())
print("After decrement:", dec())
print("Final count:", get())

# Create another independent counter
inc2, dec2, get2 = create_counter()
print("Second counter:", get2())
print("First counter still:", get())
```

## Mini Project

**Personal Finance Tracker with Scope Management**

```python
# Global financial data
total_income = 0
total_expenses = 0
transactions = []

def add_transaction():
    """Add a new transaction - demonstrates local scope"""
    def get_transaction_details():
        # Local variables
        type_input = input("Enter type (income/expense): ").lower()
        amount_input = float(input("Enter amount: $"))
        description_input = input("Enter description: ")
        return type_input, amount_input, description_input

    try:
        trans_type, amount, description = get_transaction_details()

        if trans_type not in ['income', 'expense']:
            print("Invalid transaction type!")
            return

        # Local transaction data
        transaction = {
            'type': trans_type,
            'amount': amount,
            'description': description
        }

        # Update global financial data
        global total_income, total_expenses, transactions
        transactions.append(transaction)

        if trans_type == 'income':
            total_income += amount
        else:
            total_expenses += amount

        print(f"Transaction added: {trans_type} of ${amount}")

    except ValueError:
        print("Invalid amount entered!")

def get_financial_summary():
    """Calculate and return financial summary - uses global scope"""
    global total_income, total_expenses

    net_balance = total_income - total_expenses

    def format_currency(amount):
        # Local helper function
        return f"${amount:,.2f}"

    summary = {
        'total_income': format_currency(total_income),
        'total_expenses': format_currency(total_expenses),
        'net_balance': format_currency(net_balance)
    }

    return summary

def display_transactions():
    """Display all transactions with nested function"""
    global transactions

    def display_transaction(index, trans):
        # Nested function with access to enclosing scope
        def get_type_symbol(trans_type):
            return "+" if trans_type == 'income' else "-"

        symbol = get_type_symbol(trans['type'])
        print(f"{index+1}. {symbol}${trans['amount']} - {trans['description']}")

    if not transactions:
        print("No transactions recorded.")
        return

    print("\n--- Transaction History ---")
    for i, trans in enumerate(transactions):
        display_transaction(i, trans)

def main():
    """Main program function - demonstrates scope flow"""
    print("Personal Finance Tracker")
    print("=" * 25)

    while True:
        print("\n1. Add Transaction")
        print("2. View Summary")
        print("3. View Transactions")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            summary = get_financial_summary()
            print(f"\nFinancial Summary:")
            print(f"Income: {summary['total_income']}")
            print(f"Expenses: {summary['total_expenses']}")
            print(f"Balance: {summary['net_balance']}")
        elif choice == '3':
            display_transactions()
        elif choice == '4':
            print("Thank you for using Finance Tracker!")
            break
        else:
            print("Invalid choice!")

# Run the program
# main()  # Uncomment to run interactively
```

## Assignment

**Inventory Management System with Scope Control**

Create a comprehensive inventory management system that demonstrates advanced scope concepts:

Requirements:
1. Global inventory dictionary
2. Nested functions for different operations
3. Use of `global` and `nonlocal` keywords appropriately
4. Closure-based logging system
5. Configuration management with proper scoping
6. Error handling that respects scope boundaries

Deliverables:
1. Complete working code with comments
2. Test cases demonstrating scope behavior
3. Documentation explaining scope usage in each function
4. Analysis of potential scope-related issues and solutions

## Summary

Scope in Python defines where variables can be accessed and modified. Understanding scope is fundamental to writing clean, efficient Python code. We learned:

- **Local scope** exists within functions and is destroyed when functions exit
- **Global scope** exists at the module level and persists throughout program execution
- Python follows the LEGB rule for variable lookup: Local, Enclosing, Global, Built-in
- The `global` keyword allows modification of global variables inside functions
- The `nonlocal` keyword allows modification of enclosing scope variables
- Proper scope management prevents naming conflicts and improves code maintainability
- Closures capture enclosing scope variables for later use

## Key Takeaways

1. Scope determines variable visibility and lifetime
2. Always use `global` or `nonlocal` when modifying outer scope variables
3. Local variables are faster to access than global ones
4. Nested functions can access enclosing scope variables
5. LEGB rule governs variable lookup order
6. Closures preserve enclosing scope for later function calls
7. Minimize global variable usage for better code design
8. Understanding scope prevents common programming errors

## Next Topic Preview

In the next lesson, we'll explore **Python Modules and Packages** - how to organize code across multiple files, import functionality, and create reusable code libraries. We'll cover module creation, import statements, package structure, and best practices for code organization.
