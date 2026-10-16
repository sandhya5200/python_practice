# ============================================================
# OPERATOR PRECEDENCE AND PARENTHESES
# ============================================================

# Operator precedence determines which operation Python performs
# first when an expression contains multiple operators.


# ------------------------------------------------------------
# Example 1: Without Parentheses
# ------------------------------------------------------------

result = 10 + 5 * 2
print(result)  # Output: 20

# Explanation:
# 10 + 5 * 2
# 10 + 10
# 20
#
# Multiplication (*) is performed before addition (+).


# ------------------------------------------------------------
# Example 2: With Parentheses
# ------------------------------------------------------------

result = (10 + 5) * 2
print(result)  # Output: 30

# Explanation:
# (10 + 5) * 2
# 15 * 2
# 30
#
# Parentheses force the expression inside them to be
# evaluated first.


# ------------------------------------------------------------
# Operator Precedence Order
# ------------------------------------------------------------

# The following table lists common operators from higher
# to lower precedence.
#
# Priority    Operators           Meaning
# ------------------------------------------------------------
# 1           ()                  Grouping expressions
# 2           **                  Exponentiation
# 3           +x, -x, ~x          Unary operators
# 4           *, /, //, %         Multiplication, division,
#                                 and remainder
# 5           +, -                Addition and subtraction
# 6           <<, >>              Bitwise shifts
# 7           &                   Bitwise AND
# 8           ^                   Bitwise XOR
# 9           |                   Bitwise OR
# 10          <, >, ==, !=,       Comparisons
#             is, in
# 11          not                 Logical NOT
# 12          and                 Logical AND
# 13          or                  Logical OR
# 14          :=                  Assignment expression
#
# Note:
# Assignment statements such as x = 10 are not ordinary
# expressions in this precedence table.


# ------------------------------------------------------------
# Associativity
# ------------------------------------------------------------

# When operators have the same precedence, associativity
# usually determines the evaluation order.


# Example 1: Most arithmetic operators evaluate left to right.

print(20 - 5 - 3)  # Output: 12

# Explanation:
# (20 - 5) - 3
# 15 - 3
# 12


# Example 2: Exponentiation evaluates right to left.

print(2 ** 3 ** 2)  # Output: 512

# Explanation:
# 2 ** (3 ** 2)
# 2 ** 9
# 512


# ------------------------------------------------------------
# Remember
# ------------------------------------------------------------

# Use parentheses when you want to make an expression easier
# to read or explicitly control the order of evaluation.