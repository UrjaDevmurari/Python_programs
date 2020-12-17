import sys
import time
import datetime

print "The command line arguments list is: ", str(sys.argv)

print "Total number of command line arguments is: ", len(sys.argv)

for i in sys.argv:
    print "Your name is: ", i
# example of input in python
x = input("Enter x: ")
y = input("Enter y:")
print(x+y)

#time in python -> a tick is a second

print "Current system time in ticks since 12 AM, Jan 1, 1970", time.time()
print "Current system time:", datetime.datetime.now() # prints current date and time
print "Local time using time module:", time.localtime(time.time()) #prints not presentable format of time, but parts of the time stamp
print "Printing presentable time using time moduel:", time.asctime(time.localtime(time.time())) #prints the presentable format of time stamp

a =10
print a
a = 'urja'
print a