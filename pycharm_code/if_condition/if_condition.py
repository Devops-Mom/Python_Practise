#Write a program that can tell you your BMI Category.
# Ask user to enter height
# Ask user to enter weight
# Calculate the BMI(Body Mass Index = weight / height 2) and store it in a variable
# If the BMI is 30 or greater, print “Obesity”
# If the BMI is in between 25 and 29, print “Overweight”
# If the BMI is in between 18.5 and 25, print “Normal”
# If the BMI is less than 18.5, print “Underweight”


h = input("Enter your height in cm: ")
h = int(h)/100  #convert height into meters


w = input("Enter your weight in km: ")
w = int(w)

bmi = w/h

if bmi >= 30:
    print("Obesity")
elif bmi >=25 and bmi <=29:
    print("Overweight")
elif bmi >=18.5 and bmi <=25:
    print("Normal")
else:
    print("Underweight")