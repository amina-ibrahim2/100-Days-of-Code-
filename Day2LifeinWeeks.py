# Create a program that uses math and f-Strings to determine how many weeks we have left, if we live until 90 years of age. 

age = input()
# How many years they have left?
years = 90 - int(age) # change from str to int data type 
weeks_at_age = years * 52 
print(f"You have {weeks_at_age} left.")
