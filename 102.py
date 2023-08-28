import jdatetime

now = str(jdatetime.datetime.now()).split()
time = now[1]
print(time[0:5])
