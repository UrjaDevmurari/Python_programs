# find if string1 is present in string2 or not and count the total occurence

my_str = "Here learning to code in python!"
what = input("Enter the sub string to search: ")

if what in my_str:
    count = my_str.count(what)
    print("'{}' is repeated {} time(s) in '{}'.".format(what, count, my_str))
else:
    print("'{}' is not present in '{}'!".format(what, my_str))
