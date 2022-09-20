# from datetime import datetime
# import pytz
# now = int(datetime.now().strftime('%H'))

# if (now >= 19 and now < 24):
#     hours1 = (24 - now) + 8
#     print(hours1)
# elif (now >= 8 and now <= 19):
#     print("Trails are open")
# else:
#     (now < 8)
#     hours1 = (8 - now) + 4
#     print(f"There are {hours1} until the trails open at 08:00")

from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H"))