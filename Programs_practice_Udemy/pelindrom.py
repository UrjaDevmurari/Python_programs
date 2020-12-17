# to check if the string is palindrome or not

str = raw_input("Enter a string to know if its' palindrome or not! \n")
rev = str[::-1]
#here, above slice function means that, for the given string str start from end, move towards start and take -1 step.
# ex, for urja, start from 3 and go to 0, 3-1,3-2 etc.

#alternate
# rev = str[(len(str)-1)::-1]

print "Original string is: ", str
print "Reversed string is: ", rev

if str == rev:
    print "Palindrome!"
else:
    print "Not a Palindrome!"