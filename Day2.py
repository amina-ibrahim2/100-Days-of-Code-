
# Data Types 

#print(len("Hello"))
# What happens if I replace the string with numbers?
#print(len(123456))

#String- string of characters-double quotes
# [] pull out individual characters-index starts at 0

#print("Hello" [4]) # The position of the character

# Subscripting- pulling out a particular element in a string - the number in the square brackets determines which part to pull out


# Integer-whole numbers positive or negative with out any decimals

#print(int("123" + "345")) # If we add quotes it becomes a string and the computer treats it as that. It'll just add the two strings together.

#print(123 + 345)

# Large Integers 
# replace commas by using underscores 
# Makes it easy for humans to read
123_456_789

# Float-floating point number-decimal

3.14159

# Boolean-two possible values- T or F 

#True 
#False 

# Type Error, Type Checking, and Type Conversion

#len(4837) len function doesn't like integers 
#num_char = len(input("What is your name?"))
#print("Your name has" + num_char + "characters.") # Can't concetanante a string and an integer

#print(type(num_char))

# Change from one data type to another 

#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.") #They all have the same data type


#a = float(123)
#print(type(a))

#print(80 + float(100.5))


# Mathematical Operators 

# 3 + 5 
# 7 - 3
# 3 * 2 
# 6 / 3 # End up with a floating number-happens in python
# print(type(6 / 3))
# 2 ** 2 # exponents 

# Be careful about more than one operation in one line 
# PEMDAS 

#print(3 * 3 / 3 + 3 - 3 )



# Number Manipulation and F Strings in Python 

#print(round(8 / 3, 2))
#print(type(8 //3))

#Interactive Exercise-Data Types 
# Write a program that adds the digits in a 2 digit number (if input is 35, the output should be 3 +5 =8)



#two_digit_number= input()
#print(type(two_digit_number))
#first_digit = int(two_digit_number [0])
#second_digit = int(two_digit_number[1])

# Add both integers 

#two_digit_number = first_digit + second_digit
#print(two_digit_number)

# Code Growth 
# Don't try to minimize the amount of lines in your code for optimization
# But rather make your code readable by others.

# Number Manipulation and F Strings 

print(int(8/3))
# Round numbers to a whole 
print(round(8/3, 2)) # round to the nearest decimal-use comma
#Also use two forward slashes (floor division)
print(type(8 // 3)) 
print(8 // 3) # when we use floor division, it rounds to a whole number as opposed to the / operation
print(4/2)
print(type(4 / 2))

# Using varibales 

result = 4 / 2 
result /= 2
print(result)

score = 0
# User scores a point-manipulate a value based on the previous value 
score += 1
print(score)

 # +=
# -=
# *=
# /=

# F Strings 
# Mix strings and other data types 
#print("your score is" + str(score))
# Convenient way 
# f-string allows us to- infront of a string you place f
score = 10 
height = 1.8 
isWinning = True 

print(f"your score is {score}, your height is {height}, you are winning {isWinning}  ")
# So what does f-strings help with? They make it easier to convert to string instead of manually doing it per data type 

