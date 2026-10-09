'''Data types in Python define the type of value stored in a variable.
1. Numeric Data Types
    Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
    a = 5
    Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
    b = 5.0
    Complex: It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2+3j
    c = 2=3j
2. Sequence Data Types
    Strings are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes.
    s = 'Welcome to the Geeks World'
    Lists are ordered and mutable collections used to store multiple items in a single variable.
    b = ["Geeks", "For", "Geeks", 4, 5]
    Tuples are ordered and immutable collections used to store multiple items in a single variable. 
    t = ('Geeks', 'For', 'Geeks', 1, 2)
    Sets are unordered and mutable collections used to store unique elements.
    s = {"a", "a", "b", "c", "b"}
    Dictionaries are used to store data in key:value pairs. Each key in a dictionary must be unique 
    and values are accessed using their keys with square brackets [] or get() method.
    d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
3. Boolean Data Type
    Boolean data type represents one of two values: True or False.
    None itself is not a data type; it is a special constant value. '''


##############################################################################################################################
'''TYPE CASTING

Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.
There can be two types of Type Casting in Python:

Implicit Type Conversion

Implicit type conversion is the automatic changing of a data value from one type to another by the compiler
or runtime environment without any manual intervention from the programmer'''

a = 5
print(type(a))

'''Explicit Type Conversion
Explicit type conversion is when the programmer manually changes a value’s data type using built-in type casting functions,
usually when automatic conversion is not possible or a specific type is needed.'''
a = 5
n = float(a)

print(type(a))
print(type(n))

##############################################################################################################################

# Number System Conversion

# bin() — Converts an integer to binary.
print(bin(5))       # Output: 0b101

# oct() — Converts an integer to octal.
print(oct(5))       # Output: 0o5

# hex() — Converts an integer to hexadecimal.
print(hex(5))       # Output: 0x5

# int(x, base) — Converts a string representing a number in a specified base to an integer.
print(int("1010", 2))  # 2 means binary
print(int("12", 8))   # 8 means octal 
print(int("A", 16))   # 16 means hexadecimal

##############################################################################################################################

# Floating-Point Precision, round() and Decimal Module

# Floating-point precision — Floating-point numbers may produce unexpected results.
print(0.1 + 0.2)                 # Output: 0.30000000000000004

# Floating-point comparison — Direct comparisons may fail due to precision issues.
print(0.1 + 0.2 == 0.3)          # Output: False

# round() — Rounds a number to the specified number of decimal places.
print(round(3.14159, 2))         # Output: 3.14

# round() — Rounds a number to the nearest integer when no precision is specified.
print(round(4.7))                # Output: 5

# round() — Python uses round-half-to-even for exact halfway cases.
print(round(2.5))                # Output: 2
print(round(3.5))                # Output: 4

# Decimal module — Provides decimal arithmetic with better control over precision.
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  # Output: 0.3

# Decimal multiplication — Useful for accurate decimal calculations.
print(Decimal("1.25") * Decimal("4"))   # Output: 5.00

