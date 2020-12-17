import string
import logging
from pprint import pprint


class MyClass1:
    'This is the first python class of the project!!!'
    # class variable
    studentCount = 0

    # constructor for class instances
    def __init__(self, studentName, marks):
        # instance variables
        self.studentName = studentName
        self.marks = marks
        # calling the class variable using className and . operator
        MyClass1.studentCount += 1

    # class method
    def printStudents(self):
        print("Students list:\n Name: ", self.studentName, " Marks: ", self.marks)


# creating instances of class
student1 = MyClass1("urja", 100)
student2 = MyClass1("gaurang", 99)
# calling class method on an instance
student1.printStudents()
student2.printStudents()
# printing class variable value
print("Total students : %d" % MyClass1.studentCount)
print("Class documentation : ", MyClass1.__doc__)

print("First student name: ", student1.studentName)
print("Student 1 details : ", student1.printStudents())

# adding an attribute to object1
student1.age = 18
# printing the object
print(student1.age)
pprint(vars(student1))

# =========== build in attributes of a class ========

print("\n\nDictionary containing namespace of class: ", MyClass1.__dict__)
print("Name of the class: ", MyClass1.__name__)
print("Module name in which the class is defined: ", MyClass1.__module__)
