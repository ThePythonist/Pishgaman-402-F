pythons = ["ali", "pedram", "sara", "rozbeh", "sam", "elina"]
javas = ["sara", "sam", "taha", "mohammad", "ramin"]
# for i in pythons:
#     if i in javas:
#         common.append(i)
common = [i for i in pythons if i in javas]
