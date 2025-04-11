name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)  # This converts the age to a number

def calculate_birth_year(age):
    current_year = 2025
    return current_year - age

birth_year = calculate_birth_year(age)
print("Nice to meet you, " + name + "!")
print("You were probably born in " + str(birth_year) + ".")

if age < 13:
    print("You're a kid! Enjoy it while it lasts.")
elif age < 20:
    print("Teen years! Lots of discovery ahead.")
elif age < 65:
    print("Adulthood is where the real fun begins!")
else:
    print("Hope you're enjoying retirement and peace!")

print("\nHere's how I would greet your friends too:")

friends = ["Alex", "Sam", "Taylor"]
for friend in friends:
    print("Hi, " + friend + "!")
