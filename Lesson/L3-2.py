lst_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = len(lst_one)
x = len(lst_one) // 2
z = len(lst_one) % 2
z1 = x + z
list2 = lst_one[z1:]
list1 = lst_one[:z1]
list_two = [list1] + [list2]
print(list_two)
