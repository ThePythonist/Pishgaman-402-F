numbers = []

for i in range(3):
    x = input("Enter any number : ")
    try:
        x = float(x)
        # if str(x)[-2:] == ".0":
        if int(x) == float(x):
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

print(numbers)
