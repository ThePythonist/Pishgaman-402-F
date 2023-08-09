def mysort(items):
    # items.sort(reverse=True)
    items.sort()
    return items[::-1]


print(mysort([1, 2, 5, 3, 10, 7, 6, 4]))
