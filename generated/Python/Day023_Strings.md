# Strings

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what strings are and how they work in Python
- Manipulate strings using various built-in methods
- Format strings using different techniques
- Work with string indexing and slicing
- Handle string encoding and special characters
- Apply string methods in real-world scenarios
- Solve complex problems using string operations
- Debug common string-related issues
- Follow best practices for string manipulation
- Prepare for technical interviews involving strings

## Prerequisites

Before starting this lesson, you should have:
- Basic understanding of Python syntax
- Knowledge of variables and data types
- Familiarity with basic operators
- Understanding of functions and methods
- Basic knowledge of loops and conditionals

## What is Strings?

A string in Python is a sequence of characters enclosed within quotes (single, double, or triple quotes). Strings are immutable, meaning once created, they cannot be changed. They can contain letters, numbers, symbols, and whitespace. Strings are one of the most fundamental data types in programming because they represent text data.

In Python, strings are objects of the `str` class, which provides numerous built-in methods for string manipulation. Whether you're processing user input, reading files, or generating reports, you'll be working with strings extensively.

## Why is it Important?

Strings are crucial in programming because:
- Most data we work with in applications is text-based
- User interfaces primarily consist of text elements
- Data storage often involves text formats (JSON, XML, CSV)
- Web development relies heavily on string manipulation for URLs, templates, and responses
- File handling and parsing require string operations
- Communication protocols use text-based messages
- Natural language processing and text analysis depend on string operations

Understanding strings deeply allows you to process and transform text data efficiently, which is essential for building robust applications.

## Real World Analogy

Think of strings like sentences in a book. Each sentence is a sequence of characters (letters, spaces, punctuation) that conveys meaning. Just as you can analyze, edit, search, and transform sentences in a book, you can do the same with strings in programming.

You can:
- Count words in a sentence (len(), split())
- Find specific words (find(), index())
- Replace words (replace())
- Extract parts of sentences (slicing)
- Change formatting (upper(), lower())
- Combine sentences (concatenation)

## Theory

Strings in Python are:
- **Immutable**: Once created, they cannot be changed in place
- **Sequences**: They support indexing, slicing, and iteration
- **Unicode**: Support international characters (UTF-8 by default)
- **Ordered**: Characters maintain their position
- **Iterable**: Can be looped through using for loops

String methods return new string objects rather than modifying the original string. This immutability ensures that strings are safe to use across different parts of your program without worrying about accidental modifications.

Python stores strings internally as sequences of Unicode code points, which allows representation of virtually all written languages and special symbols.

## Syntax

```python
# Single quotes
string1 = 'Hello'

# Double quotes
string2 = "World"

# Triple quotes (multi-line)
string3 = """This is a
multi-line string"""

# Triple single quotes
string4 = '''Another
multi-line string'''

# Raw strings (ignore escape characters)
raw_string = r"C:\Users\Name\Documents"

# f-strings (formatted string literals)
name = "Alice"
age = 30
formatted = f"Hello, {name}. You are {age} years old."

# String concatenation
combined = "Hello" + " " + "World"

# String repetition
repeated = "Hi" * 3  # "HiHiHi"
```

## Flow / Working

When you create a string in Python:
1. Memory is allocated for the string object
2. The string is stored as a sequence of Unicode characters
3. String methods operate on this sequence to produce new strings
4. Indexing accesses individual characters by position
5. Slicing extracts substrings based on position ranges
6. String formatting combines variables with text templates
7. Comparison operations check string equality or ordering
8. Search operations find substrings within the main string

Since strings are immutable, any operation that "modifies" a string actually creates a new string object, leaving the original unchanged.

## Example 1 (Beginner)

