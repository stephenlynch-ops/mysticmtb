# from datetime import datetime
# import pytz


# class OpenHomePage(request):

#     opening_time = 8
#     closing_time = 19

#     tz_London = pytz.timezone('Europe/London')
#     datetime_London = datetime.now(tz_London)
#     now = datetime_London.strftime("%H")

#     if (now >= closing_time and now < 24):
#         hours = ((24 - now) + opening_time)
#         context = { f"There are {hours} until the trails open tomorrow" }
#     elif now < opening_time:
#         hours = (opening_time - now)
#         context = { f"There are {hours} until the trails open today" }
#     else:
#         context = {"The trails are open"}

#     def open_home_page(self, request):
#         return render(request, 'index.html', message)
