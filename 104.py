def show_jalali_age(birth):
    import jdatetime
    # now = str(jdatetime.datetime.now()).split()
    # date = now[0]
    # thisyear = int(date[:4])
    thisyear = str(jdatetime.datetime.now().year)
    age = thisyear - birth
    print(age)


def show_gregorian_age(birth):
    import datetime
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    print(age)


show_gregorian_age(1995)
# show_jalali_age(1370)
