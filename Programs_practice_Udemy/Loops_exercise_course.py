# iterate using for loop

# str = "hello urja!"
#
# for letter in str:
#     print letter
#
# wish = 'y'
# while (wish == 'y'):
#     print 100
#     urWish = input("Do you with to print 100 on screen? (y/n)")
#     if urWish == 'n':
#         wish == 'n'
#     else:
#         wish == 'y'
#
# #the above code will give error coz I have python 2.7 running. If this code is run with python 3, it will run without error

# to find if the given name is present in list or not

list1 = ["John", "Marry", "Kiya", "Jiya"]
str = input("Enter a name you know!")
if str in list1:
    print("You know {}".format(str))
else:
    print("You don't know {}".format(str))

