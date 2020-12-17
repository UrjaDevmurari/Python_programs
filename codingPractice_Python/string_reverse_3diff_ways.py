# reverse the words in given string
# Ex: Hello there --> there Hello

my_string = "This string will be reversed."
rev = ""
for word in my_string.split():
    rev = word + " " + rev

print("{} --> {}".format(my_string, rev))


# given a sentence the characters in words in the sentence
# i/p: hello there! o/p: olleh !ereht

rev = ""
for word in my_string.split():
    rev = rev + word[::-1] + " "
print("{} --> '{}'".format(my_string, rev))

# reverse string with words and letters both reversed
# reverse string words, also reverse the characters of words

rev = ""
for word in my_string.split():
    rev = word[::-1] + " " + rev
print("{} --> '{}'".format(my_string, rev))
