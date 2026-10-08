# The print() function is inbuilt function and one of the most commonly used functions.
# By default, when you print multiple values, Python automatically separates them with a space.
print("sandhya","is","a","goodgirl")
# The sep parameter allows us to customize this separator. Instead of always using a space, one can define your own character (like -, @, |, etc.). This makes it very useful for formatting outputs in a clean and readable way.
print("sandhya","is","a","goodgirl", sep = "-")
print("sandhya","is","a","goodgirl", sep = "") #Disabling spaces completely
# Then end parameter allows us to print the multiple lines code in a single line 
print("sandhya", end= " and ")
print("Tharun", end= "--->")
print("are siblings")
#Using sep and end together
print("apple","banana","cherry", end=" are fruits\n", sep = "-")   


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

