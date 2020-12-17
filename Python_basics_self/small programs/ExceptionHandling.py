import sys
import logging

'''
print "The current platform is: ", sys.platform

# assert in python to test certain step

print "\nThe value of x needs to be less than 10"
x = 9
assert (x < 10), "x needs to be less than 10"

print "\nNow using try ... except ... finally "

try:
    print(y)
    # here, change y with x to test
except Exception:
    # other ways to write:
    # except:
    print "Y is not defined. "
finally:
    print "Execute this no matter what! "

try:
    print z
except Exception as er:
    print er
finally:
    print "Can use Except in this way too! "

# another example
try:
    f1 = open("file1")
    str = f1.read()
except Exception as er:
    print er
finally:
    print "Using base class for all exceptions to catch exception."
    
'''

# best way to use exception, so that the whole stack trace is logged and printed for debugging.
# using logging to log the full stack trace

try:
    y = 10/0
    print(y)
except Exception as e:
    logging.exception("Caught an exception here!!!")