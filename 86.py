lines = open("words.txt").readlines()
fiveletters = []
for i in lines:
    if len(i) == 6:
        fiveletters.append(i)

print(fiveletters)