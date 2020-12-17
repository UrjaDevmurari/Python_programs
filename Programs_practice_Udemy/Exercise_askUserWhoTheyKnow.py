# ask user to give a list of people they know
# ask for a name and find out if the name is there in the list or not
import logging


def askUserList():
    names = []
    print("Enter no of people you know: ")
    noOfPeople = input()
    try:
        for i in range(0, noOfPeople):
            names[i] = input("Enter a name: ")
    except Exception as e:
        logging.exception("Caught stack trace!!")
    print(noOfPeople)


askUserList()
