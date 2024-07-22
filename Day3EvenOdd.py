# Write a program that determines if a given number is an odd or even number 

print("Which number do you want to check? ")
number = int(input())

if number % 2 == 0:   # if the number divided by 2 with 0 remainder 
    print("This is an even number.")
else:   # Otherwise number cannot be divided by 2 with 0 remainder
    print("This is an odd number. ")



