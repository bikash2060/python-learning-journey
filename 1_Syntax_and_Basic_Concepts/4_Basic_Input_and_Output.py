# Basic Input and Output in Python
"""
    - Input and Output are essential parts of any programming language.
    - In Python, we use the `input()` function to take input from the user and the `print()` function to display output to the console.
"""

# Taking Input from the User
# The input() function reads a line from input, converts it into a string, and returns it.
name = input("Please enter your name: ") # Prompting the user to enter their name. And by default, input() takes input as a string.
print("hello, " + name + "!. Welcome to Python programming.") # Displaying a greeting message with the user's name.

# Taking Numeric Input
age = int(input("Please enter your age: ")) # Converting the input string to an integer using int()
print("You are",age,"years old.") # Displaying the user's age. Using commas in print() automatically adds spaces between items. So no need to manually add spaces.
# Note: If the user enters a non-numeric value when prompted for age, it will raise a ValueError.