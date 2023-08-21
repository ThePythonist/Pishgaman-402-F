# lines = open("words.txt").readlines()
# fiveletters = ""
# for i in lines:
#     if len(i) == 6:
#         fiveletters += i
#
# open("5letters.txt", "w").write(fiveletters)

lines = open("words.txt").readlines()
fiveletters = []
for i in lines:
    if len(i) == 6:
        fiveletters.append(i)

output = "".join(fiveletters)
open("5letters.txt", "w").write(output)
