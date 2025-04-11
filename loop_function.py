def greet_user():
    print("Hello there!")
    print("Welcome to my program.")

greet_user()

def greet_everyone():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print("Hello, " + name + "!")

greet_everyone()

def print_even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

print_even_numbers(1, 10)
