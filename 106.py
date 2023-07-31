from random import choice, sample


def generate1(length):
    password = []

    for i in range(length):
        digit = choice(range(0, 10))
        password.append(str(digit))

    password = "".join(password)
    return password


print(generate1(6))


def generate2(length):
    password = sample(range(0, 10), length)
    password = [str(i) for i in password]
    password = "".join(password)
    return password


print(generate2(4))
