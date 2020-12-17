# remove duplicates from a given list

some_list = [7, 7, 4, 3, 3]
print("Before: {}".format(some_list))
some_list = list(set(some_list))
print("After: {}".format(some_list))

list2 = [7, 43, 120, 5, 24, 16, 5, 120, 78]
print("Before: {}".format(list2))
ans = []
[ans.append(x) for x in list2 if x not in ans]
print("After: {}".format(ans))
