x = int(input('(number1) '))
z = input('(+ - * /) ')
y = int(input('(number2) '))
if z == '+':
    number = x + y
    print(number)
elif z == '-':
    number = x - y
    print(number)
elif z == '*':
    number = x * y
    print(number)
elif z == '/':
    if y == 0:
        print("number 0!")
    else:
        number = x / y
        print(number)
print("end")
