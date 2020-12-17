# there are different types of function arguments in python


# class functions_examples:
# keyword arguments
def key_funct(x, y):
    print("x and y are:", x, y)


# default arguments
def default_funct(a, b=9):
    print("a and b are: ", a, b)


# variable length arguments
def varia_funct(arg1, *var_arg):
    print("arg1 is: ", arg1)
    print("variable argument is: ", var_arg)


if __name__ == '__main__':
    key_funct(y=9, x=10)
    key_funct(4, 5)
    default_funct(6, 7)
    default_funct(8)
    varia_funct(10, 'k', 'hello', 200)
