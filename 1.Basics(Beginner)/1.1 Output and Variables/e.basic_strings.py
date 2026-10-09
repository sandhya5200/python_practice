'''Triple-quoted strings - Triple quotes (''' ''' or """ """) are used when you want a multi-line string
and They are also commonly used for docstrings'''

message = """
Hello,
Welcome to Python.
This is a multi-line string.
"""

print(message)

###################################################################################################################################

'''f-strings/str.format()/ %
1. f-strings are the modern and easiest way to insert variables into strings.
2. We can insert variables using str.format()
3. % formatting - This is the older/legacy way of formatting strings.
'''

name = "sandhya"
age = 25
print(f"The world best girl is {name} and her age is {age}")
print("The world best girl is {} and her age is {}".format(name,age))
print("The world best girl is %s and her age is %d" % (name,age))

#You can also put expressions inside {}:
x = 6
y = 3
print(f"The addition of these numbers is {x+y}")

