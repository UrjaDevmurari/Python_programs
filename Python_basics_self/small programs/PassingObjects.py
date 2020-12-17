# here we will see how objects are passed in python

#passing mutable object

def change_list1(another_list):
    print "got: ", another_list
    another_list.append('we')

l1 = ['he', 'she', 'they']
print '\nbefore: ', l1
change_list1(l1)
print 'after: ', l1

#here, list is mutable so appending new member will get reflected in original list as well

# let's see if we can change the list

def change_list2(new_list):
    print "got: ", new_list
    new_list = ['pelo', 'peli', 'pela']

print '\nbefore calling change_list2 l1 is: ', l1
change_list2(l1)
print 'after calling change_list2 l1 is: ', l1

#here, the list is not changed because when line 20 is run, it creates a new object for new_list

def change_string(string2):
    print "got this string: ", string2
    string2 = "salo harami manas!"

string1 = "bdha ahiya chutiya che."
print '\nbefore: ',string1
change_string(string1)
print 'after: ',string1