```python
# Basic string operations
text = "Hello, World!"

# String length
print(f"Length: {len(text)}")

# Accessing characters
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# String slicing
print(f"First 5 characters: {text[:5]}")
print(f"From index 7 to end: {text[7:]}")

# String methods
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")

# Finding substrings
print(f"Position of 'World': {text.find('World')}")
print(f"Replace 'World' with 'Python': {text.replace('World', 'Python')}")

# Checking string properties
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with '!': {text.endswith('!')}")
print(f"Contains 'World': {'World' in text}")
```

## Example 2 (Intermediate)

```python
# Advanced string manipulation
import re

# String formatting with multiple methods
name = "Alice"
age = 25
score = 95.7

# Using format() method
formatted1 = "Name: {}, Age: {}, Score: {:.1f}".format(name, age, score)

# Using f-strings (Python 3.6+)
formatted2 = f"Name: {name}, Age: {age}, Score: {score:.1f}"

# Using % formatting (older method)
formatted3 = "Name: %s, Age: %d, Score: %.1f" % (name, age, score)

print(formatted1)
print(formatted2)
print(formatted3)

# String splitting and joining
sentence = "Python is a powerful programming language"
words = sentence.split()  # Split by whitespace
print(f"Words: {words}")

# Join words back together
hyphenated = "-".join(words)
print(f"Hyphenated: {hyphenated}")

# Remove whitespace
messy_text = "  Hello World!  \n\t"
cleaned = messy_text.strip()
print(f"Cleaned: '{cleaned}'")

# Regular expressions for advanced string operations
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text_with_emails = "Contact us at support@example.com or admin@test.org"
emails = re.findall(email_pattern, text_with_emails)
print(f"Found emails: {emails}")

# String translation
translation_table = str.maketrans("aeiou", "12345")
text = "Hello World"
translated = text.translate(translation_table)
print(f"Translated: {translated}")
```

## Example 3 (Advanced)

```python
# Advanced string techniques

# String encoding and decoding
text = "Hello, 世界"
encoded_utf8 = text.encode('utf-8')
decoded_utf8 = encoded_utf8.decode('utf-8')
print(f"Original: {text}")
print(f"UTF-8 encoded: {encoded_utf8}")
print(f"UTF-8 decoded: {decoded_utf8}")

# Working with escape sequences
escape_examples = [
    "Tab:\tSeparated",
    "Newline:\nSecond line",
    "Backslash:\\",
    "Quote: \"Hello\"",
    "Unicode: \u2764"  # Heart symbol
]

for example in escape_examples:
    print(example)

# Advanced string formatting with templates
from string import Template

template = Template("Hello $name, you have $count messages.")
result = template.substitute(name="Alice", count=5)
print(result)

# Safe substitution (won't raise KeyError)
result_safe = template.safe_substitute(name="Bob")
print(result_safe)

# String alignment and padding
text = "Centered"
print(f"Left aligned:   '{text:<15}'")
print(f"Right aligned:  '{text:>15}'")
print(f"Center aligned: '{text:^15}'")
print(f"Padded with *:  '{text:*^15}'")

# Advanced string operations with list comprehension
paragraph = "Python is great. It's powerful and easy to learn."
sentences = [s.strip() for s in paragraph.split('.') if s]
print(f"Sentences: {sentences}")

# Character frequency analysis
def char_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

text = "Hello World"
freq = char_frequency(text)
print(f"Character frequency: {freq}")

# Palindrome checking with string manipulation
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?"]
for test in test_strings:
    print(f"'{test}' is palindrome: {is_palindrome(test)}")
```

## Output

