def func(x, y):
    if y == 1:
        return x
    else:
        return x * func(x, y - 1)


print(func(2, 4))
