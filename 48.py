number = int(input("Enter any number : "))
divisors = [i for i in range(1, number + 1) if number % i == 0]
print(divisors)
# if divisors == [1, number]:
if len(divisors) == 2:
    print("Prime")
else:
    print("Composite")
