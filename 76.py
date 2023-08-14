def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        digits = [int(i) for i in str(x)]
        x = sum(digits)
        return myhash(x)


print(myhash(997))
