# Data Types 

#String- string of characters-double quotes
# [] pull out individual characters-index starts at 0

print("Hello" [4])

print(int("123" + "345"))

# Integer

print(123 + 345)

# Large Integers 
# replace commas by using underscores 

123_456_789

# Float-floating point number-decimal

3.14159

# Boolean-two possible values- T or F 

True 
False 

# Type Error, Type Checking, and Type Conversion

#len(4837)
num_char = len(input("What is your name?"))
#print("Your name has" + num_char + "characters.") # Can't concetanante a string and an integer

print(type(num_char))

# Change from one data type to another 

#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.") #They all have the same data type


a = float(123)
print(type(a))

print(80 + float(100.5))


# Mathematical Operators 

3 + 5 
7 - 3
3 * 2 
6 / 3 # End up with a floating number 
print(type(6 / 3))
2 ** 2 # exponents 

# Be careful about more than one operation in one line 
# PEMDAS 

print(3 * 3 / 3 + 3 - 3 )


# Number Manipulation and F Strings in Python 

print(round(8 / 3, 2))
print(type(8 //3))
