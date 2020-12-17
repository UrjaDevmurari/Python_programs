a = "hello"
b = a

print(id(a))
print(a)
print(id(b))
print(b)

a += " world"

print(id(a))
print(a)
print(id(b))
print(b)
