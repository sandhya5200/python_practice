'''Comments in Python are used to add explanatory notes to code and are ignored during program execution.

It enhance the readability of the code.
It can be used to identify functionality or structure the code-base.
It can help understanding unusual or tricky scenarios handled by the code to prevent accidental removal or changes.
It can be used to prevent executing any specific part of your code, while making changes or testing.'''

# This is single line comment

'''
This
is
multi-
line
comment
'''

'THIS CAN ALSO BE USE'
"THIS IS ALSO VALID"

"""THIS
IS
ALSO
USED
"""


########----------DOCSTRINGS------------###############################


'''Docstrings (Documentation Strings) are special strings used to document Python code. They provide a description of what a 
module, class, function or method does.

Declared using triple quotes (' ' ' or " " ").
Written just below the definition of a function, class, or module.
Unlike comments (#), docstrings can be accessed at runtime using __doc__ or help().'''

def multiply_to_num(a,b):
    """This is the docstring example which multiplicates two numbers"""
    return a*b

x = multiply_to_num(2,3)
print(x)

print(multiply_to_num.__doc__)       # accessing the docstring with __doc__ function
# help(multiply_to_num)              # accessing the docstring with help sunction uncomment and check result
    