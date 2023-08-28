from persiantools.jdatetime import JalaliDateTime
import pytz

now = JalaliDateTime(1402, 6, 6, 16, 45, 0, 0, pytz.utc).strftime("%Y")
print(now)
