numbers = []

while True:
    x = input("Type something : ")
    if x == "exit":
        break
    else:
        try:
            x = float(x)
            if int(x) == float(x):
                numbers.append(int(x))
            else:
                numbers.append(x)
        except ValueError:
            pass

print(numbers)
print(max(numbers))
