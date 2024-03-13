digit = input("Enter 4 number: ")
digit = int(digit)
sto = 100
ten = 10
a, b = divmod(digit, sto)
c, d = divmod(a, ten)
f, g = divmod(b, ten)
print(c)
print(d)
print(f)
print(g)
