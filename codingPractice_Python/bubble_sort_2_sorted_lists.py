# to merge and sort two sorted lists

l1 = [100, 322, 400]
l2 = [100, 120, 130]

for x in l2:
    l1.append(x)
print(l1)

# can do this also to add 2 lists in 3rd one -> l3 = l1+l2

for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            temp = l1[j]
            l1[j] = l1[i]
            l1[i] = temp

print(l1)
