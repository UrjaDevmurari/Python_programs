# find if a no is prime no or not

no = int(input("Enter a number here!"))
flag = 0

for i in range(2, no):
    if no % i == 0:
        flag = 1
if flag == 1:
    print("{} is not a prime number!".format(no))
else:
    print("{} is a prime number!".format(no))