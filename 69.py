nomarat = {
    "riazi1": 17,
    "mabani computer": 20,
    "madar haye manteghi": 16,
    "zaban omomi": 18,
    "fizik1": 9,
    "andishe eslami": 13
}


def ghaboli(dars):
    if nomarat[dars] >= 10:
        print(dars, "Pass shode ast")
    else:
        print(dars, "Rad shode ast")


def moadel(doros):
    avg = sum(doros) / len(doros)
    print(avg)


# ----------------------------------------------

for dars in nomarat:
    ghaboli(dars)

moadel(nomarat.values())
