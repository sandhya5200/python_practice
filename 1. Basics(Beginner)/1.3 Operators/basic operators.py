'''Operators in general are used to perform operations on values and variables.

# - Operators: Special symbols like -, + , * , /, etc.
# - Operands: Value on which the operator is applied.'''

# Arithmetic Operators
# Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

a = 15
b = 4
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b)  # Returns a floating-point result
print("Floor Division:", a // b)  # Returns an integer result, Just trims the decimal part not round off's
print("Modulus:", a % b) # Returns the remainder
print("Exponentiation:", a ** b) 

# Comparison Operators
# Comparison(or Relational) operators compares values. It either returns True or False according to the condition.

a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Logical Operators
'''Logical operators are used to combine multiple conditions or reverse a condition. 

and Operator - Returns `True` only when both conditions are True.

| Condition 1 | Condition 2 | Result |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | False  |
| False       | True        | False  |
| False       | False       | False  |

or Operator - Returns True when at least one condition is True.

| Condition 1 | Condition 2 | Result |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | True   |
| False       | True        | True   |
| False       | False       | False  |

not Operator - Reverses the Boolean value of a condition.
- not True → False
- not False → True

| Condition | Result |
| --------- | ------ |
| True      | False  |
| False     | True   |

What is short-circuit evaluation?

Python stops evaluating a logical expression when the result is already determined.
print(False and 10 / 0)  # False'''

a = True
b = False
print(a and b)  # False 
print(a or b)   # True
print(not a)    # False 

# Bitwise Operators
'''Bitwise operators perform operations on the individual bits (0s and 1s) of integer values.
Python has 6 commonly used bitwise operators: &, |, ^, ~, <<, and >>.

Binary Representation
a = 5
print(bin(a)) # Output: 0b101 (8421)'''

# 1. Bitwise AND (&)
# Returns 1 if both corresponding bits are 1; otherwise, returns 0.

a = 5       # Binary: 101
b = 3       # Binary: 011

print(a & b)  # Output: 001 that means 1

# 2. Bitwise OR (|)
# Returns 1 if at least one corresponding bit is 1.

a = 5       # Binary: 101
b = 3       # Binary: 011

print(a | b)  # Output: 111 that means 7

# 3. Bitwise XOR (^)
# Returns 1 if the corresponding bits are different; otherwise, returns 0.

a = 5       # Binary: 101
b = 3       # Binary: 011

print(a ^ b)  # Output: 110 that means 6

# 4. Bitwise NOT (~)
# Inverts the bits of an integer. In Python, the result follows the rule ~x == -(x + 1).

a = 5
print(~a)  # Output: -6

# 5. Left shift (<<)
• Shifts the bits of a binary number to the left.
• As a consequence, it multiplies the number by (2^n), where n is the magnitude of the shift.

a = 3
a in binary is: 
011
Left shift by 1:
a << 1 = 0110 = 6
Left shift by 2:
a << 2 = 01100 = 12
Rule:
a << n = a * (2 ** n)



'''