'''Variables are used to store data that can be referenced and manipulated during program execution. 
    A variable is essentially a name that is assigned to a value.

Unlike Java and many other languages, Python variables do not require explicit declaration of type.
Type of the variable is inferred based on the value assigned.

Rules for Naming Variables
To use variables correctly, the following naming rules should be followed:

1. Names can contain letters, digits and underscores (_).
2. The first character cannot be a digit.
3. Names are case-sensitive, so myVar and myvar are treated differently.
4. Keywords such as if, else and for cannot be used as variable names.

'''

# Assigning Values to Variables
# 1. Basic Assignment: Variables are assigned values using the = operator.
x = 5
# 2. Dynamic Typing: Python is dynamically typed, you do not need to explicitly declare a variable's data type before using it.
x = 10
x = "Now a string"
# 3. Assigning Same Value: Same value can be assigned to multiple variables in a single line.
a = b = c = 100
print(a, b, c)
# 4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Deleting a Variable - we use del keyword for deleting the variable

var = "sandhya"
del var
# print(var)



'''
---------------------------------------------------------
Concept of Object Reference in Python
---------------------------------------------------------

Step 1: Assign 5 to x
x = 5

Python creates an integer object representing the value 5.
The variable 'x' does NOT store the value directly.
Instead, 'x' holds a reference to the object 5.

x ───────► 5


Step 2: Assign x to y
y = x

'y' now references the SAME object that 'x' references.
Python does NOT create a new copy of the value 5.

x ───────► 5 ◄─────── y

This is called a SHARED REFERENCE.
Multiple variables can reference the same object.


Step 3: Reassign x
x = "Geeks"

Python creates a new string object "Geeks"
and makes 'x' reference this new object.

x ───────► "Geeks"

y is NOT affected because y still references the original object 5.

y ───────► 5


Step 4: Reassign y
y = "Computer"

A new string object "Computer" is created,
and 'y' now references this new object.and the old goes to garbage

x ───────► "Geeks"
y ───────► "Computer"


IMPORTANT:
Python variables are names/references to objects,
NOT containers that directly store values.

Reassigning a variable changes what object it references.
It does not change the object that another variable references.

Once an object has no references pointing to it,
it becomes eligible for garbage collection.'''


z=5
y=z
z="sandhya"
print(y)
print(z) 

#Swapping 2 numbers

m = 5
n = 6
m,n = n,m  #m, n = n, m is called multiple assignment / tuple unpacking in Python. It is commonly used to swap two variables.
print(m,n)

# Another Method for Swapping the numbers

var1 = 2
var2 = 5

temporary = var2 #temporary = 5 and var2 = 5
print(temporary,var2)
var2 = var1 #var2 = 2 and var1 = 2
print("var1 = ",var1,"and var2 = ",var2)
var1 = temporary # var1 = 2 and temporary = 2
print("var1 = ",var1,"and var2 = ",var2)
