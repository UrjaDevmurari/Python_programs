# this program demonstrates the use of main method in python

def calculator(a,b):
    print "a+b = ", a+b
    print "a-b = ", a-b
    print "a*b = ", a*b
    print "a/b = ", a/b

if __name__ == '__main__':
    x = input("Enter a: ")
    y = input("Enter b: ")
    calculator(x,y)
