# Using the following list of cities per country,
#
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# USA = ["New York","Chicago","Las Vegas", "San Francisco"]
# UK = ["London", "Manchester", "Liverpool", "Nottingham"]
# 1- Write a program that asks the user to enter a city name, and it should tell which country the city belongs to
#
# 2- Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
# For example:
# If I enter Mumbai and Chennai, it will print "Both cities are in India" but if I enter Mumbai and New York it should print "They don't belong to the same country"

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

n = input("Enter the city name: ")

if n in India:
    print(f'{n} belongs to India')
elif n in USA:
    print(f'{n} belongs to USA')
elif n in UK:
    print(f'{n} belongs to UK')
else:
    print("Bad input")


# two cities input

a = input("Enter first city name:" )
b = input("Enter second city name:" )

if a in India and b in India :
    print(f'{a} and {b} belongs to India')
elif a in USA and b in USA:
    print(f'{a} and {b} belongs to USA')
elif a in UK and b in UK:
    print(f'{a} and {b} belongs to UK')
else:
    print("Bad input.. Both Cities doesnot belong to same country")
