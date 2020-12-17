# SET data structure stores unique elements and that too in unordered manner
# so when we print set elements we get unique elements and they are printed out of order

set1 = {300, 30, 21, 200, 45, 45, 45, 300, 65, 89, 7, 11}
print(set1)

#set operations

set2 = {300, 27, 21, 7, 700, 900, }
print(set1.intersection(set2))

#union of two sets
print(set1.union(set2))

#difference of two sets
print(set1.difference(set2))

