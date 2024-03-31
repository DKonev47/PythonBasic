start = input('Enter number: ')
x = None
while len(start) > 1:
    x = 1
    for val in start:
        x *= int(val)
        start = str(x)
else:
    x = int(start)
x = int(x)
print(x)
