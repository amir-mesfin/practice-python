import datetime

date =datetime.date(2025,11,9)
today = datetime.date.today()

time = datetime.time(14,30,0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S   %m-%d-%y")
print(date)
print(today)
print(time)
print(now)


targrt_date = datetime.datetime(2030,1,1,12,6,9)

current_date = datetime.datetime.now()


if targrt_date  < current_date:
    print("The target date has already passed.")
else:
    delta = targrt_date - current_date
    print(f"Time remaining until target date: {delta}")
