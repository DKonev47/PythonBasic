from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: первый элемент последовательности
     end: количество элементов в последовательности
     func: функция, формирующая значение для последовательности
    """
    while end > 0:
        yield begin
        begin = func(begin)
        end -= 1


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
