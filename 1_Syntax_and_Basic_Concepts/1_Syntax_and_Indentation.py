# Syntax in Python
"""
    - Syntax is the set of rules that are followed or used to write a program.
    - Just like English has grammar rules, Python has syntax rules.
    - If you break the rules, Python will give a SyntaxError and the program will not run.
"""

# Example of correct syntax
print("Hello, World!")  # This line follows the syntax rules

# Example of incorrect syntax
print("Hello, World!")
# The above line is missing a closing parenthesis ) and will raise a SyntaxError

# Key Python Syntax Rules
"""
    1. Statements usually end at the end of a line (no semicolons needed).
    2. Keywords are case-sensitive and must be written in lowercase (e.g., 'if', 'else', 'while').
    3. Parentheses, brackets, and braces must be properly opened and closed.
    4. Strings must be enclosed in matching quotes (single or double).
"""

# Python Indentation
"""
    - Indentation in Python means the spaces at the beginning of a code line.
    - Python uses indentation to define blocks of code, instead of curly braces {} like other languages.
    - Proper indentation is crucial; incorrect indentation will lead to IndentationError.
    - Typically, an indentation level is 4 spaces.
"""

# Example of correct indentation
a = 10
b = 20
if a < b:
    print("a is less than b") # The statement inside the if block is indented. So the code runs without error.

# Example of incorrect indentation
a = 10
b = 20
#if a < b:
#print("a is less than b")  # This line is not indented properly and will raise an IndentationError