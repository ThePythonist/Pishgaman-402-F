# odds = []
#
# for i in range(100):
#     if not i % 2 == 0 :
#         odds.append(i)
#

odds = [i for i in range(100) if not i % 2 == 0]
print(odds)
