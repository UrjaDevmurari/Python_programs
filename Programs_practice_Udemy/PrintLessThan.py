# to print list members less than a certain number

l1 = [3,7,14,54,89,9,100,93,25,7,56,17,43,87,90,22]
print "Enter a number and we will print all the members less than that number. "
lessThan = int(input())
l2 = []

for number in l1:
    if number < lessThan:
        print number
        l2.append(number)
print "List of all the numbers less than %d is: %s" % (lessThan,l2)

#printing the same in one line of python

print [number for number in l1 if number < lessThan]