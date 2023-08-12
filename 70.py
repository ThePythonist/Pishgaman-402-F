def numbertype(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


def checknumber(x):
    if type(x) in [int, float]:
        print("Its a number")
        print(numbertype(x))
    else:
        print("Its not a number")


checknumber(5)
