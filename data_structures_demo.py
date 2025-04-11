person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}
print(person["name"])
print(person["job"])

person["city"] = "New York"

print(person)

person["job"] = "Designer"

print(person)

for key, value in person.items():
    print(key, "->", value)

# --- SETS ---
unique_numbers = {1, 2, 3, 3, 2, 5}
print("Original set:", unique_numbers)

unique_numbers.add(10)
print("After adding 10:", unique_numbers)

unique_numbers.remove(2)
print("After removing 2:", unique_numbers)

other_numbers = {3, 6, 7, 10}
print("Other set:", other_numbers)

# Combine both sets (no duplicates)
union_set = unique_numbers.union(other_numbers)
print("Union of both sets:", union_set)

# Only values that appear in both
common_set = unique_numbers.intersection(other_numbers)
print("Intersection of both sets:", common_set)

groceries = ["milk", "eggs", "milk", "bread"]
unique_groceries = set(groceries)
print("Unique groceries:", unique_groceries)

def demo_data_structures():
    print("\n----- List Example -----")
    groceries = ["apples", "bananas", "milk", "eggs"]
    print("Original list:", groceries)
    capitalized = [item.title() for item in groceries]
    print("Capitalized list:", capitalized)

    print("\n----- Dictionary Example -----")
    person = {"name": "Alice", "age": 30, "job": "Designer", "city": "New York"}
    for key, value in person.items():
        print(f"{key}: {value}")

    print("\n----- Set Example -----")
    unique_numbers = {1, 2, 3, 2, 3, 5}
    other_numbers = {3, 6, 7, 10}
    print("Unique numbers:", unique_numbers)
    print("Union:", unique_numbers.union(other_numbers))
    print("Intersection:", unique_numbers.intersection(other_numbers))

demo_data_structures()
