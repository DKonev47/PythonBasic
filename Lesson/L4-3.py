import random

x = []
for i in range(random.randint(3, 10)):
    x.append(random.randint(0, 9))
print(x)
x1 = [x[0], x[2], x[-2]]
print(x1)
