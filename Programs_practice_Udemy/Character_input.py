# ask the user to input their name and age. Tell them in which year they will turn 100 years old.


class calculateYear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age100(self, no):
        yearOfInterest = 2019 + (100 - self.age)
        for n in ((no+1), 0):
            print("Dear %s, you will be 100 years old in year %d" % (self.name, yearOfInterest))
            n = n - 1


userName = input("Please enter your name here: ")
userAge = input("Enter your age here: ")

user1 = calculateYear(userName, userAge)
no = input("Enter a number (to print the message in loop for that many times): ")
user1.age100(no)