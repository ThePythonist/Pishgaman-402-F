items = ["Tehran", 37, 24, "Shiraz", "Qazvin", "Tabriz", 12.5]
numbers = []

for i in items :
    if type(i) == str:
        numbers.append(i)

print(numbers)
