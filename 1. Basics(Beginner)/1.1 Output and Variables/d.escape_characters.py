'''In Python, escape characters are used when we need to include special characters in a string that are otherwise hard (or illegal) to type directly. These are preceded by a backslash (\), which tells Python that the next character is going to be a special character. They’re especially helpful for:

Formatting strings (adding tabs, newlines)
Including quotes inside quotes
Writing file paths
Inserting control characters'''

# \n-Newline – Moves the cursor to the next line.
print("sandhya\nRani")

# \t-Tab – Adds a horizontal tab.
print("new\ttab")

# \\-Backslash – Inserts a literal backslash.
print("Hyderabad\\Bhagyanagaram")

# \'-Single Quote – Inserts a single quote inside a single-quoted string.
print("don\'t")

# \"-Double Quote – Inserts a double quote inside a double-quoted string.
print("\"sandhya is best in this world!!\"")

# \r-Carriage Return – Moves the cursor to the beginning of the line.
x = input(" --> This is the entered Number\r")
x = input("\rThis is the entered Number --> ")

# \b-Backspace – Moves the cursor one position back, effectively deleting the last character.
# \f-Form Feed – Moves the cursor to the next page.
# \v-Vertical Tab – Moves the cursor vertically.
# \xhh-Hexadecimal – Represents a character using hexadecimal value hh.