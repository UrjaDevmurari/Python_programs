#write a method even_numbers() so that it returns only even numbers from the list

length = input("Enter the size of the list: ")
list1 = []
for i in range(0, length):
    element = input("Enter an element: ")
    list1.append(element)
print(list1)

def even_numbers(list1):
    for member in list1:
        if (member%2 == 0):
            print(member)

even_numbers(list1)
