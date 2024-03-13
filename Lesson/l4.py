digit = 1234
x = 100
z = 10
s, d = divmod(digit, x)
left, right = divmod(s, z)
left1, right1 = divmod(d, z)
print(left)
print(right)
print(left1)
print(right1)