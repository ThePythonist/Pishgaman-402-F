def func(x, y):
    if y == 1:
        return x + 1
    else:
        return 1 + func(x, y - 1)


print(func(2, 4))
