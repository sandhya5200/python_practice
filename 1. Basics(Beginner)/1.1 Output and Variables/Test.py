# 1. Print "Hello, World!" to the screen.
print('Hello, World!')

# 2. Print your name and age on two separate lines using one print() call.
print("sandhya \n23")

# 3. Print the numbers 1 to 5 on one line separated by dashes using the sep argument.
print("1","2","3","4","5", sep="-")
print("java","python","c", sep="|")

# 4. Print three words on one line without a newline between separate print() calls using end.
print("i am sandhya", end =" ")
print("sandhya", end = " ")
print("ok")

# 5. Create a variable for your city and print it.
city = "Hyderabad"
print(city)

# 6. Swap the values of two variables a and b without using a third variable.
a = 2
b = 3

c = a
a = b
b = c

print(a,b)

# 7. Assign the same value 10 to three variables in a single statement.
a = b = c = 10
print(a,b,c)

# 8. Assign three different values to three variables in one line.
(l,m,n) = (100,200,300)
print(l,m,n)

# 9. Print the type of the values 5, 5.0, "5", True and None.
x = 5
y = 5.0
z = "5"

print(type(x))
print(type(y))
print(type(z))
print(type(True))
print(type(None))

# 10. Use an f-string to print "My name is X and I am Y years old".
name = "sandhya"
age = 25
print(f"\"My name is {name} and I am {age} years old\"")

# 11. Use str.format() to print the same sentence as the previous question.
print("My name is {} and I am {} years old".format(name,age))

# 12. Use the % operator to format a float to 2 decimal places.
print("My name is %s and I am %d years old" % (name,age))
price = 123.4567
print("The price is %.2f" % price)

# 13. Print a tab-separated table of three rows and two columns using escape characters.
print("A|\tB|\nC|\tD|\nE|\tF|")

# 14. Print a string that contains both single and double quotes.
print("\'sandhya\'")
print("\"sandhya\"")

# 15. Print a multi-line message using triple quotes.
print("""sandhya
is
very
good
girl""")

# 16. Print a backslash and a Windows file path correctly using raw strings.
print(r"C:\Users\Sandhya\Documents\file.txt")

# 17. Check which of these are valid variable names: 2name, _name, my-name, myName, class.
# 2name = "sandhya"   #invalid because no start with integr
_name = "1sandhya"   # Valid - A variable name can start with an underscore.
# my-name = "sandhya" # InValid because no other special symbol is allowed other than _
myName = "2sandhya"  # Valid
# class = "sandhya"   # InValid because no keywords
print(_name,myName)

# 18. Write a program that prints the id() of a variable before and after reassigning it.
var1 = 100
print("before assigning",id(var1))
var1 = 200
print("after assigning",id(var1))

# 19. Use the keyword module to print the list of all Python keywords.
import keyword
print(keyword.kwlist)

# 20. Add single-line and multi-line comments to explain a small program.

#This is the single line comment

'''This
is
multi
line
comment'''

def add_two_num(a,b):
    """this is docstring """
    return(a+b)

print(add_two_num(2,3))
print(add_two_num.__doc__)