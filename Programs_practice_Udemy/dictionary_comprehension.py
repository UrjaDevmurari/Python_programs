# check username and password for login using dictionary comprehension

users = [
    (0, "Urja", "123"),
    (1, "Gaurang", "456"),
    (2, "uname", "pword")
]
user_details = {user[1]:user for user in users}
# here, user[1]: user is the (key, value) pair that will go in the dictionary. Rest is the for loop.

print(user_details)

un_input = input("Enter the username here!")
pw_input = input("Enter the password here!")

if un_input in user_details:
    _, real_un, real_pw = user_details[un_input]
    if pw_input == real_pw:
        print("success!")
    else:
        print("Wrong password!")
else:
    print("Wrong username!")