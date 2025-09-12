# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
# 🐣 Beginner Level
# Problem 1: Hello, You!

# Topic: Input, print, variables
# Task:
# Write a program that asks the user for their name and prints a greeting.
def greeting():
     name = input("What is your name?")
     print("Hey! Nice to meet you, " + name + ".")
# Problem 2: Even or Odd?

# Topic: Conditionals, modulo
# Task:
# Ask the user to enter a number. Print whether the number is even or odd.
def number():
    check = int(input("Enter a number:"))
    if check % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
# 🧠 Moderate Level
# Problem 3: Count to Ten

# Topic: Loops
# Task:
# Write a loop that prints the numbers 1 to 10, each on a new line.
# (Bonus: Try it with both a for loop and a while loop.)
def count():
    i = 1
    while i <= 10:
        print(i)
        i += 1

# Problem 4: Sum of Numbers

# Topic: Loops, input, type conversion
# Task:
# Ask the user how many numbers they want to add. Then let them enter that many numbers one by one. Print the total sum.
def sum():
    l = 0
    n = int(input("How many numbers do you want to add?"))
    for i in range(n):
        ask = int(input("What number?"))
        l += ask
    print("Total: " + str(l))
# Problem 5: Multiplication Table Generator

# Topic: Loops, input, formatting
# Task:
# Ask the user to enter a number. Print its multiplication table from 1 to 10.
def table():
    l = 1
    n = int(input("Enter a number"))
    while l <= 10:
        print(n*l)
        l+=1

# 🧩 Challenging Level
# Problem 6: FizzBuzz

# Topic: Loops, conditionals
# Task:
# Print numbers from 1 to 50. But for multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# Problem 7: Find the Largest Number

# Topic: Lists, loops, conditionals
# Task:
# Ask the user to enter 5 numbers. Store them in a list. Then find and print the largest number.










# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""
greeting()
number()
count()
sum()
table()
print("All functions work!")
# print("Testing Problem 1:")
#  Add your tests here

# print("\nTesting Problem 2:")
# Add your tests here

# print("\nTesting Problem 3:")
# Add your tests here

# print("\nTesting Problem 4:")
# Add your tests here

# print("\nTesting Problem 5:")
# Add your tests here


