lines = open("words.txt").readlines()
sublist = []
for i in lines:
    if i[0:3] == "sub":
        sublist.append(i)

print(sublist)
