 # Control Flow with if/else and Conditional Operators 

#if condition:
   # do this 
#else: 
   # do this 

#water_level = 50 
#if water_level > 80: # greater than 80
    #print("Drain water")
#else: #if it's not greater than 80 
    #print("Continue ")

bill = 0 

print(" Welcome to Six Flags!")

height = int(input("what is your height in cm? "))
if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18: 
        bill = 7
        print("Youth tickets are $7")
      # Can have as much elif statements in between the if and else statements 
    
    else: 
        bill = 12 
        print("Adult tickets are $12")
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3 

    print(f"Your final bill is ${bill}")

else: 
    print("Sorry, you can't ride.")

# Comparison Operators < > <= >= ==
    # = assigning the value to the variable 
    # == checking if the values on the left and right  are 


# Nested if statements and elif statements 

# Multiple if statements in succession 
    
# if conditional1:
    # do A 
# elif condition2:
    # do B 
# else:
#   do C 
    
# Multiple if 
# if condition1: if condition 1 is true do A and so on.. 
    #do A 
# if conditiona2:
    #do B
# if condition3:
    # do C
