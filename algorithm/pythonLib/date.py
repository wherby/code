import datetime
from datetime import timedelta
testeddate = '9/9/2022'
dt_obj = datetime.datetime.strptime(testeddate,'%m/%d/%Y')
print(dt_obj)
day100 = timedelta(days=100)
day1000 = timedelta(days=1000)
d100 = (dt_obj-day100)
print(d100)
d1000 = (dt_obj-day1000)
print(d1000)