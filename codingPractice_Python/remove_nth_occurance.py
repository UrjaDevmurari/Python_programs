# remove nth occurrence of word

names = ["jane", "john", "jane", "mina", "james", "jane", "mina", "shila", "james", "john"]
print("The list of names is: {}".format(names))
remove_this = input("Enter the name you want to remove: ")
position = int(input("From which position to remove the name? "))
if remove_this in names:
    for i, name in enumerate(names):
        if name == remove_this:
            position -= 1
            if position == 0:
                names.pop(i)
                print("List of names after removal: {}".format(names))
                break
    if position != 0:
        print("The entered position is wrong!")

else:
    print("{} does not exist in given names list! ".format(remove_this))


