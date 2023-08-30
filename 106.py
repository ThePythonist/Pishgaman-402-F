def generate(length):
    from random import randint
    password = []
    for i in range(length):
        digit = str(randint(0, 9))
        password.append(digit)

    password = "".join(password)
    print(password)


generate(6)
