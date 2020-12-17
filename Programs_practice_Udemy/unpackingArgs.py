# unpacking arguments also called variable length argument
# put * before the variable name to indicate that it's an argument that can take multiple values


def multiply(*number):
    total = 1
    for num in number:
        total = total * num
    return total


print(multiply(1, 2, 3))


def calculate(*args, operator):
    if operator == "+":
        return sum(a for a in args)
        # or return sum(args)
    elif operator == "*":
        return multiply(*args)
    else:
        print("Enter correct operator!")


print(calculate(1, 2, 3, 4, 5, operator="+"))
print(calculate(1, 2, 3, 4, operator="*"))
