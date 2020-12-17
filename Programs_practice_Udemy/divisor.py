# print all the divisors of the number

print "Enter a number to find its' divisors! "
number = int(input())
list1 = []

for i in range(1, number+1, 1):
    if number % i == 0:
        list1.append(i)

print "Divisors of %d are: " % number, list1