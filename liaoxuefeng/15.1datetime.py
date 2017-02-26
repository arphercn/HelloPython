# 获取当前日期和时间

from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
# 2017-02-24 13:21:09.136734
print(type(now))
# <class 'datetime.datetime'>


# 获取指定日期和时间

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
# 2015-04-19 12:20:00


t = dt.timestamp() # 把datetime转换为timestamp
print(t)
# 1429417200.0

r = datetime.fromtimestamp(t) # timestamp转换为datetime # 本地时间
print(r)
# 2015-04-19 12:20:00

r = datetime.utcfromtimestamp(t) # UTC时间
print(r)
# 2015-04-19 04:20:00

# str转换为datetime
cday = datetime.strptime('2020-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2020-06-01 18:19:59

r = now.strftime('%a, %b %d %H:%M')
print(r)
# Fri, Feb 24 13:16

# datetime加减
from datetime import datetime, timedelta
r = now + timedelta(hours=10)
print(r)
# 2017-02-24 23:21:09.159736
r = now - timedelta(days=1)
print(r)
# 2017-02-23 13:21:09.159736
r = now + timedelta(days=2, hours=12)
print(r)
# 2017-02-27 01:21:09.159736

print('---------------')
# 本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
print(tz_utc_8)
# UTC+08:00
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)
# 2017-02-24 14:04:55.333121+08:00

print('---------------')
# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 2017-02-24 06:31:58.453958+00:00
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 2017-02-24 14:31:58.453958+08:00
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 2017-02-24 15:31:58.453958+09:00
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 2017-02-24 15:31:58.453958+09:00


















