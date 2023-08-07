number = int(input("Enter any number : "))
divisors = [i for i in range(1, number) if number % i == 0]
print(divisors)
n = 0
for i in divisors:
    n += i

if n == number:
    print("Perfect Number")
else :
    print("The number is not perfect")
