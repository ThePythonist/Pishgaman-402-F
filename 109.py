class Calculator:
    def __init__(self, n1, op, n2):
        self.num1 = n1
        self.num2 = n2
        self.operator = op

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)


operation = input("Enter your operation : ")
operation = operation.split()
n1 = int(operation[0])
op = operation[1]
n2 = int(operation[2])
# n1 = int(input("Enter number : "))
# op = input("Enter operator : ")
# n2 = int(input("Enter number : "))
calc = Calculator(n1, op, n2)

if op == "+":
    calc.add()
elif op == "-":
    calc.subtract()
elif op == "*":
    calc.multiply()
elif op == "/":
    calc.divide()
else:
    print("Invalid Operator")
