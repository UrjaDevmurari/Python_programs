# example to understand f-string and format function

# f-string
name = "Gaurang"
print(f"My name is {name}! Hi!")

name = "Urja"
print(f"Hi there! My name is {name}!")

# another way to print dynamic values in a message is using format() function

user = "Urja"
print("Hello World! I am {}".format(user))

# use of format and use of input()

sq_feet = input("Enter the square feet of the area.")
sq_feet2 = int(sq_feet)
sq_meter = sq_feet2 / 10.8
print(f"The {sq_feet2} square feet is equal to {sq_meter} square meter.")
# to get only upto 2 decimal points use .2f along with variable name as shown below
print(f"{sq_feet} square feet is {sq_meter:.2f} square meter.")