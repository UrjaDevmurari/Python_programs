# example of input in python

import os

'''
received = raw_input("Enter a string here!.. ")
print "Received this string: ", received

# this file is to demonstrate about IO in general. It will have only basic IO stuff.

print "\nThis is an example of raw_input(). "
print "Enter a string or expression."
entered_str = raw_input()
print "This is what I got: ",entered_str

print "\nThis is an example of input(). "
print "Enter a string or expression."
entered_str2 = input()
print "Received string is: ", entered_str2
'''

# File I/O functions from here

print "\nThis is to demonstrate how to open a file. "
file1 = open("Sample_file")
print "File name is: ", file1.name
print "Is file open? True means it is closed. ", file1.closed
print "File is opened in mode : ", file1.mode
file1.close()
print "Is file closed after file1.closed() ? ", file1.closed

print "\nLet's open file to write. "
file1 = open("Sample_file", "a")
print "Writing into file. "
file1.write("This line will get appended to the file. Let's see!")
file1.close()

print "\nLet's check the content of file after write. "
file1 = open("Sample_file", "r")
read_text = file1.read()
print "Text from file: ", read_text

print "\nLet's see the current position in the file. "
print "The current position is: ", file1.tell()
file1.close()

# working with the seek() abstract function
print "\nseek(offset, from_what) -> Set file's current position at offset. "
print "\nif from_what is 0 - from beginning\nif 1 - from current position\nif 2 - from end of stream"
file1 = open("Sample_file", "r")
print "Move 5 bytes from beginning : "
file1.seek(5, 1)
print file1.read()
print "Move 5 bytes from current position: "
file1.seek(5, 0)
print file1.read()
print "Move 5 bytes from the end of stream : "
file1.seek(5, 2)
print file1.read()  # will not give any output obviously
file1.close()

os.remove("ThisWillBeDeleted")  # here the file is in the same folder so no need to give absolute path.

print "\nPlatform name is: ",os.sys.platform.title()

print "\nLet's rename the file"
os.rename("Sample_file", "test_file")
file1 = open("test_file")
print "New file name is: ", file1.name
file1.close()