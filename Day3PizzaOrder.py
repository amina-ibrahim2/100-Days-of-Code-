# Create an automatic pizza order program 

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M, or L? ")
add_pepperoni = input("Would you like pepperoni? Y or N ")
extra_cheese = input("Would you like extra cheese? Y or N ")


bill = 0 
if size == "S":
     bill += 15 
elif size == "M":
     bill += 20
else:
     bill += 25

if add_pepperoni == "Y":
     if size == "S":
        bill += 2
else:
     bill += 3

if extra_cheese == "Y":
     bill += 1
        
print(f"Your final bill is ${bill}.")
