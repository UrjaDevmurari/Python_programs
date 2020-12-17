# move duplicates from given array to new array

# [5, 10, 5, 10, 5, 7, 10, 7]
arr1 = [1, 1, 3, 10, 5, 5, 5, 23, 32, 20, 32]
set1 = set(arr1)
set1 = list(set1)
# print("Unique members of {} are: {}".format(arr1, set1))
count = -1
duplicates = []

for i in set1:
    for j in arr1:
        if i == j:
            count = count + 1
            if count > 0:
                duplicates.append(j)
    count = -1

print("{} has these duplicates: \n{}".format(arr1, duplicates))
