# Keywords in Python
"""
    - Keywords are reserved words in Python that have special meaning and purpose.add()
    - They are part of the syntax and structure of the language and cannot be used as variable names, function names, or identifiers.
    - Python has a set of predefined keywords that are used to define the structure and flow of a program.
    - The following is a list of some commonly used Python keywords:
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield
"""

# Example of using keywords
def check_even_odd(number):  # 'def' and 'if' are keywords
    if number % 2 == 0:      # 'if' and 'else' are keywords
        return True          # 'return' is a keyword
    else:
        return False        # 'else' and 'return' are keywords
    
print(check_even_odd(10))  # Output: True

# Invalid use of keywords
# The following line would raise a SyntaxError because 'if' is a keyword and cannot be used as a variable name.
#if = 5 # This will cause a SyntaxError

# Identifiers in Python
"""
    - Identifiers are names used to identify variables, functions, classes, modules, and other objects in Python.
    - They are user-defined names that follow certain rules and conventions.
"""

# Rules for Naming Identifiers
"""
    1. An identifier can consist of letters (a-z, A-Z), digits (0-9), and underscores (_).
    2. An identifier must start with a letter or an underscore, not a digit.
    3. Identifiers are case-sensitive (e.g., 'myVar' and 'myvar' are different).
    4. Identifiers cannot be the same as Python keywords.
    5. There are no length restrictions on identifiers, but it's good practice to keep them reasonable.
"""

# Examples of Valid Identifiers
my_variable = 10
_variable_name = "Hello"
var123 = 25
MyVar = 50

print(my_variable)    # Output: 10
print(_variable_name) # Output: Hello   
print(var123)        # Output: 25
print(MyVar)         # Output: 50

# Examples of Invalid Identifiers
# 1_variable = 10    # Invalid: starts with a digit
# my-variable = 20   # Invalid: contains a hyphen 