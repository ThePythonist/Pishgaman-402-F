lines = open("words.txt").readlines()
inglist = []
for i in lines:
    if i[-4:-1] == "ing":
        inglist.append(i)

print(inglist)