```
Length: 13
First character: H
Last character: !
First 5 characters: Hello
From index 7 to end: World!
Uppercase: HELLO, WORLD!
Lowercase: hello, world!
Title case: Hello, World!
Position of 'World': 7
Replace 'World' with 'Python': Hello, Python!
Starts with 'Hello': True
Ends with '!': True
Contains 'World': True
Name: Alice, Age: 25, Score: 95.7
Name: Alice, Age: 25, Score: 95.7
Name: Alice, Age: 25, Score: 95.7
Words: ['Python', 'is', 'a', 'powerful', 'programming', 'language']
Hyphenated: Python-is-a-powerful-programming-language
Cleaned: 'Hello World!'
Found emails: ['support@example.com', 'admin@test.org']
Translated: H2ll4 W4rld
Original: Hello, 世界
UTF-8 encoded: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
UTF-8 decoded: Hello, 世界
Tab:	Separated
Newline:
Second line
Backslash:\
Quote: "Hello"
Unicode: ❤
Hello Alice, you have 5 messages.
Hello Bob, you have $count messages.
Left aligned:   'Centered       '
Right aligned:  '       Centered'
Center aligned: '   Centered   '
Padded with *:  '***Centered***'
Sentences: ['Python is great', "It's powerful and easy to learn"]
Character frequency: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
'A man, a plan, a canal: Panama' is palindrome: True
'race a car' is palindrome: False
'Was it a car or a cat I saw?' is palindrome: True
```

## Common Mistakes

1. **Trying to modify strings in place**:
   ```python
   # Wrong
   text = "Hello"
   text[0] = "h"  # TypeError: 'str' object does not support item assignment

   # Correct
   text = "h" + text[1:]
   ```

2. **Incorrect string comparison**:
   ```python
   # Wrong
   name = "Alice"
   if name == "alice":  # Case sensitive
       print("Found")

   # Correct
   if name.lower() == "alice":
       print("Found")
   ```

3. **Forgetting that string methods return new strings**:
   ```python
   # Wrong
   text = "Hello World"
   text.upper()  # This does nothing
   print(text)  # Still "Hello World"

   # Correct
   text = "Hello World"
   text = text.upper()
   print(text)  # "HELLO WORLD"
   ```

4. **Using wrong quote types**:
   ```python
   # Wrong
   text = "He said "Hello""  # SyntaxError

   # Correct
   text = "He said \"Hello\""
   # or
   text = 'He said "Hello"'
   ```

5. **Index out of range errors**:
   ```python
   # Wrong
   text = "Hello"
   print(text[10])  # IndexError

   # Correct
   text = "Hello"
   if len(text) > 10:
       print(text[10])
   ```

## Best Practices

1. **Use f-strings for formatting** (Python 3.6+):
   ```python
   name = "Alice"
   age = 30
   # Good
   message = f"Hello {name}, you are {age} years old"
   ```

2. **Use join() for combining many strings**:
   ```python
   # Good
   words = ["Python", "is", "great"]
   sentence = " ".join(words)

   # Avoid
   sentence = ""
   for word in words:
       sentence += word + " "
   ```

3. **Use startswith() and endswith() instead of slicing**:
   ```python
   # Good
   if filename.endswith(".txt"):
       process_file(filename)

   # Avoid
   if filename[-4:] == ".txt":
       process_file(filename)
   ```

4. **Strip whitespace when processing user input**:
   ```python
   user_input = input("Enter your name: ").strip()
   ```

5. **Use raw strings for regex patterns**:
   ```python
   # Good
   import re
   pattern = r"\d{3}-\d{3}-\d{4}"

   # Avoid
   pattern = "\\d{3}-\\d{3}-\\d{4}"
   ```

6. **Precompile regex patterns for repeated use**:
   ```python
   import re
   pattern = re.compile(r"\b\w+@\w+\.\w+\b")
   emails = pattern.findall(text)
   ```

## Pro Tips

1. **Use string methods chaining**:
   ```python
   text = "  Hello World!  "
   clean_text = text.strip().lower().replace(" ", "_")
   print(clean_text)  # "hello_world!"
   ```

2. **Leverage the power of str.translate()**:
   ```python
   # Fast character replacement
   text = "Hello World"
   translation = str.maketrans("aeiou", "12345")
   result = text.translate(translation)
   print(result)  # "H2ll4 W4rld"
   ```

