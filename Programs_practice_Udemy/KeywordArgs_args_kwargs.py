# kwargs collects the named arguments as a dictionary via kwargs


def printName(**kwargs):
    print(kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


printName(name="Kaderin", weapon="sword")


# *args will collect all the positional arguments into a tuple via args and


def anything(*args, **kwargs):
    print(args)
    print(kwargs)


anything(1, 2, 3, 4, 5, name="Khaleesi", title="mad queen")
