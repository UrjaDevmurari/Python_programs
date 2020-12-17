# using raise and try except block to handle error in python


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    else:
        return x/y


try:
    ans = divide(15, 0)
except ZeroDivisionError as e:
    # if full trace needs to be printed then use below line.
    # print(e.with_traceback())
    print("Cannot divide by 0.")
else:
    print(f"The result is: {ans}")
finally:
    print("This is how exception handling works in python.")