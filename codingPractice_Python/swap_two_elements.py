# swap two elements of a list

l1 = []
length = int(input("Enter total no of elements."))
for i in range(0, length):
    elem = int(input("l1[{}] : ".format(i)))
    l1.append(elem)
print("Original list: {}".format(l1))

no1 = int(input("Enter first number from the list"))
no2 = int(input("Enter second number from the list"))

i1 = l1.index(no1)
i2 = l1.index(no2)

temp = l1[i1]
l1[i1] = l1[i2]
l1[i2] = temp
print("List after swapping: {}".format(l1))
