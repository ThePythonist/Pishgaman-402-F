students = {
    "alireza": 23,
    "atefe": 24,
    "sahel": 31,
    "jalal": 30,
    "akbar": 41,
    "kia": 20,
}

oldest = max(students.values())

for i in students:
    if students[i] == oldest:
        print(i)
