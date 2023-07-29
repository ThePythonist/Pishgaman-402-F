items = ["Tehran", 37, 24, "Shiraz", "Qazvin", "Tabriz", 12.5]
numbers = []

for i in items :
    if type(i) == int or type(i) == float :
        numbers.append(i)

print(numbers)
