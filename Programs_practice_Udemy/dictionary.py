# a dictionary is a data structure with key-value pairs as members


name_age = {"urja": 31, "myst": 1021, "kaderin": 1088, "mina": 1200, "nikolai": 600}
print(name_age)
# to change a value of a member
name_age["nikolai"] = 623
print(name_age)
# to add a new member
name_age["Nix"] = 3000
print(name_age)

# list of dictionaries

friends = [
    {"name": "nikolai", "species": "vampire", "age": 615},
    {"name": "myst", "species": "valkyrie", "age": 1234},
    {"name": "lachlain", "species": "werewolf", "age": 3200},
]
print(friends)
# to print a particular key from a dictionary first access the dicti with the index and then use the key
print(friends[1]["name"])

# to access and print the key value pairs, use the in built function items()

for name, age in name_age.items():
    print(f"{name} is {age} years old.")

print("values from dicti --> ", name_age.values())
print("keys from dicti --> ", name_age.keys())


