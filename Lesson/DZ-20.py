def add_one(some_list):
    one = ''
    for i in some_list:
        one = one + str(i)
    one = int(one)
    one = one + 1
    one = str(one)
    end = list()
    for i in one:
        end.append(int(i))
    return end


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
