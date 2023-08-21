def f1():
    lines = open("words.txt").read().split("\n")
    lines.sort(key=len)
    longest = lines[-1]
    print(longest)
    print(len(longest))


def f2():
    lines = open("words.txt").read().split("\n")
    longest = max(lines, key=len)
    print(longest)
    print(len(longest))


def f3():
    lines = open("words.txt").read().split("\n")
    longest = max(lines, key=len)
    maxlen = len(longest)

    for i in lines:
        if len(i) == maxlen:
            print(i)


f3()
