def is_even(number):
    number = str(number)
    num_end = number[-1]
    x = '1, 3, 5, 7, 9'
    if num_end in x:
        return False
    return True


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')
