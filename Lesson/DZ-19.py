def common_elements():
    x = (range(3, 100, 3))
    y = (range(5, 100, 5))
    x = set(x)
    y = set(y)
    x.intersection_update(y)
    return x


print(common_elements())
