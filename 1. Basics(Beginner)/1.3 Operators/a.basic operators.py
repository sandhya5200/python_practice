"""
PYTHON OPERATORS — COMPLETE NOTES

Operators:
    Special symbols used to perform operations on values and variables.
    Examples: +, -, *, /, etc.

Operands:
    The values on which operators are applied.
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
# Arithmetic operators perform basic mathematical operations
# such as addition, subtraction, multiplication, and division.

a = 15
b = 4

print("\n--- Arithmetic Operators ---")

print("Addition:", a + b)                  # Output: 19
print("Subtraction:", a - b)               # Output: 11
print("Multiplication:", a * b)             # Output: 60
print("Division:", a / b)                  # Output: 3.75
print("Floor Division:", a // b)            # Output: 3
print("Modulus:", a % b)                    # Output: 3
print("Exponentiation:", a ** b)            # Output: 50625

# /  : Returns a floating-point result.
# // : Returns the floor of the division result.
# %  : Returns the remainder.
# ** : Raises the first number to the power of the second number.


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================
# Comparison (relational) operators compare two values.
# They return either True or False.

a = 13
b = 33

print("\n--- Comparison Operators ---")

print("Greater than:", a > b)               # Output: False
print("Less than:", a < b)                  # Output: True
print("Equal to:", a == b)                  # Output: False
print("Not equal to:", a != b)              # Output: True
print("Greater than or equal to:", a >= b)  # Output: False
print("Less than or equal to:", a <= b)     # Output: True


# ------------------------------------------------------------
# Chained Comparison
# ------------------------------------------------------------
# Python allows multiple comparisons in a single expression.
# Example: Checking whether a number lies between two values.

x = 15

print("\n--- Chained Comparison ---")

# Check whether x is between 10 and 20.
print("10 < x < 20:", 10 < x < 20)           # Output: True

# Check whether x is between 10 and 15, inclusive.
print("10 <= x <= 15:", 10 <= x <= 15)       # Output: True

# Combine different comparison operators.
print("20 < x != 20:", 20 < x != 20)         # Output: False


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================
"""
Logical operators combine multiple conditions or reverse
a condition.

1. and:
   Returns True only when both conditions are True.

   Condition 1    Condition 2    Result
   -------------------------------------
   True           True           True
   True           False          False
   False          True           False
   False          False          False

2. or:
   Returns True when at least one condition is True.

   Condition 1    Condition 2    Result
   -------------------------------------
   True           True           True
   True           False          True
   False          True           True
   False          False          False

3. not:
   Reverses the Boolean value.

   not True  -> False
   not False -> True

   Condition    Result
   -------------------
   True         False
   False        True
"""

a = True
b = False

print("\n--- Logical Operators ---")

print("AND:", a and b)                      # Output: False
print("OR:", a or b)                        # Output: True
print("NOT:", not a)                        # Output: False


# ------------------------------------------------------------
# Short-Circuit Evaluation
# ------------------------------------------------------------
# Python stops evaluating a logical expression when its result
# is already determined.

print("\n--- Short-Circuit Evaluation ---")

print(False and 10 / 0)                     # Output: False
print(True or 10 / 0)                       # Output: True

# The expression 10 / 0 is not evaluated in either example.


# ============================================================
# 4. BITWISE OPERATORS
# ============================================================
"""
Bitwise operators perform operations on individual bits (0s and 1s).

The six commonly used bitwise operators are:
    &   Bitwise AND
    |   Bitwise OR
    ^   Bitwise XOR
    ~   Bitwise NOT
    <<  Left shift
    >>  Right shift
"""


# ------------------------------------------------------------
# Binary Representation
# ------------------------------------------------------------
# bin() converts an integer into its binary representation.
# The prefix 0b indicates a binary number.

a = 5

print("\n--- Binary Representation ---")
print("Binary of 5:", bin(a))                # Output: 0b101


# ------------------------------------------------------------
# 4.1 Bitwise AND (&)
# ------------------------------------------------------------
# Returns 1 when both corresponding bits are 1.
# Otherwise, returns 0.

a = 5                                      # Binary: 101
b = 3                                      # Binary: 011

print("\n--- Bitwise AND ---")
print("5 & 3:", a & b)                     # Output: 1

#     101
#   & 011
#   -----
#     001  -> 1


# ------------------------------------------------------------
# 4.2 Bitwise OR (|)
# ------------------------------------------------------------
# Returns 1 when at least one corresponding bit is 1.

a = 5                                      # Binary: 101
b = 3                                      # Binary: 011

print("\n--- Bitwise OR ---")
print("5 | 3:", a | b)                     # Output: 7

#     101
#   | 011
#   -----
#     111  -> 7


# ------------------------------------------------------------
# 4.3 Bitwise XOR (^)
# ------------------------------------------------------------
# Returns 1 when corresponding bits are different.
# Returns 0 when corresponding bits are the same.

a = 5                                      # Binary: 101
b = 3                                      # Binary: 011

print("\n--- Bitwise XOR ---")
print("5 ^ 3:", a ^ b)                     # Output: 6

#     101
#   ^ 011
#   -----
#     110  -> 6


# ------------------------------------------------------------
# 4.4 Bitwise NOT (~)
# ------------------------------------------------------------
# Inverts the bits of an integer.
# In Python: ~x == -(x + 1)

a = 5

print("\n--- Bitwise NOT ---")
print("~5:", ~a)                           # Output: -6

# Explanation:
# ~5 = -(5 + 1) = -6


# ------------------------------------------------------------
# 4.5 Left Shift (<<)
# ------------------------------------------------------------
"""
Left shift moves the bits to the left.

