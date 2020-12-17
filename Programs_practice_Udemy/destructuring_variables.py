# list of tuples

friends_list = [
    ("nikolai", "vampire", 615),
    ("myst", "valkyrie", 1234),
    ("lachlain", "werewolf", 3200)
]

# now to print the values using de-structuring the dictionaries inside the list

for name1, species, age1 in friends_list:
    print(f"{name1} is a {species} who is {age1} years old.")

# to separate out the first value and the rest or vice versa using destructuring

list_3 = [1,2,3,4,5,6,7]
head, *tail = list_3
print(head)
print(tail)

*head, tail = list_3
print(head)
print(tail)