# fibonacci series

first_n = int(input("Enter the value for first n numbers of fibonacci you want to print."))
fib = [0, 1]
for i in range(2, first_n):
    ans = fib[i-1] + fib[i-2]
    fib.append(ans)
print("First {} numbers from fibonacci series are: {}".format(first_n, fib))

# find if given series is fibonacci or not

series = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
flag = True
for i in range(2, len(series)):
    if series[i] == series[i-1] + series[i-2]:
        flag = True
    else:
        flag = False
if flag is True:
    print("Fibonacci!")
else:
    print("Not Fibonacci!")
