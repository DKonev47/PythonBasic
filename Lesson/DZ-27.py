def is_even(digit):
    """ Перевірка чи є парним число """
    res = digit % 2 == 0
    return res


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

