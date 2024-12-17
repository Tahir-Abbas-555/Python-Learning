# Day 1: Python Basics
# Goal: Understand Python syntax, variables, and basic input/output.

# 1. Print Statement
print("Hello, World!")  # The classic first program

# 2. Comments in Python
# Single-line comments start with a hash symbol
"""
Multi-line comments (or docstrings) can be enclosed
in triple quotes (single or double).
"""

# 3. Variables and Data Types
name = "Tahir"      # String
age = 25            # Integer
height = 5.9        # Float
is_learning = True  # Boolean

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Learning:", is_learning)

# 4. Taking User Input
user_name = input("Enter your name: ")
print("Hello,", user_name)

# 5. Simple Arithmetic Operations
a = 10
b = 5
sum_result = a + b
print("Sum of a and b is:", sum_result)

diff_result = a - b
print("Difference of a and b is:", diff_result)

product_result = a * b
print("Product of a and b is:", product_result)

quotient_result = a / b  # Division (returns float)
print("Quotient of a and b is:", quotient_result)

floor_div_result = a // b  # Floor division (integer result)
print("Floor Division of a and b is:", floor_div_result)

modulus_result = a % b  # Remainder
print("Remainder when a is divided by b:", modulus_result)

# 6. Combining Strings
first_name = "Tahir"
last_name = "Abbas"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
