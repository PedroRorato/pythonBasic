import calendar

# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2017, 1, 0, 0)
# print(st)

# HTML Calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2017, 1)
# print(st)

# Loop Over the days of a month
# c = calendar.TextCalendar(calendar.SUNDAY)
# for i in c.itermonthdays(2017, 8):
#     print (i)
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)


#Check first friday of the month
print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2018, m)
    
    week1=cal[0]
    week2=cal[1]

    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))

