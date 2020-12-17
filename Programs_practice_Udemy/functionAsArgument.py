# aka first class function


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x/y


def calculate(a, b, operation):
    return operation(a, b)


print(calculate(20, 4, divide))

# === another example ===


friends = [
    {"name": "Nikolai", "age": 980, "designation": "warlord"},
    {"name": "Lachlain", "age": 1200, "designation": "King of lykae"},
    {"name": "Bastian", "age": 900, "designation": "Warlord"},
    {"name": "Garreth", "age": 1200, "designation": "Prince"},
    {"name": "Myst", "age": 1800, "designation": "Vlkyrie"}
]


def find_friend(friends_list, friend_name, find):
    for record in friends_list:
        if find(record) == friend_name:
            return f"Found it: {record}"
    raise RuntimeError("We found no record with such name! Please try again with correct name.")


def search_record(who):
    return who["name"]


print(find_friend(friends, "Myst", search_record))