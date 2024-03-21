x = [1, 0, 0, 0, 0, 2, 0, 3, 0, 4, 0, 0, 5, 0]
if x.count(0):
    for y in x:
        if y == 0:
            x.remove(y)
            x.append(y)
print(x)