3. **Use enumerate() with strings for indexed processing**:
   ```python
   text = "Python"
   for i, char in enumerate(text):
       print(f"Character {i}: {char}")
   ```

4. **Utilize string constants from the string module**:
   ```python
   import string
   print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
   print(string.digits)         # 0123456789
   print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
   ```

5. **Use string multiplication for patterns**:
   ```python
   separator = "-" * 50
   header = "REPORT".center(50)
   print(separator)
   print(header)
   print(separator)
   ```

## Interview Questions (10)

1. **What is the difference between string concatenation using + and using join()?**

2. **Explain the difference between str() and repr() functions.**

3. **How do you reverse a string in Python? Provide multiple approaches.**

4. **What is string interning in Python and how does it work?**

5. **Explain the difference between shallow copy and deep copy of strings.**

6. **How do you check if a string contains only alphanumeric characters?**

7. **What are f-strings and what advantages do they have over other formatting methods?**

8. **How do you handle Unicode and encoding issues in strings?**

9. **Explain the difference between strip(), lstrip(), and rstrip() methods.**

10. **How would you implement a function to check if two strings are anagrams?**

## MCQs (10)

1. **What is the output of `"python".capitalize()`?**
   a) "PYTHON"
   b) "Python"
   c) "python"
   d) "pYTHON"

2. **Which method removes whitespace from both ends of a string?**
   a) trim()
   b) strip()
   c) clean()
   d) remove()

3. **What does `"hello world".split()` return?**
   a) ["hello", "world"]
   b) "hello,world"
   c) ["hello world"]
   d) "hello world"

4. **How do you check if a string starts with "Hello"?**
   a) str.startswith("Hello")
   b) str.beginswith("Hello")
   c) str.find("Hello") == 0
   d) Both a and c

5. **What is the result of `"abc" * 3`?**
   a) "abc3"
   b) "abcabcabc"
   c) "9abc"
   d) Error

6. **Which of these is a mutable string operation?**
   a) replace()
   b) upper()
   c) None of these
   d) All of these

7. **What does `"\u2603"` represent?**
   a) A regular string
   b) A Unicode snowman character
   c) An escape sequence
   d) A syntax error

8. **How do you access the last character of a string `s`?**
   a) s[len(s)]
   b) s[-1]
   c) s[len(s)-1]
   d) Both b and c

9. **What is the output of `"Python"[1:4]`?**
   a) "Python"
   b) "ytho"
   c) "Pyt"
   d) "yth"

10. **Which method is used to find a substring in a string?**
    a) search()
    b) find()
    c) locate()
    d) index()

## Practice Questions (10)

1. **Write a function that counts the frequency of each character in a string.**

2. **Create a program that checks if a string is a palindrome (ignoring spaces and punctuation).**

3. **Implement a function that removes all vowels from a given string.**

4. **Write a program that capitalizes the first letter of each word in a sentence.**

5. **Create a function that generates a random password with specified length and character types.**

6. **Implement string compression (e.g., "aaabbcccc" becomes "a3b2c4").**

7. **Write a function that finds all anagrams of a given word from a list of words.**

8. **Create a program that validates if a string is a valid email address.**

9. **Implement a function that converts a string to title case while preserving acronyms.**

10. **Write a program that finds the longest substring without repeating characters.**

## Coding Exercises (5)

1. **String Validator**: Create a function that validates passwords based on criteria (length, special characters, numbers, etc.).

2. **Text Analyzer**: Build a program that analyzes text files for word count, sentence count, average word length, and most common words.

3. **String Encoder/Decoder**: Implement a simple Caesar cipher that shifts characters by a specified number of positions.

4. **URL Parser**: Create a function that parses URLs and extracts components (protocol, domain, path, query parameters).

5. **CSV Processor**: Write a program that processes CSV data represented as strings, handling quoted fields and escaped characters.

## Mini Project

**Text-based Adventure Game Engine**

Create a text-based adventure game engine that processes user input and generates game responses using string manipulation:

