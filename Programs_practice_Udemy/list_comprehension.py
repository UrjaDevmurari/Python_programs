# list comprehension is used to create a new list out of an existing one, the code is written in only 1 line

# 1 - create a new list which contains length of each word of a statement except the word "the"

statment = "the sun is bright and so is the moon."
words = statment.split()
word_lengh = [len(word) for word in words if word != "the"]
print(word_lengh)

# 2 - create a new list out of an existing one, the new list must contain only positive numbers.

l1 = [-300, 3, 30, 3787, -22, -234, -890]
positive = [number for number in l1 if number>1]
print(positive)
