# This line asks the user to type their name
name = input("What is your name? ")

# This line asks the user to type their age
age = input("How old are you? ")

# We need to turn the age into a number so we can do math
age = int(age)

# Now we figure out the birth year using simple math
current_year = 2025
birth_year = current_year - age

# Now we build a friendly message
print("Hello, " + name + "!")
print("You were probably born in " + str(birth_year) + ".")
