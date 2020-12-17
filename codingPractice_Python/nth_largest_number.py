# find 1st, 2nd and nth largest number in list

nos = [5, 32, 67, 12, 86]
sorted_list = nos
max1 = 0
max2 = 0
position = int(input("Enter value for nth position: "))
temp = position

if temp in range(1, len(nos)):
    sorted_list.sort(reverse=True)
    ans = sorted_list[position-1]
    print("The {}th largest element is: {}".format(position, ans))
else:
    print("Position cannot be greater than the length of list! ")