```python
class AdventureGame:
    def __init__(self):
        self.rooms = {
            "start": {
                "description": "You are in a dark forest. Paths lead north and east.",
                "exits": {"north": "cave", "east": "river"}
            },
            "cave": {
                "description": "You are in a damp cave. There's a treasure chest here.",
                "exits": {"south": "start"}
            },
            "river": {
                "description": "You are by a rushing river. A bridge leads north.",
                "exits": {"west": "start", "north": "bridge"}
            },
            "bridge": {
                "description": "You are on a rickety bridge. It looks unstable.",
                "exits": {"south": "river", "north": "castle"}
            },
            "castle": {
                "description": "You've reached the castle! You win!",
                "exits": {}
            }
        }
        self.current_room = "start"
        self.inventory = []

    def process_command(self, command):
        command = command.lower().strip()

        if command in ["quit", "exit"]:
            return "Thanks for playing!"

        if command in ["look", "describe"]:
            return self.rooms[self.current_room]["description"]

        if command.startswith("go "):
            direction = command[3:].strip()
            return self.move(direction)

        if command == "inventory":
            return f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}"

        if command.startswith("take "):
            item = command[5:].strip()
            return self.take_item(item)

        return "I don't understand that command. Try: look, go [direction], take [item], inventory, quit"

    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room["exits"]:
            self.current_room = room["exits"][direction]
            return f"{self.rooms[self.current_room]['description']}"
        return "You can't go that way."

    def take_item(self, item):
        # Simplified item system
        if item not in self.inventory:
            self.inventory.append(item)
            return f"You take the {item}."
        return f"You already have the {item}."

# Usage example
game = AdventureGame()
print(game.process_command("look"))
print(game.process_command("go north"))
print(game.process_command("look"))
```

## Assignment

**Create a String Processing Library**

Develop a comprehensive string processing library with the following features:

1. **Text Formatting Module**: Functions for capitalization, case conversion, and formatting
2. **Text Analysis Module**: Character frequency, word counting, readability analysis
3. **Text Transformation Module**: Encoding, encryption, compression utilities
4. **Text Validation Module**: Email, phone number, and URL validators
5. **Text Generation Module**: Password generators, Lorem Ipsum, pattern-based text generators

Your library should include:
- Comprehensive docstrings for all functions
- Error handling for edge cases
- Unit tests for each function
- Performance considerations for large texts
- Support for Unicode and international characters
- Integration with regular expressions for complex patterns

Documentation should include usage examples and performance benchmarks.

## Summary

In this lesson, we explored Python strings comprehensively:

- **Basics**: String creation, immutability, and fundamental operations
- **Intermediate**: Advanced formatting, regular expressions, and string methods
- **Advanced**: Encoding, Unicode handling, and complex string algorithms
- **Best Practices**: Efficient string manipulation techniques and common pitfalls
- **Applications**: Real-world examples and interview preparation

Strings are fundamental to programming, and mastering them enables you to build robust applications that process text data effectively. From simple concatenation to complex text analysis, the skills you've learned here form the foundation for many programming tasks.

## Key Takeaways

1. **Strings are immutable**: All string operations create new objects
2. **F-strings are preferred**: Modern, efficient string formatting (Python 3.6+)
3. **Use join() for multiple concatenations**: More efficient than += in loops
4. **Regular expressions are powerful**: Essential for complex string pattern matching
5. **Unicode support is built-in**: Python 3 handles international characters seamlessly
6. **String methods are chainable**: Combine operations for complex transformations
7. **Performance matters**: Choose appropriate methods for your use case
8. **Error handling is crucial**: Always validate string operations to avoid runtime errors

## Next Topic Preview

In the next lesson, we'll dive into **Lists and Tuples** - Python's sequence data types that allow you to store collections of items. You'll learn about list operations, list comprehensions, tuple immutability, and how to choose between these data structures for different scenarios.
