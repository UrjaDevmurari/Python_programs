# input string = aabbbccccaaa, maintain the insertion order and output should be a2b3c4a3

my_string = input("Enter a string. (Hint: aabbbccccaaa)")
count = 1
ans = ""
for i in range(len(my_string)-1):
    if my_string[i] == my_string[i+1]:
        count += 1
        if i == len(my_string)-2:
            ans = ans + my_string[i] + str(count)
    else:
        ans = ans + my_string[i] + str(count)
        count = 1
        if i == len(my_string)-2:
            ans = ans + my_string[i+1] + "1"

print("Result: {}".format(ans))
