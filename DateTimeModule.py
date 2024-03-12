# datetime module :-

import datetime

# datetime module contains datetime class object

# now() --> Returns current year, month, day, date, hour, second, and microsecond
d = datetime.datetime.now()        # --> yyyy-MM-DD HH:mm:ss.xxxxxx
print(d)

# creating date objects -->
x = datetime.datetime(2021, 1, 18)             # (YYYY-MM-DD) --> 2021-01-18 00:00:00
print(x)


# strftime() --> takes one parameter , format, to specify the format of the returned string
d = datetime.datetime.now()
year = d.strftime("%y")              # returns the year
print("\nyear : ", year)
k = d.strftime("%b")                # Dec
i = d.strftime("%B")                # December
j = d.strftime("%m")                # 12
l = d.strftime("%Y")                # 2023
m = d.strftime("%H")                # 16
g = d.strftime("%I")                # 04   i.e hours in 12hrs format
f = d.strftime("%p")                # PM
r = d.strftime("%M")                # 43

print("\n --> ", k)
print("\n --> ", i)
print("\n --> ", j)
print("\n --> ", l)
print("\n --> ", m)
print("\n --> ", g)
print("\n --> ", f)
print("\n --> ", r)
