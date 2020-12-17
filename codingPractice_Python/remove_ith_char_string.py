
my_string = "Hello there! How ya doin?"

# use of partition method
print(my_string.partition('l'))

# to remove a particular character from string
which_char = input("Enter the character you want to remove from string! \nOnly the first occurrence will be removed. ")
l1 = my_string.split(which_char)
after_removal = ""
for item in l1:
    after_removal = after_removal + item
print("After removing '{}', the string is: {}".format(which_char, after_removal))

# remove ith character from string

position = int(input("Enter the position for character removal: "))
print("Before: ", my_string)
to_remove = my_string[position]
print("Need to remove {}th position char {}".format(position, to_remove))

