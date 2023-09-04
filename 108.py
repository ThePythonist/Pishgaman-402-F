class Person:
    def __init__(self, name, age, job, ct):
        self.city = ct
        self.name = name
        self.age = age
        self.job = job

    def talk(self):
        print(f"""
        Hi my name is {self.name} and i am {self.age} years old
        i live in {self.city} and i am a {self.job}.
        """)


# Creating Instance
pedram = Person("Ali", 23, "Programmer", "Tehran")
pedram.talk()