For non-negative integers, shifting left by n positions
is equivalent to multiplying by 2 ** n.

Example:
    3 in binary = 11

    3 << 1:
        11  ->  110  -> 6

    3 << 2:
        11  -> 1100  -> 12

Rule:
    a << n = a * (2 ** n)
"""

a = 3

print("\n--- Left Shift ---")
print("3 << 1:", a << 1)                   # Output: 6
print("3 << 2:", a << 2)                   # Output: 12


# ------------------------------------------------------------
# 4.6 Right Shift (>>)
# ------------------------------------------------------------
"""
Right shift moves the bits to the right.

For non-negative integers, shifting right by n positions
is equivalent to floor-dividing by 2 ** n.

Example:
    12 in binary = 1100

    12 >> 1:
        1100  ->  0110  -> 6

    12 >> 2:
        1100  ->  0011  -> 3

Rule:
    a >> n = a // (2 ** n)
"""

a = 12

print("\n--- Right Shift ---")
print("12 >> 1:", a >> 1)                  # Output: 6
print("12 >> 2:", a >> 2)                  # Output: 3


# ============================================================
# 5. ASSIGNMENT OPERATORS
# ============================================================
# Assignment operators assign values to variables.
#
# =   Simple assignment
# +=  Addition assignment
# -=  Subtraction assignment
# *=  Multiplication assignment
# /=  Division assignment
# //= Floor division assignment
# %=  Modulus assignment
# **= Exponentiation assignment
#
# Bitwise augmented assignment operators:
# &=, |=, ^=, <<=, >>=


# ------------------------------------------------------------
# 5.1 Simple Assignment (=)
# ------------------------------------------------------------
# The = operator assigns a value to a variable.

x = 10

print("\n--- Simple Assignment ---")
print("x:", x)                             # Output: 10


# ------------------------------------------------------------
# 5.2 Difference Between =+ and +=
# ------------------------------------------------------------
# =+ is not an augmented assignment operator.
# x =+ 10 means x = (+10), assigning positive 10 to x.
#
# x += 10 means adding 10 to the existing value of x.

x = 10
x += 10

y = 5
y =+ 10

print("\n--- =+ vs += ---")
print("x after x += 10:", x)               # Output: 20
print("y after y =+ 10:", y)               # Output: 10


# ------------------------------------------------------------
# 5.3 Addition Assignment (+=)
# ------------------------------------------------------------

x = 10
x += 5

print("\n--- Addition Assignment ---")
print("x += 5:", x)                        # Output: 15


# ------------------------------------------------------------
# 5.4 Subtraction Assignment (-=)
# ------------------------------------------------------------

x = 10
x -= 3

print("\n--- Subtraction Assignment ---")
print("x -= 3:", x)                        # Output: 7


# ------------------------------------------------------------
# 5.5 Multiplication Assignment (*=)
# ------------------------------------------------------------

x = 10
x *= 2

print("\n--- Multiplication Assignment ---")
print("x *= 2:", x)                        # Output: 20


# ------------------------------------------------------------
# 5.6 Division Assignment (/=)
# ------------------------------------------------------------

x = 10
x /= 2

print("\n--- Division Assignment ---")
print("x /= 2:", x)                        # Output: 5.0


# ------------------------------------------------------------
# 5.7 Floor Division Assignment (//=)
# ------------------------------------------------------------

x = 10
x //= 3

print("\n--- Floor Division Assignment ---")
print("x //= 3:", x)                       # Output: 3


# ------------------------------------------------------------
# 5.8 Modulus Assignment (%=)
# ------------------------------------------------------------

x = 10
x %= 3

print("\n--- Modulus Assignment ---")
print("x %= 3:", x)                        # Output: 1


# ------------------------------------------------------------
# 5.9 Exponentiation Assignment (**=)
# ------------------------------------------------------------

x = 10
x **= 2

print("\n--- Exponentiation Assignment ---")
print("x **= 2:", x)                       # Output: 100


# ------------------------------------------------------------
# Equality Operator (==)
# ------------------------------------------------------------
# == compares two values; it does not assign a value.

print("\n--- Equality Comparison ---")
print("100 == 10:", x == 10)               # Output: False
print("100 == 100:", x == 100)             # Output: True


# ============================================================
# 6. IDENTITY OPERATORS
# ============================================================
"""
Identity operators:
    is      Checks whether two references point to the same object.
    is not  Checks whether two references point to different objects.

Two variables with equal values are not necessarily identical.
"""

a = 10
b = 20
c = a

print("\n--- Identity Operators ---")

print("a is not b:", a is not b)           # Output: True
print("a is c:", a is c)                   # Output: True

# a and c refer to the same integer object.
# Use == to compare values and is to check object identity.
# For checking None, use: value is None


# ============================================================
# 7. MEMBERSHIP OPERATORS
# ============================================================
"""
Membership operators:
    in      Checks whether a value exists in a sequence.
    not in  Checks whether a value does not exist in a sequence.
"""

x = 24
y = 20

my_list = [10, 20, 30, 40, 50]

print("\n--- Membership Operators ---")

# Check whether x is absent from the list.
if x not in my_list:
    print("x is NOT present in the given list")
else:
    print("x is present in the given list")

# Check whether y exists in the list.
if y in my_list:
    print("y is present in the given list")
else:
    print("y is NOT present in the given list")
