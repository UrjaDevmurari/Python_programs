# generate two random lists and print a list containing common elements of the random lists
import classExercise_udemy

lenList1 = int(input("Enter the length of first random list\n"))
lenList2 = int(input("Enter the length of second random list\n"))
list1 = []
list2 = []
common = []

for i in range(lenList1):
    list1.append(classExercise_udemy.randint(1, 100))

for i in range(lenList2):
    list2.append(classExercise_udemy.randint(1, 100))

print "Randome list1 is: ", list1
print "Random list2 is: ", list2

#list11 = [10,20,30,30]
#list22 = [20,30, 40]

for x in list1:
    for y in list2:
        if x == y:
            if x in common:
                pass
            else:
                common.append(x)

# trying to write in one line
#[for x in list1 for y in list2 if x == y common.append(x)]

print "Common elements are: ", common

#print list of even members from list1

evenOnly = [i for i in list1 if i%2 == 0]
print "Even numbers from list1 are: ", evenOnly