# ============================================================
# WALRUS OPERATOR (:=)
# ============================================================

"""
The walrus operator is also called the assignment expression
operator.

It assigns a value to a variable while allowing the assignment
to be part of an expression.
"""


# ------------------------------------------------------------
# Example 1: Without Walrus Operator
# ------------------------------------------------------------

numbers = [10, 20, 30, 40]

length = len(numbers)

if length > 3:
    print(length)  # Output: 4


# ------------------------------------------------------------
# Example 2: With Walrus Operator
# ------------------------------------------------------------

numbers = [10, 20, 30, 40]

if (length := len(numbers)) > 3:
    print(length)  # Output: 4


# ------------------------------------------------------------
# Explanation
# ------------------------------------------------------------

"""
1. len(numbers) calculates the length of the list, which is 4.

2. := assigns the calculated value 4 to the variable length.

3. Python checks whether length > 3.

4. Since the condition is True, Python prints 4.

Note:
Parentheses are used here to make the assignment expression's
grouping explicit.
"""


# ------------------------------------------------------------
# Example 3: Using the Walrus Operator with input()
# ------------------------------------------------------------

# Read input and store it in the variable while checking it.

if (name := input("Enter your name: ")):
    print("Hello,", name)
else:
    print("Name cannot be empty")

# Explanation:
# 1. input() reads the user's name.
# 2. := assigns the entered value to the variable name.
# 3. Python checks whether name is non-empty.
# 4. If name is non-empty, the if block executes.
# 5. If name is empty, the else block executes.


# ------------------------------------------------------------
# Remember
# ------------------------------------------------------------

# =   : Assignment statement
# :=  : Assignment expression

# The walrus operator was introduced in Python 3.8.