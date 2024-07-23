# Write a program that interprets BMI based on a users weight and height

#height = input()
#weight = input()
#weight_as_int = int(input(weight))
#height_as_float = float(input(height))
#bmi = weight_as_int / height_as_float ** 2
#bmi_integer = int(bmi)
#print(bmi)

height = float(input("Enter your height in meters: ")) 
weight = int(input("Enter your weight in kilograms: "))  

bmi = weight / (height ** 2)  # This is an alternative way to write (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
else: 
    print(f"Your BMI is {bmi:.2f}, you are clinically obese.")



