# def checknumber(x):
#     if type(x) in [int, float]:
#         print("Okay continue")
#         return "Number"
#     else:
#         print("Not okay")
#         return "Not Number"
#
#
# print(checknumber("Smt"))

# if checknumber(125) == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

def checknumber(x):
    if x % 2 == 0:
        print("Even")
        # return "Even"
    else:
        print("Odd")
        # return "Odd"


# checknumber(14)
print(checknumber(14))

# if checknumber(8) == "Even":
#     print("Pasokh zoj ast")
