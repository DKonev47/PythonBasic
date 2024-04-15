def generate_cube_numbers(end):
    def kub(value):
        return value ** 3

    for i in range(2, end + 1):
        if kub(i) <= end:
            yield kub(i)


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'Test1'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test3'
print('OK')
