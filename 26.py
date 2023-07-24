flag = 1

while flag:
    entry = input("Type something : ")
    print(entry)
    if entry == "exit":
        flag = 0
else:
    print("The flag has turned into False")
