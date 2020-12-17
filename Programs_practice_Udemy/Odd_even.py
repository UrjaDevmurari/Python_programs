# print if the number is odd or even

no = int(input("Enter a number to check if it's odd or even. "))
if no%2 == 0:
    print "Number %d is even number. \n" % no
    if no%4 == 0:
        print "Congratulations! The number %d is multiple of 4." % no
else:
    print "Number %d is odd number. " % no