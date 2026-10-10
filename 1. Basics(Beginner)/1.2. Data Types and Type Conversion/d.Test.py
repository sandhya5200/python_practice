# 21. Convert the string "123" to an integer and add 7 to it.
x = "123"
y = int(x)
z = y + 7
print(z)
print(type(z))

# 22. Convert the integer 45 to a string and concatenate it with "years".
a = 45
b = str(a)
c = b + " years"
print(c)
print(type(c))

# 23. Convert the float 9.99 to an integer and explain what happens to the decimals.
m = 9.99  
n = int(m)        
print(n)      
print(type(n))  # Python simply truncates the decimal part, No Rounding off even thought its near

# 24. Convert the string "3.14" to a float.
var = float("3.14")
print(var)
print(type(var))

# 25. Convert the number 0 and the number 5 to booleans and print them.
number1 = 0
number2 = 5
print(bool(number1))
print(bool(number2))

# 26. Print the boolean value of "", " ", [], [0] and None.
print(bool(""))
print(bool(" "))
print(bool([]))
print(bool([0]))
print(bool(None))

# 27. Convert an integer to its binary, octal and hexadecimal string forms.
integer_x = 10
print(bin(integer_x))
print(oct(integer_x))
print(hex(integer_x))

# 28. Convert the binary string "1010" to a decimal integer.
r = "1010"
print(int(r,2))

# 29. Convert a character to its ASCII code and an ASCII code back to a character.
print(ord("%"))
print(chr(37))

# 30. Check the type of the result of 10 / 2 and 10 // 2.
print(10 / 2)   # returns float
print(10 // 2) # returns the floor division result

# 31. Demonstrate that int, float and str are immutable by trying to change a string character.
lt = [1,2,3]   # This is simple list whisch is basically mutable
lt[0] = 5
print(lt)

x = 10
# x[0] = 5  # TypeError: 'int' object does not support item assignment

y = 10.5
# y[0] = 5  # TypeError: 'float' object does not support item assignment

s = "Python"
# s[0] = "J"  # TypeError: 'str' object does not support item assignment
s = "J" + s[1:] # Reassigning a variable is allowed. Modifying an existing immutable object in place is not.
print(s)

# 32. Find the largest integer Python can handle by computing 2 ** 1000.
print(2 ** 1000)

# 33. Show floating point imprecision with 0.1 + 0.2 and fix the comparison using round().
p = 0.1 + 0.2
print(round(p))

# 34. Use the decimal module to add 0.1 and 0.2 exactly.
from decimal import Decimal
w = Decimal("0.1") + Decimal("0.2")
print(w)  # Output: 0.3

# 35. Create a complex number and print its real and imaginary parts.
c = 4 + 3j
print(c.imag)
print(c.real)