pythons = ["ali", "pedram", "sara", "rozbeh", "sam", "elina"]
javas = ["sara", "sam", "taha", "mohammad", "ramin"]
common = []

# for i in pythons:
#     if i in javas:
#         common.append(i)
#
# ---------------------------------------
for i in pythons:  # Martabe ejrayi : 5 * 6 = 30
    for j in javas:
        if i == j:
            common.append(i)
print(common)
