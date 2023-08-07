scores = {
    "riazi1": 14,
    "zaban": 20,
    "mabani computer": 20,
    "fizik1": 12,
    "andishe eslami": 6,
    "sakhteman dadeh": 16
}

for k, v in scores.items():
    if v >= 10:
        print(k, "is passed")
    else:
        print(k, "is failed")

grade = sum(scores.values()) / len(scores)
print(grade)
