import time


class SedanCar:
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb
        self.rpm = 0

    def carbreak(self):
        print("Tormoz")

    def carhorn(self):
        print("Boogh")

    def accelerate(self, value):
        for i in range(value):
            self.rpm += 1000
            time.sleep(2)
            print(self.rpm)


# Creating instance
dena = SedanCar(113, "Black", "Petrol", "Automatic")
samand = SedanCar(113, "white", "Petrol", "Manual")

# dena.carhorn()
# dena.carbreak()
dena.accelerate(value=4)
