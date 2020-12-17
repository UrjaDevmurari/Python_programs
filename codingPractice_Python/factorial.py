# find a factorial of given number

no = int(input("Enter a number to find it's factorial"))
ans = 1

for i in range(1, no+1, 1):
    ans = ans * i


print("Factorial of {} is {}".format(no, ans))
