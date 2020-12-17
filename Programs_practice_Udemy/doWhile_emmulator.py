# here we will see the use of while to emulate the do... while effect in python. Python does not have do...while loop

'''
choice = input("Do you wish to continue? (Y/n)")
# the choices Y/n means that we continue this until user enters "n"
while choice != "n":
    print("you did not enter 'n'...")

    choice = input("Do you wish to continue? (Y/n)")
'''

# better than the above code is the below one

while True:
    choice = input("Do you wish to continue?(Y/n)")
    if choice == 'n':
        break
    else:
        print("You did not enter 'n'...")