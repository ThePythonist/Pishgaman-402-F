numbers = []

for i in range(3):
    x = input("Enter any number : ")
    try:
        x = float(x)
        numbers.append(x)
    except ValueError:
        pass

print(numbers)
