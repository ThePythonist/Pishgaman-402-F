# def status(number):
#     divisors = [i for i in range(1, number + 1) if number % i == 0]
#     print("Prime") if len(divisors) == 2 else print("Composite")
#
#
# number = int(input("Enter any number : "))
# status(number)


def status(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return "Prime" if len(divisors) == 2 else "Composite"


number = int(input("Enter any number : "))
print(status(number))
