word = "engineer"
d = {}
# n = 0
# for i in word:
#     d.setdefault(i, n)
#     n += 1
#
# print(d)
# ---------------------------------------
for i in range(len(word)):
    d.setdefault(i, word[i])

print(d)
