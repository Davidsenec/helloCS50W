# Define a list of names
names = ["Harry", "Ron", "Hermione", "Ginny"]
# Define a tuple
coordinate = (10.0, 20.0)
# Add a name to the "names" list
names.append("Draco")
# Define a set
s = set()
# Define a dictionary
houses = {"Harry":"Gryffindor", "Draco":"Slytherin"}
# Adds a name with their house in the dictionary
houses["Hermione"] = "Gryiffindor"

# Add numbers to the set
s.add(1)
s.add(1)
s.add(2)
s.add(2)
s.add(3)
s.add(4)
# Remove the number 1 from the set
s.remove(1)

# Sorts the name in alphabetical (A-Z) order
names.sort()
# Prints all the names
print(names)
# States the first and the third name in the list
print(names[0], names[2])
# Prints the tuple
print(coordinate)
# Prints the set
print(s)
# States the amount of numbers in the list
print(f"This set has {len(s)} elements.")
# Print the dictionary
print("Hermione is in", houses["Hermione"],".")

# For each name in the list, print each of that name
for name in names:
    print(name)