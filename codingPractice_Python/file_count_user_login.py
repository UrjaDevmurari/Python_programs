# read from file and count the user login for each user

# my_file = open("file1.txt", "r+")
# # my_file.write("user1, user2, user3, user9, user1, user3, user50, user2, user3, user50, user1, user3, user2, user50,
# # user2, user3, user50, user1, user3, user2, user50")
# print(my_file.read())
# my_file.close()

login_data = open("file1.txt", "r")
lines = login_data.readlines()
print(lines)
user_names = [word for line in lines for word in line.split(",")]
print(user_names)
user_names = [word.strip() for word in user_names]
# for word in user_names:
#     word = word.strip()
print("User names after removing extra space: {}".format(user_names))

# now to find out how many times each user is repeated in list
unique_users = []
count = 1

for i in range(len(user_names)-1):
    if user_names[i] not in unique_users:
        unique_users.append(user_names[i])
        for j in range(i+1, len(user_names)):
            if user_names[i] == user_names[j]:
                count += 1
        print("{} has logged in {} times.".format(user_names[i], count))
        count = 1
login_data.close()
