import datetime

today_date = datetime.date.today()

yesterday_date = today_date - datetime.timedelta(days=1)

month_ago = today_date - datetime.timedelta(days=30)

print(today_date, yesterday_date, month_ago)

date_string = "01/01/17 12:10:03.234567"

date_dt = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%I:%M.%f')

print(date_string)