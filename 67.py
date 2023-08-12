def filter(items=[]):
    numbers = []
    for i in items :
        if type(i) in [int,float]:
            numbers.append(i)

    print(numbers)


data = [True, 12.5, "Guitar", "Tar", 5, "Piano", 3.2]
filter(data)
