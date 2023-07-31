def show_jalali_age(birth):
    import jdatetime
    # today = str(jdatetime.date.today()).split("-")
    # thisyear = int(today[0])
    now = jdatetime.datetime.now()
    thisyear = int(now.year)
    age = thisyear - birth
    print(f"You are {age} years old")


def show_gregorian_age(birth):
    import datetime
    now = datetime.datetime.now()
    thisyear = int(now.year)
    age = thisyear - birth
    print(f"You are {age} years old")

# show_jalali_age(1378)
# show_gregorian_age(1995)
