# interchange first and last element of list

l1 = [100, 23, 545, 3, 9]
print("Original list: {}".format(l1))
print(l1[-1])
temp = l1[0]
l1[0] = l1[-1]
l1[-1] = temp
print("List after swapping first and last: {}".format(l1))