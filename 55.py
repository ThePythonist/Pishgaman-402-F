info = {
    "name": "james",
    "sex": "male",
    "city": "san fransisco",
    "height": 183,
    "weight": 80,
    "band": "metallica"
}

key = input("Search any key : ")
if key in info.keys():
    print("Found :", info[key])
else:
    print("Not Found")
