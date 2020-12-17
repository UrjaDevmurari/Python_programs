# palindrome or not

word = "lol"
rev = ""

for char in word:
    rev = char + rev

print(f"word = {word} \n reverse = {rev}")

# using slice operation on string

reverse = word[::-1]

print(reverse)

if word == reverse:
    print("yes")
else:
    print("no")