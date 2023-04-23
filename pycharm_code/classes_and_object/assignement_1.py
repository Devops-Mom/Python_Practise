# 1- Avengers is a Marvel’s American Superheroes team, and if you are a fan of avengers, recently you have learned about classes and objects in your python course.
# Now you want to showcase your programming skills by representing the Avengers team using classes.
# Create a class called Avenger and create these six superheroes using this class.
# super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# 2- Your Avenger class should have these properties:
#   - Name
#   - Age
#   - Gender
#   - Super Power
#   - Weapon
# 3- Captain America has Super strength, Iron Man has Technology, Black Widow is superhuman, Hulk has Unlimited Strength, Thor has super Energy and Hawkeye has fighting skills as superpowers.
# 4- Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and Arrows
# 5- Create methods to get the information about each superhero
# 6- Create a method is_leader() which will tell if the superhero is a leader or not.
class Avenger():
    def __init__(self,name,age,gender,super_power,weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

        self.isLeader = False

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_superpower(self):
        return self.super_power


    def info(self):
        return f"""
           Avenger Profile:
           Name:   {self.name},
           Age:    {self.age},
           Gender: {self.gender},
           
           Has {self.weapon} weapon and {self.super_power} super power.
           """

    def is_leader(self):
        return self.isLeader

    def remove_leader(self):
        self.isLeader = False
        return self.isLeader

    def make_leader(self):
        self.isLeader = True
        return self.isLeader


    def __str__(self):
        return f"Avenger({self.name}, {self.age}, ..)"


super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
s_pwer = ["strength", "Technology", "superhuman", "Unlimited Strength", "Energy", "fighting skills"]
weapons = ["Shield", "Armor", "Batons", "No Weapon", "Mjölnir", "Bow", "Arrows"]

# let's create a ages and gender list randomly
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']

avengers = []

for name,age,gender,super_power,weapon in zip(super_heroes,ages,genders,s_pwer,weapons):
    avengers.append(
        Avenger(name,age,gender,super_power,weapon)
    )


print(avengers[0])

print(avengers[0].get_name())
print(avengers[0].get_superpower())



avengers[0].make_leader()

print(avengers[0].is_leader())

print(avengers[2].info())




