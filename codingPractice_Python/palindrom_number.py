# check if the number is palindrome or not

no = int(input("Enter an integer no!"))
temp = no
rev_no = 0
# no = no.__str__()
# rev_no = int(no[::-1])
#
# print(no)
# print(rev_no)

while temp // 10 > 0:
    d = temp % 10
    rev_no = rev_no*10 + d
    temp = temp // 10

rev_no = rev_no*10 + temp

print("No entered is: {} and reverse of no is: {}".format(no, rev_no))
if no == rev_no:
    print("palindrome!")
else:
    print("Not a palindrome!")

# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")