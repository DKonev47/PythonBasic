on = 1
while on >= 1:
    x = int(input('(number1) '))
    z = input('(+ - * /) ')
    c = int(input('(number2) '))
    if z == '+':
        number = x + c
        print(number)
    elif z == '-':
        number = x - c
        print(number)
    elif z == '*':
        number = x * c
        print(number)
    elif z == '/':
        if c == 0:
            print("number 0!")
        else:
            number = x / c
            print(number)
    v1 = "y"
    v2 = "n"
    v3 = 1
    while v3 >= 1:
        v = (input("continue? y/n "))
        if v == v2:
            on -= 1
            break
        elif v == v1:
            break
        if (v != v1) and (v != v2):
            print("only (y or n)")
